# Repository Rules

## 1. Purpose

This repository is the persistent source-controlled environment for the
Strategy Knowledge System.

It contains research artifacts, knowledge representations, reviews,
methodology, migration records, application layers, and release artifacts.

Git history is part of the project's epistemic provenance.

---

## 2. Governing Principle

Research agents may propose knowledge.

Review agents may challenge knowledge.

Neither research nor review findings automatically authorize changes to
established knowledge.

Material knowledge changes require explicit adjudication and traceable
change control.

---

## 3. Source-of-Truth Policy

During the current migration stage:

1. Original research DOCX artifacts are the historical research baseline.
2. Migration summaries describe project state but do not override original
   research artifacts.
3. Historical conversation recollection has lower authority than preserved
   research artifacts and explicit architecture decisions.
4. Markdown is the intended future canonical working format.
5. Converted Markdown does not become canonical merely because conversion
   succeeded.
6. Canonical promotion requires fidelity validation.
7. Publication artifacts and canonical working sources are different
   concepts.

Where sources disagree, record the discrepancy. Do not silently reconcile it.

---

## 4. Migration Rule

Migration and intellectual revision are separate operations.

During migration, do not:

- improve arguments;
- repair claims silently;
- resolve conceptual debt;
- change chapter conclusions;
- restructure research for elegance;
- replace historical terminology merely because newer terminology appears
  preferable;
- treat migration summaries as stronger evidence than source artifacts.

The migration sequence is:

Preservation
→ Faithful Representation
→ Structural Normalization
→ Validation
→ Improvement

Improvement begins only after migration fidelity has been established.

---

## 5. Established Knowledge

An artifact should be treated as established knowledge when repository state
or an approved release identifies it as such.

Established knowledge must not be materially changed without the project's
review and change-control process.

Editorial changes that do not alter meaning may use a lighter process, but
semantic changes must remain traceable.

---

## 6. Research Protocol

Before conducting new substantive chapter research, follow the current
research methodology defined by the repository.

The current methodological sequence includes:

Pre-Chapter Overview
→ Human Annotation
→ AI Research & Review Annotation
→ Layer 0 / Chapter Passport
→ Reference Reconnaissance
→ Research Pass 1
→ Independent Adversarial Research Pass 2
→ Pass 3 for Core / System-Forming knowledge
→ Audit Layer
→ Cumulative Self-Review
→ Claim Ledger
→ Chapter Exit Gate
→ Final Educational Synthesis

Do not shorten mandatory research passes without an explicit architecture
decision.

---

## 7. Independent Review

Research Pass 2 and independent reviewer roles must genuinely attempt to
challenge the current conclusion.

They must not merely strengthen, rewrite, or summarize the first-pass result.

Independent reviews should start from the same identified baseline whenever
possible.

Reviewer findings are findings, not authorized patches.

---

## 8. Core / System-Forming Knowledge

Core or system-forming chapters require stronger adversarial review.

Current methodology requires a Concept Destruction / Lock-in Audit that tests,
among other things:

- hidden tautology;
- circularity;
- generic management language;
- hidden normativity;
- construct redundancy;
- object or level confusion;
- unfalsifiability;
- over-integration;
- boundary cases;
- minimal counterexamples;
- remove-the-concept tests;
- decision usefulness.

---

## 9. Cumulative Review

A chapter must not be evaluated only in isolation.

Where the methodology requires cumulative review, inspect relevant prior:

- chapters;
- claims;
- review findings;
- contradiction records;
- conceptual debts;
- deferred decisions;
- architecture findings.

Repeated concepts are not automatically duplication.

Distinguish productive repetition from harmful conceptual duplication.

---

## 10. Open Questions

Open Questions are explicit uncertainty objects.

They are not automatically tasks.

Do not resolve an Open Question merely because it is listed in the repository.

Resolution requires the appropriate research or review process.

Do not delete resolved questions when provenance matters; update their status
and link the resolving evidence or artifact.

---

## 11. Conceptual Debt

Conceptual debt may be preserved when it does not block responsible progress.

Debt should be classified and visible.

Do not silently convert deferred conceptual debt into an assumed conclusion.

---

## 12. Claim Changes

Material claim changes should preserve:

- original claim;
- reason for challenge;
- evidence or reasoning;
- verdict;
- required change;
- downstream impact;
- approval state;
- applied revision.

Git diff alone is not sufficient provenance for major epistemic changes.

---

## 13. Architecture Decisions

Architecture decisions are stored separately from ordinary prose.

Accepted decisions should not be casually reopened.

If new evidence justifies reversal or substantial modification, create or
update the appropriate architecture decision record while preserving the
historical decision.

---

## 14. Application Separation

Universal Strategy knowledge and organization-specific application must remain
separate.

Do not use an existing organizational idea as evidence that a universal theory
is correct.

Preferred direction:

Universal Knowledge
→ Organizational Evidence
→ Candidate Interpretation
→ Strategic Implication

Avoid:

Existing Idea
→ Search for Supporting Theory
→ Confirmation

---

## 15. Agent Authority

Agents must operate within assigned roles.

Researcher:
- investigates and synthesizes;
- may propose claims;
- does not independently authorize final knowledge changes.

Reviewer:
- challenges claims and architecture;
- may propose findings;
- does not automatically modify established knowledge.

Adjudicator:
- evaluates competing findings and proposed changes;
- may authorize changes according to repository governance.

Orchestrator:
- coordinates workflow;
- does not substitute coordination authority for epistemic adjudication.

No agent should assume merge authority merely because it generated a finding.

---

## 16. Repository Modification Rules

Before modifying repository knowledge:

1. Identify the artifact and its current status.
2. Read applicable repository instructions.
3. Determine whether the action is migration, research, review, editorial
   correction, or intellectual revision.
4. Preserve provenance.
5. Follow the corresponding review/change-control path.
6. Avoid unrelated cleanup during controlled migration or review work.

Do not combine migration repair and substantive knowledge revision in the same
change unless explicitly authorized.

---

## 17. Git Rules

Use Git as epistemic version control, not only file backup.

Prefer:

- focused commits;
- meaningful commit messages;
- identifiable baselines;
- review from immutable commits;
- preserved superseded artifacts where required;
- explicit release states.

Do not force-push or rewrite shared history unless explicitly authorized.

Do not commit secrets, credentials, environment files, or local scratch data.

---

## 18. DOCX Migration

Original DOCX files must be preserved during migration.

For DOCX → Markdown conversion:

1. preserve the DOCX source;
2. create a candidate Markdown representation;
3. run fidelity validation;
4. record discrepancies;
5. correct representation errors without altering intellectual content;
6. promote Markdown to canonical status only after approval.

Do not delete the original DOCX after canonical promotion unless a later
explicit retention decision authorizes it.

---

## 19. Fidelity Before Improvement

A migrated chapter must first answer:

"Does this faithfully represent the source?"

Only after that gate passes may the project ask:

"How should this knowledge be improved?"

These are separate reviews.

---

## 20. Prohibited Silent Actions

Do not silently:

- alter conclusions;
- strengthen scope;
- weaken scope;
- universalize bounded claims;
- remove counterarguments;
- resolve contradictions;
- delete conceptual debt;
- renumber historical research questions;
- overwrite superseded history;
- promote candidate Markdown to canonical;
- convert provisional architecture into established architecture;
- close Open Questions.

---

## 21. Current Migration Context

Before migration work, also inspect:

- `migration/PROJECT_CONTEXT.md`
- `migration/PROJECT_STATE.md`
- `migration/METHODOLOGY_STATE.md`
- `migration/ARCHITECTURE_DECISIONS.md`
- `migration/OPEN_QUESTIONS.md`
- `migration/MIGRATION_MANIFEST.yaml`
- `migration/MIGRATION_PLAN.md`

These files transfer project state into the repository but do not supersede
original research artifacts.

---

## 22. Conflict Rule

If repository instructions conflict, stop the affected operation and report:

- the conflicting instructions;
- the affected artifact;
- the practical consequence;
- the smallest decision needed to resolve the conflict.

Do not invent an authority hierarchy that is not documented.

---

## 23. Default Safety Rule for Ambiguity

When uncertain whether an action would modify established knowledge, treat the
action as potentially substantive and preserve the current state until the
ambiguity is resolved.

Preservation takes precedence over convenience.
