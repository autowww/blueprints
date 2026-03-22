# Software architecture

Reusable, **project-agnostic** blueprint for **software architecture** — the discipline of making and documenting the fundamental structural decisions about a software system. It addresses quality attributes, architectural styles, component boundaries, and the trade-offs that shape a system's long-term viability.

Software architecture answers **"how is the system structured, and why?"** — a question that bridges PDLC feasibility (P2–P3) with SDLC design and governance (phases A–E).

| Document | Purpose |
|----------|---------|
| [**SOFTWARE-ARCHITECTURE.md**](SOFTWARE-ARCHITECTURE.md) | Quality attributes, architectural viewpoints, documentation approaches, decision-making frameworks, competencies |
| [**ARCH-SDLC-PDLC-BRIDGE.md**](ARCH-SDLC-PDLC-BRIDGE.md) | How architecture maps across SDLC phases A–F and PDLC phases P1–P6 — design authority, governance, tech debt lifecycle |
| [**approaches/**](approaches/README.md) | Architectural documentation and reasoning approaches: C4 model, arc42, 4+1 views, TOGAF ADM, domain-driven design |
| [**patterns/**](patterns/README.md) | Architectural patterns catalog: monolith, microservices, event-driven, serverless, CQRS, hexagonal |

## Relationship to other packages

| Package | How Software Architecture relates |
|---------|-----------------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Architecture decisions shape SDLC phases A–C (Discover, Specify, Design). ADRs, component diagrams, and non-functional requirements are architecture outputs that feed delivery. The SDLC Definition of Done may include architecture review gates. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P2 (Validate) includes feasibility assessment — architecture provides the technical feasibility lens. P3 (Strategize) defines NFRs and constraints that architecture must satisfy. P5 (Grow) generates tech debt and scalability demands that architecture must address. |
| [`blueprints/disciplines/product/ba/`](../../product/ba/README.md) | BA non-functional requirements (performance, security, scalability) are primary inputs to architectural decisions. Requirements architecture (how requirements are structured) complements system architecture. |
| [`blueprints/disciplines/governance/pm/`](../../governance/pm/README.md) | PM risk management includes architectural risk. Architecture decisions affect schedule, cost, and resource requirements. |
| [`blueprints/disciplines/engineering/testing/`](../testing/README.md) | Architecture determines testability. Test strategies (integration points, contract testing, performance testing) depend on architectural boundaries. |
| [`blueprints/disciplines/engineering/devops/`](../devops/README.md) | Architecture enables or constrains deployment strategies. Microservices, containers, and infrastructure-as-code are architecture-DevOps intersections. |

## Scope

This package covers **software architecture as a discipline** — not just system diagrams. It includes:

- **Quality attributes** — performance, scalability, security, reliability, maintainability, and their trade-offs
- **Architectural viewpoints** — logical, development, process, physical, and scenario views
- **Documentation approaches** — C4 model, arc42, 4+1, lightweight ADRs
- **Decision frameworks** — how to evaluate architectural trade-offs, when to decide, when to defer
- **Architectural patterns** — structural patterns and their fitness for different contexts
- **Architecture governance** — review processes, fitness functions, evolutionary architecture
- **Technical debt** — identification, measurement, and management strategies

Reference bodies of knowledge: ISO/IEC 42010 (architecture description), SEI architecture practices, TOGAF, DDD (Eric Evans).

---

*Keep project-specific architecture documentation in `docs/architecture/` and `docs/adr/`, not in this file.*
