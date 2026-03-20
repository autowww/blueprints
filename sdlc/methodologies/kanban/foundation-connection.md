# Kanban — connection to the SDLC foundation

Kanban optimizes **flow** through a **visualized value stream** with **explicit policies** and **WIP limits**. This blueprint still requires **traceability** (intent → spec → plan → PR → release) and **ceremony intents** as a vocabulary for *why* you meet.

## 1. SDLC phases A–F (how Kanban maps)

| Phase | Kanban expression |
|-------|-------------------|
| **A — Shape** | Upstream discovery; options on board or separate funnel; ordering policies |
| **B — Plan** | **Replenishment** selects what enters “committed” columns; no fixed sprint box unless you add it |
| **C — Build** | Pull through columns per **Definition of Workflow**; daily coordination |
| **D — Verify** | Explicit column/Done policy; test/QA swimlanes |
| **E — Release** | Release policy (on demand, batch, train) |
| **F — Operate & learn** | Service delivery review; retrospectives; feedback to upstream options |

**Prescriptive rule:** If you have **no** replenishment and **no** review cadence, you have a board, not a managed Kanban system.

## 2. Tracking spine

| Artifact | Kanban mapping |
|----------|----------------|
| **Intent / request** | Ticket/card at intake; may live off-board until triaged |
| **Spec** | Linked doc / acceptance on card |
| **Plan** | Column policies + optional commitment point |
| **Tasks** | Subtasks or child cards |
| **PRs** | Linked from card; DoW may require link before merge |
| **Reviews** | Policy per transition |
| **Release** | Release train or continuous; card state “released” |

## 3. Ceremony intents (C1–C6) ↔ Kanban meetings

| Intent | Typical Kanban ceremony |
|--------|-------------------------|
| **C1 — Align & decide** | Replenishment; prioritization cadence with stakeholders |
| **C2 — Plan the slice** | Refinement before pull; splitting options |
| **C3 — Execute & unblock** | Stand-up / workflow meeting |
| **C4 — Review & quality** | Review columns; QA ceremonies; release checklist |
| **C5 — Reflect & improve** | Team retrospective; systems thinking on flow |
| **C6 — Knowledge share** | Review meeting with stakeholders; doc walkthrough |

## 4. Role archetypes

| Kanban role (typical names) | Archetypes |
|----------------------------|------------|
| **Service request manager** / product manager | **Sponsor proxy**, **Orchestrator** |
| **Delivery team** | **Implementer**, **Quality advocate** |
| **Coach** (optional) | **Orchestrator**, **Quality advocate** |

## 5. Kanban-specific commitments (conceptual)

- **Visualization** of workflow.  
- **WIP limits** (or explicit WIP policies).  
- **Explicit policies** (Definition of Workflow, DoD per column).  
- **Manage flow** — focus on lead time and predictability, not utilization alone.

## 6. Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| Infinite columns, no WIP policy | Define minimal viable workflow + limits |
| “Everything urgent” bypass lane | Governance: only Steer can authorize class-of-service |
| Board only for dev; upstream invisible | Extend visualization or link to intake funnel |

## 7. Links

- [`../kanban.md`](../kanban.md) · [ceremonies/kanban.md](../ceremonies/kanban.md) · [SDLC.md](../../SDLC.md)
