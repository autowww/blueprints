---
slug: discipline-architecture
tier: 201
lens: discipline
nav_section: "Disciplines"
---

# Software architecture body of knowledge

This document maps the core concerns of **software architecture** — quality attributes, viewpoints, decision-making, governance, and technical debt — to the blueprint ecosystem. It describes **what** each concern covers, **when** it applies, and **where** its outputs land in the project structure.

**How architecture relates to PDLC and SDLC:** Architecture is a **cross-cutting discipline** that provides structural reasoning to both lifecycles. See [`ARCH-SDLC-PDLC-BRIDGE.md`](ARCH-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Patterns:** Architectural patterns (monolith, microservices, event-driven, etc.) are cataloged in [`patterns/`](patterns/README.md). The pattern catalog describes fitness criteria, trade-offs, and migration paths.

**Approaches:** Documentation and reasoning approaches (C4, arc42, 4+1, TOGAF, DDD) are in [`approaches/`](approaches/README.md).

---

## 1. Quality attributes

Quality attributes (also called non-functional requirements, cross-cutting concerns, or "-ilities") are the primary drivers of architectural decisions. Functional requirements can usually be satisfied by many architectures; quality attributes constrain the viable set.

### Core quality attributes

| Attribute | Definition | Architectural impact | Measurement |
|-----------|-----------|---------------------|-------------|
| **Performance** | Response time, throughput, resource utilization under expected load | Caching, async processing, database design, CDN, connection pooling | P95/P99 latency, requests/second, resource saturation |
| **Scalability** | Ability to handle increased load by adding resources | Horizontal vs vertical scaling, statelessness, partitioning, queue-based decoupling | Load test ceiling, cost-per-user at scale, scaling linearity |
| **Reliability** | Probability of failure-free operation over a given period | Redundancy, failover, circuit breakers, retry policies, graceful degradation | Uptime (SLA), MTBF, MTTR, error budget |
| **Availability** | Proportion of time the system is operational and accessible | Multi-region deployment, health checks, auto-scaling, data replication | Uptime %, recovery time objective (RTO) |
| **Security** | Protection against unauthorized access, data breaches, and attacks | Authentication/authorization architecture, encryption, network segmentation, input validation, audit logging | Vulnerability count, time-to-patch, penetration test results |
| **Maintainability** | Ease of modifying the system for fixes, improvements, or adaptation | Modularity, loose coupling, high cohesion, clear interfaces, documentation | Cyclomatic complexity, change failure rate, time-to-change |
| **Testability** | Ease of demonstrating faults through testing | Dependency injection, interface-based design, observable state, deterministic behavior | Test coverage, test execution time, defect detection rate |
| **Deployability** | Ease and frequency of releasing to production | Container-based deployment, feature flags, blue-green/canary strategies, infrastructure as code | Deployment frequency, lead time for changes (DORA) |
| **Observability** | Ability to understand internal system state from external outputs | Structured logging, distributed tracing, metrics, health endpoints | Time to detect, time to diagnose, signal-to-noise ratio |

### Trade-off analysis

Quality attributes frequently conflict — optimizing one may degrade another:

| Trade-off | Tension | Resolution strategy |
|-----------|---------|---------------------|
| Performance vs Security | Encryption adds latency; input validation adds processing | Benchmark impact; use hardware acceleration; accept measured overhead |
| Scalability vs Consistency | Distributed systems face CAP theorem constraints | Choose consistency model per use case (strong for financial, eventual for feeds) |
| Maintainability vs Performance | Abstractions add indirection; clean code may be slower | Profile first; optimize measured bottlenecks; preserve abstractions elsewhere |
| Availability vs Cost | Redundancy and multi-region add infrastructure cost | Define SLA tiers; invest proportionally to business impact of downtime |
| Security vs Usability | Strong auth adds friction; frequent re-auth frustrates users | Risk-based authentication; step-up auth for sensitive operations |

---

## 2. Architectural viewpoints

Different stakeholders need different views of the system. A complete architecture description addresses multiple viewpoints.

### IEEE 42010 / Kruchten 4+1

| Viewpoint | Audience | Shows | Typical diagrams |
|-----------|----------|-------|-----------------|
| **Logical** | Developers, architects | Key abstractions, domain model, module decomposition | Class diagrams, component diagrams, domain model |
| **Development** | Developers, build engineers | Code organization, build structure, dependency management | Package diagrams, layer diagrams, build dependency graphs |
| **Process** | Integrators, performance engineers | Runtime behavior, concurrency, communication | Sequence diagrams, activity diagrams, data flow |
| **Physical** | Operations, DevOps | Deployment topology, infrastructure, networking | Deployment diagrams, network topology, cloud architecture |
| **Scenarios** | All stakeholders | Key use cases that exercise the architecture | Use case diagrams, quality attribute scenarios |

### C4 model (recommended starting point)

The C4 model provides four levels of abstraction for software architecture diagrams:

| Level | Shows | Audience | When to create |
|-------|-------|----------|----------------|
| **Context** | System and its relationships to users and other systems | All stakeholders | Always — first diagram for any system |
| **Container** | High-level technology choices (applications, databases, message brokers) | Technical stakeholders | When the system has multiple deployable units |
| **Component** | Logical components within a container | Developers | When a container is complex enough to warrant decomposition |
| **Code** | Classes, interfaces within a component | Developers | Rarely — only for critical/complex components; code itself is often sufficient |

---

## 3. Architecture decision records (ADRs)

Architectural decisions should be documented as **Architecture Decision Records** — short documents that capture the context, decision, and consequences of significant choices.

### When to write an ADR

- Technology selection (database, framework, language, cloud provider)
- Architectural style change (monolith → microservices, sync → async)
- Cross-cutting concerns (authentication approach, logging strategy, error handling)
- Integration patterns (API design, event schemas, data contracts)
- Any decision that is **costly to reverse** or that **multiple team members need to understand**

### ADR structure (lightweight)

| Section | Content |
|---------|---------|
| **Title** | Short descriptive name (ADR-NNN: Use PostgreSQL for primary storage) |
| **Status** | Proposed / Accepted / Deprecated / Superseded by ADR-NNN |
| **Context** | Why is this decision needed? What forces are at play? |
| **Decision** | What was decided and why |
| **Consequences** | What are the trade-offs? What becomes easier or harder? |

ADRs live in `docs/adr/` in consuming repos. They are **immutable once accepted** — if a decision changes, create a new ADR that supersedes the old one.

---

## 4. Architecture governance

### Fitness functions

Fitness functions are automated or manual checks that verify the architecture remains fit for purpose over time:

| Category | Examples |
|----------|---------|
| **Structural** | No circular dependencies between modules; layer violation detection; dependency direction enforcement |
| **Performance** | Response time stays under threshold; resource utilization within bounds |
| **Security** | No known vulnerabilities in dependencies; encryption at rest/in-transit verified |
| **Operational** | Deployment time within target; rollback capability verified |

### Evolutionary architecture

Systems evolve. Architecture governance should support guided change, not prevent it:

- **Incremental change** — make small architectural changes that can be validated independently
- **Fitness functions** — automated checks that catch architectural drift
- **Last responsible moment** — defer decisions until you have enough information, but not longer
- **Reversibility** — prefer decisions that can be reversed over irreversible commitments

---

## 5. Technical debt

### Classification

| Type | Description | Example |
|------|-------------|---------|
| **Deliberate-prudent** | Conscious trade-off for speed, with a plan to repay | "Ship without caching; add it in sprint 3 when we have usage data" |
| **Deliberate-reckless** | Conscious shortcut without a repayment plan | "We don't have time for proper auth; we'll figure it out later" |
| **Inadvertent-prudent** | Better approach discovered after implementation | "Now that we understand the domain, the module boundaries should be different" |
| **Inadvertent-reckless** | Poor decisions from lack of knowledge | Junior team builds tightly coupled system without realizing the cost |

### Management

- **Identify** — track tech debt items alongside feature work in the backlog
- **Quantify** — estimate cost of carrying (slowed delivery, increased defect risk) vs cost of repaying
- **Prioritize** — address debt that blocks current goals or compounds fastest
- **Allocate** — reserve capacity (e.g. 15–20% of sprint) for debt reduction
- **Prevent** — architecture reviews, fitness functions, coding standards reduce new debt creation

---

## 6. Competencies

| Competency | Description |
|------------|-------------|
| **Systems thinking** | Understanding interactions between components, emergent properties, and unintended consequences |
| **Trade-off analysis** | Evaluating competing quality attributes and making justified decisions |
| **Communication** | Explaining architectural decisions to diverse stakeholders (executives, developers, operations) |
| **Domain knowledge** | Understanding the business domain well enough to align architecture with business needs |
| **Technology breadth** | Awareness of available technologies, patterns, and their fitness for different contexts |
| **Pragmatism** | Balancing ideal architecture with delivery constraints, team capabilities, and organizational context |

---

## 7. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| ISO/IEC/IEEE 42010 | https://www.iso.org/standard/74393.html | International standard for architecture description |
| C4 model | https://c4model.com/ | Recommended lightweight architecture documentation approach |
| arc42 | https://arc42.org/ | Comprehensive architecture documentation template |
| TOGAF | https://www.opengroup.org/togaf | Enterprise architecture framework |
| Building Evolutionary Architectures (Ford, Parsons, Kua) | https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/ | Fitness functions and guided architectural change |
| Domain-Driven Design (Eric Evans) | https://www.domainlanguage.com/ddd/ | Strategic and tactical design patterns for complex domains |
| Fundamentals of Software Architecture (Richards, Ford) | https://www.oreilly.com/library/view/fundamentals-of-software/9781492043447/ | Modern architecture styles, patterns, and soft skills |

---

*Keep project-specific architecture documentation in `docs/architecture/` and `docs/adr/`, not in this file.*
