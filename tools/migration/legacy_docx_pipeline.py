#!/usr/bin/env python3
"""Deterministic legacy DOCX inventory, conversion, and fidelity checks.

The tool uses only the Python standard library. It never edits a DOCX source,
never overwrites a Markdown candidate unless --force is supplied, and stops on
structures that require risk-triggered handling unless --allow-risk is explicit.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import zipfile
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Iterable
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "pr": "http://schemas.openxmlformats.org/package/2006/relationships",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}

TOOL_VERSION = "1.0.0"


def qn(prefix: str, local: str) -> str:
    return f"{{{NS[prefix]}}}{local}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def attr(element: ET.Element | None, name: str, default: str = "") -> str:
    if element is None:
        return default
    return element.attrib.get(qn("w", name), default)


@dataclass
class Paragraph:
    text: str
    markdown: str
    style: str
    alignment: str
    list_kind: str | None
    list_level: int
    list_number: int | None
    page_break: bool
    bold_spans: list[str] = field(default_factory=list)
    italic_spans: list[str] = field(default_factory=list)


@dataclass
class Table:
    plain_rows: list[list[str]]
    markdown_rows: list[list[str]]
    bold_spans: list[str] = field(default_factory=list)
    italic_spans: list[str] = field(default_factory=list)


@dataclass
class DocumentModel:
    source: Path
    sha256: str
    size_bytes: int
    paragraphs: list[Paragraph]
    tables: list[Table]
    blocks: list[Paragraph | Table]
    risk_triggers: list[dict[str, Any]]
    archive_members: list[str]


class DocxReader:
    def __init__(self, source: Path):
        self.source = source
        self.styles: dict[str, str] = {}
        self.relationships: dict[str, str] = {}
        self.numbering: dict[tuple[str, int], tuple[str, int]] = {}
        self.counters: dict[tuple[str, int], int] = {}

    @staticmethod
    def _xml(archive: zipfile.ZipFile, name: str) -> ET.Element | None:
        try:
            return ET.fromstring(archive.read(name))
        except KeyError:
            return None

    def _load_styles(self, archive: zipfile.ZipFile) -> None:
        root = self._xml(archive, "word/styles.xml")
        if root is None:
            return
        for style in root.findall("w:style", NS):
            style_id = attr(style, "styleId")
            name = style.find("w:name", NS)
            self.styles[style_id] = attr(name, "val", style_id)

    def _load_relationships(self, archive: zipfile.ZipFile) -> None:
        root = self._xml(archive, "word/_rels/document.xml.rels")
        if root is None:
            return
        for rel in root.findall("pr:Relationship", NS):
            rel_id = rel.attrib.get("Id", "")
            target = rel.attrib.get("Target", "")
            if rel_id and target:
                self.relationships[rel_id] = target

    def _load_numbering(self, archive: zipfile.ZipFile) -> None:
        root = self._xml(archive, "word/numbering.xml")
        if root is None:
            return
        abstracts: dict[str, dict[int, tuple[str, int]]] = {}
        for abstract in root.findall("w:abstractNum", NS):
            abstract_id = attr(abstract, "abstractNumId")
            levels: dict[int, tuple[str, int]] = {}
            for level in abstract.findall("w:lvl", NS):
                index = int(attr(level, "ilvl", "0"))
                fmt = attr(level.find("w:numFmt", NS), "val", "decimal")
                start = int(attr(level.find("w:start", NS), "val", "1"))
                levels[index] = (fmt, start)
            abstracts[abstract_id] = levels
        for num in root.findall("w:num", NS):
            num_id = attr(num, "numId")
            abstract_id = attr(num.find("w:abstractNumId", NS), "val")
            for level, data in abstracts.get(abstract_id, {}).items():
                self.numbering[(num_id, level)] = data

    def _run_text(self, run: ET.Element) -> tuple[str, str, bool, list[str], list[str]]:
        plain_parts: list[str] = []
        markdown_parts: list[str] = []
        page_break = False
        for node in run.iter():
            if node.tag == qn("w", "t"):
                text = node.text or ""
                plain_parts.append(text)
                markdown_parts.append(text)
            elif node.tag == qn("w", "tab"):
                plain_parts.append("\t")
                markdown_parts.append("\t")
            elif node.tag == qn("w", "br"):
                if attr(node, "type") == "page":
                    page_break = True
                else:
                    plain_parts.append("\n")
                    markdown_parts.append("<br>")
            elif node.tag == qn("w", "cr"):
                plain_parts.append("\n")
                markdown_parts.append("<br>")
        plain = "".join(plain_parts)
        rendered = "".join(markdown_parts)
        props = run.find("w:rPr", NS)
        bold = props is not None and props.find("w:b", NS) is not None and attr(props.find("w:b", NS), "val", "1") != "0"
        italic = props is not None and props.find("w:i", NS) is not None and attr(props.find("w:i", NS), "val", "1") != "0"
        bold_spans = [normalize(plain)] if bold and normalize(plain) else []
        italic_spans = [normalize(plain)] if italic and normalize(plain) else []
        if rendered:
            if bold and italic:
                rendered = f"***{rendered}***"
            elif bold:
                rendered = f"**{rendered}**"
            elif italic:
                rendered = f"*{rendered}*"
        return plain, rendered, page_break, bold_spans, italic_spans

    def _paragraph(self, element: ET.Element) -> Paragraph:
        ppr = element.find("w:pPr", NS)
        style_id = attr(ppr.find("w:pStyle", NS) if ppr is not None else None, "val")
        style = self.styles.get(style_id, style_id or "Normal")
        alignment = attr(ppr.find("w:jc", NS) if ppr is not None else None, "val")
        num_pr = ppr.find("w:numPr", NS) if ppr is not None else None
        num_id = attr(num_pr.find("w:numId", NS) if num_pr is not None else None, "val")
        level = int(attr(num_pr.find("w:ilvl", NS) if num_pr is not None else None, "val", "0"))
        list_kind: str | None = None
        list_number: int | None = None
        if num_id:
            fmt, start = self.numbering.get((num_id, level), ("decimal", 1))
            list_kind = "bullet" if fmt == "bullet" else "number"
            if list_kind == "number":
                key = (num_id, level)
                list_number = self.counters.get(key, start - 1) + 1
                self.counters[key] = list_number
        elif "list bullet" in style.lower():
            list_kind = "bullet"
        elif "list number" in style.lower():
            list_kind = "number"
            key = (style.lower(), level)
            list_number = self.counters.get(key, 0) + 1
            self.counters[key] = list_number

        plain_parts: list[str] = []
        markdown_parts: list[str] = []
        bold_spans: list[str] = []
        italic_spans: list[str] = []
        page_break = False
        for child in element:
            if child.tag == qn("w", "r"):
                plain, rendered, run_break, bold, italic = self._run_text(child)
                plain_parts.append(plain)
                markdown_parts.append(rendered)
                page_break = page_break or run_break
                bold_spans.extend(bold)
                italic_spans.extend(italic)
            elif child.tag == qn("w", "hyperlink"):
                link_plain: list[str] = []
                link_rendered: list[str] = []
                for run in child.findall("w:r", NS):
                    plain, rendered, run_break, bold, italic = self._run_text(run)
                    link_plain.append(plain)
                    link_rendered.append(rendered)
                    page_break = page_break or run_break
                    bold_spans.extend(bold)
                    italic_spans.extend(italic)
                label_plain = "".join(link_plain)
                label_rendered = "".join(link_rendered)
                rel_id = child.attrib.get(qn("r", "id"), "")
                target = self.relationships.get(rel_id)
                plain_parts.append(label_plain)
                markdown_parts.append(f"[{label_rendered}]({target})" if target else label_rendered)

        return Paragraph(
            text="".join(plain_parts),
            markdown="".join(markdown_parts),
            style=style,
            alignment=alignment,
            list_kind=list_kind,
            list_level=level,
            list_number=list_number,
            page_break=page_break,
            bold_spans=bold_spans,
            italic_spans=italic_spans,
        )

    def _table(self, element: ET.Element) -> Table:
        plain_rows: list[list[str]] = []
        markdown_rows: list[list[str]] = []
        bold_spans: list[str] = []
        italic_spans: list[str] = []
        for row in element.findall("w:tr", NS):
            plain_cells: list[str] = []
            markdown_cells: list[str] = []
            for cell in row.findall("w:tc", NS):
                paragraphs = [self._paragraph(p) for p in cell.findall("w:p", NS)]
                plain_cells.append("\n".join(p.text for p in paragraphs if normalize(p.text)))
                markdown_cells.append("<br>".join(p.markdown for p in paragraphs if normalize(p.text)))
                bold_spans.extend(span for p in paragraphs for span in p.bold_spans)
                italic_spans.extend(span for p in paragraphs for span in p.italic_spans)
            plain_rows.append(plain_cells)
            markdown_rows.append(markdown_cells)
        return Table(
            plain_rows=plain_rows,
            markdown_rows=markdown_rows,
            bold_spans=bold_spans,
            italic_spans=italic_spans,
        )

    @staticmethod
    def _risk_inventory(root: ET.Element, archive: zipfile.ZipFile) -> list[dict[str, Any]]:
        checks = {
            "images_or_objects": ["drawing", "pict", "object"],
            "text_boxes": ["txbxContent"],
            "equations": ["oMath", "oMathPara"],
            "tracked_changes": ["ins", "del", "moveFrom", "moveTo"],
            "fields": ["fldSimple", "instrText"],
            "content_controls": ["sdt"],
            "alternate_content": ["altChunk"],
        }
        local_counts: dict[str, int] = {}
        for node in root.iter():
            local = node.tag.rsplit("}", 1)[-1]
            local_counts[local] = local_counts.get(local, 0) + 1
        risks: list[dict[str, Any]] = []
        for kind, names in checks.items():
            count = sum(local_counts.get(name, 0) for name in names)
            if count:
                risks.append({"kind": kind, "count": count})
        merge_count = sum(
            1
            for node in root.iter()
            if node.tag in {qn("w", "gridSpan"), qn("w", "vMerge")}
        )
        if merge_count:
            risks.append({"kind": "merged_table_cells", "count": merge_count})
        cols = root.findall(".//w:sectPr/w:cols", NS)
        multi_column = sum(1 for node in cols if int(attr(node, "num", "1")) > 1)
        if multi_column:
            risks.append({"kind": "multi_column_layout", "count": multi_column})
        names = set(archive.namelist())
        for member, kind in (
            ("word/comments.xml", "comments"),
            ("word/footnotes.xml", "footnotes"),
            ("word/endnotes.xml", "endnotes"),
        ):
            if member in names:
                member_root = ET.fromstring(archive.read(member))
                substantive = 0
                for item in list(member_root):
                    item_id = attr(item, "id", "-1")
                    if item_id.lstrip("-").isdigit() and int(item_id) >= 0 and normalize("".join(item.itertext())):
                        substantive += 1
                if substantive:
                    risks.append({"kind": kind, "count": substantive})
        embedded = [name for name in names if name.startswith("word/embeddings/")]
        if embedded:
            risks.append({"kind": "embedded_files", "count": len(embedded)})
        return sorted(risks, key=lambda item: item["kind"])

    def read(self) -> DocumentModel:
        if not self.source.is_file():
            raise FileNotFoundError(self.source)
        with zipfile.ZipFile(self.source) as archive:
            self._load_styles(archive)
            self._load_relationships(archive)
            self._load_numbering(archive)
            root = self._xml(archive, "word/document.xml")
            if root is None:
                raise ValueError("DOCX has no word/document.xml")
            body = root.find("w:body", NS)
            if body is None:
                raise ValueError("DOCX has no w:body")
            blocks: list[Paragraph | Table] = []
            paragraphs: list[Paragraph] = []
            tables: list[Table] = []
            for child in body:
                if child.tag == qn("w", "p"):
                    paragraph = self._paragraph(child)
                    paragraphs.append(paragraph)
                    blocks.append(paragraph)
                elif child.tag == qn("w", "tbl"):
                    table = self._table(child)
                    tables.append(table)
                    blocks.append(table)
            return DocumentModel(
                source=self.source,
                sha256=sha256_file(self.source),
                size_bytes=self.source.stat().st_size,
                paragraphs=paragraphs,
                tables=tables,
                blocks=blocks,
                risk_triggers=self._risk_inventory(root, archive),
                archive_members=sorted(archive.namelist()),
            )


def inventory(model: DocumentModel) -> dict[str, Any]:
    nonempty = [p for p in model.paragraphs if normalize(p.text)]
    headings = [p for p in nonempty if p.style.lower().startswith("heading")]
    bullets = [p for p in nonempty if p.list_kind == "bullet"]
    numbered = [p for p in nonempty if p.list_kind == "number"]
    table_rows = sum(len(table.plain_rows) for table in model.tables)
    table_cells = sum(len(row) for table in model.tables for row in table.plain_rows)
    return {
        "tool": {"name": "legacy_docx_pipeline", "version": TOOL_VERSION},
        "source": {
            "path": model.source.as_posix(),
            "sha256": model.sha256,
            "size_bytes": model.size_bytes,
        },
        "structure": {
            "body_blocks": len(model.blocks),
            "paragraphs": len(model.paragraphs),
            "knowledge_bearing_paragraphs": len(nonempty),
            "headings": len(headings),
            "bullets": len(bullets),
            "numbered_items": len(numbered),
            "tables": len(model.tables),
            "table_rows": table_rows,
            "table_cells": table_cells,
        },
        "risk_triggers": model.risk_triggers,
        "supported_for_unattended_conversion": not model.risk_triggers,
    }


def escape_table(value: str) -> str:
    return value.replace("\\", "\\\\").replace("|", "\\|").replace("\n", "<br>")


def paragraph_markdown(paragraph: Paragraph) -> str:
    value = paragraph.markdown.strip()
    style = paragraph.style.lower()
    if style.startswith("heading"):
        match = re.search(r"(\d+)", style)
        level = min(int(match.group(1)) if match else 1, 6)
        return f"{'#' * level} {value}"
    if paragraph.list_kind:
        indent = "  " * paragraph.list_level
        marker = "-" if paragraph.list_kind == "bullet" else f"{paragraph.list_number or 1}."
        return f"{indent}{marker} {value}"
    return value


def convert_markdown(model: DocumentModel) -> str:
    output: list[str] = []
    center_open = False

    def blank() -> None:
        if output and output[-1] != "":
            output.append("")

    for block in model.blocks:
        if isinstance(block, Paragraph):
            if block.page_break:
                if center_open:
                    blank()
                    output.append("</div>")
                    center_open = False
                blank()
                output.append('<div style="page-break-after: always;"></div>')
                blank()
            if not normalize(block.text):
                continue
            centered = block.alignment == "center"
            if centered and not center_open:
                output.append('<div align="center">')
                output.append("")
                center_open = True
            elif not centered and center_open:
                output.append("</div>")
                output.append("")
                center_open = False
            output.append(paragraph_markdown(block))
            blank()
        else:
            if center_open:
                output.append("</div>")
                output.append("")
                center_open = False
            rows = block.markdown_rows
            if not rows:
                continue
            width = max(len(row) for row in rows)
            padded = [row + [""] * (width - len(row)) for row in rows]
            output.append("| " + " | ".join(escape_table(cell) for cell in padded[0]) + " |")
            output.append("| " + " | ".join("---" for _ in range(width)) + " |")
            for row in padded[1:]:
                output.append("| " + " | ".join(escape_table(cell) for cell in row) + " |")
            output.append("")
    if center_open:
        output.append("</div>")
        output.append("")
    while output and output[-1] == "":
        output.pop()
    return "\n".join(output) + "\n"


def strip_markdown_inline(value: str) -> str:
    value = re.sub(r"<br\s*/?>", " ", value, flags=re.I)
    value = re.sub(r"!\[([^]]*)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("***", "").replace("___", "")
    value = value.replace("**", "").replace("__", "")
    value = re.sub(r"(?<!\\)[*_]", "", value)
    value = re.sub(r"\\([\\`*{}\[\]()#+.!_|>-])", r"\1", value)
    return normalize(value)


def split_table_row(line: str) -> list[str]:
    value = line.strip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    parts = re.split(r"(?<!\\)\|", value)
    return [strip_markdown_inline(part.strip().replace("\\|", "|")) for part in parts]


def markdown_structure(text: str) -> dict[str, Any]:
    units: list[str] = []
    headings: list[tuple[int, str]] = []
    lists: list[tuple[str, str]] = []
    tables: list[list[list[str]]] = []
    paragraphs: list[str] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line or re.fullmatch(r"</?div(?:\s+[^>]*)?>", line, flags=re.I):
            index += 1
            continue
        if line.startswith("|") and line.endswith("|"):
            rows: list[list[str]] = []
            while index < len(lines):
                current = lines[index].strip()
                if not (current.startswith("|") and current.endswith("|")):
                    break
                cells = split_table_row(current)
                if not all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells):
                    rows.append(cells)
                index += 1
            tables.append(rows)
            units.extend(cell for row in rows for cell in row if cell)
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            value = strip_markdown_inline(heading.group(2))
            headings.append((len(heading.group(1)), value))
            units.append(value)
            index += 1
            continue
        bullet = re.match(r"^[-+*]\s+(.*)$", line)
        numbered = re.match(r"^\d+[.)]\s+(.*)$", line)
        if bullet or numbered:
            match = bullet or numbered
            value = strip_markdown_inline(match.group(1))
            lists.append(("bullet" if bullet else "number", value))
            units.append(value)
            index += 1
            continue
        value = strip_markdown_inline(line)
        if value:
            paragraphs.append(value)
            units.append(value)
        index += 1
    bold = [normalize(strip_markdown_inline(value)) for value in re.findall(r"\*\*(.+?)\*\*|__(.+?)__", text) for value in value if normalize(value)]
    italic = [normalize(strip_markdown_inline(value)) for value in re.findall(r"(?<!\*)\*([^*\n]+)\*(?!\*)|(?<!_)_([^_\n]+)_(?!_)", text) for value in value if normalize(value)]
    return {
        "units": units,
        "headings": headings,
        "lists": lists,
        "tables": tables,
        "paragraphs": paragraphs,
        "bold_spans": bold,
        "italic_spans": italic,
    }


def source_structure(model: DocumentModel) -> dict[str, Any]:
    units: list[str] = []
    headings: list[tuple[int, str]] = []
    lists: list[tuple[str, str]] = []
    tables: list[list[list[str]]] = []
    bold: list[str] = []
    italic: list[str] = []
    for block in model.blocks:
        if isinstance(block, Paragraph):
            value = normalize(block.text)
            if not value:
                continue
            units.append(value)
            style = block.style.lower()
            if style.startswith("heading"):
                match = re.search(r"(\d+)", style)
                headings.append((int(match.group(1)) if match else 1, value))
            if block.list_kind:
                lists.append((block.list_kind, value))
            bold.extend(normalize(item) for item in block.bold_spans if normalize(item))
            italic.extend(normalize(item) for item in block.italic_spans if normalize(item))
        else:
            rows = [[normalize(cell) for cell in row] for row in block.plain_rows]
            tables.append(rows)
            units.extend(cell for row in rows for cell in row if cell)
            bold.extend(normalize(item) for item in block.bold_spans if normalize(item))
            italic.extend(normalize(item) for item in block.italic_spans if normalize(item))
    return {
        "units": units,
        "headings": headings,
        "lists": lists,
        "tables": tables,
        "bold_spans": bold,
        "italic_spans": italic,
    }


def mismatch_sample(source: list[Any], candidate: list[Any], limit: int = 12) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    matcher = SequenceMatcher(a=source, b=candidate, autojunk=False)
    for tag, a1, a2, b1, b2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        findings.append(
            {
                "operation": tag,
                "source_range": [a1, a2],
                "candidate_range": [b1, b2],
                "source_sample": source[a1 : min(a2, a1 + 3)],
                "candidate_sample": candidate[b1 : min(b2, b1 + 3)],
            }
        )
        if len(findings) >= limit:
            break
    return findings


def check_fidelity(model: DocumentModel, candidate: Path) -> dict[str, Any]:
    text = candidate.read_text(encoding="utf-8")
    source = source_structure(model)
    target = markdown_structure(text)
    checks = {
        "knowledge_bearing_units": source["units"] == target["units"],
        "heading_hierarchy_and_text": source["headings"] == target["headings"],
        "list_kind_order_and_text": source["lists"] == target["lists"],
        "table_dimensions_cells_and_order": source["tables"] == target["tables"],
        "bold_spans": source["bold_spans"] == target["bold_spans"],
        "italic_spans": source["italic_spans"] == target["italic_spans"],
    }
    source_text = "\n".join(source["units"])
    target_text = "\n".join(target["units"])
    doi_pattern = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
    citation_pattern = re.compile(r"\[(?:\d+(?:\s*[-,]\s*\d+)*)\]")
    source_dois = doi_pattern.findall(source_text)
    target_dois = doi_pattern.findall(target_text)
    source_citations = citation_pattern.findall(source_text)
    target_citations = citation_pattern.findall(target_text)
    checks["doi_strings"] = source_dois == target_dois
    checks["citation_markers"] = source_citations == target_citations
    material_difference = not all(checks.values())
    return {
        "tool": {"name": "legacy_docx_pipeline", "version": TOOL_VERSION},
        "source_identity": {
            "path": model.source.as_posix(),
            "sha256": model.sha256,
            "size_bytes": model.size_bytes,
        },
        "candidate_identity": {
            "path": candidate.as_posix(),
            "sha256": sha256_file(candidate),
            "size_bytes": candidate.stat().st_size,
        },
        "checks": checks,
        "counts": {
            "source_units": len(source["units"]),
            "candidate_units": len(target["units"]),
            "source_headings": len(source["headings"]),
            "candidate_headings": len(target["headings"]),
            "source_lists": len(source["lists"]),
            "candidate_lists": len(target["lists"]),
            "source_tables": len(source["tables"]),
            "candidate_tables": len(target["tables"]),
            "source_dois": len(source_dois),
            "candidate_dois": len(target_dois),
            "source_citations": len(source_citations),
            "candidate_citations": len(target_citations),
        },
        "difference_sample": mismatch_sample(source["units"], target["units"]),
        "risk_triggers": model.risk_triggers,
        "material_difference_detected": material_difference,
        "risk_triggered_review_required": bool(model.risk_triggers or material_difference),
        "independent_review_required": True,
    }


def write_json(data: dict[str, Any], output: Path | None) -> None:
    serialized = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized, encoding="utf-8", newline="\n")
    else:
        print(serialized, end="")


def verify_expected_hash(model: DocumentModel, expected: str | None) -> None:
    if expected and model.sha256 != expected.upper():
        raise ValueError(f"Source SHA-256 changed: expected {expected.upper()}, found {model.sha256}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=f"%(prog)s {TOOL_VERSION}")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in ("inventory", "convert", "check"):
        command = subparsers.add_parser(name)
        command.add_argument("source", type=Path)
        command.add_argument("--expected-source-sha256")
        command.add_argument("--output", type=Path, help="Write machine-readable JSON result.")
        command.add_argument("--allow-risk", action="store_true", help="Proceed only after an explicit risk escalation decision.")
        if name == "convert":
            command.add_argument("candidate", type=Path)
            command.add_argument("--force", action="store_true")
        elif name == "check":
            command.add_argument("candidate", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        model = DocxReader(args.source).read()
        verify_expected_hash(model, args.expected_source_sha256)
        if args.command == "inventory":
            result = inventory(model)
            write_json(result, args.output)
            return 0 if args.allow_risk or not model.risk_triggers else 3
        if args.command == "convert":
            if model.risk_triggers and not args.allow_risk:
                write_json(inventory(model), args.output)
                print("Conversion stopped: risk-triggered structures require escalation.", file=sys.stderr)
                return 3
            if args.candidate.exists() and not args.force:
                raise FileExistsError(f"Candidate exists; refusing overwrite: {args.candidate}")
            args.candidate.parent.mkdir(parents=True, exist_ok=True)
            args.candidate.write_text(convert_markdown(model), encoding="utf-8", newline="\n")
            result = check_fidelity(model, args.candidate)
            write_json(result, args.output)
            return 0 if not result["material_difference_detected"] else 2
        result = check_fidelity(model, args.candidate)
        write_json(result, args.output)
        if result["material_difference_detected"]:
            return 2
        if model.risk_triggers and not args.allow_risk:
            return 3
        return 0
    except (FileNotFoundError, FileExistsError, ValueError, zipfile.BadZipFile, UnicodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
