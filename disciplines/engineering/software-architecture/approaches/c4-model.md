# C4 model for software architecture

The **C4 model** (Context, Containers, Components, Code) is a lean notation for describing software architecture at four levels of abstraction. It was created by Simon Brown to make diagrams **easy to produce, read, and maintain** without drowning stakeholders in UML detail. Each level “zooms in” from the system in its environment down to optional class-level detail.

| Level | Name | Primary question |
|-------|------|------------------|
| 1 | **System context** | Who uses the system, and what external systems does it talk to? |
| 2 | **Containers** | What are the major deployable/runtime pieces and how do they communicate? |
| 3 | **Components** | How is a single container structured internally (major building blocks)? |
| 4 | **Code** | Classes, interfaces, modules (often omitted; the codebase is the truth) |

---

## Level 1 — System context (online store example)

Shows people and software systems at the boundary of **your** system — not internal technology.

```mermaid
C4Context
title Level 1 — Online Store (system context)

Person(shopper, "Shopper", "Browses catalog and places orders")
Person(admin, "Admin", "Manages catalog and orders")

System(store, "Online Store", "Sells products, takes payments, fulfills orders")

System_Ext(payment, "Payment Gateway", "External PSP")
System_Ext(shipping, "Carrier API", "Shipping labels and tracking")
System_Ext(email, "Email Service", "Transactional email")

Rel(shopper, store, "Shops via browser/mobile")
Rel(admin, store, "Operates back office")
Rel(store, payment, "Charges cards", "HTTPS")
Rel(store, shipping, "Creates shipments", "HTTPS")
Rel(store, email, "Sends notifications", "HTTPS")
```

---

## Level 2 — Container diagram (same example)

Shows **applications, data stores, and queues** — the things that could be deployed or run as separate processes.

```mermaid
C4Container
title Level 2 — Online Store (containers)

Person(shopper, "Shopper", "Customer")
Person(admin, "Admin", "Operations")

System_Boundary(store, "Online Store") {
    Container(web, "Web Application", "SPA", "Delivers UI")
    Container(api, "Order & Catalog API", "Java/Spring or similar", "Business APIs")
    Container(worker, "Fulfillment Worker", "Background jobs", "Async processing")
    ContainerDb(db, "Operational DB", "PostgreSQL", "Orders, catalog, accounts")
    ContainerQueue(mq, "Message broker", "RabbitMQ/Kafka", "Domain events")
}

System_Ext(payment, "Payment Gateway", "External PSP")
System_Ext(shipping, "Carrier API", "Shipping")

Rel(shopper, web, "Uses", "HTTPS")
Rel(admin, web, "Uses", "HTTPS")
Rel(web, api, "JSON/HTTPS")
Rel(api, db, "SQL/TCP")
Rel(api, mq, "Publishes/consumes")
Rel(worker, mq, "Consumes")
Rel(worker, shipping, "HTTPS")
Rel(api, payment, "HTTPS")
```

---

## Level 3 — Component diagram (inside the API container)

Decomposes **one container** into major logical parts — not every class.

```mermaid
C4Component
title Level 3 — Order & Catalog API (components)

Container_Boundary(api, "Order & Catalog API") {
    Component(ctrl, "REST Controllers", "Spring MVC / JAX-RS", "HTTP adapters")
    Component(app, "Application services", "Use cases, orchestration", "Transactions, validation")
    Component(domain, "Domain services", "Pure domain rules", "Pricing, availability")
    Component(repo, "Repositories", "Persistence adapters", "JPA / JDBC")
    Component(pub, "Event publisher", "Outbox / broker client", "Publishes domain events")
}

ContainerDb(db, "Operational DB", "PostgreSQL")
ContainerQueue(mq, "Message broker", "Events")

Rel(ctrl, app, "Invokes")
Rel(app, domain, "Uses")
Rel(app, repo, "Uses")
Rel(app, pub, "Uses")
Rel(repo, db, "Reads/writes")
Rel(pub, mq, "Publishes")
```

---

## Level 4 — Code (optional zoom)

Use **sparingly** for hot spots (e.g. payment integration, pricing engine). Prefer the repository for full detail; this level shows **key types and dependencies** inside one component.

```mermaid
classDiagram
    class OrderController {
        +placeOrder(dto)
    }
    class PlaceOrderApplicationService {
        +execute(cmd)
    }
    class OrderRepository {
        +save(order)
    }
    class DomainEventPublisher {
        +publish(events)
    }
    OrderController --> PlaceOrderApplicationService
    PlaceOrderApplicationService --> OrderRepository
    PlaceOrderApplicationService --> DomainEventPublisher
```

---

## Notation (C4 shapes and meaning)

| Element | Typical shape / style | Color convention (common) | Description |
|---------|------------------------|---------------------------|-------------|
| **Person** | Stick figure / person icon | Often blue or neutral | Human user or role interacting with software |
| **Software system** | Box with system boundary | Own system vs external (different fill) | Delivers value; may be yours or external |
| **Container** | Box inside system boundary | Distinct per container type (e.g. web, API, DB) | Independently deployable or runnable unit |
| **Component** | Box inside a container | Subtle variation inside one palette | Logical grouping inside one container |

Exact colors vary by tool; consistency within a diagram set matters more than a universal palette.

---

## When to use each level — audience mapping

| Level | Typical audience | When it earns its keep |
|-------|------------------|-------------------------|
| **L1 Context** | C-suite, product, security, new engineers | Always first — sets scope and trust boundaries |
| **L2 Containers** | Tech leads, SRE, security reviews, integration partners | Multiple runtimes, data stores, or integration points |
| **L3 Components** | Dev team, reviewers of a complex service | Container has non-obvious internal structure or ownership splits |
| **L4 Code** | Implementers | Rarely as a separate diagram; link to ADR + repo for hot spots |

---

## Tooling comparison

| Tool | Strengths | Trade-offs |
|------|-----------|------------|
| **Structurizr** | Model-as-code, DSL, workspace views, aligns with C4 author’s practice | Learning curve for DSL; hosting choices |
| **PlantUML + C4-PlantUML** | Text-based diagrams, version control friendly | Requires PlantUML toolchain; layout tuning |
| **Mermaid (C4)** | Native in many Markdown viewers | Feature parity and layout vs Structurizr varies by version |
| **draw.io / diagrams.net** | C4 shape libraries, WYSIWYG | Drift from code unless disciplined export/process |

---

## C4 vs other approaches

| Dimension | **C4** | **UML** | **arc42** | **4+1 views** |
|-----------|--------|---------|-----------|---------------|
| **Primary goal** | Communicate structure at agreed zoom levels | General-purpose modeling | Full architecture description template | Stakeholder-specific viewpoints |
| **Formality** | Lightweight rules | Can be heavy | Structured sections + any notation | View catalog + scenarios |
| **Best for** | Most product teams’ diagram sets | Detailed OO design, standards-heavy orgs | Written doc + diagrams together | Explicit multi-audience separation |

C4 is **notation + abstraction levels**; arc42 and 4+1 are **document or viewpoint structures** — they can embed C4 diagrams.

---

## Integration with ADRs

- **Link diagrams to decisions:** In ADRs, reference diagram IDs or file paths (e.g. “See context diagram `store-context.png`”).
- **One decision, one zoom:** When an ADR changes a container or integration, update **L2**; if it refactors internal modules, update **L3**.
- **Avoid duplicating ADR text in diagrams:** Diagrams show structure; ADRs capture **context, options, decision, consequences**.
- **Versioning:** Store exported images or generated outputs next to ADRs when reviewers need frozen artifacts; prefer **diagrams-as-code** when possible.

---

## Anti-patterns

| Anti-pattern | Why it hurts | Remedy |
|--------------|--------------|--------|
| **Mixing abstraction levels** | L1 shows internal DB names; audience loses the big picture | One diagram, one level; use hyperlinks between levels |
| **Unlabeled relationships** | Arrows become Rorschach tests | Every `Rel` has a short verb + optional technology |
| **Diagram sprawl** | Dozens of L2 boxes with no boundaries | Split by subsystem or use context diagrams per bounded context |
| **L4 everywhere** | Duplicates IDE; goes stale instantly | Prefer code + tests; diagram only critical subsystems |

---

## External references

- [c4model.com](https://c4model.com/) — official C4 model site (notation, FAQ, tooling links).
- [Structurizr](https://structurizr.com/) — DSL, workspace, and documentation aligned with the model.
- Simon Brown’s talks and articles (search “Simon Brown C4 model”) — rationale and real-world usage.

*Keep project-specific architecture decisions in docs/adr/ and system documentation in docs/architecture/, not in this file.*
