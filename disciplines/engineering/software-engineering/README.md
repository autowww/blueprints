---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Software engineering

**How we practice the craft of software engineering.**

Reusable, **project-agnostic** blueprint for **software engineering** — the foundational discipline of turning specifications into reliable programs: paradigms, data structures and algorithms, design patterns, principles, clean code, concurrency, networking, version control, and diagnostic practice. Other engineering disciplines (architecture, DevOps, testing, frontend, mobile, embedded) **build on** this base.

Software engineering answers **"how do we practice the craft of building software?"** — a question that spans every SDLC phase (A–F) and supports PDLC execution from validation spikes through growth and maintenance.

| Document | Purpose |
|----------|---------|
| [**SOFTWARE-ENGINEERING.md**](SOFTWARE-ENGINEERING.md) | Body of knowledge: paradigms, DS&A, patterns, principles, clean code, concurrency, networking, VCS, debugging — competencies and references |
| [**SE-SDLC-PDLC-BRIDGE.md**](SE-SDLC-PDLC-BRIDGE.md) | How software engineering maps across SDLC phases A–F and PDLC phases P1–P6 — skills, artifacts, and calibration |
| [**paradigms/**](paradigms/README.md) | Deep guides: OOP, FP, reactive, procedural, multi-paradigm composition |
| [**patterns/**](patterns/README.md) | Deep guides: GoF creational/structural/behavioral, enterprise integration, concurrency patterns |

## Relationship to other packages

| Package | How software engineering relates |
|---------|-----------------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | SE competence is assumed across A–F: readable code, reviews, branching, debugging, and performance awareness. Methodology detail lives under `sdlc/methodologies/`; this package is the **discipline knowledge base**. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | P1–P2 prototypes and P3 trade-off discussions need implementable spikes; P4–P6 sustainment depends on maintainable code and operational literacy (logs, metrics, repro steps). |
| [`blueprints/BRIDGES.md`](../../../BRIDGES.md) | Index of discipline ↔ SDLC ↔ PDLC bridges; this package adds the SE bridge. |
| [`../software-architecture/`](../software-architecture/README.md) | Architecture sets boundaries and NFRs; SE provides implementation craft (modularity, APIs, performance habits) inside those boundaries. |
| [`../devops/`](../devops/README.md) | Delivery automation assumes version control fluency, build-aware code, and observable implementations — all SE concerns. |
| [`../testing/`](../testing/README.md) | Testability is shaped by design and coding habits (determinism, seams, dependency injection); tests exercise SE artifacts (units, modules, contracts). |
| [`../frontend/`](../frontend/README.md) | UI engineering layers state management, rendering models, and web platform APIs on top of general SE (async, performance, types). |
| [`../mobile/`](../mobile/README.md) | Mobile adds platform constraints (lifecycle, storage, networking); core SE still governs structure, concurrency, and quality. |
| [`../embedded-iot/`](../embedded-iot/README.md) | Embedded stresses resource limits, determinism, and safety-related coding; SE fundamentals apply with stricter profiles. |
| [`../../data/`](../../data/README.md) | Data pipelines and storage choices interact with algorithmic complexity, serialization, and correctness (idempotency, ordering). |
| [`../../product/`](../../product/README.md) | Product discovery turns into experiments and features that must be built and measured — SE skill determines cost of iteration. |
| [`../../governance/`](../../governance/README.md) | Policy and PM practices set priorities; engineering standards and review culture (SE) determine how policy becomes durable code. |
| [`../../security/`](../../security/README.md) | Secure design and coding (threat modeling inputs, safe APIs, crypto use) extends SE principles into the security discipline. |
| [`../../security/compliance/`](../../security/compliance/README.md) | Regulatory evidence often requires traceability, controlled change, and auditable engineering practice grounded in SE hygiene. |

## Scope

This package covers **software engineering as a foundational discipline**, including:

- **Programming paradigms** — object-oriented, functional, reactive, procedural; strengths and fit
- **Data structures and algorithms** — complexity, selection heuristics, pragmatic trade-offs
- **Design patterns** — GoF and enterprise integration patterns; intent and consequences
- **Engineering principles** — SOLID, DRY, KISS, YAGNI, separation of concerns, composition over inheritance
- **Clean code** — naming, functions, errors, formatting, review discipline
- **Concurrency and parallelism** — threads, async models, synchronization, failure modes
- **Networking fundamentals** — layered models, HTTP/TLS/DNS, API styles at a craft level
- **Version control** — branching models, merge/rebase, commit hygiene
- **Debugging and profiling** — systematic diagnosis, performance and memory analysis

Reference bodies of knowledge: **SWEBOK** (IEEE), **Clean Code** (Robert C. Martin), **Design Patterns** (Gamma et al. / GoF), **The Pragmatic Programmer** (Hunt & Thomas), **Structure and Interpretation of Computer Programs** (Abelson & Sussman).

---

*Keep project-specific engineering standards in `docs/development/` and architecture decisions in `docs/adr/`, not in this file.*
