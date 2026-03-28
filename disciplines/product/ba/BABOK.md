---
slug: discipline-business-analysis
tier: 201
lens: discipline
nav_section: "Disciplines"
---

# Business Analysis Body of Knowledge (BABOK)

This document maps the six **knowledge areas** defined by the [BABOK Guide v3](https://www.iiba.org/babok-guide/) (IIBA — International Institute of Business Analysis) to the blueprint ecosystem. It describes **what** each knowledge area covers, **when** it applies, and **where** its outputs land in the project structure.

**How BA relates to PDLC and SDLC:** BA is a **cross-cutting discipline** that provides techniques and rigor to both lifecycles. See [`BA-SDLC-PDLC-BRIDGE.md`](BA-SDLC-PDLC-BRIDGE.md) for the full mapping, role comparison, and worked example.

**Techniques:** Each knowledge area uses a subset of the 50+ techniques cataloged in [`techniques/README.md`](techniques/README.md). The knowledge area guides in [`knowledge-areas/`](knowledge-areas/README.md) list applicable techniques per activity.

**Perspectives:** BA adapts to context — agile teams, BI initiatives, enterprise architecture, process improvement. See [`perspectives/`](perspectives/README.md).

---

## 1. Knowledge areas overview

```blueprint-diagram
key: swimlane
alt: Diagram
```

### Summary table

| # | Knowledge Area | Core Question | Key Outputs | Deeper Guide |
|---|----------------|---------------|-------------|--------------|
| 1 | **BA Planning & Monitoring** | How should we approach BA work on this initiative? | BA plan, stakeholder engagement approach, performance metrics | [`knowledge-areas/ba-planning-monitoring.md`](knowledge-areas/ba-planning-monitoring.md) |
| 2 | **Strategy Analysis** | Why is this change needed and what does the future state look like? | Current state assessment, future state definition, change strategy, solution scope | [`knowledge-areas/strategy-analysis.md`](knowledge-areas/strategy-analysis.md) |
| 3 | **Elicitation & Collaboration** | What do stakeholders know, need, and expect? | Elicitation results (confirmed), stakeholder engagement | [`knowledge-areas/elicitation-collaboration.md`](knowledge-areas/elicitation-collaboration.md) |
| 4 | **Requirements Life Cycle Management** | Are requirements traced, approved, and maintained? | Traced requirements, approved requirements, requirements architecture | [`knowledge-areas/requirements-lifecycle.md`](knowledge-areas/requirements-lifecycle.md) |
| 5 | **Requirements Analysis & Design Definition** | What does the solution need to do and look like? | Requirement specifications (functional, non-functional), design definitions, verified requirements | [`knowledge-areas/requirements-analysis-design.md`](knowledge-areas/requirements-analysis-design.md) |
| 6 | **Solution Evaluation** | Does the solution deliver the expected value? | Solution performance assessment, limitation identification, replacement/retirement recommendation | [`knowledge-areas/solution-evaluation.md`](knowledge-areas/solution-evaluation.md) |

---

## 2. Knowledge area → lifecycle mapping

Each knowledge area has a **primary** lifecycle alignment and **secondary** touchpoints:

| Knowledge Area | PDLC Phases | SDLC Phases | Primary Alignment |
|----------------|-------------|-------------|-------------------|
| **BA Planning & Monitoring** | Across P1–P6 | Across A–F | Governance layer — scoped per initiative |
| **Strategy Analysis** | P1–P3 (Discover, Validate, Strategize) | — | PDLC — defines why change is needed |
| **Elicitation & Collaboration** | P1–P2 (research, interviews) | A–B (requirements gathering) | Both — techniques serve discovery and specification |
| **Requirements Life Cycle Management** | P3 (scope definition) | A–B (specs, traceability) | Both — bridges validated intent to delivery specs |
| **Requirements Analysis & Design Definition** | P2 (solution validation) | B–C (specify, design) | SDLC-heavy — models and specifies the solution |
| **Solution Evaluation** | P5–P6 (grow, sunset) | E (verify) | PDLC-heavy — measures value delivered |

---

## 3. Requirement classification

BABOK distinguishes requirement types. This classification maps to existing project artifacts:

| Requirement Type | BABOK Definition | Where It Lives in This Repo |
|------------------|------------------|-----------------------------|
| **Business requirements** | High-level needs of the organization | `docs/product/vision/`, PDLC P1–P3 artifacts |
| **Stakeholder requirements** | Needs of specific stakeholder groups | `docs/product/personas/`, `docs/product/journeys/` |
| **Solution requirements (functional)** | Capabilities the solution must provide | `docs/product/features/`, `docs/requirements/` (story specs) |
| **Solution requirements (non-functional)** | Quality attributes, constraints | `docs/requirements/` (NFR specs), `docs/architecture/` |
| **Transition requirements** | Temporary capabilities for migration | Release/migration docs, PDLC P4 launch artifacts |

---

## 4. Underlying competencies

BABOK defines six competency areas for business analysts. These complement the role definitions in [`blueprints/sdlc/methodologies/roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md):

| Competency | What It Means | Related Blueprint Concept |
|------------|---------------|---------------------------|
| **Analytical thinking & problem solving** | Decomposition, systems thinking, decision-making | Spec-driven development ([`spec-driven-development.md`](../../../sdlc/methodologies/spec-driven-development.md)) |
| **Behavioral characteristics** | Ethics, trustworthiness, adaptability, organization | Role expectations in [`SDLC.md`](../../../sdlc/SDLC.md) §1 and [`PDLC.md`](../../../pdlc/PDLC.md) §1 |
| **Business knowledge** | Domain expertise, industry awareness, organizational understanding | Domain context in `docs/product/glossary.md` and `docs/product/data/` |
| **Communication skills** | Written and verbal clarity, active listening, presentation | Ceremony facilitation — [Ceremonies hub](https://blueprints.forgesdlc.com/sdlc--methodologies-ceremonies.html) |
| **Interaction skills** | Facilitation, negotiation, conflict resolution, leadership | Stakeholder management, product trio collaboration |
| **Tools & technology** | Modeling tools, requirements management tools, prototyping | Tool landscape in [`sdlc/AI-TOOLS-AND-MODELS-LANDSCAPE.md`](../../../sdlc/AI-TOOLS-AND-MODELS-LANDSCAPE.md) |

---

## 5. BABOK perspectives (summary)

Perspectives describe how BA practices adapt to specific contexts. Full guides are in [`perspectives/`](perspectives/README.md).

| Perspective | Focus | When to Apply |
|-------------|-------|---------------|
| **Agile** | Iterative discovery, just-in-time requirements, collaboration over documentation | Teams using Scrum, Kanban, XP, or Dual-Track Agile |
| **Business Intelligence** | Data requirements, analytics, reporting, data quality | BI/analytics initiatives, data-driven product decisions |
| **Business Architecture** | Enterprise-level capability mapping, value streams, organizational alignment | Enterprise transformations, cross-product initiatives |
| **Business Process Management** | Process modeling, optimization, automation | Process improvement, workflow automation, operational efficiency |

BABOK v3 also defines an **Information Technology** perspective — in this blueprint, IT concerns are already covered by [`blueprints/sdlc/`](../../../sdlc/README.md) and are not duplicated here.

---

## 6. External references

| Topic | URL | Why It Is Linked |
|-------|-----|------------------|
| IIBA — BABOK Guide v3 | https://www.iiba.org/babok-guide/ | **Canonical source** — the standard this package aligns to |
| IIBA — Business Analysis Competency Model | https://www.iiba.org/business-analysis-competency-model/ | Competency framework underlying §4 |
| IIBA — Agile Extension to the BABOK Guide | https://www.iiba.org/agile-extension/ | Detailed guidance for agile BA — source for [`perspectives/agile-perspective.md`](perspectives/agile-perspective.md) |
| Karl Wiegers — Software Requirements | https://www.processimpact.com/software-requirements/ | **Practical requirements engineering** — techniques, templates, and process; complements BABOK with an engineering lens |
| Alistair Cockburn — Writing Effective Use Cases | https://alistair.cockburn.us/use-cases/ | **Use case technique** depth — the authoritative reference for structured use case writing |
| Dean Leffingwell — Agile Software Requirements | https://scaledagileframework.com/agile-software-requirements/ | **Scaled agile requirements** — how BA works in SAFe/large-scale agile; bridges to [`methodologies/safe.md`](../../../sdlc/methodologies/safe.md) |
| BPMN.org | https://www.bpmn.org/ | **Process modeling standard** — notation used in business process management perspective |

---

*Keep project-specific BA artifacts in `docs/product/` and `docs/requirements/`, not in this file.*
