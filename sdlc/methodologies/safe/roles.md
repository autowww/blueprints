---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# SAFe — roles

**Purpose:** Define SAFe role accountabilities at **team** and **program** levels, map them to blueprint [archetypes](../roles-archetypes.md), and clarify participation in SAFe events.

**Normative source:** [Scaled Agile Framework](https://scaledagileframework.com/) — role definitions are SAFe's; this file maps them to the blueprint.

---

## 1. Team-level roles

These are identical to single-team Agile roles; SAFe does not redefine them.

| Role | Accountability | Archetype emphasis |
|------|---------------|--------------------|
| **Product Owner** | Owns **Team Backlog**; defines, prioritizes, and accepts stories; collaborates with Product Management on feature decomposition. | Sponsor proxy + Orchestrator |
| **Scrum Master / Team Coach** | Facilitates team-level Agile practices; removes impediments; coaches on Scrum/Kanban/XP. | Orchestrator + Quality advocate |
| **Developers** | Cross-functional members who design, build, test, and deliver the iteration increment. | Implementer + Quality advocate |

## 2. Program-level roles (ART)

| Role | Accountability | Archetype emphasis |
|------|---------------|--------------------|
| **Release Train Engineer (RTE)** | Servant leader for the ART. Facilitates PI Planning, I&A, ART Sync. Manages risks, escalates impediments, drives relentless improvement. | Orchestrator (program-level) + Quality advocate (flow) |
| **Product Management** | Owns the **Program Backlog**. Defines features, accepts features at System Demo, communicates vision and roadmap to teams. Works with Business Owners on priorities. | Sponsor proxy + Orchestrator |
| **System Architect / Engineer** | Defines and evolves **architectural runway**. Participates in PI Planning to guide enabler work. Reviews cross-team technical decisions. | Implementer (architectural) + Quality advocate (NFRs) |
| **Business Owners** | Key stakeholders accountable for **business outcomes** of the ART. Participate in PI Planning (assign business value to PI Objectives) and I&A. | Sponsor |

## 3. Large Solution and Portfolio roles (when applicable)

| Role | Accountability |
|------|---------------|
| **Solution Train Engineer (STE)** | Facilitates Solution-level events; coordinates multiple ARTs. |
| **Solution Management** | Owns the **Solution Backlog**; defines capabilities across ARTs. |
| **Solution Architect** | System-of-systems architecture; cross-ART technical alignment. |
| **Epic Owners** | Shepherd epics through the portfolio Kanban; develop Lean business cases. |
| **Lean Portfolio Management (LPM)** | Strategic themes, Lean budgets, portfolio governance, value stream funding. |

## 4. Event participation matrix

| Event | RTE | Product Mgmt | System Arch | PO | SM | Developers | Business Owners |
|-------|-----|-------------|-------------|----|----|------------|-----------------|
| **PI Planning** | Facilitates | Presents vision, prioritizes features | Architecture briefing | Participates with team | Facilitates team breakout | Plan and commit | Assign business value |
| **Iteration Planning** | Optional | Optional | Optional | Facilitates | Facilitates | Plan and commit | — |
| **Daily Stand-up** | — | — | Optional | Participates | Facilitates | Drive | — |
| **Iteration Review** | Optional | Attends | Optional | Facilitates | Facilitates | Demo | Optional |
| **System Demo** | Facilitates | Accepts features | Reviews integration | Supports | — | Demo | Attends |
| **I&A** | Facilitates | Participates | Participates | Participates | Participates | Participates | Participates |
| **ART Sync** | Facilitates | Participates | Participates | SM or PO delegate | Participates | Delegate | — |
| **Iteration Retro** | Optional | — | — | Participates | Facilitates | Drive | — |

## 5. Role boundaries (prescriptive)

| Boundary | Guidance |
|----------|----------|
| **PO ≠ Product Management** | PO owns team-level stories; Product Management owns program-level features. PO does *not* independently define features. |
| **RTE ≠ project manager** | RTE facilitates and serves; does not assign work or dictate team plans. |
| **System Architect ≠ ivory tower** | Participates in team work, writes code, pairs — not just diagrams and reviews. |
| **Business Owners ≠ passive sponsors** | Active participants in PI Planning and I&A; not just quarterly status consumers. |
| **SM ≠ RTE** | SM serves one team; RTE serves the ART. SM escalates ART-level impediments to RTE. |

## 6. References

- [`../roles-archetypes.md`](../roles-archetypes.md) — methodology-neutral archetypes
- [`https://forgesdlc.com/methodology-safe.html`](https://forgesdlc.com/methodology-safe.html) — SAFe methodology summary
- [`foundation-connection.md`](foundation-connection.md) — SDLC phase and tracking mapping
