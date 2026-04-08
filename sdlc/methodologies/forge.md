---
slug: methodology-overview
tier: 101
lens: methodology
nav_section: Discover ForgeSDLC
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge SDLC

## Why AI changes everything

Traditional delivery methodologies — Scrum, SAFe, Kanban, Waterfall — were designed for a world where humans write code and AI assists. That world is ending. AI agents now produce the majority of code, tests, and specifications in leading development teams. **The human role has shifted from producer to governor.** Forge SDLC is built for this inversion: humans own intent, judgment, and evidence-based release decisions; AI produces, and **Versonas**—discipline **virtual personas** whose activities include structured **challenge** passes—evaluate AI output before it ships.

## What it is

**Forge** is a delivery methodology for work that benefits from rapid iteration, explicit challenge, and evidence-based release decisions. It keeps standard industry terms where the process is standard (backlog, refinement, planning, daily, review, retro, release) and introduces new terms only where the method is genuinely different.

Raw ideas enter as **Ore**, are refined into **Ingots**, decomposed into **Sparks** (the smallest meaningful executable unit), and selected into a daily **Charge**. **Versonas** (discipline virtual personas) apply discipline-specific judgment—including structured **challenge** passes that pressure-test work from each lens. Key decisions are captured in the **Ember Log**. Intentionally paused work is **Banked**. Release decisions pass an evidence-based **Assay Gate**.

Forge is **not** a rebranding of Agile — it is an extension of it for modern AI-enabled work. It improves clarity, decision quality, speed of learning, and release confidence.

## Process diagram

```blueprint-diagram
key: swimlane
alt: Diagram
```

*Ore → Ingot → Spark → Charge → Review → Assay Gate → Release → learning feeds new Ore.*

---

## Core vocabulary (8 terms)

| Term | What it adds | Detail |
|------|-------------|--------|
| **Ore** | Raw input that is not ready for commitment | [State model](forge/process-and-flows.md#3-state-model) · [Intake ceremony](forge/ceremonies-prescriptive.md#0-ongoing--ore-intake) · [Refinement flow](forge/process-and-flows.md#4-refinement-flow-ore--ingot) |
| **Ingot** | Refined work that is ready for planning | [Refinement ceremony](forge/ceremonies-prescriptive.md#1-refinement-ore--ingot) · [Planning flow](forge/process-and-flows.md#5-planning-flow-ingot--sparks--iteration-scope) |
| **Spark** | The smallest meaningful executable unit | [Spark = Task mapping](#spark--task-hierarchy-mapping) · [Work unit hierarchy](forge/process-and-flows.md#2-work-unit-hierarchy) · [Planning ceremony](forge/ceremonies-prescriptive.md#2-planning-ingot--sparks) |
| **Charge** | The daily selected set of Sparks | [Daily sync ceremony](forge/ceremonies-prescriptive.md#3-daily-sync-charge-confirmation) · [Daily operations](forge/daily/README.md) · [Execution loop](forge/process-and-flows.md#6-daily-execution-loop) |
| **Versonas** | Discipline virtual personas; activities include structured challenge (contract-specified) and other discipline work | [Versonas overview](forge/versona/README.md) · [Versona flow (sessions)](forge/process-and-flows.md#8-versona-flow-sessions-and-discipline-work) · [Template catalog](forge/versona/README.md#template-catalog) |
| **Ember Log** | Lightweight record of decisions, assumptions, and unresolved risks | [Daily operations](forge/daily/README.md) · [Review ceremony](forge/ceremonies-prescriptive.md#4-review-evidence-assessment) |
| **Banked** | Intentionally paused work with preserved context | [State model](forge/process-and-flows.md#3-state-model) |
| **Assay Gate** | Evidence-based release gate | [Assay Gate ceremony](forge/ceremonies-prescriptive.md#5-assay-gate-release-readiness) · [Assay Gate flow](forge/process-and-flows.md#7-assay-gate-flow) |

### Exploration spikes (discipline)

A **discipline exploration spike** is **time-boxed learning** (feasibility, unknowns)—**not** a Forge **Spark**, which is the smallest **delivery** task. Spikes use Versona sessions under `forge-logs/versona/`, close with `outputs/SPIKE-CLOSE.md`, and may hand off to roadmap/WBS when anchors are missing. Full lifecycle: [Discipline exploration spike](forge/versona/DISCIPLINE-SPIKE.md).

### Spark = Task (hierarchy mapping)

In projects using a **milestone → epic → story → task** hierarchy, Forge terms map directly to existing levels — no parallel namespace:

| Existing level | Forge equivalent | Notes |
|----------------|-----------------|-------|
| Epic / feature request (pre-refinement) | **Ore** | Work is vague, not yet schedulable |
| Story (refined, ready) | **Ingot** | Clear value, constraints, and acceptance criteria |
| Task (implementation slice) | **Spark** | Every executable unit is a Spark under Forge |

Spark IDs inherit from the project's WBS scheme (e.g. `M1E1S1T1`). Spark-specific data (state, DoD, journal) lives in `forge-logs/`, not in the requirements tree.

---

## Mapping to this blueprint's SDLC

[`SDLC.md`](../SDLC.md) uses **Phases A–F**. Forge maps Sparks to phases via a prefix convention:

| Phase | Spark prefix | Example |
|-------|-------------|---------|
| A Discover | `discover:` | "discover: interview stakeholders about notification preferences" |
| B Specify | `specify:` | "specify: acceptance criteria for push notifications" |
| C Design | `design:` | "design: notification service architecture + ADR" |
| D Build | `build:` | "build: implement FCM integration" |
| E Verify | `verify:` | "verify: integration tests for notification delivery" |
| F Release | `release:` | "release: changelog, tag v1.2.0" |

A Forge iteration typically contains Sparks across multiple phases.

---

## Core principles and execution detail

Forge is anchored by **four core principles** for AI-native delivery (*shape before speed*, *flow over ceremony*, *AI-first human-gated*, *make gains compound*). Narrative on the product site: [Four core principles](https://forgesdlc.com/blog/four-core-principles.html).

[Forge principles (full list)](https://forgesdlc.com/forge-principles-deep-dive.html) adds **execution principles** and **lean tenets**—how those ideas show up in practice. The summary below matches that page.

---

## Principles (summary)

1. **Refine before you commit.** Ore must become Ingot before execution.
2. **Keep work small enough to challenge.** Sparks make learning fast and waste visible.
3. **AI strengthens thinking; humans own judgment.** Versonas challenge, not decide.
4. **Decisions deserve memory.** The Ember Log captures *why*.
5. **Release on evidence, not optimism.** The Assay Gate makes release discipline explicit.
6. **Paused is not failed.** Banked is a strategic choice with preserved context.
7. **Standard process stays standard.** Forge adds precision inside ceremonies, not alternatives.
8. **Scale by trust, not by process weight.** Same vocabulary solo through enterprise.

### Lean tenets (keeping Forge lightweight)

Forge must never add more ceremony than it removes waste. Key tenets:

- **One hierarchy, one set of IDs.** Sparks are existing Tasks with Forge semantics layered on — do not duplicate the WBS.
- **Collapse levels when they already fit.** If refinement already produces ready Stories, those are Ingots. No extra ceremony.
- **Log decisions, not narration.** Two lines explaining *why* beat two pages of session recap.
- **Automate the journal.** If logging feels like overhead, fix the tooling.
- **Versonas at decision points, not everywhere.** Before costly commitments, not as bureaucracy.
- **Charge is a view, not a board.** Label or filter, not a separate tracking surface.
- **Scale formality to risk.** Solo: self-assessment checklist. Enterprise: gate meeting.
- **Defer tooling until volume demands it.** Start with journal + git; add dashboards later.
- **No shadow rituals.** Standard Forge ceremony names and mechanics inside—no parallel standing meetings for the same intent.

---

## Scaling model

| Scale | Team size | Configuration |
|-------|-----------|---------------|
| **Solo** | 1 | All hats on one person. Versonas are primarily AI agents. Charge is a personal daily list. Ember Log is a running markdown file. Assay Gate is a self-assessment checklist. |
| **Small team** | 2–5 | Explicit Owner and Implementer(s). Charge is negotiated in a brief daily sync. Versonas combine AI agents and peer challenge. |
| **Team** | 5–12 | Full ceremony set. Designated Versona disciplines. Ember Log maintained collaboratively. Assay Gate may include stakeholder sign-off. |
| **Multi-team** | 12+ | Shared Ore pipeline. Cross-team Assay Gates. Versonas may include dedicated challenge roles. Forge iterations align across teams. |

**Git:** Branching and commit conventions scale with this table — see [`forge/setup/BRANCHING-STRATEGY.md`](forge/setup/BRANCHING-STRATEGY.md).

---

## Prescriptive deep dive

| Chapter | File |
|---------|------|
| Foundation & fit | [`forge/foundation-connection.md`](forge/foundation-connection.md) |
| Roles | [`forge/roles.md`](forge/roles.md) |
| Ceremonies | [`forge/ceremonies-prescriptive.md`](forge/ceremonies-prescriptive.md) |
| Meeting model | [`forge/meetings-model.md`](forge/meetings-model.md) |
| Process & flows | [`forge/process-and-flows.md`](forge/process-and-flows.md) |
| Bridge (PDLC ↔ SDLC) | [`forge/FORGE-SDLC-PDLC-BRIDGE.md`](forge/FORGE-SDLC-PDLC-BRIDGE.md) |
| Versonas (discipline agents) | [`forge/versona/README.md`](forge/versona/README.md) |
| Discipline exploration spike | [`forge/versona/DISCIPLINE-SPIKE.md`](forge/versona/DISCIPLINE-SPIKE.md) |
| Daily operations | [`forge/daily/README.md`](forge/daily/README.md) |
| Product planning | [`forge/planning/README.md`](forge/planning/README.md) |
| Setup & adoption | [`forge/setup/README.md`](forge/setup/README.md) |
| Git branching & commits | [`forge/setup/BRANCHING-STRATEGY.md`](forge/setup/BRANCHING-STRATEGY.md) |

---

## Related guides

- [Agentic SDLC](agentic-sdlc.md) — cross-cutting agent layer (Forge extends this with Versonas)
- [Agentic coding standards](agentic-coding-standards.md) — AI-assisted coding and review standards; Forge mapping (Charge, Ember Log, Versonas, Assay)
- [Spec-driven development](spec-driven-development.md) — durable specs complement Forge's Ingot refinement
- [Scrum](scrum.md) · [Kanban](kanban.md) · [XP](xp.md) — Forge ceremonies map to the same C1–C6 foundation
- [Ceremonies — Forge fork](ceremonies/forge.md) — C1–C6 mapped to Forge events
- [Roles & archetypes](roles-archetypes.md) — human accountability model