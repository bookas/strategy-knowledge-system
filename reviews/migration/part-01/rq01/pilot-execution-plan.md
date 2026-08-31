# RQ-01 Migration Pilot — Pre-Conversion Execution Plan

## 1. Статус і межі

Цей план операціоналізує схвалені:

- [`Migration Fidelity Protocol v1`](../../../../methodology/migration/migration-fidelity-protocol-v1.md);
- [`Migration Discrepancy Taxonomy v1`](../../../../methodology/migration/migration-discrepancy-taxonomy-v1.md).

Він не змінює methodology і не є Entry Gate Decision Record.

Поточні межі:

- `rq01_pilot_entry_authorized: false`;
- RQ-01 conversion не авторизовано;
- target Markdown ще не створено;
- intellectual revision і translation заборонено;
- canonical promotion заборонено.

## 2. Source Identity Check

### До conversion

Оператор має повторно зафіксувати:

- repository path:
  `knowledge-books/strategy/part-01/source-docx/current/Strategy_Knowledge_Book_Part01_RQ01_Nature_v1.docx`;
- SHA-256:
  `81639A1143B98E7CFC763910760613458A10BF83ED732CE360FF0DA11A05CD36`;
- Git blob: `b86a93605a785f179c8c461e38d604056f9e2672`;
- immutable working baseline: `d4b40ca7981b41177cf862f18ba278774175f6ef`;
- migration baseline: `c0116d3`;
- file size: `50707` bytes;
- successful ordinary read і OOXML package readability.

Будь-яка невідповідність зупиняє conversion і маршрутизується як source/version
issue. Заборонено створювати або підміняти source модифікованою копією.

### Після conversion і review

Source SHA-256 і Git blob перевіряються повторно. DOCX не може бути у migration
diff. Зміна identity зупиняє fidelity review до traceable source/version
adjudication.

## 3. Actor Map

### Converter

**Operational role:** `Codex Conversion Operator`

**Execution identity:** має бути зафіксована до conversion.

Відповідальність:

- faithful DOCX → Markdown representation;
- збереження source language;
- conversion provenance та evidence;
- реєстрація discrepancies;
- лише дозволені representation corrections;
- жодного intellectual improvement або fidelity verdict.

### Independent Fidelity Reviewer

**Operational role:** fresh isolated Codex review context.

**Execution identity:** має бути зафіксована до conversion і відрізнятися від
converter.

Reviewer:

- починає з immutable source і candidate identities;
- не виконує conversion;
- не приймає converter reasoning як доказ;
- спочатку виконує власне source/candidate comparison, а conversion evidence
  використовує окремо там, де цього вимагає Protocol;
- не виконує material correction, яку потім independently verifies;
- не проводить intellectual revision;
- лише після повного Pre-Verdict Review Package може видати fidelity verdict.

### Adjudicator

**Operational role:** repository owner, який явно діє як adjudicator.

Застосовується лише для traceable source/version, classification, authority або
іншого рішення, якого вимагає approved methodology. Ownership саме по собі не є
adjudication decision.

### Correction Author і Material Correction Verifier

Correction Author призначається лише за наявності correction. Для S2–S4 або
іншої material correction verifier має бути іншим actor. Correction author не
може бути значенням `verification_by` власної material correction.

### Independence Controls

Перед conversion actor map має містити фактичні identities, non-identity checks,
попередню участь у methodology, conflicts і, якщо потрібен exception, окремий
traceable exception record. Methodology approval не скасовує independence.

## 4. Evidence Locations

Operational root:

`reviews/migration/part-01/rq01/`

Поточні control files:

- `discrepancy-log.yaml` — єдиний RQ-01 pilot Discrepancy Log;
- `pilot-execution-plan.md` — actor, comparison, evidence та correction plan.

Candidate path, який може бути створений лише після окремого Entry Gate
authorization:

`knowledge-books/strategy/part-01/chapters/RQ01_Nature.md`

Додаткові evidence artifacts створюються лише коли реально виникають під час
authorized pilot; speculative empty files не створюються.

## 5. Structural Inventory

Expected source inventory для pilot evidence:

- 156 body paragraphs;
- 20 Heading 1;
- 12 Heading 2;
- 31 bulleted items;
- 25 numbered items;
- 6 tables;
- 54 table rows;
- 160 table cells;
- no images;
- no equations;
- no footnotes/endnotes;
- no tracked changes/comments.

Ці значення є expected evidence, а не безумовною істиною. Converter має
незалежно повторити inventory та зареєструвати будь-яку різницю до conversion.

## 6. Ordered Content Comparison

Converter формує ordered source-block inventory і mapping кожного source unit
до candidate unit. Перевірка має виявляти:

- omission та addition;
- reordering;
- semantic change;
- втрату heading hierarchy;
- втрату bullet/number semantics;
- зміщення boundary, qualification, audit або Open Question blocks.

Independent reviewer проходить mapping від першого до останнього source block
без sampling і окремо перевіряє candidate на content, якого немає у source.

## 7. Table Review

Для всіх шести tables обов’язкова 100% cell-level та structural verification:

- table, row і effective column counts;
- row/column relationships;
- cell text і ordering;
- headers;
- відсутність merged-cell distortion;
- notes та meaning-bearing formatting;
- функціонально еквівалентне Markdown representation.

Flattening, data movement, lost headers або ambiguity є blocking до accepted
disposition, correction і re-review.

## 8. Citation / Reference Review

Перевіряються без sampling:

- inline citation markers;
- DOI strings;
- reference entries та ordering;
- attribution і relation між citation та reference;
- відсутність invented links;
- відсутність citation improvement або repair source defects.

## 9. Emphasis / Formatting Review

Source і candidate comparison має визначити, чи збережено meaning-bearing:

- bold та italic;
- headings;
- numbered і bulleted lists;
- table headers і distinctions;
- page/section boundary, якщо він впливає на meaning;
- header/footer provenance, якщо його content переноситься або відображається
  як migration metadata.

Cosmetic differences маршрутизуються як verified Normalization Difference.
При сумніві щодо semantic role formatting не вважається cosmetic автоматично.

## 10. Language / Semantic Review

Обов’язково підтвердити:

- Russian source text лишився Russian;
- English technical terminology збережено;
- translation і paraphrase відсутні;
- theory, citations і conclusions не покращено;
- modal, negation, uncertainty та contestability wording збережено;
- distinctions, qualifications, caveats, boundary cases і audit roles збережено;
- apparent source/intellectual issues faithfully represented і routed окремо.

## 11. Rendered / Visual Review

До verdict evidence package має назвати exact tools, versions, parameters і
дати. Reproducible procedure:

1. Render source DOCX за допомогою packaged `render_docx.py` у versioned або
   однозначно ідентифікований review-output directory.
2. Render candidate Markdown у стабільний HTML/PDF або інший inspection view;
   зафіксувати renderer, version і parameters.
3. Переглянути всі source та candidate pages/views, особливо tables, headings,
   lists, emphasis, header/footer і section boundary.
4. Звірити visual findings зі structural inventory та ordered mapping.
5. Зареєструвати material representation loss у Discrepancy Log до correction.

Pixel identity не вимагається. Visual review визначає representation loss, а не
естетичну схожість.

## 12. Pre-Verdict Review Package

До independent verdict мають існувати:

1. exact source identity і post-conversion recheck;
2. exact candidate path, SHA-256 та Git/worktree identity;
3. actor map, non-identity checks і independence statement;
4. conversion tool/version/parameters, dates і operator identity;
5. independently confirmed structural inventory;
6. complete ordered-block і source-section → candidate-section mapping;
7. 100% table verification evidence;
8. citation/reference verification;
9. language, semantic, qualification й formatting checks;
10. rendered/visual comparison evidence;
11. complete `discrepancy-log.yaml`;
12. correction before/after evidence та verification, якщо застосовно;
13. automated-check results;
14. confirmation that source DOCX is unchanged;
15. reviewer independence statement.

Відсутність evidence для застосовної category є blocking condition. Fidelity
verdict і canonical decision не входять до Pre-Verdict Package.

## 13. Discrepancy and Correction / Re-Review Workflow

`DETECTION → CLASSIFICATION → ROUTING → AUTHORIZED CORRECTION → INDEPENDENT
VERIFICATION → DISPOSITION → RE-REVIEW → VERDICT ELIGIBILITY`

1. **Detection:** difference або source/intellectual issue реєструється до
   correction; fabricated findings заборонені.
2. **Classification:** застосовуються approved classes A–O, `record_kind`,
   S0–S5 лише для migration discrepancies та `severity: null` для faithfully
   preserved source/intellectual issues.
3. **Routing:** встановлюються fidelity effect, owner, correction authority і
   proposed routing disposition.
4. **Authorized correction:** automatic correction дозволена лише для
   deterministic S0/S1 Representation Error, Conversion Tool Artifact або
   Normalization Difference. S2 може бути mechanically corrected operator, але
   не automatically closed. S3–S5 не виправляються автоматично.
5. **Independent verification:** material correction verifier не може бути її
   author; зберігаються before/after evidence, actor і dates.
6. **Disposition:** closure потребує terminal accepted disposition. Routing або
   proposed disposition не закриває record.
7. **Re-review:** перевіряються corrected unit, parent section, adjacent units,
   relevant automated checks і regression; після S3/S4 повторно перевіряється
   вся fidelity category.
8. **Verdict eligibility:** unresolved blocking discrepancy, undetermined
   fidelity effect або non-final disposition забороняє fidelity PASS.

Source Defect і Potential Intellectual Issue не ремонтуються в candidate.
Source/version ambiguity, S5 або genuinely adjudication-required record
передаються explicit traceable adjudicator. Converter не обирає source reading
мовчки.

## 14. Pre-Conversion Confirmation Checklist

До окремого Entry Gate confirmation необхідно підтвердити:

- [ ] source ordinary-read access, SHA-256, blob, size та OOXML readability;
- [ ] clean immutable Git baseline;
- [ ] фактична converter identity;
- [ ] інша фактична independent reviewer identity;
- [ ] non-identity/conflict checks;
- [ ] initialized empty `discrepancy-log.yaml` без fabricated records;
- [ ] comparison і rendering procedure accepted for execution;
- [ ] correction/re-review workflow accepted for execution;
- [ ] target відсутній і RQ-01 conversion ще не розпочато;
- [ ] `rq01_pilot_entry_authorized` лишається `false` до окремого decision record;
- [ ] canonical promotion лишається unauthorized;
- [ ] OQ-062 лишається окремою pre-canonical-promotion condition.

Цей checklist не є authorization і не може бути self-approved converter.
