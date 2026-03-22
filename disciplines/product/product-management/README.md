# Product management

Reusable, **project-agnostic** blueprint for **product management** — the discipline of identifying the right problems, defining product strategy, and guiding the product through its lifecycle to deliver measurable outcomes. Synthesizes practices from Marty Cagan's *Inspired / Empowered*, Teresa Torres' *Continuous Discovery Habits*, Melissa Perri's *Escaping the Build Trap*, and the Silicon Valley Product Group (SVPG) body of knowledge.

Product management answers **"are we building the right product for the right market, and is our strategy coherent?"** — a question rooted in PDLC (P1–P6) and operationalized through SDLC delivery.

| Document | Purpose |
|----------|---------|
| [**PRODUCT-MANAGEMENT.md**](PRODUCT-MANAGEMENT.md) | Body of knowledge: vision, strategy, roadmap, prioritization, market analysis, competitive intelligence, business model, product-market fit, discovery cadence, stakeholder communication |
| [**PRODMGMT-SDLC-PDLC-BRIDGE.md**](PRODMGMT-SDLC-PDLC-BRIDGE.md) | How product management maps across PDLC P1–P6 and SDLC A–F — role mapping, artifact flow, calibration, anti-patterns |

## Relationship to other packages

| Package | How Product Management relates |
|---------|-------------------------------|
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC defines the lifecycle stages (P1–P6); product management is the **discipline that drives decisions** at each stage — what to discover, what to validate, when to commit, how to grow, when to sunset. |
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Product management feeds SDLC with **prioritized, validated work** (Phase A inputs). During delivery, the PM ensures build decisions stay aligned with product strategy and outcome goals. |
| [`blueprints/disciplines/product/ba/`](../ba/README.md) | PM defines the **problem space, market opportunity, and strategic direction**; BA defines the **detailed requirements, elicitation, and solution validation**. PM says "what and why"; BA says "what exactly and how to prove it." In small teams, one person often fills both roles. |
| [`blueprints/disciplines/governance/pm/`](../../governance/pm/README.md) | Product Management defines **priorities and outcomes**; Project Management (Governance) governs **delivery constraints** — schedule, budget, scope, risk. Product decides what to build; Project ensures it ships on time. |
| [`blueprints/disciplines/product/ux-design/`](../ux-design/README.md) | PM partners with UX on discovery and validation (P1–P2); UX owns experience design while PM owns value proposition and market positioning. Together they form the core of the "product trio." |
| [`blueprints/disciplines/product/marketing/`](../marketing/README.md) | PM defines positioning and ICP; Marketing operationalizes GTM, channels, and growth. PM owns "why this product wins"; Marketing owns "how the market knows." |
| [`blueprints/disciplines/product/customer-success/`](../customer-success/README.md) | PM uses CS signals (churn, health scores, support themes) as P5 inputs; CS uses PM's roadmap and vision to set customer expectations. |

## Scope

This package covers **product management as a strategic discipline** — not project delivery, not requirements engineering, not UX craft. It includes:

- **Vision and strategy** — defining the problem space, identifying opportunities, articulating strategic positioning
- **Roadmap management** — outcome-driven roadmaps, planning horizons, stakeholder alignment
- **Prioritization** — frameworks for deciding what to build next (RICE, ICE, weighted scoring, opportunity cost)
- **Market analysis** — TAM/SAM/SOM, segmentation, market dynamics, regulatory landscape
- **Competitive intelligence** — positioning maps, feature parity, differentiation, moats
- **Business model and pricing** — value capture, pricing strategies, unit economics
- **Product-market fit** — signal detection, retention analysis, Sean Ellis test, cohort behavior
- **OKRs and success metrics** — North Star metric, leading/lagging indicators, product health
- **Discovery cadence** — continuous discovery, dual-track integration, experiment-driven decisions
- **Stakeholder communication** — executive updates, customer advisory, cross-functional alignment

The package is **descriptive, not prescriptive**: apply the practices that fit your team size, product stage, and market context.
