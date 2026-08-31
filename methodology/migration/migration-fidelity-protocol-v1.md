---
artifact_id: SKS-MIG-FID-001
artifact_type: migration_control_methodology
title: "Протокол перевірки точності міграції v1"
version: "1.0"
status: candidate
review_status: revise_and_re_review
approval_status: pending_re_review
language: uk
open_question: OQ-059
uses_taxonomy: "methodology/migration/migration-discrepancy-taxonomy-v1.md"
pilot_scope: RQ-01
canonical_effect: none
---

# Протокол перевірки точності міграції v1

## 1. Призначення

Цей протокол визначає, як встановити, чи є candidate Markdown достатньо
точним представленням вихідного DOCX для завершення fidelity review.

Протокол застосовується до зміни представлення:

DOCX → Markdown

Він не дозволяє:

- інтелектуально переглядати зміст;
- перекладати текст;
- виправляти концептуальні проблеми джерела;
- змінювати висновки, межі тверджень або застереження;
- надавати Markdown canonical status.

Статус цього документа — `candidate`. До окремого схвалення він не надає
permission to convert RQ-01.

## 2. Нормативна основа

Протокол реалізує чинні правила з таких джерел:

- [`AGENTS.md`](../../AGENTS.md);
- [`agents/core/repository-rules.md`](../../agents/core/repository-rules.md);
- [`migration/METHODOLOGY_STATE.md`](../../migration/METHODOLOGY_STATE.md);
- [`migration/MIGRATION_PLAN.md`](../../migration/MIGRATION_PLAN.md);
- [`migration/MIGRATION_MANIFEST.yaml`](../../migration/MIGRATION_MANIFEST.yaml);
- [`migration/ARCHITECTURE_DECISIONS.md`](../../migration/ARCHITECTURE_DECISIONS.md),
  зокрема ADR-023, ADR-024, ADR-025, ADR-026, ADR-027, ADR-037, ADR-048 і
  ADR-049;
- [`migration/OPEN_QUESTIONS.md`](../../migration/OPEN_QUESTIONS.md), зокрема
  OQ-059, OQ-060 та OQ-062.

У разі конфлікту цей протокол не скасовує repository governance. Операція
зупиняється, а конфлікт реєструється для окремого рішення.

## 3. Пов’язана taxonomy

Кожна виявлена відмінність класифікується за документом
[`Migration Discrepancy Taxonomy v1`](./migration-discrepancy-taxonomy-v1.md).

Розподіл функцій є обов’язковим:

- Taxonomy визначає клас, severity, correction authority, обов’язкові поля та
  disposition розбіжності.
- Цей Protocol визначає сукупний fidelity verdict для конкретного артефакту.
- Taxonomy не може самостійно оголосити `PASS` або `FAIL`.
- Кількість чи відсоток збігів не можуть замінити семантичний review.

## 4. Основні терміни

**Source artifact** — DOCX, визначений manifest як вихідний артефакт і
зафіксований у незмінному Git baseline.

**Candidate Markdown** — представлення source artifact, яке ще не має
canonical status.

**Conversion operator** — людина або агент, що створює candidate Markdown і
виправляє дозволені representation errors.

**Fidelity reviewer** — окрема review-функція, що порівнює source artifact із
candidate Markdown і формує findings та verdict.

**Discrepancy Log** — повний реєстр усіх виявлених розбіжностей, їх доказів,
severity, статусів і dispositions.

**Faithful representation** — представлення, яке зберігає інтелектуальний
зміст, структуру значення, порядок, застереження, межі, provenance та інші
семантично важливі властивості джерела.

**Structural normalization** — зміна синтаксису або технічної структури, що
покращує Markdown-представлення без зміни значення.

## 5. Розподіл повноважень

| Повноваження | Хто може надати | Мінімальна передумова | Чого не дозволяє |
|---|---|---|---|
| Permission to convert | Authority, названий у traceable RQ-01 Entry Gate Decision Record | `RQ-01 PILOT ENTRY GATE: PASS` із decision provenance | Не дозволяє довільні виправлення чи canonical promotion |
| Permission to correct representation errors | Процес міграції в межах Taxonomy та цього Protocol | Зареєстрований discrepancy і допустимий correction authority | Не дозволяє виправляти source defects або intellectual issues |
| Permission to declare fidelity verdict | Fidelity reviewer; для спірних випадків — adjudication | Завершений Pre-Verdict Review Package, review і Discrepancy Log | Не надає canonical status |
| Permission to promote Markdown to canonical | Окремий canonical-promotion authority згідно з repository governance | Fidelity verdict, окремі promotion conditions і врегульований OQ-062 | Не випливає автоматично з конвертації або fidelity PASS |

Одна дія не створює наступне повноваження автоматично.

### 5.1 Candidate, immutable review baseline та approval

Методологічний artifact може перебувати у трьох різних process states:

1. **Candidate artifact state** — content редагується; `status: candidate` не
   надає operational authority.
2. **Immutable candidate review baseline** — exact candidate зафіксовано у Git
   commit, а review request містить commit SHA і SHA-256 кожного artifact.
   Commit лише створює незмінну review version і не означає approval.
3. **Approved artifact state** — traceable Methodology Approval Record прийняв
   exact reviewed hashes. Лише після цього metadata може відобразити
   `status: approved`.

Methodology Approval Record має містити щонайменше:

- `approval_id`;
- `artifact_id` і version;
- immutable candidate Git SHA;
- reviewed artifact SHA-256;
- decision — `approved`, `revise_and_re_review` або `rejected`;
- `decision_by`;
- `decision_date`;
- review/adjudication reference;
- disposition accepted findings.

Самостійна зміна front matter або manifest з `candidate` на `approved` без
такого record не має governance effect.

RQ-01 Entry Gate approval фіксується окремим Entry Gate Decision Record:

- `gate_decision_id`;
- approval references для Protocol і Taxonomy;
- immutable working baseline Git SHA;
- source path і source hash;
- target path і scope;
- conversion operator;
- fidelity reviewer;
- verdict — `pass` або `fail`;
- `decision_by` і `decision_date`;
- evidence/reference.

Поле `pilot_entry_authorized: true` може з’явитися лише як відображення цього
record, а не як самодостатнє рішення.

## 6. Preconditions для будь-якої міграції

До запуску conversion мають бути виконані всі умови:

1. Source artifact однозначно визначений у
   `migration/MIGRATION_MANIFEST.yaml`.
2. Source artifact існує у визначеному repository path.
3. Source artifact зафіксований у названому immutable Git baseline.
4. Перед початком записано щонайменше Git SHA, blob identity або SHA-256
   source artifact.
5. Working tree чистий або всі сторонні зміни явно ізольовані й не можуть
   потрапити до migration diff.
6. Target path визначений у manifest.
7. Scope обмежений одним явно названим source artifact.
8. Існують Methodology Approval Records для exact hashes цього Protocol і
   пов’язаної Taxonomy.
9. Визначено conversion operator і fidelity reviewer.
10. Визначено місце Discrepancy Log та формат Pre-Verdict Review Package.
11. Зафіксовано інструмент, його версію, параметри й суттєві проміжні кроки.
12. Зафіксовано source language; translation заборонений.
13. Підтверджено, що conversion не включає intellectual revision.
14. Визначено, як буде перевірено незмінність source artifact після роботи.
15. Exact methodology candidates, що використовуються для Entry Gate,
   зафіксовані в immutable Git review baseline; наявність commit не
   інтерпретується як approval.

Невиконання будь-якої умови означає `ENTRY GATE: FAIL`.

## 7. Незмінність source artifact

Source DOCX має залишатися байт-ідентичним визначеному baseline протягом
усього migration cycle.

Обов’язкові докази:

- repository path;
- baseline Git SHA;
- source blob identity або SHA-256 до conversion;
- повторна перевірка identity після завершення review;
- підтвердження відсутності DOCX у migration diff.

Якщо source identity змінилася, fidelity review зупиняється з `FAIL`, доки не
буде встановлено правильний baseline. Нова версія DOCX не може мовчазно
підмінити затверджене джерело.

## 8. Межі conversion procedure

### 8.1 Дозволено

- перенести текст без зміни формулювань;
- відобразити Word headings засобами Markdown;
- перетворити списки, таблиці, примітки та посилання у функціонально
  еквівалентний Markdown;
- нормалізувати line wrapping, пробіли й технічний Markdown syntax;
- замінити декоративне форматування, якщо воно не несе значення;
- виправити зареєстровані representation errors у межах correction authority;
- додати migration metadata поза змістом розділу, якщо воно чітко відділене
  від source-derived content і прямо передбачене процедурою.

### 8.2 Заборонено

- перекладати текст іншою мовою;
- перефразовувати для ясності або стилю;
- виправляти фактичні, логічні, термінологічні чи концептуальні проблеми
  джерела;
- посилювати або послаблювати scope тверджень;
- додавати нові аргументи, приклади, пояснення, citations або conclusions;
- видаляти повтори, counterarguments, caveats чи unresolved questions;
- змінювати порядок для кращої композиції;
- об’єднувати або розділяти поняття так, що змінюється їхня роль;
- перетворювати migration summary на джерело змісту;
- проводити canonical promotion.

## 9. Pre-Verdict Review Package

До початку формування verdict reviewer має отримати завершений Pre-Verdict
Review Package. Це набір входів для review, а не його фінальний результат.

Package містить:

1. Source identity: path, Git SHA, blob identity або SHA-256.
2. Candidate identity: path і відповідний diff або commit/worktree state.
3. Назву й версію conversion tool та застосовані параметри.
4. Source language і підтвердження відсутності translation.
5. Інвентар headings із їхнім порядком та рівнями.
6. Інвентар paragraphs або еквівалентних content blocks.
7. Інвентар lists, notes, quotations та callouts, якщо вони є.
8. Інвентар tables із кількістю рядків, стовпців, merged-cell semantics та
   заголовками.
9. Інвентар citations, footnotes, hyperlinks і references.
10. Mapping source sections → Markdown sections.
11. Повний Discrepancy Log.
12. Перелік corrections із before/after evidence.
13. Результати automated checks.

Відсутність доказу для застосовної категорії є blocking condition.

Fidelity verdict, final accepted dispositions, reviewer decision і
canonical-status statement не входять до Pre-Verdict Review Package. Вони
створюються після review у Final Pilot Review Record, визначеному в §19.

## 10. Методи порівняння

### 10.1 Automated checks

Автоматизовані перевірки можуть включати:

- порівняння повного extracted text;
- кількість і порядок headings;
- кількість content blocks;
- пошук пропущених або доданих text spans;
- перевірку link targets;
- зіставлення citation/reference identifiers;
- порівняння table dimensions і cell values;
- перевірку source hash;
- перевірку Markdown syntax та internal paths.

Automated checks є допоміжними. Вони не встановлюють семантичну тотожність і
не можуть бути єдиною підставою для verdict.

### 10.2 Семантичне порівняння

Reviewer послідовно порівнює rendered DOCX із rendered або структурно
прочитаним Markdown section-by-section.

Для кожного змістового блоку reviewer перевіряє:

- чи збережено повний зміст;
- чи не змінилося значення речень і зв’язків між ними;
- чи збережено negation, modality, uncertainty та scope;
- чи не зникли caveats, exceptions або counterarguments;
- чи не додано інтерпретацію, якої немає в source;
- чи технічна нормалізація не змінила читання.

### 10.3 Структурне порівняння

Reviewer зіставляє карту source structure з Markdown structure та перевіряє:

- hierarchy;
- containment;
- adjacency;
- list membership;
- table membership;
- note/reference anchoring;
- section ordering;
- review/audit boundaries.

## 11. Категорії fidelity review

### 11.1 Content fidelity

**Має бути збережено:** усі заголовки, абзаци, речення, спискові елементи,
цитати, примітки, підписи, research questions, conclusions та інші content
units.

**Може змінитися без semantic loss:** line wrapping, Markdown escaping,
технічні пробіли, еквівалентне подання списку або quotation syntax.

**Discrepancy:** пропуск, додавання, неточне відтворення, paraphrase або
злиття/поділ content units зі зміною читання.

**Blocking:** будь-який невиправлений omission, addition або semantic change;
відсутній блок; невизначене походження доданого тексту.

**Non-blocking:** лише перевірена S0/S1 normalization difference без зміни
тексту або значення.

**Evidence:** extracted-text comparison, block inventory, source/target
locations, diff.

**Перевірка reviewer:** повне section-by-section читання та вибіркова повторна
перевірка exact text для кожного content type.

### 11.2 Structural fidelity

**Має бути збережено:** heading hierarchy, section boundaries, вкладеність,
list membership, relation між основним текстом, примітками й додатками.

**Може змінитися:** Word styles можуть бути відображені Markdown headings,
lists, blockquotes або явно позначеними sections.

**Discrepancy:** flattening hierarchy, неправильний heading level, розрив
section containment, перетворення list items на непов’язані paragraphs.

**Blocking:** структура змінює scope, належність, порядок аргументу або
можливість ідентифікувати частину джерела.

**Non-blocking:** інше технічне кодування тієї самої структури, підтверджене
structure map.

**Evidence:** heading tree, source-to-target section map, rendered views.

**Перевірка reviewer:** зіставлення кожного structural node та його parent,
siblings і content range.

### 11.3 Citation/reference fidelity

**Має бути збережено:** citation text, author/year/page data, footnote/endnote
content, reference entries, anchors, hyperlinks і зв’язок citation → source.

**Може змінитися:** технічний syntax link або footnote, якщо content і target
залишаються еквівалентними.

**Discrepancy:** зламане посилання, втрачена footnote, змінений page number,
неправильний anchor, citation без reference або навпаки.

**Blocking:** будь-яка corruption, що змінює attribution, evidence або
перевірність; невідновлена missing reference.

**Non-blocking:** лише явно зареєстрована source defect, відтворена без змін,
або перевірена syntax normalization.

**Evidence:** повний citation/reference inventory, link check, mapping і
rendered verification.

**Перевірка reviewer:** перевірка кожного citation identifier, target і
reference entry; sampling недостатній для RQ-01 pilot.

### 11.4 Table fidelity

**Має бути збережено:** table identity, headers, row/column relation, cell
values, order, units, empty-cell meaning, notes і merged-cell semantics.

**Може змінитися:** visual styling, column width або Markdown/HTML syntax, якщо
relation і meaning залишаються точними.

**Discrepancy:** втрачена row/column, зміщена cell value, неправильний header,
flattening без збереження relations, змінена unit або note.

**Blocking:** будь-яка data corruption або втрата relation; таблиця, яку не
можна однозначно представити без рішення.

**Non-blocking:** layout difference без зміни даних і зв’язків.

**Evidence:** table-by-table inventory, dimensions, cell comparison, screenshots
або renderings для складних таблиць.

**Перевірка reviewer:** 100% cell-level verification для pilot; окрема
перевірка merged cells, headers і notes.

### 11.5 Ordering fidelity

**Має бути збережено:** порядок sections, paragraphs, list items, tables,
figures, notes і references, коли він визначає розвиток аргументу або scope.

**Може змінитися:** лише технічне розміщення metadata, яке чітко відділене від
source content і не змінює reading order.

**Discrepancy:** перестановка, винесення або зближення блоків, що не відповідає
source sequence.

**Blocking:** reordering із можливим впливом на logic, qualification,
reference anchoring або interpretation.

**Non-blocking:** технічне розташування non-source metadata поза content body.

**Evidence:** ordered block signature та source-to-target order map.

**Перевірка reviewer:** послідовний прохід від першого до останнього блоку без
sampling.

### 11.6 Distinction/boundary fidelity

**Має бути збережено:** явні concept distinctions, taxonomies, definitions,
scope boundaries, object/level distinctions і відносини між concepts.

**Може змінитися:** лише syntax presentation, якщо logical boundaries
залишаються очевидними й тотожними.

**Discrepancy:** злиття distinct concepts, втрата contrast marker, зміна
heading/list structure, що приховує taxonomy або boundary.

**Blocking:** будь-яка зміна, що може розширити, звузити або змішати concepts.

**Non-blocking:** візуальна нормалізація з повністю збереженою relation map.

**Evidence:** перелік ключових distinctions і mapping їх представлення.

**Перевірка reviewer:** семантична перевірка кожної визначеної distinction та
її обох або всіх сторін.

### 11.7 Qualification/caveat fidelity

**Має бути збережено:** uncertainty, modality, conditions, exceptions,
counterarguments, limitations, boundary cases і provisional status у source.

**Може змінитися:** технічне виділення за умови незмінності wording, scope і
зв’язку з qualified claim.

**Discrepancy:** втрачений `may`, `not`, condition, exception, caveat;
переміщення qualification від твердження; зміна provisional на definitive.

**Blocking:** будь-яка зміна epistemic force або scope.

**Non-blocking:** еквівалентне formatting представлення без зміни wording.

**Evidence:** inventory ключових qualifications, paired source/target excerpts
і location mapping.

**Перевірка reviewer:** цільова перевірка всіх negations, modal expressions,
exceptions і limitation sections у поєднанні з повним читанням.

### 11.8 Review/audit structure fidelity

**Має бути збережено:** research/review annotations, audit sections, findings,
open questions, verdicts, deferred issues і межа між research та review layers.

**Може змінитися:** Markdown syntax headings або callouts без зміни role,
status, content і containment.

**Discrepancy:** review finding подано як chapter conclusion; втрачено status;
audit layer змішано з educational prose; open question вилучено.

**Blocking:** будь-яке змішування epistemic roles або втрата audit content.

**Non-blocking:** еквівалентний Markdown container із документованим mapping.

**Evidence:** inventory review/audit blocks, role labels і structure map.

**Перевірка reviewer:** перевірка кожного review object, його status, parent
section і відмежування від основного тексту.

### 11.9 Provenance fidelity

**Має бути збережено:** title, version, source identity, historical status,
authorship/date metadata, supersession links та інша provenance information,
якщо вона присутня або визначена manifest.

**Може змінитися:** encoding metadata у front matter, якщо source-derived і
migration-added fields чітко розділені.

**Discrepancy:** неправильна version, приховане змішування metadata, втрачена
source identity або attribution.

**Blocking:** неможливо встановити, з якого source і baseline походить
candidate; version conflict; неправильний historical status.

**Non-blocking:** додана process metadata, чітко позначена як migration
metadata і перевірена проти manifest.

**Evidence:** manifest entry, source hash, front matter diff і provenance map.

**Перевірка reviewer:** звірка кожного provenance field із source, manifest і
Git baseline.

### 11.10 Formatting fidelity where formatting carries meaning

**Має бути збережено:** emphasis, indentation, numbering, symbols, color або
layout, якщо вони кодують distinction, warning, hierarchy, status, scope,
quotation, deletion або relation.

**Може змінитися:** font family, точний розмір, page break, margins, decorative
color, spacing і pagination, якщо вони не несуть значення.

**Discrepancy:** втрата semantic emphasis, list numbering, warning state,
relation або meaningful visual grouping.

**Blocking:** formatting loss змінює interpretation або приховує structure.

**Non-blocking:** cosmetic difference з documented determination, що meaning
відсутнє.

**Evidence:** rendered comparison, screenshots для спірних випадків і запис
рішення про semantic significance.

**Перевірка reviewer:** порівняння rendered source і target; будь-яка
невпевненість класифікується як Source Ambiguity до рішення.

## 12. Severity та вплив на gate

S0–S5 визначається Taxonomy і оцінює лише migration fidelity risk. Scale не
оцінює conceptual quality або істинність source. Verdict враховує class,
fidelity effect, record lifecycle і final accepted disposition.

Загальне правило:

- S0 — не блокує після реєстрації, якщо запис потрібний.
- S1 — не блокує після verification; може залишитися лише як accepted
  non-semantic discrepancy.
- S2 — блокує до correction і re-review або до обґрунтованої reclassification.
- S3 — блокує, доки migration fidelity risk не отримав accepted disposition.
- S4 — завжди блокує; candidate містить підтверджене semantic corruption.
- S5 — блокує conversion або fidelity verdict до adjudication source/version.

Faithfully preserved Source Defect або Potential Intellectual Issue має
`severity: null`. Він не блокує fidelity після verified exact preservation та
accepted deferral. Якщо candidate змінює такий issue або source issue створює
representation ambiguity, для цього створюється окремий migration discrepancy
record із S0–S5.

## 13. Correction rules

1. Усі corrections починаються з Discrepancy Log entry.
2. Автоматичне виправлення дозволене лише для deterministic S0/S1
   Representation Error, Conversion Tool Artifact або Normalization Difference.
3. S2 може бути mechanically corrected, але не може бути automatically closed;
   потрібна human/reviewer verification.
4. S3–S5 не виправляються автоматично.
5. Semantic Change, Source Ambiguity, Version Conflict і Potential Intellectual
   Issue потребують human review або adjudication відповідно до Taxonomy.
6. Source Defect та Potential Intellectual Issue не виправляються у candidate
   під час migration; source reading зберігається, issue відкладається до
   controlled revision.
7. Correction не може розширюватися за межі зафіксованої discrepancy.
8. Після correction зберігаються before/after evidence, actor, timestamp і
   correction authority.
9. Proposed disposition не закриває record. Потрібні final accepted
   disposition і provenance за спільною моделлю Taxonomy §7.
10. Protocol не вводить локальних aliases для lifecycle або disposition
    fields: використовується контрольована модель Taxonomy §§6–7.

## 14. Re-review rules

Після будь-якої correction reviewer має:

1. повторно перевірити виправлений unit;
2. перевірити його parent section і сусідні units;
3. повторити релевантні automated checks;
4. підтвердити відсутність regression;
5. заповнити `verification_by`, `verification_date` і resolution evidence;
6. переглянути сукупний verdict.

Після S3 або S4 correction повторно перевіряється вся категорія fidelity, а не
лише окремий рядок.

## 15. Reviewer independence

Для RQ-01 pilot незалежний fidelity reviewer є обов’язковим.

Reviewer:

- починає з того самого immutable source baseline;
- не підміняє conversion operator під час формування первинного verdict;
- не приймає conversion report як доказ без перевірки;
- має доступ до rendered DOCX, candidate Markdown, Pre-Verdict Review Package і
  Discrepancy Log;
- реєструє findings, але не виконує intellectual revision;
- ескалює спірні S3–S5 до adjudication;
- явно заявляє conflict of interest або попередню участь.

Для технічних S0/S1 checks допускається automated verification, але фінальний
pilot verdict залишається review-рішенням.

## 16. Fidelity verdicts

### 16.1 Спільні mandatory conditions для успішного verdict

І `PASS`, і `PASS WITH NON-BLOCKING DISCREPANCIES` вимагають одночасного
виконання всіх умов:

1. Усі застосовні fidelity categories перевірено.
2. Pre-Verdict Review Package повний.
3. Source identity підтверджено до й після review.
4. Reviewer independence виконано.
5. Немає migration discrepancy з `fidelity_effect: blocking` або
   `undetermined`.
6. Кожен migration discrepancy має gate-relevant resolved state за Taxonomy
   §7.3.
7. Усі corrections verified; correction provenance повний.
8. Немає неврахованої uncertainty щодо faithful representation.
9. Candidate не містить translation або intellectual revision.
10. Faithfully preserved source/intellectual issues мають `severity: null`,
    verified preservation і accepted deferral disposition.

**Residual non-blocking item** — gate-relevant resolved record, який не
потребує correction, але має залишитися явно розкритим у Final Pilot Review
Record. До нього належать accepted S0/S1 representation differences,
faithfully preserved Source Defects, Potential Intellectual Issues або інші
accepted non-blocking observations.

### 16.2 PASS

`PASS` видається тоді й лише тоді, коли:

- виконано всі common mandatory conditions; і
- кількість residual non-blocking items дорівнює нулю.

Усі migration discrepancies у цьому випадку або corrected and verified, або
закриті як `false_positive`/`not_applicable`, і жоден final record не потребує
окремого disclosure як залишкова відмінність.

**Worked example:** conversion tool надав одному heading неправильний level
(class B, S2). Operator відновив level, reviewer verified correction, final
disposition `corrected_representation` accepted, record став `resolved`.
Інших records немає. Verdict: `PASS`.

### 16.3 PASS WITH NON-BLOCKING DISCREPANCIES

`PASS WITH NON-BLOCKING DISCREPANCIES` видається тоді й лише тоді, коли:

- виконано всі common mandatory conditions; і
- існує щонайменше один residual non-blocking item; і
- кожен такий item має `fidelity_effect: non_blocking`, accepted disposition,
  owner, verification provenance та final `resolved` або `deferred` status.

**Worked example:** source містить очевидний typo. Candidate відтворює його
без змін. Source Defect має `record_kind: source_issue`, `severity: null`,
exact preservation verified, accepted disposition
`source_preserved_issue_deferred`, record status `deferred`. Blocking
discrepancies відсутні. Verdict:
`PASS WITH NON-BLOCKING DISCREPANCIES`.

### 16.4 FAIL

`FAIL` видається, якщо хоча б одна common mandatory condition не виконана.
Зокрема:

- source identity не підтверджено або source змінено;
- Pre-Verdict Review Package неповний;
- хоча б одна застосовна category не перевірена;
- існує blocking або undetermined discrepancy;
- record не має accepted final disposition або final lifecycle state;
- є невиправлений S2 або нерозв’язаний S3–S5;
- candidate містить omission, addition або semantic change;
- correction не verified або виконана поза authority;
- reviewer не може встановити faithful representation.

**Worked example:** candidate пропустив caveat, що обмежує scope claim (class D
із linked class C, S4). Record залишається `correction_required`; accepted
disposition і verification відсутні. Verdict: `FAIL`.

### 16.5 Детермінований порядок рішення

Reviewer застосовує правила в такому порядку:

1. Якщо будь-яка common mandatory condition не виконана → `FAIL`.
2. Інакше, якщо residual non-blocking item count = 0 → `PASS`.
3. Інакше → `PASS WITH NON-BLOCKING DISCREPANCIES`.

Отже, один reviewed migration cycle завжди отримує рівно один verdict.

## 17. Заборона percentage-only gate

Text-match percentage, paragraph count, citation count або інший quantitative
metric не може бути єдиною підставою для verdict.

Навіть 99,9% text match може приховувати втрату одного `not`, caveat, table
header або boundary condition. І навпаки, нижчий syntax match може бути
допустимим через коректне перетворення tables, footnotes або Markdown syntax.

Quantitative checks мають лише:

- виявляти зони ризику;
- підтверджувати completeness;
- підтримувати reviewer;
- забезпечувати repeatability.

## 18. RQ-01 Pilot Entry Gate

До початку RQ-01 conversion необхідно підтвердити:

1. Methodology Approval Record підтверджує approval exact SHA-256 цього
   Protocol у названому immutable Git review baseline.
2. Methodology Approval Record підтверджує approval exact SHA-256 Migration
   Discrepancy Taxonomy v1 у тому самому або явно пов’язаному review baseline.
3. Git working tree чистий.
4. Названо immutable working baseline SHA.
5. Source DOCX відповідає артефакту `STR-P01-RQ01` у manifest:
   `knowledge-books/strategy/part-01/source-docx/current/Strategy_Knowledge_Book_Part01_RQ01_Nature_v1.docx`.
6. Source identity звірено з baseline `c0116d3` або з його явно затвердженим
   незмінним наступником.
7. Target path є саме
   `knowledge-books/strategy/part-01/chapters/RQ01_Nature.md`.
8. Scope включає лише faithful representation RQ-01.
9. Translation, claim repair, conceptual improvement і canonical promotion
   явно заборонено.
10. Визначено conversion operator.
11. Визначено незалежного fidelity reviewer.
12. Створено порожній або початковий Discrepancy Log із required fields.
13. Визначено Pre-Verdict Review Package і rendering/comparison procedure.
14. Визначено correction та re-review workflow.
15. Підтверджено, що OQ-062 залишається окремою pre-canonical-promotion
   умовою.

Verdict Entry Gate:

- усі 15 умов виконано — `RQ-01 PILOT ENTRY GATE: PASS`;
- будь-яка умова не виконана — `RQ-01 PILOT ENTRY GATE: FAIL`.

Поточний `candidate` status без approved Methodology Approval Records означає,
що Entry Gate ще не пройдено. Front matter або manifest status не замінює
approval provenance.

## 19. Final Pilot Review Record і RQ-01 Pilot Fidelity Gate

Після отримання Pre-Verdict Review Package, виконання review і завершення
record dispositions незалежний reviewer формує Final Pilot Review Record. Це
output review, а не prerequisite для нього.

Final Pilot Review Record містить:

- source identity;
- candidate identity;
- Pre-Verdict Review Package identity;
- categories reviewed;
- automated check results;
- Discrepancy Log summary;
- corrections і re-review results;
- snapshot final `record_status`, `accepted_disposition`, `disposition_by`,
  `disposition_date`, `verification_by` і `verification_date` для всіх records;
- residual non-blocking items;
- reviewer independence statement;
- final verdict;
- verdict authority, date і evidence reference;
- canonical-status statement.

Допустимі фінальні verdicts:

- `RQ-01 PILOT FIDELITY: PASS`;
- `RQ-01 PILOT FIDELITY: PASS WITH NON-BLOCKING DISCREPANCIES`;
- `RQ-01 PILOT FIDELITY: FAIL`.

Якщо verdict `FAIL`, candidate не переходить до наступного process stage.
Причини виправляються або adjudicated, після чого запускається re-review.

## 20. Exit criteria

Fidelity cycle завершений лише коли:

- source залишився незмінним;
- candidate і review evidence ідентифіковані;
- усі categories перевірені;
- кожна migration discrepancy має class, S0–S5, final record status і accepted
  disposition;
- кожен faithfully preserved source/intellectual issue має `severity: null`,
  verified preservation і accepted deferral;
- усі blocking items закриті або процес завершено з `FAIL`;
- corrections пройшли re-review;
- reviewer видав один із визначених verdicts;
- Final Pilot Review Record містить decision і disposition provenance;
- manifest/process metadata може бути оновлено без проголошення canonical
  status;
- source DOCX збережено.

## 21. Canonical-promotion limitation

Fidelity verdict підтверджує лише якість representation.

Він не встановлює:

- що Markdown є canonical;
- що original DOCX більше не потрібний;
- що Part 01 knowledge переглянуто;
- що source defects виправлено;
- що OQ-062 вирішено;
- що bulk migration дозволена.

Canonical promotion потребує окремого gate, окремого authority та явно
визначеної source-of-truth policy після migration.

## 22. Умова перегляду v1

Протокол слід переглянути після першого повного RQ-01 pilot cycle, якщо:

- taxonomy не покриває фактичні discrepancies;
- gate створює хибні PASS або непропорційні FAIL;
- evidence requirements виявляються недостатніми або надмірними;
- складні DOCX structures не можуть бути перевірені наявними методами;
- review independence не забезпечує практичної надійності.

Зміни до protocol після pilot мають зберігати v1 у Git history і не можуть
ретроспективно змінити вже виданий verdict без окремого re-review.
