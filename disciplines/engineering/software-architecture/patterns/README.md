# Architectural patterns (blueprint)

**Purpose:** Catalog of **architectural patterns** — recurring structural solutions to system design problems. Each pattern describes structure, quality trade-offs, fitness criteria, and migration paths.

**Why pattern thinking matters:** Naming a pattern gives the team a **shared vocabulary** for structure, not just technology. Patterns bundle deployment shape, coupling, and operational load; choosing without that lens often confuses “we use Kubernetes” (platform) with “we use microservices” (organizational and runtime commitment). Use this catalog to **compare** options against quality goals, then record the actual choice and exceptions in ADRs.

**Audience:** Teams adopting [`blueprints/disciplines/engineering/software-architecture/`](../README.md). Per-project pattern choices and exceptions belong in **`docs/adr/`**.

```ks-diagram
key: decision
alt: Diagram
```

Each pattern's quality-attribute trade-offs are analyzed in [SOFTWARE-ARCHITECTURE.md §1](../SOFTWARE-ARCHITECTURE.md#1-quality-attributes). Record your architecture choice and exceptions as [ADRs](../SOFTWARE-ARCHITECTURE.md#3-architecture-decision-records-adrs).

| Pattern | Core idea | When to use | Trade-offs |
|---------|-----------|-------------|------------|
| **Monolith** | Single deployable with all functionality | Small team, early product, low ops maturity | Simple deploy; can become tangled without discipline |
| **Modular monolith** | Enforced modules and explicit interfaces inside one deployable | Want monolith ops with future split option | Needs governance; boundaries can erode without reviews |
| **Microservices** | Independently deployable services over the network | Large org, scaling axes differ, autonomy per service | Ops complexity, distributed failure modes, consistency cost |
| **Event-driven** | Producers/consumers via events (pub/sub, logs) | Decouple teams, audit streams, burst handling | Debugging flow, ordering, idempotency, schema evolution |
| **Serverless** | FaaS + managed services, scale-to-zero | Spiky load, minimize undifferentiated ops | Cold start, vendor limits, distributed tracing harder |
| **CQRS** | Separate read and write models | Read scaling or models diverge strongly from writes | Complexity, eventual consistency, more moving parts |
| **Hexagonal** | Domain inside; ports/adapters for I/O | Many integrations, testability, swap infrastructure | More indirection; team must understand the style |
| **Layered** | Presentation → domain → data with dependency rules | CRUD-heavy, small team, stable domain | Can hide inappropriate coupling across layers |
| **Service mesh** | Sidecar/data plane for mTLS, traffic, observability | Many services, uniform cross-cutting policy | Operational overhead, skill set, latency budget |

**Decision guidance:** Prioritize quality attributes and team/ops maturity first. See [`SOFTWARE-ARCHITECTURE.md`](../SOFTWARE-ARCHITECTURE.md) (quality attributes, viewpoints, ADRs) for the trade-off framework.

**Migration paths:** Systems rarely land on a final architecture on day one. Common paths: monolith → modular monolith → microservices; monolith → strangler fig → services; layered → hexagonal.

**Related:** NFR trade-offs, viewpoints, and decision records are covered in [`SOFTWARE-ARCHITECTURE.md`](../SOFTWARE-ARCHITECTURE.md).

*Keep project-specific architecture decisions in docs/adr/ and system documentation in docs/architecture/, not in this file.*
