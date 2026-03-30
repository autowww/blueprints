# Product development lifecycle (PDLC)

Reusable, **product-agnostic** blueprint for the full **product** lifecycle — from problem discovery through growth and sunset. It answers **"are we building the right product?"** while [`blueprints/sdlc/`](../sdlc/README.md) answers **"are we building the product right?"**

SDLC phases A–F sit **inside** the PDLC as the Build & Release engine; PDLC wraps around them with upstream validation and downstream outcome measurement.

| Document | Purpose |
|----------|---------|
| [**PDLC.md**](PDLC.md) | Phases P1–P6, artifacts, exit criteria, roles — includes [benchmark map](PDLC.md#benchmark-map-seven-phase-reference) vs a common seven-phase *reference* pattern |
| [**PDLC-SDLC-BRIDGE.md**](PDLC-SDLC-BRIDGE.md) | How PDLC and SDLC relate — diagrams, role mapping, artifact handoffs, worked example |
| [**approaches/**](approaches/README.md) | Deeper guides: Dual-Track Agile, Stage-Gate, Design Thinking, Lean Startup, PLM, Opportunity Solution Trees |
| [**templates/**](templates/README.md) | Copy-paste starters: vision, experiment log, stage-gate review, metrics, GTM, sunset plan |

## Relationship to other packages

| Package | How PDLC relates |
|---------|-----------------|
| [`blueprints/sdlc/`](../sdlc/README.md) | SDLC phases A–F are the delivery engine **inside** PDLC phases P3→P4. See [**PDLC-SDLC-BRIDGE.md**](PDLC-SDLC-BRIDGE.md). |
| [`blueprints/product/`](../product/README.md) | Product-functional docs (`docs/product/`) hold the living artifacts that PDLC phases produce — vision, personas, journeys, capabilities. |
| [`blueprints/disciplines/governance/pm/`](../disciplines/governance/pm/README.md) | PM provides the **governance layer** between PDLC strategy and SDLC delivery — schedule, budget, risk, stakeholder management. PDLC decides **what** to build; PM governs **how** the execution is managed. See [**PM-SDLC-PDLC-BRIDGE.md**](../disciplines/governance/pm/PM-SDLC-PDLC-BRIDGE.md). |
| [`blueprints/disciplines/product/ba/`](../disciplines/product/ba/README.md) | BA provides the **analytical techniques** that PDLC phases rely on — Strategy Analysis maps to P1–P3, Elicitation feeds P1–P2 discovery, Solution Evaluation maps to P5–P6. See [**BA-SDLC-PDLC-BRIDGE.md**](../disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md). |
| [`blueprints/agents/`](../agents/README.md) | Automation recipes may support PDLC activities (e.g. analytics collection, A/B test infrastructure). |

## Adopt in your repo

1. Copy or submodule `blueprints/pdlc/` alongside `blueprints/sdlc/`.
2. Copy templates from `templates/` into your project's `docs/product/` or equivalent.
3. Use [**PDLC.md**](PDLC.md) to orient your team on where product work lives relative to delivery work.
4. If you already use `blueprints/sdlc/`, read [**PDLC-SDLC-BRIDGE.md**](PDLC-SDLC-BRIDGE.md) to understand handoff points.

---

*Canonical source is this repository on `main`. See [`POLICY.md`](POLICY.md) for change rules.*
