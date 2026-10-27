---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge — major processes & flow maps

Diagrams below use **` ```blueprint-diagram `** fences on the published handbook; GitHub shows the source as a fenced block.

## 1. Forge iteration lifecycle (high level)

```blueprint-diagram
key: swimlane
alt: Forge iteration lifecycle (high level)
title: Forge iteration delivery cycle
summary: How forward delivery and inspect-and-adapt feedback run in parallel across one bounded Forge iteration.
node: Forge iteration lifecycle (high level)
detail: Frames the dual-lane view of ceremonies and outcomes inside one iteration.
more: Ore intake stays continuous; refinement, planning, Charge, review, and Assay Gate shape what ships in the cycle.
node: Lane A
detail: The forward path from intake through ceremonies toward release outcomes.
more: Refinement shapes Ore into Ingots; planning decomposes Ingots into Sparks scoped for the iteration.
node: handoff
detail: Explicit transfer when work crosses ceremony or ownership boundaries.
more: Daily syncs confirm the Charge; review surfaces evidence before the Assay Gate release decision.
node: shared outcome
detail: The traceable increment and evidence the iteration must leave behind.
more: Sparks across phases A–F produce artifacts ready for governed release when the Assay Gate passes.
node: Lane B
detail: The parallel inspect-and-adapt path across iteration ceremonies.
more: Teams challenge scope and evidence without losing decision memory in forge-logs.
node: inspect / adapt
detail: Ceremonies review progress against acceptance criteria and blockers.
more: Retro captures learning that feeds back as new Ore so the next cycle improves.
node: feedback
detail: Learnings loop back into continuous Ore intake and upstream planning.
more: Blocked versus Banked states preserve context when work pauses strategically versus externally.
fallback_ascii: |
  Forge iteration lifecycle (high level)

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

## 2. Work unit hierarchy

```
Product backlog
  └── Ore              (raw, unrefined)
        └── Ingot      (refined, plannable)
              └── Spark (executable, testable)

Daily execution
  └── Charge           (today's selected Sparks)

Time horizon
  └── Forge iteration  (one delivery cycle containing Sparks across phases A–F)
```

| Level | Forge term | Comparable concept | Typical lifespan |
|-------|------------|-------------------|------------------|
| **Coarsest** | Ore | Epic or feature request (pre-refinement) | Days to weeks |
| **Mid** | Ingot | User story or feature (refined, ready) | One iteration |
| **Finest** | Spark | Task or sub-task (executable) | One focused session (~1–4 hours) |
| **Daily set** | Charge | Daily commitment | One day |
| **Cycle** | Forge iteration | Sprint or release cycle | 1–2 weeks |

> **Under the Epic execution profile.** **Charge** lists **Epics** in play (a daily view, not a Kanban system of record). **Forge Spark** remains the smallest **delivery** unit in **core Forge** (Ore → Ingot → Spark → Charge with Sparks). The profile is an opt-in overlay — see [`EPIC-EXECUTION-PROFILE.md`](EPIC-EXECUTION-PROFILE.md).

### Spark = Task (WBS mapping)

In projects with an existing **milestone → epic → story → task** hierarchy, Forge terms map directly — no parallel namespace:

| Existing level | Forge equivalent | ID example |
|----------------|-----------------|------------|
| Epic / feature request | **Ore** | `M1E3` (pre-refinement) |
| Story (refined) | **Ingot** | `M1E3S2` |
| Task (implementation slice) | **Spark** | `M1E3S2T4` |

Spark IDs inherit from the WBS scheme. Spark-specific data (state, DoD, journal) lives in `forge-logs/`, not in the requirements tree. If existing Stories already carry clear acceptance criteria, they are effectively Ingots — no extra ceremony needed.

### Exploration spike vs Forge Spark

An **exploration spike** (also **discipline spike**) is **time-boxed learning**—prototyping, feasibility checks, unknowns—whose primary outcome is **evidence and a written record**, not a shippable increment. It is **not** a Forge **Spark**: a Spark is the smallest **committed delivery** unit (task-level) in the Ore → Ingot → Spark → Charge pipeline.

Exploration spikes often use Versona **sessions** with `work_item_kind` `spike_discipline` or `spike_general`, live under `forge-logs/versona/`, and close with `outputs/SPIKE-CLOSE.md` plus Ember Log when decisions are made. They may **spawn** new Ore, Ingots, or WBS lines; follow-up work then appears as normal Sparks (often `discover:` or `design:` flavored). Full lifecycle: [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md).

### Versona sessions under `forge-logs/`

**Versona** invocation context (per-call folders, inputs/outputs, optional transcripts) should live under **`forge-logs/versona/<actor>/<session-id>/`** as the default layout—see [`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §7. Optional **enriched** artifacts (ledger, JSON manifests, diagram IR, graph append-only logs) extend that model per [`VERSONA-OPERATING-MODEL.md`](VERSONA-OPERATING-MODEL.md). Teams that keep all Forge state under `forge/` may use the alias **`forge/versona-sessions/`** instead; pick one convention per repo and document it in `forge/` or `sdlc/README.md`. Cursor rule **templates** in blueprints live under [`versona/README.md`](versona/README.md) (see **Source layout** there).

## 3. State model

```blueprint-diagram
key: state
alt: State model
title: Forge work-unit states
summary: How Ore advances through refinement, execution, and release gates to a governed outcome.
node: State model
detail: Frames the lifecycle states that govern Forge work units on this page.
more: The state table below defines Ore through Released and Rejected with meanings distinct from simple Kanban.
node: Start
detail: Work enters as raw Ore or returns from retro as new intake.
more: Spark-specific state and journal data live in forge-logs/, not the requirements tree.
node: Core steps (see walkthrough below)
detail: Units move through refinement, Charge, Done, and gate review.
more: Banked differs from Blocked; Done is not Released until the Assay Gate passes with evidence.
node: Outcome
detail: Work exits as Released after the gate or Rejected with a recorded reason.
more: Rejected items close with rationale rather than silent deletion, keeping the trail reviewable.
node: Note: | Raw, unrefined input |
detail: Anchors Ore as the default entry state for unrefined intake.
more: Ore maps to pre-refinement epics or features before refinement shapes plannable Ingots.
fallback_ascii: |
  State model

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: | Raw, unrefined input |
  |
```

| State | Meaning |
|-------|---------|
| **Ore** | Raw, unrefined input |
| **Ingot** | Refined, plannable work |
| **Spark** | Decomposed, executable work |
| **In Charge** | Active in today's daily set |
| **Blocked** | External impediment prevents progress |
| **Banked** | Intentionally paused with preserved context (strategic) |
| **Done** | Evidence gathered, ready for Assay Gate |
| **Released** | Passed Assay Gate, shipped |
| **Rejected** | Not viable; closed with reason |

## 4. Refinement flow (Ore → Ingot)

```blueprint-diagram
key: decision
alt: Refinement flow (Ore → Ingot)
title: Ore to Ingot refinement
summary: How refinement shapes raw Ore into plannable Ingots ready for iteration planning.
node: Refinement flow (Ore
detail: Refinement begins with raw Ore selected for shaping at the ceremony.
more: Aligns with SDLC Phase B Specify and specify: Sparks; stories with clear acceptance may already qualify as Ingots.
node: Ingot)
detail: Refined work exits with enough clarity for planning decomposition.
more: Versonas may be invoked at this decision point for structured discipline review before planning.
fallback_ascii: |
  Refinement flow (Ore
      |
      v
  Ingot)
```

## 5. Planning flow (Ingot → Sparks → iteration scope)

```blueprint-diagram
key: decision
alt: Planning flow (Ingot → Sparks → iteration scope)
title: Ingot to iteration scope
summary: How planning decomposes Ingots into Sparks and bounds what one iteration will deliver.
node: Planning flow (Ingot
detail: Planning starts from a refined Ingot ready for decomposition.
more: Engineering hat typically leads Spark decomposition while product hat shaped upstream Ingots.
node: Sparks
detail: Ingots break into executable, testable Sparks with inherited WBS IDs.
more: Sparks map to tasks; flavor prefixes discover: through release: align to phases A–F.
node: iteration scope)
detail: The bounded set of Sparks committed for one Forge iteration.
more: Charge is a daily view of selected Sparks, not a separate backlog board.
fallback_ascii: |
  Planning flow (Ingot
      |
      v
  Sparks
      |
      v
  iteration scope)
```

## 6. Daily execution loop

```blueprint-diagram
key: decision
alt: Daily execution loop
title: Daily Charge execution gate
summary: How daily sync confirms the Charge and routes blockers through refine or escalate paths.
node: Current state
detail: Today's Charge reflects which Sparks are active in execution.
more: Daily sync surfaces blockers and confirms the day's selected Sparks across build: work.
node: Checkpoint / gate
detail: The team checks whether each Spark can proceed or needs intervention.
more: Blocked marks external impediment; Banked preserves context for strategic pause.
node: refine or escalate
detail: Rework scope, unblock, or escalate when the gate does not clear.
more: Charge execution aligns with Phase D Build; impediments get traceable resolution paths.
node: Continue flow
detail: Cleared Sparks proceed through bounded execution toward Done evidence.
more: Done gathers evidence but is not Released until the Assay Gate passes.
fallback_ascii: |
  Daily execution loop

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 7. Assay Gate flow

```blueprint-diagram
key: decision
alt: Assay Gate flow
title: Assay Gate release decision
summary: How strict release review decides whether Done work may ship as Released.
node: Current state
detail: Sparks marked Done arrive with gathered evidence at the gate.
more: Done means evidence is ready for Assay Gate review, not yet shipped.
node: Checkpoint / gate
detail: The Assay Gate judges evidence quality against release criteria.
more: Aligns with Phase E Verify and F Release; verify: and release: Sparks support the ceremony.
node: refine or escalate
detail: Rework evidence or escalate when the release bar is not met.
more: Failed gates return work for refinement rather than silent partial release.
node: Continue flow
detail: Passed work advances to Released with governed ship approval.
more: Released means Assay Gate pass; the distinction from Done keeps release reviewable.
fallback_ascii: |
  Assay Gate flow

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 8. Versona flow (sessions and discipline work)

```blueprint-diagram
key: decision
alt: Versona flow (sessions and discipline work)
title: Versona session decision gate
summary: How bounded Versona sessions support discipline work at Forge decision points.
node: Current state
detail: A decision point or discipline question triggers optional Versona invocation.
more: Sessions live under forge-logs/versona/; exploration spikes use spike kinds, not Forge Sparks.
node: Checkpoint / gate
detail: The session checks whether discipline input is ready to proceed or merge.
more: Each Versona calibrates review depth to the current SDLC phase via bridge documents.
node: refine or escalate
detail: Rework inputs or escalate when structured output is insufficient.
more: §5 structured output or other discipline artifacts must be reviewable before downstream work continues.
node: Continue flow
detail: Accepted session outputs inform the next Forge ceremony or Spark work.
more: Discipline spikes close with SPIKE-CLOSE.md and may spawn new Ore or Ingots as follow-up.
fallback_ascii: |
  Versona flow (sessions and discipline work)

  Current state
      |
      v
  Checkpoint / gate
      |
      +-- no ──► refine or escalate
      |
     yes
      v
  Continue flow
```

## 9. Cross-phase mapping (A–F) in one iteration

| Phase | Where it happens in Forge |
|-------|---------------------------|
| A Discover | Continuous Ore intake + `discover:` Sparks |
| B Specify | Refinement (Ore → Ingot) + `specify:` Sparks |
| C Design | Planning decomposition + `design:` Sparks |
| D Build | Charge execution + `build:` Sparks |
| E Verify | Assay Gate + `verify:` Sparks |
| F Release | Assay Gate pass + `release:` Sparks |

## 10. Flow details (walkthrough)

**Iteration lifecycle** — Ore intake is continuous; Refinement shapes selected Ore into Ingots with enough clarity for Planning. Inside the iteration, daily syncs confirm the Charge and surface blockers. Review assesses evidence quality; the Assay Gate makes the strict release decision. Retro captures learning that feeds back as new Ore.

**Work unit hierarchy** — Forge terms layer on existing WBS conventions. Ore maps to pre-refinement epics/features; Ingots to refined stories; Sparks to tasks. The Charge is a daily view, not a separate backlog. Forge iterations align with milestones in the project's existing structure.

**State model** — The key distinctions from a simple Kanban board: (1) Banked vs Blocked separates strategic pause from external impediment, (2) Done is not Released until the Assay Gate passes, and (3) Rejected items are closed with a reason rather than silently deleted.

**Versonas** — Discipline **virtual personas** are invoked at **decision points** (refinement, pre-build, pre-release) for §5 structured output or other discipline work—not on every action. When using the §5 report shape, each Versona uses its bridge document to calibrate **review depth** to the current SDLC phase ([`versona/VERSONA-FRAMEWORK.md`](versona/VERSONA-FRAMEWORK.md) §1–2).

## 11. Links

- [Ceremonies detail](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md) · [Overview](https://forgesdlc.com/methodology-overview.html)
