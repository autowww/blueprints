# Engineering

**How we build software** — the technical disciplines that turn designs and requirements into working, maintainable, deployable systems.

Engineering disciplines share a foundation of computer science and software craft ([Software Engineering](software-engineering/README.md)), then specialize by system concern (architecture, delivery, quality) or platform (web, mobile, embedded).

| Discipline | Core question | Package |
|-----------|---------------|---------|
| [**Software Engineering**](software-engineering/README.md) | What CS fundamentals, paradigms, and craft practices underpin all engineering work? | Algorithms, data structures, design patterns, paradigms, clean code, concurrency, networking |
| [**Software Architecture**](software-architecture/README.md) | How are systems structured, and why? | Quality attributes, viewpoints, ADRs, patterns, approaches (C4, DDD, TOGAF) |
| [**DevOps**](devops/README.md) | How do we deliver and operate continuously and reliably? | CALMS, DORA, SRE, CI/CD, IaC, observability, incident management |
| [**Testing**](testing/README.md) | Is the software correct, reliable, and fit for purpose? | ISTQB vocabulary, test levels, design techniques, automation landscape |
| [**Frontend**](frontend/README.md) | How do we build fast, accessible, maintainable web UIs? | Component architecture, rendering strategies, performance, CSS, design system implementation |
| [**Mobile**](mobile/README.md) | How do we build performant, reliable mobile experiences? | Native/cross-platform, offline-first, push, app store lifecycle, device fragmentation |
| [**Embedded / IoT**](embedded-iot/README.md) | How do we build reliable, safe software for constrained environments? | Real-time systems, firmware, protocols, OTA, edge computing, safety-critical standards |

## Relationship to other families

| Family | How Engineering relates |
|--------|------------------------|
| [**Data**](../data/README.md) | Data disciplines (BigData, Data Science) depend on engineering infrastructure — pipelines, APIs, compute. DataOps applies DevOps principles to data. |
| [**Product**](../product/README.md) | Product disciplines define *what* to build and for *whom*; Engineering defines *how* to build it. UX Design deliverables (wireframes, tokens) are implemented by Frontend/Mobile. |
| [**Governance**](../governance/README.md) | PM governs delivery timelines and budgets that engineering executes within. Lean improvement targets engineering processes. |
| [**Security**](../security/README.md) | Security is embedded in every engineering discipline — secure coding, DevSecOps, security testing, platform-specific security (mobile pinning, IoT firmware signing). |
| [**Compliance**](../compliance/README.md) | Compliance requirements (GDPR data deletion, WCAG accessibility, PCI-DSS controls) are implemented by engineering teams. |

## Bridge documents

Each discipline has a bridge document (`*-SDLC-PDLC-BRIDGE.md`) mapping its practices to SDLC phases A–F and PDLC phases P1–P6. See [`BRIDGES.md`](../../../BRIDGES.md) for the concept and full index.
