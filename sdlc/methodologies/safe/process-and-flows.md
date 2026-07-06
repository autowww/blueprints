---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SAFe — process and flows

**Purpose:** Visual and narrative description of SAFe process flows at **team**, **program (ART)**, and **portfolio** levels. KS diagram templates for key lifecycle patterns.

---

## 1. PI lifecycle (program level)

A **Program Increment (PI)** is the primary planning and delivery cadence in SAFe — typically 8–12 weeks containing 4–5 iterations plus an Innovation & Planning (IP) iteration.

```blueprint-diagram
key: linear
alt: PI lifecycle (program level)
title: Program Increment lifecycle
summary: How an ART plans, executes, and closes one bounded program-level planning and delivery cadence.
node: PI lifecycle (program level)
detail: Primary SAFe cadence spanning development iterations plus an Innovation and Planning iteration.
more: Typically eight to twelve weeks with four to five iterations and one IP iteration reserved for exploration, demos, and next-PI preparation.
node: Start
detail: Opens the PI with cross-team alignment from PI Planning and committed objectives.
node: Core steps (see walkthrough below)
detail: Teams execute iterations, integrate work, and demonstrate progress through the increment.
more: Each iteration follows team Scrum or Kanban while feeding program ceremonies such as System Demo and ART sync.
node: Outcome
detail: Closes the PI with inspect-and-adapt learning and readiness for the next planning event.
fallback_ascii: |
  PI lifecycle (program level)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome
```

### IP iteration

The final iteration in a PI is typically reserved for:
- Innovation and exploration (hackathons, spikes)
- Infrastructure and tooling improvements
- PI-level System Demo and I&A
- Preparation for next PI Planning
- Training and cross-team knowledge sharing

Teams should **not** plan feature work into the IP iteration.

---

## 2. Iteration flow (team level)

Within each iteration, team-level flow follows standard Scrum/Kanban patterns:

```blueprint-diagram
key: linear
alt: Iteration flow (team level)
title: Team iteration flow
summary: How a single team runs Scrum or Kanban work within each PI iteration.
node: Iteration flow (team level)
detail: Team-scoped delivery rhythm nested inside the larger program increment.
node: Start
detail: Begins iteration planning with a committed backlog slice for the timebox.
node: Core steps (see walkthrough below)
detail: Daily execution, refinement, and review against iteration goals.
more: Follows standard Scrum or Kanban patterns; the page defers step detail to the walkthrough below.
node: Outcome
detail: Produces a potentially shippable increment and iteration review outcomes.
node: Note: SAFe-specific addition:
detail: Every iteration culminates in a cross-team System Demo.
more: This SAFe addition ensures continuous integration visibility across the ART, not only within the team.
fallback_ascii: |
  Iteration flow (team level)

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: SAFe-specific addition:
```

**SAFe-specific addition:** team iterations feed into the **System Demo** every iteration, ensuring continuous cross-team integration.

---

## 3. ART coordination flow

```blueprint-diagram
key: swimlane
alt: ART coordination flow
title: ART coordination lanes
summary: How parallel teams on a release train coordinate delivery handoffs and inspect-and-adapt feedback.
node: ART coordination flow
detail: Program-level coordination pattern for teams sharing one Agile Release Train.
node: Lane A
detail: Delivery lane where teams execute feature work toward integrated outcomes.
node: handoff
detail: Visible transfer of dependency output to a consuming team or iteration.
more: Dependencies surfaced at PI Planning are tracked on the program board and reviewed in ART sync.
node: shared outcome
detail: Integrated result demonstrated to the ART and stakeholders.
node: Lane B
detail: Improvement lane for structured review and adaptation across the train.
node: inspect / adapt
detail: Reviews progress, risks, and process adjustments at program cadence.
node: feedback
detail: Actionable input that informs the next planning or execution cycle.
fallback_ascii: |
  ART coordination flow

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
```

---

## 4. Portfolio Kanban flow

Epics flow through the portfolio Kanban system before reaching ARTs:

```blueprint-diagram
key: linear
alt: Portfolio Kanban flow
title: Portfolio epic Kanban flow
summary: How strategic epics are governed from intake through validation before ART implementation.
node: Portfolio Kanban flow
detail: Portfolio-level Kanban governing epics before they consume ART capacity.
node: Start
detail: Epics enter from strategic themes, stakeholders, or team proposals.
node: Core steps (see walkthrough below)
detail: Epics pass funnel, review, analysis, and go or no-go portfolio gates.
more: Stages include reviewing, Lean business case analysis, LPM decision, backlog, implementing on ARTs, and done validation.
node: Outcome
detail: Benefit hypothesis is validated or invalidated with traceable portfolio decisions.
node: Note: | Capture epics from strategic themes, stakeholders, teams |
detail: Funnel stage captures candidate epics without heavy upfront investment.
more: Lightweight intake filters duplicates and low-value items before deeper analysis begins.
fallback_ascii: |
  Portfolio Kanban flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: | Capture epics from strategic themes, stakeholders, teams |
  |
```

| Stage | Activity |
|-------|----------|
| **Funnel** | Capture epics from strategic themes, stakeholders, teams |
| **Reviewing** | Lightweight evaluation; filter out low-value or duplicate items |
| **Analyzing** | Develop **Lean business case** (benefit hypothesis, MVP scope, cost estimate) |
| **Go / No-Go** | LPM decides based on Lean budget, strategy alignment, capacity |
| **Portfolio Backlog** | Approved epics awaiting ART capacity |
| **Implementing** | Epic decomposed into features on ART program backlog |
| **Done** | Benefit hypothesis validated or invalidated |

---

## 5. Release on demand

SAFe decouples **release** from **PI cadence**. Teams can release at any point when:

1. Features meet **Definition of Done** and acceptance criteria
2. Continuous delivery pipeline is green (build, test, stage)
3. Business decides to release (business value, market timing)

```blueprint-diagram
key: linear
alt: Release on demand
title: Release on demand flow
summary: How teams ship value on a cadence independent of PI planning boundaries.
node: Release on demand
detail: Decouples customer-facing release timing from program increment rhythm.
node: Start
detail: A feature reaches Definition of Done with passing acceptance criteria.
node: Core steps (see walkthrough below)
detail: Pipeline builds, tests, and stages before a governed business release decision.
more: Requires a green continuous delivery pipeline; the business chooses timing for market or value reasons.
node: Outcome
detail: Value reaches users without waiting for the next PI boundary.
node: Note: continuous delivery pipeline
detail: Spans build, test, stage, and release readiness across all release activities.
more: PI cadence provides alignment while release cadence provides value delivery; they need not match.
fallback_ascii: |
  Release on demand

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: continuous delivery pipeline
```

The **continuous delivery pipeline** spans all four activities. PI cadence provides **alignment**; release cadence provides **value delivery**. They need not be the same.

---

## 6. Dependency management

Dependencies are first surfaced at **PI Planning** and tracked throughout the PI:

| When | How |
|------|-----|
| **PI Planning** | Teams identify dependencies during breakouts; visualized on the **program board** as strings between teams/iterations |
| **ART Sync** | RTE and SMs review dependency status; escalate blocked items |
| **Daily Stand-up** | Teams surface intra-team blockers; cross-team items go to SM → ART Sync |
| **I&A** | Review dependency-related delays; improve architectural runway to reduce future dependencies |

**ROAM model** for risks identified at PI Planning:

| Status | Meaning |
|--------|---------|
| **Resolved** | Risk no longer exists |
| **Owned** | Someone accepted responsibility and has a mitigation plan |
| **Accepted** | Impact understood and accepted; no further action |
| **Mitigated** | Actions taken to reduce probability or impact |

---

## 7. References

- [`https://forgesdlc.com/methodology-safe.html`](https://forgesdlc.com/methodology-safe.html) — SAFe methodology summary
- [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) — event detail with inputs/outputs
- [`roles.md`](roles.md) — who does what
- [`foundation-connection.md`](foundation-connection.md) — SDLC phase mapping
