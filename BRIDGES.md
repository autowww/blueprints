# Bridges

A **bridge document** connects two or more distinct knowledge domains — lifecycles, disciplines, or abstraction layers — by mapping their phases, roles, artifacts, and terminology to each other. Bridges answer the question: *"I understand domain X — how does domain Y relate to it?"*

## Why bridges exist

The blueprints repository is organized into **lifecycles** (SDLC, PDLC) and **disciplines** grouped into families (Engineering, Data, Product, Governance) plus cross-cutting disciplines (Security, Compliance). Each package defines its own vocabulary, phases, and artifacts. Without bridges, practitioners default to a single-domain view and miss the connections:

- A Product Manager who only reads PDLC doesn't know which SDLC phase their artifacts feed into.
- An engineer who only reads SDLC doesn't know why certain requirements exist or how to validate outcomes.
- A discipline specialist who only reads their body of knowledge doesn't know when their techniques apply in either lifecycle.

Bridges prevent siloed understanding by making cross-domain relationships explicit.

## Where bridges live

Bridges live **next to the domain they originate from**, not in a central folder:

| Bridge type | Location pattern | Example |
|---|---|---|
| Cross-lifecycle | In the "outer" lifecycle package | `pdlc/PDLC-SDLC-BRIDGE.md` |
| Discipline-to-lifecycle | In the discipline package | `disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md` |
| Intra-lifecycle | In the relevant sub-package | `sdlc/methodologies/ceremonies/methodology-bridge.md` |

This keeps discovery natural (looking at a discipline? its bridge is right there), ownership clear (the package owns its bridge), and links short (relative paths within the package).

---

## Bridge index

### Cross-lifecycle bridges

| Bridge | File | Connects |
|---|---|---|
| **PDLC ↔ SDLC** | [`pdlc/PDLC-SDLC-BRIDGE.md`](pdlc/PDLC-SDLC-BRIDGE.md) | Product lifecycle (P1–P6) ↔ delivery lifecycle (A–F): phase alignment, role mapping, artifact handoffs, metrics comparison, decision framework |

### Discipline-to-lifecycle bridges

Each discipline has a bridge that maps its practices to SDLC phases A–F and PDLC phases P1–P6.

| Discipline | Bridge file | Core question |
|---|---|---|
| **Product Management** | [`disciplines/product/product-management/PRODMGMT-SDLC-PDLC-BRIDGE.md`](disciplines/product/product-management/PRODMGMT-SDLC-PDLC-BRIDGE.md) | Is our strategy coherent, our priorities defensible, and our market position sound? |
| **Business Analysis** | [`disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md`](disciplines/product/ba/BA-SDLC-PDLC-BRIDGE.md) | Do we understand the needs and will the solution satisfy them? |
| **Project Management** | [`disciplines/governance/pm/PM-SDLC-PDLC-BRIDGE.md`](disciplines/governance/pm/PM-SDLC-PDLC-BRIDGE.md) | Are we delivering on time, on budget, within scope? |
| **Testing** | [`disciplines/engineering/testing/TESTING-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/testing/TESTING-SDLC-PDLC-BRIDGE.md) | Is the software correct, reliable, and fit for purpose? |
| **Software Architecture** | [`disciplines/engineering/software-architecture/ARCH-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/software-architecture/ARCH-SDLC-PDLC-BRIDGE.md) | How should the system be structured to satisfy both quality and business needs? |
| **DevOps** | [`disciplines/engineering/devops/DEVOPS-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/devops/DEVOPS-SDLC-PDLC-BRIDGE.md) | Can we deliver and operate continuously and reliably? |
| **Big Data** | [`disciplines/data/bigdata/BIGDATA-SDLC-PDLC-BRIDGE.md`](disciplines/data/bigdata/BIGDATA-SDLC-PDLC-BRIDGE.md) | How do we collect, process, store, and govern data to serve both lifecycles? |
| **Data Science** | [`disciplines/data/data-science/DS-SDLC-PDLC-BRIDGE.md`](disciplines/data/data-science/DS-SDLC-PDLC-BRIDGE.md) | Can we learn from data to create value? |
| **Software Engineering** | [`disciplines/engineering/software-engineering/SE-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/software-engineering/SE-SDLC-PDLC-BRIDGE.md) | What CS fundamentals and craft practices underpin all engineering work? |
| **UX / UI Design** | [`disciplines/product/ux-design/UX-SDLC-PDLC-BRIDGE.md`](disciplines/product/ux-design/UX-SDLC-PDLC-BRIDGE.md) | Is the product usable, desirable, and accessible? |
| **Frontend** | [`disciplines/engineering/frontend/FE-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/frontend/FE-SDLC-PDLC-BRIDGE.md) | How do we build fast, accessible, maintainable web UIs? |
| **Mobile** | [`disciplines/engineering/mobile/MOB-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/mobile/MOB-SDLC-PDLC-BRIDGE.md) | How do we build performant, reliable mobile experiences? |
| **Embedded / IoT** | [`disciplines/engineering/embedded-iot/IOT-SDLC-PDLC-BRIDGE.md`](disciplines/engineering/embedded-iot/IOT-SDLC-PDLC-BRIDGE.md) | How do we build reliable, safe software for constrained environments? |
| **Security** | [`disciplines/security/SEC-SDLC-PDLC-BRIDGE.md`](disciplines/security/SEC-SDLC-PDLC-BRIDGE.md) | Is the product safe from unauthorized access, breaches, and attacks? |
| **Compliance** | [`disciplines/compliance/COMP-SDLC-PDLC-BRIDGE.md`](disciplines/compliance/COMP-SDLC-PDLC-BRIDGE.md) | Does the product meet regulatory and legal obligations? |
| **Marketing** | [`disciplines/product/marketing/MKT-SDLC-PDLC-BRIDGE.md`](disciplines/product/marketing/MKT-SDLC-PDLC-BRIDGE.md) | How do we acquire, engage, and retain users? |
| **Customer Success** | [`disciplines/product/customer-success/CS-SDLC-PDLC-BRIDGE.md`](disciplines/product/customer-success/CS-SDLC-PDLC-BRIDGE.md) | How do we help users achieve their goals and reduce churn? |

### Methodology-to-lifecycle bridges

| Bridge | File | Connects |
|---|---|---|
| **Forge ↔ SDLC ↔ PDLC** | [`sdlc/methodologies/forge/FORGE-SDLC-PDLC-BRIDGE.md`](sdlc/methodologies/forge/FORGE-SDLC-PDLC-BRIDGE.md) | Forge delivery methodology ↔ SDLC phases A–F ↔ PDLC phases P1–P6: Ore pipeline to PDLC discovery, Assay Gate to launch readiness, Versonas to discipline challenges |

### Intra-lifecycle bridges

| Bridge | File | Connects |
|---|---|---|
| **Methodology bridge** | [`sdlc/methodologies/ceremonies/methodology-bridge.md`](sdlc/methodologies/ceremonies/methodology-bridge.md) | Abstract ceremony intents (C1–C6) ↔ named ceremonies across 10 methodologies (Scrum, Kanban, Phased, XP, SAFe, Lean, Spiral, V-Model, DevOps, Forge) |

---

## Standard structure for discipline bridges

Discipline-to-lifecycle bridges follow a consistent structure. Not every section is mandatory — calibrate depth to the discipline's complexity — but the pattern ensures readers can navigate any bridge with the same mental model.

| # | Section | Purpose |
|---|---|---|
| 1 | **Purpose** | What understanding gap this bridge closes; which domains it connects |
| 2 | **Canonical sources** | Links to the authoritative docs for each bridged domain |
| 3 | **Comparison table** | Side-by-side dimensions: core question, scope, primary owner, timeline, success metric, risk focus, artifacts, failure mode |
| 4 | **"When one is missing"** | Consequences of practicing one domain without the other |
| 5 | **Phase alignment / lifecycle table** | Mapping discipline activities to PDLC P1–P6 and SDLC A–F |
| 6 | **Role mapping** | Who owns what across domains at each phase |
| 7 | **Artifact flow** | What crosses between domains and in which direction |
| 8 | **Calibration / decision framework** | When to invest more or less in this discipline |
| 9 | **Anti-patterns** | Common failures when the bridge is missing or misapplied |
| 10 | **Worked example** | End-to-end scenario showing the discipline across both lifecycles |
| 11 | **Related reading** | Links to sibling docs within the package and across packages |

The cross-lifecycle bridge (`PDLC-SDLC-BRIDGE.md`) and methodology bridge (`methodology-bridge.md`) follow variations of this structure appropriate to their scope.

## Naming convention

Discipline bridges use the pattern `{ABBREV}-SDLC-PDLC-BRIDGE.md`:

- The discipline abbreviation comes first (e.g. `BA`, `PM`, `ARCH`, `TESTING`)
- `SDLC` and `PDLC` follow in that order
- `BRIDGE` suffix, all uppercase, Markdown extension

The PDLC package's own cross-lifecycle bridge uses `PDLC-SDLC-BRIDGE.md` (the two lifecycles it connects). The methodology bridge uses `methodology-bridge.md` (lowercase, within the ceremonies sub-package).

---

## Related reading

| Doc | Why |
|-----|-----|
| [`disciplines/README.md`](disciplines/README.md) | Discipline hub — lists all disciplines and their relationship to lifecycles |
| [`sdlc/SDLC.md`](sdlc/SDLC.md) | Delivery phases A–F, DoD, ceremonies |
| [`pdlc/PDLC.md`](pdlc/PDLC.md) | Product phases P1–P6, stage gates, artifacts |
