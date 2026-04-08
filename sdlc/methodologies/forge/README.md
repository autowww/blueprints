---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Forge — deep-dive package (blueprint)

**Purpose:** Prescriptive **operating detail** for teams running Forge alongside this blueprint: **roles**, **foundation fit** (tracking + ceremonies C1–C6 + archetypes), **ceremonies** with inputs/outputs/participants, **process maps**, **Versonas** (discipline-focused virtual personas; §5 structured output when teams use that shape), **daily operations**, **product planning**, and **project setup**.

**Executive summary + diagram:** [`https://forgesdlc.com/methodology-overview.html`](https://forgesdlc.com/methodology-overview.html)

| Chapter | File | Contents |
|---------|------|----------|
| **Foundation & fit** | [`foundation-connection.md`](foundation-connection.md) | SDLC A–F mapping, tracking spine, ceremony intents C1–C6, role archetypes |
| **Roles** | [`roles.md`](roles.md) | Owner/Implementer, hat-switching protocol, Versonas as virtual personas (not org roles), scaling tiers |
| **Ceremonies (prescriptive)** | [`ceremonies-prescriptive.md`](ceremonies-prescriptive.md) | Each ceremony: inputs, outputs, agenda, participants, timebox |
| **Meeting model** | [`meetings-model.md`](meetings-model.md) | Delivery modes (human-only / hybrid / Versona-assisted), meeting matrix, refinement vs planning, per-meeting fields, accountability, drift |
| **Artifacts & decisions** | [`ARTIFACT-AND-DECISION-MODEL.md`](ARTIFACT-AND-DECISION-MODEL.md) | Minimum artifact set, artifact matrix vs meetings/PDLC/SDLC, canonical names, Ember Log / ADR / directive boundaries, lightweight Markdown schemas |
| **Process & flows** | [`process-and-flows.md`](process-and-flows.md) | State model, work unit hierarchy, iteration lifecycle, KS diagram templates |
| **Naming reference** | [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) | Forge terms, meanings, meetings vs ceremonies vs Versona sessions, seven-phase benchmark vs P1–P6, source file paths |
| **Concept map** | [`CONCEPT-MAP.md`](CONCEPT-MAP.md) | Canonical concept matrix (lifecycles, owners, artifacts, meetings) and term-collision register |
| **Product → delivery IPE** | [`PRODUCT-DELIVERY-FORGE-IPE.md`](PRODUCT-DELIVERY-FORGE-IPE.md) | PDLC/SDLC phases: industry + Forge + Inputs–Process–Outputs + example Sparks |
| **Bridge** | [`FORGE-SDLC-PDLC-BRIDGE.md`](FORGE-SDLC-PDLC-BRIDGE.md) | How Forge connects to PDLC P1–P6 and SDLC A–F |
| **Versonas** | [`versona/README.md`](versona/README.md) | Discipline virtual personas: contract, templates, bridge-awareness — **layout:** generic at `versona/` root; other templates under `versona/catalog/` |
| **Discipline exploration spike** | [`versona/DISCIPLINE-SPIKE.md`](versona/DISCIPLINE-SPIKE.md) | Time-boxed learning spikes: anchors, open/close, roadmap/WBS handoffs (vs Forge Spark) |
| **Daily operations** | [`daily/README.md`](daily/README.md) | Charge, Ember Log, day journal: templates and scripts |
| **Product planning** | [`planning/README.md`](planning/README.md) | PoC/MVP/Phased planning, Product Spark hierarchy, Ore pipeline |
| **Product Manager agent** | [`product-manager/README.md`](product-manager/README.md) | Product strategy orchestrator, product bootstrap flow, first Charge template |
| **Setup & adoption** | [`setup/README.md`](setup/README.md) | Questionnaire, scaffold script, configuration template |
| **Scripts** | [`scripts/README.md`](scripts/README.md) | Shell scripts for Charge, Ember Log, journal, and status |

**Key references:**

- **Spark = Task:** Spark occupies the Task level in any existing WBS hierarchy. No parallel namespace — enrich, don't duplicate. See [process-and-flows.md § Spark = Task](process-and-flows.md#spark--task-wbs-mapping) and [foundation-connection.md § tracking spine](foundation-connection.md).
- **Lean tenets:** Forge must never add more ceremony than it removes waste. See [forge.md § Lean tenets](https://forgesdlc.com/methodology-overview.html#lean-tenets-keeping-forge-lightweight) and [foundation-connection.md § anti-patterns](foundation-connection.md#6-anti-patterns-prescriptive-dont).

**Related blueprint:** [Roles & archetypes](../roles-archetypes.md) · [Ceremony foundation](../ceremonies/ceremony-foundation.md) · [Methodology bridge](../ceremonies/methodology-bridge.md) · [Forge ceremonies fork](../ceremonies/forge.md) · [Agentic SDLC](../agentic-sdlc.md) · [Agentic coding standards](../agentic-coding-standards.md) · [Disciplines hub](../../../disciplines/README.md)
