# Strategy Knowledge System — Architecture Decisions

## 1. Document Purpose

This document records significant architecture and methodology decisions made during the development of the Strategy Knowledge System before and during migration to Git and Codex.

Its purpose is to preserve decision history.

It answers:

- What was decided?
- Why was it decided?
- What alternatives were considered?
- What consequences follow from the decision?
- Is the decision still active?
- Under what conditions may it be reconsidered?

This document is not:

- a research chapter;
- a project-state summary;
- the research methodology itself;
- an Open Questions Register;
- a list of every working preference or minor implementation choice.

Only decisions with meaningful downstream architectural, methodological, epistemic, or migration consequences should be recorded here.

---

# 2. Decision Status Vocabulary

The following statuses are used:

**Accepted**  
Current governing decision.

**Provisional**  
Currently used but explicitly awaiting further validation.

**Deferred**  
Decision intentionally postponed.

**Superseded**  
Replaced by a later decision.

**Rejected**  
Considered and explicitly not adopted.

**Under Review**  
Previously accepted or provisional decision currently being reconsidered.

A decision must not be treated as permanent merely because it appears in this register.

---

# 3. Decision Record Structure

Each Architecture Decision Record should contain, where relevant:

- ID
- Title
- Status
- Context
- Decision
- Rationale
- Alternatives Considered
- Consequences
- Revisit Trigger
- Related Decisions / Artifacts

---

# ADR-001 — Universal Knowledge Before Organizational Application

**Status:** Accepted

## Context

The Strategy Knowledge System will eventually be used for real organizational strategy development.

This creates a strong risk that existing company ideas, projects, preferences, or desired conclusions could influence supposedly universal theoretical research.

## Decision

Universal strategic knowledge must be developed before organization-specific application.

The preferred reasoning direction is:

Universal Knowledge
→ Organizational Evidence
→ Candidate Interpretation
→ Strategic Implication
→ Decision

The reverse direction must be actively guarded against:

Existing Idea
→ Search for Supporting Theory
→ Retrospective Justification

## Rationale

This separation reduces confirmation bias and prevents company hypotheses from becoming evidence for universal theoretical claims.

## Alternatives Considered

- Build theory and company strategy simultaneously.
- Use current company problems as the primary organizing structure for theory.
- Validate theory through organizational examples.

These alternatives were rejected as the default architecture.

## Consequences

Application material must remain clearly separated from universal research.

A dedicated Application / Translation methodology is required.

## Revisit Trigger

Revisit if later research demonstrates that the separation creates artificial barriers to legitimate action-based learning.

---

# ADR-002 — Separate Research Corpus from Educational Knowledge Book

**Status:** Accepted

## Context

Deep research produces substantially more evidence, disputes, qualifications, and audit material than is appropriate for normal educational reading.

## Decision

Maintain a distinction between:

1. Research Corpus;
2. Strategy Knowledge Book.

The Research Corpus preserves deep research and epistemic history.

The Knowledge Book provides a mature educational synthesis.

## Rationale

Research depth and reading depth serve different purposes.

Combining them would either weaken research or overload the educational text.

## Alternatives Considered

- One document containing everything.
- A short book without preserving deep research.

Rejected.

## Consequences

Publication and educational synthesis may be significantly shorter than the underlying Research Corpus.

---

# ADR-003 — Separate Curriculum from Research Order

**Status:** Accepted

## Context

The order in which concepts are researched is not necessarily the best order for learning.

Neither order necessarily represents the order in which Strategy forms in organizational reality.

## Decision

Treat the following as distinct:

- research order;
- learning order;
- book architecture;
- organizational reality/process order.

## Rationale

Conflating these orders can silently transform a research workflow into an unsupported theory of Strategy formation.

## Consequences

Historical RQ numbering should be preserved even if later educational architecture changes.

Architecture Maps may show alternative conceptual sequences.

---

# ADR-004 — Research by Questions, Not Topic Accumulation

**Status:** Accepted

## Context

Topic-based research easily becomes accumulation of definitions, frameworks, and citations without resolving meaningful uncertainty.

## Decision

Major research should be organized around explicit Research Questions.

## Rationale

Questions create a clearer relationship between evidence, competing explanations, conclusions, and remaining uncertainty.

## Consequences

There is no fixed required number of RQs.

Research coherence takes priority over quantity.

---

# ADR-005 — Mandatory Independent Adversarial Research Pass

**Status:** Accepted

## Context

A single research pass can reinforce its own framing and source selection.

## Decision

Every substantial research chapter requires at least:

- Research Pass 1 — constructive;
- Research Pass 2 — independent adversarial.

Pass 2 begins from the premise:

> If Pass 1 is wrong, what is the strongest theory, evidence, alternative explanation, or boundary case that would show it?

## Rationale

Simple self-editing is insufficient protection against confirmation bias.

## Consequences

Pass 2 must pass an independence test.

Rephrasing Pass 1 does not qualify.

---

# ADR-006 — Mandatory Pass 3 for Core / System-Forming Knowledge

**Status:** Accepted

## Context

Some chapters determine definitions, architecture, and assumptions used throughout the Knowledge System.

Errors in these chapters have disproportionate downstream impact.

## Decision

Core/system-forming chapters require:

**Research Pass 3 — Concept Destruction / Lock-in Audit.**

## Rationale

Contrary evidence alone may not detect problems such as tautology, redundancy, hidden normativity, or architecture lock-in.

## Consequences

Core chapters receive deeper adversarial review than ordinary chapters.

Pass 3 includes tests such as:

- Remove-the-Concept;
- Minimal Counterexample;
- Decision Usefulness;
- construct redundancy;
- circularity;
- level/object confusion;
- strongest surviving claim.

---

# ADR-007 — No Inline Epistemic Status Tags in Educational Prose

**Status:** Accepted

## Context

Inline labels such as:

[Established]
[Contested]
[Working]

were considered for representing epistemic status.

## Decision

Do not use inline epistemic status tags in the main educational prose.

## Rationale

They reduce readability and mix knowledge-control metadata with the learning layer.

Epistemic status should instead be communicated through:

- wording;
- attribution;
- evidence;
- alternatives;
- citations;
- boundary conditions;
- Claim Ledger;
- review artifacts.

## Alternatives Considered

Explicit inline epistemic labels.

Rejected.

## Consequences

The structured knowledge layer becomes more important.

---

# ADR-008 — Cross-Chapter Cumulative Review Is Mandatory

**Status:** Accepted

## Context

A chapter can be internally coherent while contradicting or duplicating other parts of the Knowledge System.

## Decision

New substantial research must be reviewed against relevant accumulated knowledge and previous review findings.

## Rationale

Knowledge-system quality cannot be established through isolated chapter quality.

## Consequences

Cumulative review must consider:

- prior chapters;
- review findings;
- conceptual debts;
- deferred decisions;
- contradiction risks;
- previous review conclusions.

---

# ADR-009 — Conceptual Debt Is Allowed but Must Be Explicit

**Status:** Accepted

## Context

Requiring every conceptual uncertainty to be resolved immediately would make research inefficient or impossible.

Ignoring unresolved issues creates hidden epistemic risk.

## Decision

Allow explicit Conceptual Debt.

Working categories:

- Safe Borrowing;
- Controlled Debt;
- Blocking Debt.

## Rationale

This allows research to proceed while preserving unresolved problems.

## Consequences

Conceptual Debt must be registered and revisited.

Blocking debt may stop downstream research.

---

# ADR-010 — Review Findings Do Not Automatically Change Knowledge

**Status:** Accepted

## Context

Adversarial reviewers may produce useful findings, but reviewers themselves can also be wrong.

Allowing reviewers to directly rewrite canonical knowledge would eliminate meaningful adjudication.

## Decision

Research agents propose knowledge.

Review agents challenge knowledge.

Review findings do not directly modify established knowledge.

Controlled adjudication authorizes significant changes.

## Rationale

This separates criticism from authority to change the knowledge base.

## Consequences

Reviewer roles should normally operate without direct merge authority into canonical knowledge.

---

# ADR-011 — Significant Knowledge Changes Require a Change Register

**Status:** Accepted

## Context

Retrospective review can alter claims with downstream consequences.

Silent editing would destroy provenance.

## Decision

Significant changes should follow:

Finding
→ Original Claim
→ New Evidence / Reasoning
→ Verdict
→ Required Change
→ Downstream Impact
→ Approval
→ Applied Revision

## Rationale

The project should preserve not only the current claim but also why it changed.

## Consequences

Git history and structured Change Register should complement each other.

---

# ADR-012 — Retrospective Revalidation After Major Book Parts

**Status:** Accepted

## Context

Problems may become visible only after multiple chapters have accumulated.

## Decision

After a major book part, perform Retrospective Revalidation.

Current architecture:

1. Claim-by-Claim Review;
2. Cross-System Contradiction & Boundary Review;
3. Architecture Destruction / Lock-in Audit;
4. Open AI Critique / Unknown-Unknown Red Team.

## Rationale

Local chapter review cannot reliably detect all system-level errors.

## Consequences

Completion of individual chapters does not automatically mean the major Part is release-ready.

---

# ADR-013 — Architecture Review Follows Retrospective Revalidation

**Status:** Accepted

## Context

Even individually defensible claims may be organized into a misleading or biased knowledge architecture.

## Decision

Perform an explicit Architecture Review after major retrospective revalidation.

## Rationale

Knowledge architecture itself can encode assumptions and theoretical bias.

## Consequences

Architecture is treated as an object of research and critique.

---

# ADR-014 — Research Architecture Must Not Become Reality Ontology

**Status:** Accepted

## Context

The book uses structured research processes such as diagnosis, choice, causal logic, and evaluation.

There is a risk that this educational structure could be mistaken for a universal sequence in which Strategy forms.

## Decision

Explicitly separate:

Research Architecture
from
Reality Architecture.

## Rationale

Strategy may emerge through action, learning, selection, or retrospective articulation.

## Consequences

Claims about chronological strategic processes require independent evidence.

---

# ADR-015 — Deliberate and Emergent Strategy Must Both Remain Representable

**Status:** Accepted

## Context

Early Part 01 architecture leaned toward deliberate/formulated Strategy.

Revalidation identified this as a systematic bias.

## Decision

The Knowledge System must remain capable of representing both deliberate/formulated and realized/emergent Strategy.

## Rationale

A theory that defines Strategy primarily through prior deliberate choice risks excluding legitimate emergent Strategy by construction.

## Consequences

Several Part 01 claims were bounded rather than universalized.

The final architecture should support both deliberate and realized/learning loops.

---

# ADR-016 — Strategy Quality Is Not Identical to Outcome

**Status:** Accepted

## Context

Successful outcomes can result from luck or favorable environmental change.

Good strategic reasoning can also encounter adverse external conditions.

However, procedural quality must not become an excuse for persistent failure.

## Decision

Treat outcome as important evidence about Strategy, but not as the definition of Strategy quality.

Accumulated ex-post evidence must be capable of challenging the strategic thesis.

## Rationale

This avoids both outcome bias and procedural absolution.

## Consequences

Strategy evaluation requires multiple objects of assessment.

---

# ADR-017 — Frameworks Are Tools, Not Strategy

**Status:** Accepted

## Context

Strategy practice frequently substitutes framework completion for strategic reasoning.

## Decision

Frameworks should be studied according to:

- question solved;
- assumptions;
- inputs;
- outputs;
- limitations;
- failure modes;
- legitimate decision use.

## Rationale

A framework is a representation or analytical instrument, not Strategy itself.

## Consequences

The Knowledge Book should avoid becoming a framework catalogue.

---

# ADR-018 — Failure and Antipatterns Are Cross-Cutting Research Requirements

**Status:** Accepted

## Context

Successful cases alone create survivorship and retrospective interpretation problems.

## Decision

Important chapters should examine:

- failure;
- misuse;
- antipatterns;
- consequences;
- failed mechanisms;
- violated assumptions.

## Rationale

Failure can reveal boundaries that successful examples hide.

## Consequences

Failure analysis becomes a recurring research layer rather than a separate decorative section.

---

# ADR-019 — Application Notes Remain Separate and Limited

**Status:** Accepted

## Context

Practical application improves learning but can contaminate universal theory.

## Decision

Where useful, include clearly separated Application Notes.

Working guideline:

approximately 10–20% of a theoretical block.

This is a guideline, not a fixed quota.

## Rationale

The system should remain practically useful without allowing company-specific material to dominate theoretical research.

## Consequences

Application examples cannot be used as proof of universal claims.

---

# ADR-020 — Founder Question Map Must Be Derived from Research

**Status:** Accepted

## Context

A practical question framework is useful for later strategy formulation.

Creating it before sufficient research risks embedding current assumptions into the Knowledge System.

## Decision

The Founder / Organizational Strategy Question Framework must be derived from accumulated research rather than predefined as the theory architecture.

## Rationale

The application framework should be an output of knowledge, not an input that constrains it.

## Consequences

The current Organizational Strategy Question Framework v0.1 remains provisional and must be re-derived later.

---

# ADR-021 — Organizational Strategy Question Framework Is a Translation Layer, Not a Theory Chapter

**Status:** Accepted

## Context

The Organizational Strategy Question Framework was developed after Part 01.

## Decision

Treat it as a translation/application layer.

It is not:

- RQ-12;
- a new Strategy theory;
- a substitute for later Knowledge Book chapters.

## Rationale

Its purpose is to translate knowledge into questions organizations must answer.

## Consequences

It may evolve substantially as later Parts are completed.

---

# ADR-022 — Strategy-to-Execution Decomposition Is Cross-Cutting, Not Yet a Core Chapter

**Status:** Accepted

## Context

A useful decomposition emerged:

Strategy
→ Strategic Choice
→ Go / No-Go
→ Strategic Initiative
→ Work Package
→ Execution
→ Feedback / Review

## Decision

Preserve this as a cross-cutting artifact.

Do not create a separate Core chapter yet.

## Rationale

Its deepest treatment belongs provisionally within Strategy Formulation / decomposition.

## Consequences

Architecture Review may later reconsider its placement.

---

# ADR-023 — Preserve Original DOCX During Migration

**Status:** Accepted

## Context

Part 01 research currently exists primarily in Word documents.

Conversion can lose structure or content.

## Decision

Original DOCX files must be preserved unchanged as migration baseline artifacts.

## Rationale

They provide provenance and a reference against which migrated representations can be checked.

## Consequences

DOCX files are not deleted after Markdown conversion.

Superseded versions should be retained separately where useful.

---

# ADR-024 — Markdown Is Intended as Future Canonical Working Format

**Status:** Accepted

## Context

DOCX is poorly suited to line-level diff, structured AI review, and Git-based knowledge control.

## Decision

Use Markdown as the intended canonical prose format after successful migration.

Use structured formats such as YAML/JSON where appropriate for machine-readable knowledge.

## Rationale

Text-based formats provide substantially better version control, diff, automation, and AI review.

## Consequences

DOCX/PDF become primarily source-baseline, publication, or archival artifacts depending on lifecycle stage.

---

# ADR-025 — Conversion Does Not Automatically Grant Canonical Status

**Status:** Accepted

## Context

A technically successful DOCX → Markdown conversion may still contain omissions or distortions.

## Decision

Migrated Markdown becomes canonical only after the required fidelity validation.

## Rationale

Representation change must not silently become knowledge change.

## Consequences

Migration status and canonical status must be tracked separately.

---

# ADR-026 — Migration and Intellectual Revision Must Be Separate

**Status:** Accepted

## Context

Known issues already exist in Part 01.

Codex may also discover new issues during migration.

Correcting them while converting documents would make it impossible to distinguish migration changes from research changes.

## Decision

Follow:

Preservation
→ Faithful Representation
→ Structural Normalization
→ Validation
→ Improvement

## Rationale

This preserves intellectual provenance.

## Consequences

Errors discovered during migration become findings.

They are corrected later through Controlled Revision.

---

# ADR-027 — RQ-01 Is the Migration Pilot

**Status:** Accepted

## Context

Mass conversion of all Part 01 documents before testing the process creates unnecessary risk.

## Decision

Use RQ-01 as the first controlled DOCX → Markdown migration pilot.

## Rationale

The pilot allows the fidelity procedure to be tested before bulk migration.

## Consequences

Bulk migration should begin only after the pilot process is accepted.

---

# ADR-028 — Structured Knowledge Must Be Separated from Prose

**Status:** Accepted

## Context

Important claims, contradictions, boundaries, and review states are difficult to manage when they exist only inside prose.

## Decision

Progressively create structured knowledge artifacts such as:

- claims;
- sources;
- contradictions;
- concept boundaries;
- conceptual debt;
- open questions;
- change records.

## Rationale

This supports traceability, automation, cross-chapter review, and epistemic version control.

## Consequences

The Knowledge System becomes more than a directory of chapters.

---

# ADR-029 — Git Is Used as Epistemic Version Control

**Status:** Accepted

## Context

The project requires traceable evolution of knowledge, not only document storage.

## Decision

Use Git to preserve and review meaningful changes to knowledge artifacts.

## Rationale

A strategic claim should eventually be traceable across revisions.

## Consequences

Migration commits, research commits, review findings, and approved knowledge revisions should be distinguishable where practical.

---

# ADR-030 — Canonical Source and Publication Artifact Are Different Concepts

**Status:** Accepted

## Context

A polished Word or PDF document may look authoritative while not representing the latest canonical knowledge.

## Decision

Canonical status is determined by repository governance, not presentation format.

## Rationale

Visual polish should not determine epistemic authority.

## Consequences

Publication artifacts may be generated from canonical sources.

---

# ADR-031 — Root AGENTS.md Is a Router, Not the Full Methodology

**Status:** Accepted

## Context

A single giant agent instruction file would mix repository governance, methodology, role behavior, and domain rules.

## Decision

Keep root `AGENTS.md` short.

Its role is to direct agents toward relevant detailed instructions.

## Rationale

This improves modularity and reduces instruction duplication.

## Consequences

Detailed rules belong under `agents/`, `methodology/`, and domain-specific profiles.

---

# ADR-032 — Agent Roles Must Be Specialized

**Status:** Accepted

## Context

One AI agent performing research, critique, evidence audit, architecture review, and final adjudication creates self-confirmation risk.

## Decision

Use specialized roles where appropriate.

Candidate roles include:

- Researcher;
- Validator;
- Falsifier;
- Evidence Auditor;
- Architecture Red Team;
- Alternative Paradigm Reviewer;
- Adjudicator;
- Orchestrator.

## Rationale

Role separation improves adversarial independence.

## Consequences

Role files should define epistemic responsibilities and limits.

---

# ADR-033 — Reviewer Agents Do Not Receive Automatic Merge Authority

**Status:** Accepted

## Context

Reviewers are intentionally optimized to find defects and may overcorrect.

## Decision

Reviewer output should normally produce findings rather than direct canonical changes.

## Rationale

Criticism and adjudication are different epistemic functions.

## Consequences

Canonical changes require controlled revision.

---

# ADR-034 — Same Baseline for Independent Reviews

**Status:** Accepted

## Context

Independent reviewers cannot be meaningfully compared if each begins from a different modified state.

## Decision

Where parallel independent review is required, reviewers should start from the same immutable baseline or Git SHA.

## Rationale

This preserves review independence and comparability.

## Consequences

Reviewer branches or workspaces should avoid contaminating one another before adjudication.

---

# ADR-035 — Codex Must First Demonstrate Repository Comprehension

**Status:** Accepted

## Context

Codex is being introduced after substantial prior research and architecture work.

Immediate write access creates risk of unintended restructuring.

## Decision

The first substantive Codex interaction with the migrated repository should be a read-only comprehension / inventory test.

## Rationale

The system should verify that Codex understands:

- repository purpose;
- source-of-truth policy;
- current migration stage;
- instructions;
- prohibited actions.

## Consequences

No initial “improve the repository” task should be issued.

---

# ADR-036 — Part 01 Is the First Codex Benchmark

**Status:** Accepted

## Context

Part 01 already has known Revalidation findings.

This provides a useful benchmark for evaluating the new Codex review architecture.

## Decision

Use Part 01 as the first controlled benchmark.

Where appropriate, independent reviewer roles should attempt to rediscover known issues without being shown all existing findings in advance.

## Rationale

This tests whether the review system can detect real known weaknesses rather than merely reproduce supplied critiques.

## Consequences

Benchmark results should be compared with existing Revalidation findings.

---

# ADR-037 — Codex Must Not Improve Migrated Knowledge Before Fidelity Validation

**Status:** Accepted

## Context

AI coding/research environments naturally tend to normalize or improve material while processing it.

## Decision

During migration, Codex must preserve content before proposing intellectual improvements.

## Rationale

Migration fidelity has priority over elegance.

## Consequences

Improvement belongs to later Controlled Revision.

---

# ADR-038 — External Model Review Is a Gate, Not a Constant Requirement

**Status:** Provisional

## Context

Independent external models may identify blind spots missed by the primary research/review system.

Using them continuously would add cost and process complexity.

## Decision

Use external model adversarial validation selectively, primarily for Core/system-forming work or major release gates.

## Rationale

External independence has highest value where downstream epistemic risk is high.

## Alternatives Considered

- External model review on every RQ.
- No external model review.

Neither is currently preferred.

## Revisit Trigger

Evaluate after the first controlled external review experiment.

---

# ADR-039 — Universal Research Kernel + Domain Profile Architecture

**Status:** Provisional

## Context

Much of the methodology is reusable beyond Strategy, while some review requirements are domain-specific.

## Decision

Explore a future architecture consisting of:

Universal Research Kernel
+
Domain Research Profile
+
Project Brief

## Rationale

This may allow reuse without forcing one generic methodology onto every domain.

## Consequences

The current Strategy methodology should not automatically be generalized to all research domains.

## Revisit Trigger

Formal methodology decomposition and testing in another domain.

---

# ADR-040 — Do Not Create Empty Agent Files Merely to Complete Repository Structure

**Status:** Accepted

## Context

A visually complete directory tree can create the appearance of a mature agent architecture before role definitions actually exist.

## Decision

Create role files when their responsibilities and instructions can be defined substantively.

## Rationale

Repository completeness should represent real capability rather than placeholders.

## Consequences

Some planned directories or files may remain absent during bootstrap.

---

# ADR-041 — Preserve Historical RQ Numbering

**Status:** Accepted

## Context

Architecture Review showed that the conceptual sequence differs from historical research order.

Renumbering RQs would weaken provenance and break references.

## Decision

Preserve RQ-01 through RQ-11 numbering.

Use Architecture Maps to represent alternative conceptual ordering.

## Rationale

Historical identity and conceptual order are different concerns.

## Consequences

Future revisions should not renumber historical research artifacts merely to improve book flow.

---

# ADR-042 — Strategic Coherence Remains a Working Umbrella Pending Later Boundary Review

**Status:** Provisional

## Context

RQ-09 developed Strategic Coherence as a system-level diagnostic umbrella.

Potential overlap exists with later Systems Thinking and configuration concepts.

## Decision

Retain Strategic Coherence provisionally while explicitly carrying the overlap as Conceptual Debt.

## Rationale

Premature removal would discard useful relational analysis before later concepts are researched.

## Revisit Trigger

Systems Thinking / configuration research or later Architecture Review.

---

# ADR-043 — Power, Politics and Institutional Factors Must Be Added to Future Diagnosis Research

**Status:** Accepted

## Context

Part 01 revalidation identified underrepresentation of power, politics, organizational contestation, and institutional constraints.

## Decision

Carry this as explicit downstream research debt.

The provisional Strategic Diagnosis architecture must include a dedicated investigation of these factors.

## Rationale

A purely rational-choice architecture risks misrepresenting how organizational Strategy forms and is implemented.

## Consequences

Later diagnosis research cannot treat organizational interpretation as politically neutral by default.

---

# ADR-044 — Part 02 Provisionally Begins with Strategic Diagnosis

**Status:** Provisional

## Context

Earlier book planning could have moved directly from Strategy into Purpose / Vision / Mission.

Part 01 research increased the importance of diagnosis and problem framing.

## Decision

Current preferred next major Part is:

**Strategic Diagnosis & Problem Framing**

before deep Purpose / Vision / Mission work.

## Rationale

This reduces the risk that desired direction determines diagnosis retrospectively.

## Revisit Trigger

Part 01 Consolidated Synthesis and final Architecture Gate.

---

# ADR-045 — Part 01 Requires Controlled Revision Before v1.0

**Status:** Accepted

## Context

RQ-01 through RQ-11 are complete, but Revalidation produced material findings.

## Decision

Do not release Part 01 v1.0 directly from the existing research drafts.

Required sequence:

Controlled Revision
→ Consolidated Synthesis
→ Organizational Strategy Question Framework v1
→ Part 01 Exit / Readiness Gate
→ Release v1.0

## Rationale

Known system-level findings must be resolved or explicitly bounded before release.

---

# ADR-046 — Migration Context Must Replace Dependence on Historical Chat

**Status:** Accepted

## Context

A substantial portion of project architecture developed through long-form conversation.

Future Codex sessions cannot safely depend on access to that conversation.

## Decision

Transfer significant project context into repository artifacts.

Current migration package includes:

- `MIGRATION_PLAN.md`
- `PROJECT_CONTEXT.md`
- `PROJECT_STATE.md`
- `METHODOLOGY_STATE.md`
- `ARCHITECTURE_DECISIONS.md`
- `OPEN_QUESTIONS.md`
- `MIGRATION_MANIFEST.yaml`

## Rationale

The repository must become sufficiently self-describing to continue work without hidden conversational dependencies.

## Consequences

The full chat transcript is not itself the intended canonical migration artifact.

---

# ADR-047 — Do Not Copy the Entire Historical Chat into the Canonical Knowledge System

**Status:** Accepted

## Context

The historical conversation contains:

- superseded ideas;
- exploratory discussion;
- temporary formulations;
- duplicated reasoning;
- decisions later revised.

## Decision

Perform controlled state transfer rather than treating the full conversation as canonical project knowledge.

## Rationale

Raw conversational history is useful provenance but poor canonical architecture.

## Consequences

Significant decisions, state, methodology, and open questions are reconstructed into explicit repository artifacts.

---

# ADR-048 — Original Research Artifacts Have Priority Over Reconstructed Migration Summaries

**Status:** Accepted

## Context

Migration context documents are partly reconstructed from accumulated project history.

They may simplify or compress the original research.

## Decision

For substantive research content during migration:

Original Research Artifact
>
Migration Summary
>
Conversation Recollection

## Rationale

Migration summaries should explain the system, not silently replace primary research artifacts.

## Consequences

Conflicts must be registered rather than resolved by assuming the summary is correct.

---

# ADR-049 — Migration Discrepancies Must Be Explicit

**Status:** Accepted

## Context

Differences may appear between:

- DOCX;
- migration summaries;
- historical versions;
- later review documents;
- converted Markdown.

## Decision

Material discrepancies should become explicit migration findings.

## Rationale

Silent reconciliation destroys provenance.

## Consequences

A migration discrepancy may later trigger:

- fidelity correction;
- version classification;
- research review;
- controlled revision.

---

# ADR-050 — Architecture Decisions Are Revisable but Not Casually Reopened

**Status:** Accepted

## Context

A living Knowledge System must remain revisable.

At the same time, repeatedly reopening settled architecture decisions creates circular work and instability.

## Decision

Accepted ADRs remain governing decisions until:

- new evidence;
- implementation failure;
- contradiction;
- architecture review;
- significant downstream discovery

creates a legitimate revisit trigger.

## Rationale

The system requires both revisability and decision stability.

## Consequences

Codex should not reopen an Accepted ADR merely because it can propose an alternative.

A materially justified challenge should instead create a review finding.

---

# ADR-051 — Use a Lean Batch Pipeline After the RQ-01 Migration Pilot

**Status:** Accepted

## Context

RQ-01 completed the controlled DOCX → Markdown pilot with verdict `PASS WITH
NON-BLOCKING DISCREPANCIES`. The pilot showed that deterministic identity,
text, structure, table and reference checks can carry routine comparison cost,
while full visual and exhaustive manual comparison add value primarily when a
risk signal is present.

## Decision

Approve Lean Migration Pipeline v2 as the scoped operational profile for
legacy DOCX → noncanonical Markdown migration RQ-02–RQ-11 and authorize those
artifacts as one migration series. Do not repeat per-chapter Entry Gates or
methodology approvals while source class, methodology, authority and risk
conditions remain unchanged.

The standard flow is:

Source identity
→ Deterministic conversion
→ Automated fidelity checks
→ Independent difference-focused review
→ Correction only for material discrepancies
→ Fidelity closure
→ Commit

Full visual QA, exhaustive manual comparison and separate adjudication are
risk-triggered. Escalation is required only for ambiguous/changed source
identity, unsupported or complex DOCX structures, automated material
differences, semantic uncertainty from independent review, or material
methodology change.

## Governance Boundary

This scoped v2 profile governs routine comparison mechanics for RQ-02–RQ-11
where they differ from the RQ-01 pilot procedure. Migration Fidelity Protocol
v1 and Migration Discrepancy Taxonomy v1 continue to govern preservation,
discrepancy classification, correction provenance, reviewer independence and
the separation of fidelity from canonical promotion.

RQ-01 remains noncanonical. OQ-062 remains unresolved. Translation, theory
revision, research-content changes and canonical promotion are not authorized.

## Consequences

- a reusable deterministic converter/checker is the normal execution control;
- each source receives an identity and complexity screen, not a new Entry Gate;
- each candidate still receives independent difference-focused review and a
  fidelity closure record;
- any escalation trigger pauses the affected artifact without automatically
  pausing unaffected artifacts in the series;
- canonical promotion remains a separate future governance action.

---

# 4. Current Decision Summary

## Accepted Core Decisions

The current architecture strongly commits to:

- universal knowledge before organizational application;
- Research Corpus separate from educational synthesis;
- research order separate from learning and reality order;
- question-driven research;
- mandatory adversarial Pass 2;
- mandatory Pass 3 for Core/system-forming knowledge;
- cumulative review;
- explicit conceptual debt;
- Claim / Change governance;
- no inline epistemic tags;
- retrospective revalidation;
- architecture review;
- deliberate and emergent Strategy both remaining representable;
- preservation before improvement;
- DOCX preservation;
- Markdown as intended future canonical working format;
- fidelity validation before canonical promotion;
- Git-based epistemic version control;
- specialized AI roles;
- reviewer/adjudicator separation;
- read-only Codex comprehension before modification;
- controlled revision before Part 01 v1.0.

## Important Provisional Decisions

Currently provisional:

- selective external-model release Gate;
- Universal Research Kernel + Domain Profile architecture;
- final boundary of Strategic Coherence;
- Part 02 beginning with Strategic Diagnosis;
- final broader Knowledge Book architecture.

These must not be silently promoted to permanent rules.

---

# 5. Governance Rule for Future ADRs

A new ADR should be created when a decision:

- materially changes repository architecture;
- changes canonical-source policy;
- changes research methodology;
- changes review governance;
- changes major knowledge architecture;
- changes migration rules;
- changes AI role authority;
- reverses or materially modifies an earlier Accepted ADR.

Minor operational choices do not require ADRs.

---

# 6. Superseding Decisions

If a later decision replaces an earlier ADR:

1. Do not delete the old ADR.
2. Change its status to `Superseded`.
3. Identify the superseding ADR.
4. Explain why the previous decision changed.
5. Preserve downstream consequences where relevant.

The objective is historical traceability.

---

# 7. Current Architecture Principle

The governing architecture principle at migration is:

> Preserve decisions strongly enough to prevent accidental regression, but keep them criticizable enough to permit evidence-based improvement.
