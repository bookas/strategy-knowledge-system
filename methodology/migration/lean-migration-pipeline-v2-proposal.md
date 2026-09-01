---
artifact_id: SKS-MIG-LEAN-V2-PROPOSAL-001
version: v2
status: approved
approval_status: approved
approval_record_id: lean-migration-pipeline-v2-approval-001
scope: RQ-02 through RQ-11 legacy DOCX migration
basis: reviews/migration/part-01/rq01/final-pilot-review-record.yaml
authorization_effect: rq02-rq11-series-authorized
canonical_promotion_effect: none
approved_date: 2026-09-01
---

# Lean Migration Pipeline v2

Цей документ фіксує approved operational profile після RQ-01 pilot для
legacy DOCX → noncanonical Markdown migration RQ-02–RQ-11. Він зберігає
governance, discrepancy та canonical-boundary principles схвалених Migration
Fidelity Protocol v1 і Migration Discrepancy Taxonomy v1. Для названого scope
routine comparison mechanics визначає цей v2 profile: repeated per-chapter
Entry Gates і methodology approvals не потрібні, а exhaustive manual/visual
comparison застосовується лише за risk triggers. Canonical promotion цей
approval не дозволяє.

## Оцінка пілота

| Вимір | Висновок |
|---|---|
| Reliability | Висока для джерела складності RQ-01: незалежне порівняння не виявило material discrepancies; три class-N normalization records перевірено та прийнято без змін. |
| Cost | Пілот був дорожчим за необхідний routine flow через повну 162-block evidence map, обов’язковий dual-render visual pass і повторення вже встановленого governance. |
| Automation | Hashes, OOXML inventory, conversion, normalized text/order/heading/list/table/reference checks та repository integrity checks придатні до механізації. |
| Scalability | Доказів достатньо для RQ-02–RQ-11 за умов стандартизованого tooling, source-specific risk screen і окремої scale authorization. |

## Lean Migration Pipeline v2

`source identity → deterministic conversion → automated normalized text / structure / table / reference checks → independent difference-focused fidelity review → correction only for material discrepancy → fidelity closure`

Full visual comparison є risk-triggered. Його слід запускати за наявності
images, text boxes, equations, merged/irregular tables, tracked changes,
comments/fields, layout-dependent meaning, parser mismatch або нез’ясованої
normalized difference.

## Класифікація controls

### KEEP

- exact source/candidate identities та повторна перевірка source після conversion;
- deterministic source-language-preserving conversion зі збереженням DOCX;
- independent difference-focused fidelity review;
- discrepancy routing, correction/verification separation і Final Review Record;
- окрема canonical-promotion boundary.

### AUTOMATE

- SHA-256, Git blob, size та OOXML complexity inventory;
- text/order, heading/list, table dimensions/cells/relationships та reference/DOI checks;
- candidate identity, post-conversion source integrity, repository diff/status і evidence summary.

### RISK-TRIGGERED

- full visual comparison і manual table-cell review;
- повне manual line-by-line semantic review замість inspection лише detected differences;
- adjudication для source ambiguity, authority change, S5 або contested material disposition.

### PILOT-ONLY / REMOVE FROM ROUTINE FLOW

- повторне methodology approval або повний Entry Gate для кожного chapter, якщо source class, methodology, authority і risk profile істотно не змінилися;
- постійне зберігання exhaustive block-by-block map для zero-diff routine cases;
- mandatory dual 11-page visual comparison без risk trigger;
- повторення спільних identities у кожному discrepancy record замість log-level identity.

## Різні control families

Legacy DOCX migration потребує source identity, OOXML complexity inventory,
conversion equivalence, discrepancy/correction records, source preservation і
risk-triggered visual checks. Native AI Knowledge Book production не має
DOCX-to-Markdown equivalence gate; для нього потрібні structured authoring
schemas, claim/evidence provenance, research review, versioning та release
validation. Migration-specific controls застосовуються до native production
лише коли воно імпортує legacy artifacts.

## Scale authorization і умови

**SCALE WITH CONDITIONS — APPROVED AND AUTHORIZED.** RQ-02–RQ-11 становлять одну
authorized migration series. Перед кожною conversion reusable deterministic
tool виконує identity та complexity/risk screen; це не є повторним Entry Gate.
Series execution зупиняється й ескалюється лише якщо source identity ambiguous
або changed, виявлено unsupported/complex DOCX structures, automated checks
знайшли material differences, independent review виявив semantic uncertainty
або methodology materially changed.

Minimum reusable tool:
`tools/migration/legacy_docx_pipeline.py` (`inventory`, `convert`, `check`).

Standard flow:

`source identity → deterministic conversion → automated fidelity checks → independent difference-focused review → correction only for material discrepancies → fidelity closure → commit`

Translation, theory revision, research-content changes і canonical promotion
не авторизовані. OQ-062 залишається unresolved. RQ-01 candidate залишається
noncanonical.
