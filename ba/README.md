# Business analysis (BA)

Reusable, **project-agnostic** blueprint for **business analysis** — the discipline of understanding organizational needs, defining solutions, and managing requirements across their lifecycle. Grounded in the [BABOK Guide v3](https://www.iiba.org/babok-guide/) (IIBA), adapted for teams already using [`blueprints/sdlc/`](../sdlc/README.md) and [`blueprints/pdlc/`](../pdlc/README.md).

BA answers **"what do stakeholders need, and does the solution satisfy those needs?"** — a question that spans both PDLC (right product) and SDLC (product right).

| Document | Purpose |
|----------|---------|
| [**BABOK.md**](BABOK.md) | Six knowledge areas, underlying competencies, BABOK v3 alignment |
| [**BA-PDLC-SDLC-BRIDGE.md**](BA-PDLC-SDLC-BRIDGE.md) | How BA maps across PDLC P1–P6 and SDLC A–F — role mapping, technique selection, anti-patterns |
| [**knowledge-areas/**](knowledge-areas/README.md) | Deep guides per knowledge area |
| [**techniques/**](techniques/README.md) | Master catalog of BA techniques mapped to knowledge areas and lifecycle phases |
| [**perspectives/**](perspectives/README.md) | How BA adapts to context: agile, BI, business architecture, BPM |
| [**templates/**](templates/README.md) | Copy-paste starters: stakeholder register, business case, requirements package, decision analysis |

## Relationship to other packages

| Package | How BA relates |
|---------|---------------|
| [`blueprints/sdlc/`](../sdlc/README.md) | BA techniques feed SDLC phases A–B (discover, specify). Requirements traceability, acceptance criteria, and specification practices in SDLC are **outputs** of BA work. The BA role in [phased delivery](../sdlc/methodologies/phased/roles.md) is one methodology-specific expression of this package. |
| [`blueprints/pdlc/`](../pdlc/README.md) | BA Strategy Analysis maps to PDLC P1–P3; Solution Evaluation maps to P5–P6. BA provides the **techniques** (interviews, workshops, modeling) that PDLC phases rely on for evidence generation. See [**BA-PDLC-SDLC-BRIDGE.md**](BA-PDLC-SDLC-BRIDGE.md). |
| [`blueprints/product/`](../product/README.md) | Product-functional docs (`docs/product/`) hold the living artifacts that BA activities produce — personas, capabilities, journeys, glossaries. BA templates in this package complement the doc IA templates. |
| [`blueprints/agents/`](../agents/README.md) | Automation recipes may support BA activities (e.g. requirements validation scripts, traceability matrix generation). |

## Scope

This package covers **business analysis as a discipline** — not just requirements engineering. It includes:

- **Strategy Analysis** — understanding the enterprise context, defining change strategy
- **Elicitation & Collaboration** — gathering and confirming information from stakeholders
- **Requirements Life Cycle Management** — tracing, maintaining, prioritizing, approving requirements
- **Requirements Analysis & Design Definition** — modeling, specifying, verifying, validating
- **Solution Evaluation** — assessing solution performance against business needs
- **BA Planning & Monitoring** — planning the BA approach itself

The package is **descriptive, not prescriptive**: use the knowledge areas and techniques that fit your team's context. See [`perspectives/`](perspectives/README.md) for context-specific guidance.
