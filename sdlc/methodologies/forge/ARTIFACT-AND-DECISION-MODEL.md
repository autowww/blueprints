# Forge — artifact and decision model

**Purpose:** Define how **artifacts** (inputs/outputs) and **decisions** attach to Forge’s **locked canon**—lifecycle model ([`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md), [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md), [`../../SDLC.md`](../../SDLC.md)), **meeting model** ([`meetings-model.md`](meetings-model.md), [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md)), and **concept map** ([`CONCEPT-MAP.md`](CONCEPT-MAP.md))—without adding bureaucracy.

**Companion:** [`meetings-model.md`](meetings-model.md) specifies **meetings** (cadence, modes, accountability). This document specifies **durable artifacts** and **decision records** and how they connect.

**Non-goals:** Replace project-specific `docs/` layouts, duplicate [`../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md) ADR guidance, or introduce a second tracking spine.

---

## Design goals and rules

| Goal | Implication |
|------|-------------|
| Every core meeting and key decision has clear **inputs/outputs** and **ownership** | Map artifacts to meetings in § [Artifact matrix](#artifact-matrix); name an **owner** per artifact type. |
| No bureaucracy | Prefer **minimal** types; reuse Ember Log + existing templates; **consumer** must exist before adding a type. |

**Rules:**

- Every artifact must have a **consumer** (human process, gate, or downstream doc).
- Every artifact must answer **why** (reasoning / trigger) and **for what** (intent / outcome)—same bar as [`meetings-model.md`](meetings-model.md) per-meeting **Why** / **For what**.
- Keep the set **minimal but sufficient**.
- Classify artifacts (one primary class each; some rows span two when bridged):

| Class | Meaning |
|-------|---------|
| **Planning** | Commits scope, sequence, or horizon before execution. |
| **Work execution** | Describes or tracks units of delivery work. |
| **Evidence** | Proves quality, readiness, or compliance for a gate or review. |
| **Decision** | Records a choice, trade-off, or risk acceptance. |
| **Learning / improvement** | Captures outcomes of inspect-and-adapt; feeds backlog or directives. |
| **Directive** | Governs *how the team works* (rules, norms, process)—not product behavior. |

---

## Authoring specification (design brief)

The following block is the **authoring checklist** used to maintain this document. When extending Forge’s artifact set, satisfy these items and update § [Decisions kept](#decisions-kept) / § [Drift](#drift) / § [Open questions](#open-questions).

**Sources of truth:** [`CONCEPT-MAP.md`](CONCEPT-MAP.md), [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md), [`meetings-model.md`](meetings-model.md), [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md), [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md), [`PRODUCT-DELIVERY-FORGE-IPE.md`](PRODUCT-DELIVERY-FORGE-IPE.md).

**Task checklist:**

1. Define the **minimum artifact set** for Forge (see § [Recommended artifact set](#recommended-artifact-set)).
2. For each artifact, specify: purpose; **for what**; **why**; owner; **Versona** contribution; creation trigger; update trigger; required fields; downstream consumers; linked meetings; linked PDLC/SDLC phases—**artifact matrix** in § [Artifact matrix](#artifact-matrix).
3. Recommend **canonical names** and flag **redundant or collision-prone** names (§ [Canonical names and collision register](#canonical-names-and-collision-register)).
4. Provide **lightweight Markdown schemas** for the highest-value artifacts (§ [Markdown schemas](#markdown-schemas)).
5. Include a **critical question** structure for formal decision documentation plus a **decision schema** with at minimum: why; for what; options considered; chosen direction; evidence; risks; owner; review date / revisit trigger.

**Evaluated artifact names (minimum):** Opportunity/problem; discovery/validation; Product Increment / release-slice planning; Spark definition; Decision Record; Review evidence pack; Assay packet; Release/launch; Retro Record; Directive file; ADR (technical decision).

---

## Recommended artifact set

Minimum **durable** types teams should be able to point to (paths are typical; projects may namespace under `docs/` or `forge/` per [`../../templates/forge/README.template.md`](../../templates/forge/README.template.md)):

| # | Canonical artifact | Primary class | Canon pointer |
|---|---------------------|---------------|---------------|
| 1 | **Ore** (intake item) | Planning + work execution | [`CONCEPT-MAP.md`](CONCEPT-MAP.md), [`process-and-flows.md`](process-and-flows.md) |
| 2 | **Ingot** (refined, plannable) | Planning + work execution | Same |
| 3 | **Forge Spark** (delivery unit) | Work execution | Same; **Spark definition** = Ingot + Spark breakdown at Planning |
| 4 | **Charge** (daily commitment view) | Work execution | [`daily/README.md`](daily/README.md) |
| 5 | **Product Spark plan** (PoC/MVP/phase/release plan) | Planning | [`planning/README.md`](planning/README.md), [`planning/release-plan.template.md`](planning/release-plan.template.md) |
| 6 | **Ember Log** (operational decision memory) | Decision | [`daily/README.md`](daily/README.md), [`CONCEPT-MAP.md`](CONCEPT-MAP.md) **Decision Record** row |
| 7 | **ADR** (architecture decision record) | Decision | [`../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md) |
| 8 | **Directive** (team working rules) | Directive | [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) retro → directives |
| 9 | **Review evidence pack** (increment + evidence posture for Review) | Evidence | [`meetings-model.md`](meetings-model.md) § Review |
| 10 | **Assay packet** (release candidate + checklist + rationale) | Evidence + decision | [`assay-gate.template.md`](../../templates/forge/assay-gate.template.md), **Assay Gate** |
| 11 | **Release / launch record** (what shipped, where, flags) | Evidence (+ PDLC P4 handoff) | Release notes + bridge to **P4 Launch** in [`../../../pdlc/PDLC-SDLC-BRIDGE.md`](../../../pdlc/PDLC-SDLC-BRIDGE.md) |
| 12 | **Retro → experiment / directive trace** | Learning + directive | Documented retro outputs with owner and evidence per [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) |
| 13 | **Opportunity / problem** (often as Ore + product docs) | Planning | P1 → Ore; may live in `docs/product/` per [`../../../product/`](../../../product/README.md) |
| 14 | **Discovery / validation** (experiments, learnings) | Evidence + learning | PDLC P1–P2; feeds Ore and Product Spark scope |

**Not** a separate Forge artifact type: a second “decision database” if **Ember Log + ADR + directives** already cover operational, architectural, and team-rule decisions ([`CONCEPT-MAP.md`](CONCEPT-MAP.md)).

---

## Artifact matrix

Summary of the **evaluated** names. “**Spark definition**” is realized as **Ingots + phase-tagged Sparks** committed in Planning, not a separate document unless the team adds one.

| Artifact (evaluated name) | Canonical Forge mapping | Purpose (short) | For what | Why | Owner (typical) | Versona contribution | Creation trigger | Update trigger | Required fields (minimum) | Downstream consumers | Linked meetings | PDLC / SDLC |
|---------------------------|-------------------------|-----------------|----------|-----|----------------|----------------------|------------------|----------------|---------------------------|----------------------|-----------------|-------------|
| Opportunity / problem | **Ore** + product context | Capture raw problems/ideas | Feed refinement and prioritization | Avoid silent funnel loss | Product hat | Product / strategy lenses | Intake | Re-scope, merge, reject | Problem statement, value hypothesis | Refinement, roadmap | Refinement, ad hoc | P1 | A |
| Discovery / validation | PDLC experiments + evidence | Learn before scaling commitment | Validate assumptions cheaply | Reduce wrong build | Product + research | Discipline Versonas at **P2** | Hypothesis | Learn / kill / pivot | Hypothesis, method, result | Ore backlog, Product Spark scope | Refinement, review | P1–P2 | A–B |
| Product Increment / release-slice planning | **Product Spark** plan | Horizon scope for a slice | Align delivery to a releasable chunk | Make Assay and roadmap coherent | Product / PM | PM Versona, roadmap gates | New slice / milestone | Scope change | Goals, out-of-scope, success measures | Planning, Assay, GTM | Planning | P3 | B–F container |
| Spark definition | **Ingot** + **Forge Spark** list | Executable breakdown | Commit iteration work | Translate plan to tractable units | Owner + Engineering | Decomposition drafts | Planning | Re-plan mid-iteration | IDs, AC, phase tags | Daily sync, review | Planning | P3 | B–F |
| Decision Record | **Ember Log** entry | Operational decision memory | Recover “why” later | Auditability and fewer re-debates | Owner / governance | Prompt to log at §5 / activities | Decision made | Supersede with new log line | See [Formal decision (Ember Log block)](#1-formal-decision-ember-log-block) | Backlog, Assay, retros | Any | P3–P6 | A–F |
| Review evidence pack | Review inputs bundle | Show increment + quality posture | Iteration accountability | Early signal before Assay | Whole team | Prep drafts | End of iteration | Each iteration | Demo, test summary, known issues | Assay readiness, Ember Log | Review | P3–P4 | D–E |
| Assay packet | **Assay Gate** evidence + [`assay-gate.template.md`](../../templates/forge/assay-gate.template.md) | Release readiness proof | Ship vs not yet | Protect users and commitments | Governance steward | Security/compliance checks | RC + criteria ready | New RC | Checklists, gaps, result | Launch, ops, stakeholders | Assay Gate | P4 | E–F |
| Release / launch artifact | Ship record + comms handoff | What went out and how it was activated | Market/ops alignment | Close loop PDLC **P4** | Product + engineering | Release notes drafts | Successful Assay | Patch / hotfix | Version, scope, flags, notes | Customers, support, metrics | Assay (prep), launch sync | P4 | F |
| Retro Record | Retro notes + **directive** trace | Improve system | Sustainable change | Encode learning | Team; experiment owner | Effectiveness review | Retro | Next retro | Themes, experiments, evidence | Directives, Ore | Retro | P5 | C5 |
| Directive file | `sdlc/`, `.cursor/rules/`, team norms | Govern **how** we work | Consistent execution | Stability without heroics | Named owner + approver | May encode Versona norms | Retro graduation / policy change | Policy review date | Change rationale, evidence | All execution | Retro | P3–P6 | Application of SDLC |
| ADR / technical decision | **`docs/adr/`** style ADR | Architecture significance | Long-lived tech coherence | Onboard and avoid rework | Tech lead | Architecture Versona | Significant design fork | Supersede ADR | Context, decision, consequences | Implementation, reviews | Refinement, design | P2–P3 | C |

---

## Canonical names and collision register

| Use this | Avoid / clarify |
|----------|-----------------|
| **Ember Log** for day-to-day **decision memory** | “Decision Record” as a *fourth* bucket—map to Ember Log ([`CONCEPT-MAP.md`](CONCEPT-MAP.md)). |
| **ADR** for **architecture** | “Technical Decision Record” only as plain-language alias for ADR—not for Ember Log or directives. |
| **Directive** for **team rules** | Charter / working agreement: merge into directives or link explicitly. |
| **Product Spark** | **Release slice**, **product increment** = aliases; **Forge Spark** = task-level—never interchange. |
| **Assay packet** | Align with **evidence package** language in [`meetings-model.md`](meetings-model.md); template: [`assay-gate.template.md`](../../templates/forge/assay-gate.template.md). |
| **Review evidence pack** | Do not merge with **Assay packet**—Review judges readiness *to pursue* Assay; Assay is **release** verdict. |
| **User persona** (PDLC) vs **Versona** (Forge) | [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md). |

---

## Critical questions (formal decision)

Use at **ad hoc decision** meetings and whenever logging a **non-trivial** choice in the Ember Log:

1. **What decision is being made** (one sentence)?
2. **For what outcome** are we optimizing this week / increment?
3. **Why now**—what breaks if we defer?
4. **Options considered** (including “do nothing”)?
5. **Evidence** we relied on—what would falsify this later?
6. **Risks and mitigations**—who owns each?
7. **Revisit trigger**—date or signal to re-open?

Architecture-only decisions use the ADR template instead; **process** changes that govern the team belong in **directives** with retro evidence.

---

## Markdown schemas

### 1. Formal decision (Ember Log block)

Use inside `ember-logs/YYYY-MM-DD.md` for decisions that need more than one line:

```markdown
### Decision — <short title>

- **Why:** <reason / forcing function>
- **For what:** <outcome or constraint this enables>
- **Options considered:** <A | B | C>
- **Chosen direction:** <pick>
- **Evidence:** <links, metrics, session ids>
- **Risks:** <bullet list + owners>
- **Owner:** <name / role>
- **Review date / revisit trigger:** <YYYY-MM-DD or signal>
```

### 2. ADR (pointer)

Author full ADRs per [`../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md`](../../../disciplines/engineering/software-architecture/SOFTWARE-ARCHITECTURE.md). Ember Log entries should **link** to the ADR file rather than duplicating architecture detail.

### 3. Directive change (retro graduation)

**Full templates:** [`retro-record.template.md`](../../templates/forge/retro-record.template.md) (post-retro), [`directive-change-proposal.template.md`](../../templates/forge/directive-change-proposal.template.md) (pre-merge), [`project-sdlc-directive.template.md`](../../templates/forge/project-sdlc-directive.template.md), [`technical-directive.template.md`](../../templates/forge/technical-directive.template.md). **Loop and routing:** [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) § “From retro to directives”.

```markdown
## Directive update — <area>

- **Why:** <retro theme / incident / evidence>
- **For what:** <behavior we want on every iteration>
- **Change:** <rule text or pointer to PR>
- **Owner:** <who maintains>
- **Review date:** <optional>
```

### 4. Review evidence pack (lightweight)

```markdown
# Review evidence — <iteration> — <date>

- **Increment summary:** <what shipped vs planned>
- **Demo / walkthrough:** <link or notes>
- **Quality posture:** <tests, defects, known issues>
- **Assay readiness:** <ready | needs evidence | scope adjust>
- **Ember Log pointers:** <decisions to review>
```

### 5. Assay packet (extends template)

Start from [`../../templates/forge/assay-gate.template.md`](../../templates/forge/assay-gate.template.md). Ensure **gaps**, **result**, and **rationale** are filled; attach or link **Review evidence pack** when Review and Assay are adjacent.

---

## Decisions kept

- **Three decision buckets** remain: **Ember Log** (operational), **ADR** (architecture), **Directive** (how we work)—[`CONCEPT-MAP.md`](CONCEPT-MAP.md).
- **Meeting model** remains authoritative for **cadence and modes**; artifacts **feed** meetings, not replace them.
- **Assay Gate** stays the named **release evidence** decision; PDLC stage gates remain **product** lifecycle constructs—[`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md).

---

## Drift

- **Risk:** Retro Records become **verbose minutes**—**mitigation:** cap themes; prioritize **pointers** over prose ([`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) § “From retro to directives”).
- **Risk:** DCP backlog **blocks** trivial fixes—**mitigation:** small clarifications may ship via PR with a **Retro Record** bullet; reserve full DCP for scope/approval/expiry changes.
- **Risk:** Teams invent a “Decision Record” **repository** that duplicates Ember Log—**mitigation:** use the Markdown block in § [Formal decision (Ember Log block)](#1-formal-decision-ember-log-block).
- **Risk:** **Review evidence pack** and **Assay packet** are merged into one slide deck—**mitigation:** keep **readiness** (Review) and **release pass/fail** (Assay) separable in naming and checklist.
- **Risk:** “Spark definition” becomes a duplicate WBS—**mitigation:** treat **Spark = Task**; one hierarchy ([`process-and-flows.md`](process-and-flows.md)).

---

## Inconsistencies

| Topic | Resolution |
|-------|------------|
| Industry “decision log” vs Forge | **Ember Log** is the prescriptive home; alias “Decision Record” to Ember Log lines or the formal block above. |
| “Retro Record” as a document name | Acceptable if it **links** experiments to directive PRs; not a parallel taxonomy if retro notes + traceability suffice ([`CONCEPT-MAP.md`](CONCEPT-MAP.md)). |
| Seven-phase benchmark vs P1–P6 | Map artifacts in the **artifact matrix** using **P1–P6**; benchmark names in [`../../../pdlc/PDLC.md`](../../../pdlc/PDLC.md). |

---

## Open questions

- Whether to publish a **single** combined template for “Review pack + Assay packet” handoff versus keeping two files—**product ops** preference.
- How strictly to require the **long Ember Log block** vs one-line entries for small decisions—**team scale**; default: block for cross-hat or irreversible choices only.
- Optional **project-local** `sdlc/` schema for structured decisions—allowed if it still **rolls up** to Ember Log traceability ([`CONCEPT-MAP.md`](CONCEPT-MAP.md)).

---

## Related links

| Topic | File |
|-------|------|
| Concept matrix | [`CONCEPT-MAP.md`](CONCEPT-MAP.md) |
| Meetings | [`meetings-model.md`](meetings-model.md), [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) |
| Daily artifacts | [`daily/README.md`](daily/README.md) |
| Product Spark / planning | [`planning/README.md`](planning/README.md) |
| PDLC / SDLC bridge | [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md) |
