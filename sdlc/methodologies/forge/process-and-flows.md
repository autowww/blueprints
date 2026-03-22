# Forge — major processes & flow maps

Mermaid diagrams below render on GitHub and in many Markdown viewers.

## 1. Forge iteration lifecycle (high level)

```mermaid
flowchart LR
  subgraph intake[Continuous]
    OreIntake[Ore intake]
  end
  subgraph iteration[Forge iteration]
    Refine[Refinement]
    Plan[Planning]
    Daily[Daily sync loop]
    Review[Review]
    Assay[Assay Gate]
  end
  subgraph ship[Ship]
    Release[Release]
  end
  Retro[Retro]
  OreIntake --> Refine
  Refine --> Plan
  Plan --> Daily
  Daily --> Daily
  Daily --> Review
  Review --> Assay
  Assay --> Release
  Release --> Retro
  Retro --> OreIntake
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

### Spark = Task (WBS mapping)

In projects with an existing **milestone → epic → story → task** hierarchy, Forge terms map directly — no parallel namespace:

| Existing level | Forge equivalent | ID example |
|----------------|-----------------|------------|
| Epic / feature request | **Ore** | `M1E3` (pre-refinement) |
| Story (refined) | **Ingot** | `M1E3S2` |
| Task (implementation slice) | **Spark** | `M1E3S2T4` |

Spark IDs inherit from the WBS scheme. Spark-specific data (state, DoD, journal) lives in `forge-logs/`, not in the requirements tree. If existing Stories already carry clear acceptance criteria, they are effectively Ingots — no extra ceremony needed.

## 3. State model

```mermaid
stateDiagram-v2
  [*] --> Ore
  Ore --> Ingot: refine
  Ore --> Rejected: reject
  Ingot --> Spark: decompose
  Ingot --> Banked: bank
  Spark --> InCharge: pull
  Spark --> Banked: bank
  InCharge --> Done: evidence gathered
  InCharge --> Blocked: external impediment
  InCharge --> Banked: bank
  Blocked --> InCharge: unblock
  Banked --> Spark: unbank
  Banked --> Ingot: unbank
  Done --> Released: Assay Gate pass
  Done --> Spark: Assay Gate fail
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

```mermaid
flowchart TD
  A[Ore item] --> B{Problem and value clear?}
  B -->|No| C[Clarify with stakeholders]
  C --> A
  B -->|Yes| D{Acceptance route defined?}
  D -->|No| E[Define acceptance criteria]
  E --> D
  D -->|Yes| F{Bellows challenge needed?}
  F -->|Yes| G[Invoke relevant Bellows]
  G --> H{Concerns raised?}
  H -->|Critical| I[Rework or Bank]
  I --> A
  H -->|Minor or none| J[Promote to Ingot]
  F -->|No| J
  J --> K[Ingot in backlog]
```

## 5. Planning flow (Ingot → Sparks → iteration scope)

```mermaid
flowchart TD
  A[Ordered Ingots] --> B[Decompose into Sparks]
  B --> C{Spark small enough?}
  C -->|No| D[Split further]
  D --> C
  C -->|Yes| E[Assign phase prefix]
  E --> F[Add to iteration backlog]
  F --> G{Capacity remaining?}
  G -->|Yes| A
  G -->|No| H[Iteration scope locked]
  H --> I[Leave margin for interruption]
```

## 6. Daily execution loop

```mermaid
flowchart TD
  S[Start of day] --> M[Daily sync 15m]
  M --> C[Confirm Charge]
  C --> W[Work Sparks]
  W --> B{Blocked?}
  B -->|Yes| BK{Strategic or external?}
  BK -->|External| BL[Mark Blocked; escalate]
  BL --> W
  BK -->|Strategic| BA[Bank with context]
  BA --> C
  B -->|No| D{Decision point?}
  D -->|Yes| EL[Ember Log entry]
  D -->|No| W
  EL --> W
  W --> E[End of day: journal entry]
```

## 7. Assay Gate flow

```mermaid
flowchart TD
  C[Completed Sparks] --> T[Tests pass]
  T --> A[Acceptance criteria met]
  A --> R[Risk checks completed]
  R --> P[Performance thresholds met]
  P --> AG{All evidence present?}
  AG -->|Yes| Pass[Assay Gate PASS → Release]
  AG -->|No| Gap[Identify gaps]
  Gap --> Fix[Gather missing evidence]
  Fix --> C
```

## 8. Bellows challenge flow

```mermaid
flowchart TD
  DP[Decision point reached] --> ID[Identify relevant disciplines]
  ID --> INV[Invoke Bellows for selected disciplines]
  INV --> CH[Challenge runs: concerns, severity, recommendation]
  CH --> SEV{Critical concerns?}
  SEV -->|Yes| ACT[Act: rework, split, Bank, or accept risk]
  ACT --> EL[Ember Log: capture decision]
  SEV -->|No| PROC[Proceed with work]
  PROC --> EL
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

**Bellows challenge** — Bellows are invoked at decision points (refinement, pre-build, pre-release), not on every action. Each Bellows references its discipline's bridge document to calibrate challenge intensity to the current SDLC phase.

## 11. Links

- [Ceremonies detail](ceremonies-prescriptive.md) · [Foundation](foundation-connection.md) · [Overview](../forge.md)
