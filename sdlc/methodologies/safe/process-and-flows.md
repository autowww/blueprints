# SAFe — process and flows

**Purpose:** Visual and narrative description of SAFe process flows at **team**, **program (ART)**, and **portfolio** levels. KS diagram templates for key lifecycle patterns.

---

## 1. PI lifecycle (program level)

A **Program Increment (PI)** is the primary planning and delivery cadence in SAFe — typically 8–12 weeks containing 4–5 iterations plus an Innovation & Planning (IP) iteration.

```ks-diagram
key: linear
alt: Diagram
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

```ks-diagram
key: linear
alt: Diagram
```

**SAFe-specific addition:** team iterations feed into the **System Demo** every iteration, ensuring continuous cross-team integration.

---

## 3. ART coordination flow

```ks-diagram
key: swimlane
alt: Diagram
```

---

## 4. Portfolio Kanban flow

Epics flow through the portfolio Kanban system before reaching ARTs:

```ks-diagram
key: linear
alt: Diagram
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

```ks-diagram
key: linear
alt: Diagram
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
