# Project management (PM)

Reusable, **product-agnostic** blueprint for project management — the discipline of governing delivery: schedule, budget, resources, risk, and stakeholders. It answers **"are we delivering on time, on budget, within scope, with acceptable risk?"** while [`blueprints/sdlc/`](../../../sdlc/README.md) answers **"are we building the product right?"** and [`blueprints/pdlc/`](../../../pdlc/README.md) answers **"are we building the right product?"**

PM provides the **governance layer** between product strategy (PDLC) and software delivery (SDLC). In small Agile teams, PM concerns are often absorbed into existing roles (PO, Scrum Master). In enterprise contexts, PM is an explicit discipline with dedicated roles, processes, and reporting structures.

| Document | Purpose |
|----------|---------|
| [**PM.md**](PM.md) | What PM is, roles, process groups, governance model, metrics |
| [**PM-SDLC-PDLC-BRIDGE.md**](PM-SDLC-PDLC-BRIDGE.md) | How PM relates to SDLC and PDLC — three-domain comparison, nesting, role mapping, anti-patterns |
| [**approaches/**](approaches/README.md) | Deeper guides: PMI/PMBOK, PRINCE2, Six Sigma / Lean Six Sigma |

## Relationship to other packages

| Package | How PM relates |
|---------|---------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | SDLC phases A–F execute **inside** PM governance. PM provides schedule, budget, and risk management around SDLC delivery. See [**PM-SDLC-PDLC-BRIDGE.md**](PM-SDLC-PDLC-BRIDGE.md). |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC decides **what** to build; PM governs **how** the delivery is executed. Product strategy (P1–P3) feeds into project initiation; project outputs feed back into PDLC launch and growth (P4–P6). |
| [`blueprints/product/`](../../../product/README.md) | PM artifacts (project charter, status reports, risk register) complement product-functional docs. |
| [`blueprints/agents/`](../../../agents/README.md) | Automation recipes may support PM activities (status aggregation, risk dashboards, resource tracking). |

## Adopt in your repo

1. Copy or submodule `blueprints/disciplines/governance/pm/` alongside `blueprints/sdlc/` and `blueprints/pdlc/`.
2. Use [**PM.md**](PM.md) to orient your team on where project governance lives relative to product strategy and software delivery.
3. If you already use `blueprints/sdlc/` and `blueprints/pdlc/`, read [**PM-SDLC-PDLC-BRIDGE.md**](PM-SDLC-PDLC-BRIDGE.md) to understand how the three domains interact.
4. Choose an approach from [`approaches/`](approaches/README.md) that fits your organizational context — or use the generic PM model from [**PM.md**](PM.md) and tailor.

---

*Canonical source is this repository on `main`. See [`POLICY.md`](POLICY.md) for change rules.*
