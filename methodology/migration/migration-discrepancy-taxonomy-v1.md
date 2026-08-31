---
artifact_id: SKS-MIG-DISC-001
artifact_type: migration_control_methodology
title: "Таксономія розбіжностей міграції v1"
version: "1.0"
status: candidate
review_status: revise_and_re_review
approval_status: pending_re_review
language: uk
open_question: OQ-060
used_by: "methodology/migration/migration-fidelity-protocol-v1.md"
defines_fidelity_verdict_independently: false
canonical_effect: none
---

# Таксономія розбіжностей міграції v1

## 1. Призначення

Ця taxonomy визначає, як класифікувати, оцінювати, реєструвати й передавати
на disposition відмінності, виявлені під час DOCX → Markdown migration.

Вона потрібна, щоб:

- однакові проблеми отримували однакові назви;
- migration fidelity risk не приховувався під загальним словом “formatting”;
- correction authority був явним;
- source defects не виправлялися як conversion errors;
- fidelity review був відтворюваним і traceable.

Статус документа — `candidate`. Taxonomy набуває обов’язкової сили для RQ-01
pilot лише після окремого схвалення.

## 2. Відношення до Fidelity Protocol

Ця taxonomy використовується документом
[`Migration Fidelity Protocol v1`](./migration-fidelity-protocol-v1.md).

Taxonomy визначає:

- discrepancy class;
- severity migration fidelity risk;
- типовий ризик спотворення source у candidate;
- correction authority;
- required record fields;
- required disposition;
- можливий blocking effect.

Fidelity Protocol визначає:

- сукупний вплив усіх discrepancies;
- достатність evidence;
- `PASS`, `PASS WITH NON-BLOCKING DISCREPANCIES` або `FAIL`.

Severity або class окремо не є фінальним verdict.

## 3. Базові принципи

1. Кожна матеріальна відмінність реєструється до correction.
2. Класифікація описує проблему, а не виправдовує автоматичну зміну.
3. Якщо одна проблема має кілька незалежних ефектів, створюються пов’язані
   records або primary class із secondary classes.
4. Невпевненість щодо fidelity не занижує severity; вона фіксується як
   migration fidelity risk або Source Ambiguity.
5. Source artifact не виправляється під час migration.
6. Potential Intellectual Issue зберігається у faithful representation і
   передається до controlled revision.
7. Silent correction, silent reclassification і silent closure заборонені.
8. Інтелектуальна слабкість source не отримує S0–S5 і не є migration fidelity
   defect, якщо candidate faithfully її зберігає.

## 4. Severity scale

S0–S5 оцінює лише migration fidelity risk: ризик того, що candidate неточно
представляє визначений source або що правильний source/representation не може
бути встановлений. Scale не оцінює якість аргументів, істинність claims чи
концептуальну силу source.

Source Defect і Potential Intellectual Issue, faithfully preserved у
candidate, мають `severity: null`. Якщо вони спричиняють окрему ambiguity,
omission, addition або semantic change у representation, для цього створюється
пов’язаний migration discrepancy record із severity S0–S5.

### S0 — Informational

Спостереження без semantic loss і без потреби змінювати candidate.

Приклад: зафіксовано, що Word pagination не переноситься до Markdown і не
несе значення.

Типовий gate effect: non-blocking.

### S1 — Cosmetic / Non-semantic

Підтверджена відмінність представлення без зміни змісту, structure of meaning
або provenance.

Приклад: інший line wrapping або заміна декоративного font style.

Типовий gate effect: non-blocking після verification.

### S2 — Structural but recoverable

Втрата або помилка representation, яку можна точно виправити з source, але
яка порушує structure, navigation, attribution або readability настільки, що
потребує correction і re-review.

Приклад: неправильний heading level або втрачений list nesting без
підтвердженої semantic change.

Типовий gate effect: blocking до correction і re-review.

### S3 — Migration semantic risk / unresolved representation ambiguity

Є обґрунтований ризик зміни interpretation, scope, relation, attribution або
epistemic force саме в candidate representation, але corruption ще не
підтверджено.

Приклад: незрозуміло, чи bold позначає defined term, або source містить
двозначну merged cell.

Типовий gate effect: blocking до disposition.

### S4 — Confirmed semantic corruption

Candidate підтверджено змінює зміст source.

Приклад: втрачено заперечення; значення table cell переміщено до іншого row;
`may` перетворено на definitive claim.

Типовий gate effect: завжди blocking до correction і повного re-review.

### S5 — Source/version conflict requiring adjudication

Неможливо однозначно визначити правильний source, version, ordering або
authoritative reading без окремого adjudication.

Приклад: дві DOCX-версії претендують на active status або manifest path не
відповідає затвердженому baseline.

Типовий gate effect: blocking для conversion або fidelity verdict до
adjudication.

## 5. Correction authority

| Authority | Дозволена дія | Межа |
|---|---|---|
| `automatic` | Детерміноване S0/S1 normalization або видалення очевидного tool artifact | Не може закривати S2–S5 або змінювати source-derived meaning |
| `operator_with_review` | Точне відновлення representation з source | Потребує reviewer verification і re-review evidence |
| `human_review` | Класифікація semantic significance, ambiguity або складної structure | Не надає права на intellectual revision |
| `adjudication` | Рішення щодо version conflict, source ambiguity чи спірного semantic effect | Має бути traceable й не може мовчазно змінювати source |
| `controlled_revision_only` | Майбутнє виправлення conceptual/source issue | Заборонене в migration candidate до окремого change-control process |

Automatic correction ніколи не означає automatic closure: record має містити
evidence виконаної перевірки.

## 6. Обов’язкові поля кожного discrepancy record

Кожен record має містити:

- `discrepancy_id` — стабільний ID;
- `record_kind` — `migration_discrepancy`, `source_issue` або
  `intellectual_issue`;
- `artifact_id` — ID мігрованого артефакту;
- `source_path`;
- `source_baseline_sha`;
- `source_hash` або blob identity;
- `target_path`;
- `class`;
- `secondary_classes`, якщо застосовно;
- `severity` — S0–S5 лише для `migration_discrepancy`; `null` для faithfully
  preserved `source_issue` або `intellectual_issue`;
- `fidelity_effect` — `blocking`, `non_blocking` або `undetermined`;
- `source_location`;
- `target_location`;
- `source_observation`;
- `target_observation`;
- `migration_fidelity_risk`;
- `evidence`;
- `detected_by`;
- `detection_stage`;
- `owner`;
- `correction_authority`;
- `proposed_disposition`;
- `accepted_disposition` — `null`, доки рішення не прийнято;
- `disposition_status` — `proposed`, `accepted`, `rejected` або `superseded`;
- `disposition_by` — `null`, доки disposition не прийнято;
- `disposition_date` — `null`, доки disposition не прийнято;
- `record_status`;
- `resolution_evidence`, якщо закрито;
- `verification_by` — `null`, якщо verification ще не виконано або не
  застосовується;
- `verification_date` — `null`, якщо verification ще не виконано або не
  застосовується;
- `intellectual_issue_status` — лише для `intellectual_issue`;
- `adjudication_reference`, якщо потрібне;
- `controlled_revision_reference`, якщо issue передано далі.

Location має бути достатньо точною для повторного знаходження проблеми:
section/heading, paragraph, table/cell, footnote або інший стабільний anchor.

## 7. Disposition vocabulary

Рекомендовані machine-readable values:

- `accepted_no_change` — verified non-semantic difference;
- `corrected_representation` — representation відновлено за source;
- `source_preserved_issue_deferred` — source issue збережено й передано далі;
- `requires_human_review`;
- `requires_source_adjudication`;
- `requires_version_adjudication`;
- `reclassified`;
- `false_positive`;
- `not_applicable`;
- `rejected_correction` — запропонована correction порушувала fidelity;
- `controlled_revision_required`.

Disposition не вважається завершеним без evidence і reviewer attribution.

### 7.1 Disposition status

- `proposed` — існує лише proposed disposition; gate-relevant рішення ще
  немає.
- `accepted` — уповноважена особа прийняла `accepted_disposition` і вказала
  `disposition_by` та `disposition_date`.
- `rejected` — proposed disposition відхилено; record залишається unresolved до
  нового proposal або adjudication.
- `superseded` — попереднє proposal замінено новим із збереженням provenance.

Disposition acceptance authority:

- Fidelity reviewer може прийняти representation disposition для S0–S4 лише
  після потрібної verification.
- Source/version ambiguity, policy conflict або будь-який record із
  `adjudication_required` може отримати accepted disposition лише через
  traceable adjudication.
- Fidelity reviewer може прийняти deferral faithfully preserved
  source/intellectual issue тільки як migration disposition. Це не є
  інтелектуальним verdict щодо самого issue.
- `disposition_by` і, якщо застосовно, `adjudication_reference` мають однозначно
  ідентифікувати authority.

### 7.2 Мінімальний record lifecycle

`record_status` використовує лише такі values:

- `detected` — відмінність зафіксовано, але ще не класифіковано;
- `classified` — class, severity/applicability і fidelity effect запропоновано;
- `correction_required` — потрібна representation correction;
- `corrected` — correction виконано, але ще не verified;
- `verified` — correction або exact preservation перевірено, але final
  disposition ще не прийнято;
- `disposition_pending` — evidence повний, очікується final disposition;
- `adjudication_required` — без adjudication record не може рухатися далі;
- `deferred` — source/intellectual issue faithfully preserved, final
  disposition прийнято, downstream handoff зафіксовано;
- `resolved` — final disposition прийнято й усі потрібні verification виконано.

Типові transitions:

Detected
→ Classified
→ Correction Required
→ Corrected
→ Verified
→ Disposition Pending
→ Resolved

або:

Classified
→ Adjudication Required
→ Verified / Disposition Pending
→ Resolved

або для faithfully preserved source/intellectual issue:

Classified
→ Verified
→ Disposition Pending
→ Deferred

### 7.3 Gate-relevant resolved state

Record є gate-relevant resolved лише якщо:

1. `fidelity_effect` не дорівнює `undetermined`.
2. `accepted_disposition` заповнено.
3. `disposition_status: accepted`.
4. `disposition_by`, `disposition_date` та `owner` заповнено.
5. `record_status` дорівнює `resolved` або `deferred`.
6. Для correction або exact-preservation claim заповнено `verification_by`,
   `verification_date` і `resolution_evidence`.
7. Для `adjudication_required` існує `adjudication_reference`.
8. Для deferred intellectual issue вказано `intellectual_issue_status` і, якщо
   вже створено, `controlled_revision_reference`.

Сам запис proposed disposition або зміна `record_status` без цих полів не
закриває discrepancy для gate.

## 8. Класи розбіжностей

### A. Representation Error

**Визначення:** candidate неточно кодує source content або structure, хоча
правильне представлення однозначно визначається з source.

**Приклад:** quotation перетворено на звичайний paragraph; emphasis застосовано
не до того слова.

**Semantic risk:** від низького до підтвердженої зміни reading.

**Типова severity:** S1–S4.

**Automatic correction:** лише deterministic S1.

**Human/adjudication review:** human review для S2–S4; adjudication лише якщо
виникає source ambiguity.

**Блокує PASS:** S2–S4 блокують до correction і re-review.

**Додаткові required fields:** тип representation, expected mapping,
before/after rendering.

**Required disposition:** `corrected_representation`, `reclassified` або
`accepted_no_change` для verified S1.

### B. Structural Loss

**Визначення:** у candidate втрачено hierarchy, containment, grouping,
membership або section boundary.

**Приклад:** subsection став peer section; nested list став набором незалежних
paragraphs.

**Semantic risk:** scope і relation можуть бути прочитані неправильно.

**Типова severity:** S2–S4.

**Automatic correction:** ні; механічне відновлення дозволене operator лише з
review.

**Human/adjudication review:** human review обов’язковий.

**Блокує PASS:** так, доки structure не відновлено й перевірено.

**Додаткові required fields:** source node, target node, parent/child mapping,
structure map.

**Required disposition:** `corrected_representation` або
`requires_human_review`.

### C. Semantic Change

**Визначення:** candidate змінює meaning, scope, modality, causal relation,
epistemic force або conclusion source.

**Приклад:** “може сприяти” перетворено на “спричиняє”; qualified claim став
universal.

**Semantic risk:** безпосередня corruption знання.

**Типова severity:** S3–S4, за підтвердження — S4.

**Automatic correction:** заборонене.

**Human/adjudication review:** human review обов’язковий; adjudication для
спірного source reading.

**Блокує PASS:** завжди до exact restoration і re-review.

**Додаткові required fields:** paired excerpts, changed semantic dimension,
affected claims/boundaries.

**Required disposition:** `corrected_representation`; якщо source reading
спірний — `requires_source_adjudication`.

### D. Omission

**Визначення:** source content повністю або частково відсутній у candidate.

**Приклад:** пропущено paragraph, footnote, caveat, list item або table row.

**Semantic risk:** від локальної втрати structure до зміни conclusion.

**Типова severity:** S2–S4.

**Automatic correction:** automatic closure заборонене; exact reinsertion
може виконати operator із review.

**Human/adjudication review:** human verification обов’язкова.

**Блокує PASS:** так, доки omission не відновлено й не перевірено.

**Додаткові required fields:** omitted source range, expected target location,
completeness evidence.

**Required disposition:** `corrected_representation`.

### E. Addition

**Визначення:** candidate містить content, якого немає у source і який не є
чітко відділеною дозволеною migration metadata.

**Приклад:** додане пояснення, citation, summary або “уточнене” conclusion.

**Semantic risk:** source provenance змішується з новим content.

**Типова severity:** S2–S4.

**Automatic correction:** очевидний S1 tool artifact може бути вилучений
автоматично з verification; інше — ні.

**Human/adjudication review:** human review обов’язковий для source-derived
body.

**Блокує PASS:** так, доки addition не вилучено або не доведено, що це
дозволена відокремлена metadata.

**Додаткові required fields:** added range, asserted origin, metadata/body
classification.

**Required disposition:** `corrected_representation`, `reclassified` або
`rejected_correction`.

### F. Reordering

**Визначення:** content units з’являються в іншій послідовності, ніж у source.

**Приклад:** caveat перенесено після conclusion; table переміщено до іншої
section.

**Semantic risk:** змінюється логіка, scope, anchoring або interpretation.

**Типова severity:** S2–S4.

**Automatic correction:** ні; exact restoration — operator із review.

**Human/adjudication review:** human review обов’язковий.

**Блокує PASS:** так, якщо source-derived reading order змінено.

**Додаткові required fields:** source order index, target order index, affected
anchors.

**Required disposition:** `corrected_representation` або
`requires_source_adjudication` для неоднозначного source order.

### G. Citation/Reference Corruption

**Визначення:** attribution, citation data, link, footnote, endnote або
reference relation втрачено чи змінено.

**Приклад:** citation вказує на неправильного автора; page number зник;
footnote anchor веде до іншої note.

**Semantic risk:** evidence і provenance стають неправильними або
неперевірними.

**Типова severity:** S2–S4.

**Automatic correction:** лише deterministic syntax repair S1; content repair
потребує review.

**Human/adjudication review:** human review кожної affected reference.

**Блокує PASS:** так для будь-якої невиправленої corruption.

**Додаткові required fields:** citation identifier, reference identifier,
source/target link, attribution fields.

**Required disposition:** `corrected_representation`; source citation defect —
`source_preserved_issue_deferred`.

### H. Table/Data Corruption

**Визначення:** candidate змінює table structure, cell value, unit, header,
row/column relation або note.

**Приклад:** значення зміщено на один column; merged header втрачено; empty
cell перетворено на zero.

**Semantic risk:** неправильні дані або relations.

**Типова severity:** S2–S4.

**Automatic correction:** лише deterministic syntax artifact S1; data repair
не закривається автоматично.

**Human/adjudication review:** human cell-level review обов’язковий.

**Блокує PASS:** так до повного table re-review.

**Додаткові required fields:** table ID, row/column/cell coordinates,
dimensions, units, merged-cell mapping.

**Required disposition:** `corrected_representation` або
`requires_source_adjudication`.

### I. Formatting-with-Meaning Loss

**Визначення:** втрачено formatting, яке кодує hierarchy, emphasis, warning,
scope, distinction, status або relation.

**Приклад:** strikethrough, що позначає rejected option, зник; numbering, яке
визначає sequence, перетворено на bullets.

**Semantic risk:** від прихованої distinction до зміни epistemic status.

**Типова severity:** S2–S4.

**Automatic correction:** ні, доки semantic role не підтверджено.

**Human/adjudication review:** human rendered comparison; adjudication для
невизначеної source convention.

**Блокує PASS:** так, якщо meaningful formatting не відновлено.

**Додаткові required fields:** formatting property, inferred role, rendering
evidence.

**Required disposition:** `corrected_representation`, `accepted_no_change`
після доведення cosmetic nature або `requires_source_adjudication`.

### J. Source Ambiguity

**Визначення:** source допускає кілька materially different readings або не
дає змоги однозначно визначити representation.

**Приклад:** незрозуміло, до якого heading належить paragraph; merged table
structure має дві можливі інтерпретації.

**Semantic risk:** migration operator може непомітно обрати одну
інтерпретацію.

**Типова severity:** S3 або S5.

**Automatic correction:** заборонене.

**Human/adjudication review:** human review обов’язковий; material alternatives
потребують adjudication.

**Блокує PASS:** так, якщо ambiguity впливає на representation. Може стати
non-blocking лише коли ambiguity faithfully preserved і це підтверджено.

**Додаткові required fields:** alternative readings, source evidence,
representation options, decision authority.

**Required disposition:** `requires_source_adjudication` або документоване
`source_preserved_issue_deferred`, якщо ambiguity можна зберегти без вибору.

### K. Source Defect

**Визначення:** проблема вже існує у source: typo, broken citation,
inconsistent numbering, factual defect або інша помилка джерела.

**Приклад:** source містить неправильний internal reference або дубльований
номер section.

**Intellectual/source risk:** залежить від defect, але сам defect не вимірюється
fidelity severity і не може виправлятися як representation error.

**Типова severity:** `null`, якщо defect faithfully preserved. Якщо defect
створює окрему representation ambiguity або version conflict, створюється
пов’язаний class J або L record із S3/S5.

**Automatic correction:** заборонене у source-derived content.

**Human/adjudication review:** human classification; intellectual correction —
лише controlled revision.

**Блокує PASS:** не блокує, якщо defect точно збережено, зареєстровано й
verified. Якщо неможливо визначити faithful reading, блокує не Source Defect
як такий, а пов’язаний Source Ambiguity або Version Conflict record.

**Додаткові required fields:** source defect evidence, preserved target
evidence, downstream handoff.

**Required disposition:** `source_preserved_issue_deferred` або
`controlled_revision_required`.

### L. Version Conflict

**Визначення:** існує конфлікт щодо active source, version, supersession або
manifest identity.

**Приклад:** filename вказує v1, metadata — v1.1, або дві tracked files мають
active status.

**Semantic risk:** мігрується неправильний історичний стан.

**Типова severity:** S5.

**Automatic correction:** заборонене.

**Human/adjudication review:** adjudication обов’язкове.

**Блокує PASS:** так; зазвичай блокує й початок conversion.

**Додаткові required fields:** усі candidate versions, hashes, manifest
entries, supersession evidence.

**Required disposition:** `requires_version_adjudication` із traceable decision.

### M. Conversion Tool Artifact

**Визначення:** conversion tool додає, спотворює або залишає технічний residue,
якого немає у source.

**Приклад:** зайві anchors, повторний heading, HTML residue, неправильне
escaping або duplicated text.

**Semantic risk:** від cosmetic noise до omission/addition/corruption.

**Типова severity:** S1–S4.

**Automatic correction:** дозволена лише для deterministic S1 artifact;
решта — за primary effect class.

**Human/adjudication review:** human verification обов’язкова для S2+.

**Блокує PASS:** S2–S4 блокують до correction; S1 може бути non-blocking після
verification.

**Додаткові required fields:** tool/version, reproducibility, generated token
або pattern, affected units.

**Required disposition:** `corrected_representation` або reclassification до
Omission, Addition, Structural Loss чи Semantic Change.

### N. Normalization Difference

**Визначення:** навмисна технічна відмінність, потрібна для коректного
Markdown, без semantic loss.

**Приклад:** Word heading style відображено як `##`; line breaks нормалізовано;
decorative font не перенесено.

**Semantic risk:** низький, але лише після verification.

**Типова severity:** S0–S1.

**Automatic correction:** дозволена для детермінованих випадків.

**Human/adjudication review:** human review потрібний, якщо є сумнів щодо
meaningful formatting або structure.

**Блокує PASS:** ні після verification; сумнів reclassified до I, J або B.

**Додаткові required fields:** normalization rule, reason, equivalence evidence.

**Required disposition:** `accepted_no_change` або `reclassified`.

### O. Potential Intellectual Issue Discovered During Migration

**Визначення:** source, імовірно, містить conceptual, factual, logical,
terminological або argumentative problem, який не є conversion error.

**Приклад:** твердження виглядає надмірно universal; два source paragraphs
можуть суперечити один одному; causal claim не має достатнього support.

**Intellectual risk:** може бути високим для knowledge quality, але це окремий
об’єкт від migration fidelity risk.

**Типова severity:** `null`. S0–S5 до intellectual issue не застосовується.

**Intellectual issue status:** `observed`, `recorded`, `deferred` або
`handed_off`.

**Automatic correction:** категорично заборонене.

**Human/adjudication review:** реєстрація й routing до controlled revision;
міграційний reviewer не adjudicates істинність claim.

**Блокує PASS:** сам intellectual issue не блокує fidelity, якщо source
faithfully preserved, preservation verified, final deferral disposition
accepted і candidate не містить repair. Якщо operator “виправив” issue,
створюється окремий class C або E migration discrepancy із S0–S5; саме він
блокує PASS.

**Додаткові required fields:** affected claim/source location, reason for
concern, preservation evidence, proposed downstream review, no-repair
confirmation.

**Required disposition:** `source_preserved_issue_deferred` та, за окремим
рішенням, `controlled_revision_required`.

## 9. Gate-effect rules

1. Відкрита S4 або S5 migration discrepancy завжди означає fidelity `FAIL`.
2. Відкрита S2 migration discrepancy блокує verdict до correction/re-review
   або accepted reclassification.
3. S3 migration discrepancy блокує, доки fidelity risk не отримав accepted
   disposition.
4. Source Defect і Potential Intellectual Issue мають `severity: null`, не
   виправляються в migration і не блокують fidelity після verified exact
   preservation та accepted deferral.
5. Якщо source/intellectual issue спричиняє representation risk, цей risk
   отримує окремий linked migration discrepancy record із S0–S5.
6. `PASS WITH NON-BLOCKING DISCREPANCIES` можливий лише за gate-relevant
   resolved records і повного evidence.
7. Record із `fidelity_effect: undetermined`, `disposition_status`, відмінним
   від `accepted`, або non-final `record_status` блокує verdict.
8. Закритий record не можна видаляти; provenance зберігається.

## 10. Machine-readable record example

```yaml
discrepancy_id: "RQ01-MIG-0001"
record_kind: "migration_discrepancy"
artifact_id: "STR-P01-RQ01"
source_path: "knowledge-books/strategy/part-01/source-docx/current/Strategy_Knowledge_Book_Part01_RQ01_Nature_v1.docx"
source_baseline_sha: "c0116d3"
source_hash: "<sha256-or-git-blob>"
target_path: "knowledge-books/strategy/part-01/chapters/RQ01_Nature.md"
class: "B_STRUCTURAL_LOSS"
secondary_classes: []
severity: "S2"
fidelity_effect: "blocking"
source_location: "<section/paragraph/table-anchor>"
target_location: "<heading/line/anchor>"
source_observation: "<опис source українською>"
target_observation: "<опис candidate українською>"
migration_fidelity_risk: "<ризик неточного представлення українською>"
evidence:
  - "<path-or-review-reference>"
detected_by: "<actor-or-role>"
detection_stage: "fidelity_review"
owner: "<actor-or-role>"
correction_authority: "operator_with_review"
proposed_disposition: "corrected_representation"
accepted_disposition: null
disposition_status: "proposed"
disposition_by: null
disposition_date: null
record_status: "correction_required"
resolution_evidence: []
verification_by: null
verification_date: null
intellectual_issue_status: null
adjudication_reference: null
controlled_revision_reference: null
```

Keys та enum-like values є stable technical identifiers. Описові values мають
бути українською відповідно до language policy.

## 11. Мінімальний workflow

1. Виявити відмінність.
2. Створити discrepancy record до correction.
3. Встановити `record_kind`, primary class і, за потреби, secondary classes.
4. Для migration discrepancy визначити S0–S5; для faithfully preserved
   source/intellectual issue встановити `severity: null`.
5. Визначити `fidelity_effect`, owner і correction authority.
6. Додати evidence та proposed disposition.
7. Виконати дозволену correction або передати record на review/adjudication.
8. Провести verification і заповнити verification provenance.
9. Прийняти або відхилити disposition через уповноважене рішення.
10. Перевести record у `resolved` або `deferred` лише після виконання §7.3.
11. Передати повний log до Fidelity Protocol для final verdict.

## 12. Межа між migration і intellectual revision

Критичне правило:

> Виявлення проблеми у source не надає права виправити її під час migration.

Правильний маршрут:

Potential Intellectual Issue
→ faithful preservation у candidate
→ `record_kind: intellectual_issue`, `severity: null`
→ `source_preserved_issue_deferred`
→ окремий controlled revision process

Неправильний маршрут:

Potential Intellectual Issue
→ мовчазне переписування candidate
→ fidelity PASS

Другий маршрут створює окремий Semantic Change або Addition migration
discrepancy із fidelity severity і має блокувати PASS. Сам intellectual issue
не отримує fidelity severity.

## 13. Умова перегляду v1

Taxonomy слід переглянути після RQ-01 pilot, якщо:

- реальна discrepancy не належить жодному class;
- classes систематично перетинаються без корисної distinction;
- severity не відображає operational risk;
- correction authority є надто широким або надто вузьким;
- source issues регулярно помилково трактуються як migration errors;
- machine-readable fields недостатні для traceability.

Перегляд taxonomy не може ретроспективно видаляти або приховувати records,
створені за v1.
