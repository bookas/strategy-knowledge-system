## Этап 2. Перенос интеллектуального контекста проекта

### Цель

Перенести из истории работы над Strategy Knowledge Book знания и решения, которые не полностью представлены в исходных DOCX-документах.

Задача этапа — сделать Git-репозиторий самодостаточным настолько, чтобы новый Codex-сеанс мог понять:

- зачем существует проект;
- что уже исследовано;
- какие архитектурные решения уже приняты;
- почему они были приняты;
- какая исследовательская методология действует;
- какие решения были отвергнуты;
- какие вопросы остаются открытыми;
- что разрешено и запрещено менять во время миграции;
- с какого состояния необходимо продолжать работу.

### Принцип

История чата не переносится целиком.

Вместо копирования всей переписки выполняется контролируемая трансляция:

Chat history
→ Significant Decisions
→ Project State
→ Methodology
→ Open Questions
→ Migration Context

Необходимо сохранять не каждую реплику, а интеллектуально значимое состояние проекта.

### Создаваемые документы

migration/
├── PROJECT_CONTEXT.md
├── PROJECT_STATE.md
├── METHODOLOGY_STATE.md
├── ARCHITECTURE_DECISIONS.md
├── OPEN_QUESTIONS.md
└── MIGRATION_MANIFEST.yaml

### PROJECT_CONTEXT.md

Назначение:
объяснить, что представляет собой Strategy Knowledge System и зачем он создаётся.

Содержит:

- purpose проекта;
- границы проекта;
- Knowledge Book concept;
- Research Corpus concept;
- Curriculum concept;
- Application Layer;
- основные принципы построения знания;
- различие universal knowledge и organizational application;
- роль Git и Codex;
- целевую архитектуру Knowledge System.

Не должен содержать подробный пересказ отдельных RQ.

### PROJECT_STATE.md

Назначение:
зафиксировать текущее состояние проекта на момент миграции.

Содержит:

- Part 01 status;
- RQ-01 — RQ-11 status;
- основные результаты каждой RQ;
- Retrospective Revalidation status;
- Architecture Review status;
- Organizational Strategy Question Framework status;
- известные conceptual debts;
- pending revisions;
- следующий предполагаемый Part;
- release status.

Это snapshot состояния, а не методология.

### METHODOLOGY_STATE.md

Назначение:
зафиксировать действующую исследовательскую систему.

Содержит:

Pre-Chapter Overview
→ Human Annotation
→ AI Research & Review Annotation
→ Layer 0 / Chapter Passport
→ Reference Reconnaissance
→ Research Pass 1
→ Independent Adversarial Pass 2
→ Concept Destruction / Pass 3 for Core chapters
→ Audit Layer
→ Cumulative Self-Review
→ Claim Ledger
→ Chapter Exit Gate
→ Final Educational Synthesis

Также фиксируются:

- Causal Claim Audit;
- Transfer Validity Test;
- Contradiction Matrix;
- Concept Boundary Registry;
- Conceptual Debt;
- Retrospective Revalidation;
- Architecture Review;
- Change Register;
- Second-Pass Independence Test;
- source hierarchy;
- research depth rules;
- chapter entry protocol;
- chapter exit protocol.

Этот документ описывает CURRENT methodology.

Позже он будет декомпозирован в полноценные файлы внутри methodology/.

### ARCHITECTURE_DECISIONS.md

Назначение:
сохранить историю значимых решений проекта.

Используется формат Architecture Decision Record.

Пример:

ADR-001

Decision:
Do not use inline epistemic status tags in educational chapter prose.

Reason:
Epistemic metadata should remain available to the research system without degrading readability of the educational text.

Alternatives considered:
Inline tags such as [Established], [Contested], [Working].

Status:
Accepted.

Implications:
Epistemic state must instead be represented through evidence, attribution, Claim Ledger, review artifacts and appropriate wording.

Каждое важное решение должно иметь:

- ID;
- Decision;
- Context;
- Reason;
- Alternatives;
- Status;
- Consequences;
- Related artifacts where applicable.

Особенно важно фиксировать не только принятые, но и явно отвергнутые архитектурные решения.

### OPEN_QUESTIONS.md

Назначение:
не потерять вопросы, которые сознательно оставлены нерешёнными.

Категории:

- conceptual;
- architecture;
- methodology;
- research;
- migration;
- tooling;
- application;
- deferred.

Для каждого вопроса:

ID
Question
Origin
Why unresolved
Current status
Dependencies
When to revisit

Отсутствие ответа не должно автоматически восприниматься Codex как ошибка или приглашение немедленно закрыть вопрос.

### MIGRATION_MANIFEST.yaml

Назначение:
машиночитаемый контроль миграции.

Он связывает:

- original DOCX;
- document ID;
- document type;
- version;
- migration status;
- canonical status;
- future Markdown destination;
- superseded/current state;
- fidelity audit status.

Пример:

document_id: STR-P01-RQ01
source:
  format: docx
  status: current
migration:
  markdown_status: not_started
  fidelity_audit: not_started
canonical:
  current: docx
  future: markdown

### Важное ограничение этапа

На этапе 2 мы НЕ:

- переписываем главы;
- исправляем старые claims;
- проводим новый research;
- разрешаем conceptual debts;
- меняем архитектуру Part 01;
- превращаем migration summary в новый источник теории;
- позволяем Codex "улучшать" существующий материал.

Этап 2 — preservation and state reconstruction.

### Source-of-truth hierarchy во время миграции

Для содержания завершённых исследований:

Original DOCX
> Migration Summary
> Chat recollection

Для архитектурных решений, отсутствующих в DOCX:

Explicit documented decision
> confirmed project state
> reconstructed chat context

При конфликте информация не исправляется молча.

Создаётся migration discrepancy / open issue.

### Exit Gate этапа 2

Этап считается завершённым, если новый AI-сеанс, не имеющий доступа к старой переписке, способен по repository определить:

1. Что представляет собой проект.
2. Зачем он существует.
3. Что уже сделано.
4. Что ещё не сделано.
5. Какая методология действует.
6. Какие архитектурные решения уже приняты.
7. Какие вопросы сознательно оставлены открытыми.
8. Какие документы являются исходными.
9. Что является canonical source на текущей стадии.
10. Какие изменения запрещены до окончания миграции.

Після проходження цього історичного phase Gate можна переходити до формалізації
repository architecture та підготовки migration pilot RQ-01. Це не є чинною
operational authorization на conversion: її визначають live Manifest, Project
State та окремий RQ-01 Pilot Entry Gate; до його `PASS` RQ-01 залишається
неавторизованим.
