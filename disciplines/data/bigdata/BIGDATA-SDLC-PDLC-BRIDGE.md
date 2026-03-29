# Big Data ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **data engineering** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Data Engineering** — "How do we **collect, process, store, and govern data** to serve both?"

Data engineering provides the infrastructure that product analytics (PDLC P5) and software features (SDLC) depend on.

**Canonical sources:** [`BIGDATA.md`](BIGDATA.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how data engineering relates to PDLC and SDLC |
| [Comparison table](#comparison-table) | Data engineering vs SDLC vs PDLC across core dimensions |
| [When one is missing](#when-one-is-missing) | Consequences when any of the three lenses is absent |
| [Data engineering across the lifecycle](#data-engineering-across-the-lifecycle) | Phase-by-phase activities and outputs (P1–P6, A–F) |
| [Role mapping](#role-mapping) | Who owns data engineering decisions; alignment with SDLC archetypes and PDLC roles |
| [Artifact flow](#artifact-flow) | Handoffs between data engineering, delivery, and product |
| [Calibration](#calibration) | When to deepen or lighten data engineering investment |
| [Anti-patterns](#anti-patterns) | Common failures when the bridge is weak or ignored |
| [Worked example](#worked-example) | End-to-end scenario: recommendation analytics and serving path |
| [Related reading](#related-reading) | Authoritative docs in this package and lifecycle packages |

---

## Comparison table

| Dimension | Data engineering | SDLC | PDLC |
|-----------|------------------|------|------|
| **Core question** | How do we collect, process, store, and govern data so consumers can trust it and ship on it? | Are we building the product **right**? | Are we building the **right** product? |
| **Scope** | Ingestion through governed consumption: pipelines, storage tiers, metadata, quality, access, cost | Discovery through release: specify, design, build, verify, deploy | Problem discovery through sunset: validate, plan & commit, launch, grow, retire |
| **Primary owner** | Data engineering lead, data platform team, or domain data owner (e.g. data mesh) | Engineering / delivery team | Product manager / product trio |
| **Timeline** | Platform and pipeline roadmaps; cadence often tied to product increments and compliance cycles | Sprint, iteration, or release train | Quarters to years on the product horizon |
| **Success metric** | Quality (accuracy, completeness, consistency, timeliness, validity, uniqueness), pipeline SLAs, freshness, lineage coverage, cost per useful dataset | Velocity, defect rate, DORA-style delivery metrics, release health | Adoption, retention, revenue, experiment outcomes, strategic fit |
| **Key artifacts** | Schemas, data contracts, pipeline definitions, catalogs, quality rules, DataOps runbooks, IaC for data infrastructure | Specifications, code, tests, release artifacts | Research synthesis, metrics definitions, experiment readouts, roadmap |
| **Risk focus** | Silent corruption, schema drift, privacy and residency breaches, vendor lock-in, runaway compute/storage cost | Defects, security flaws, operational incidents | Wrong problem, weak fit, timing, viability |
| **Failure mode** | Data swamp; analytics nobody trusts; pipelines that block every release | Rework; production firefighting; mounting tech debt | Shipping features that do not move outcomes |

---

## When one is missing

| Scenario | What happens |
|----------|--------------|
| **Data engineering without PDLC** | Platforms and pipelines optimize for technical completeness while product bets lack clear outcomes; investment in lakehouse, mesh, or medallion layers does not trace to validated customer or business value. |
| **Data engineering without SDLC** | Data changes bypass versioned delivery: schema drift in production, migrations without rollback discipline, and no shared Definition of Done for data path changes alongside application releases. |
| **SDLC without data engineering** | Features ship without durable event capture, conformed dimensions, or governed interfaces; each team builds one-off ETL; quality and lineage are unknown until incidents or wrong decisions surface. |
| **PDLC without data engineering** | Discovery and growth rely on ad-hoc extracts and spreadsheet analytics; experiments lack trustworthy assignment, metrics, or timeliness; strategy debates proceed without a reliable data substrate. |
| **PDLC and SDLC without shared data engineering standards** | Product and delivery each define “truth” differently; dashboards disagree with the app; reconciliation waste replaces confident decisions. |
| **All three practiced** | Instrumented product learning, governed data products (DMBOK-style accountability), and coordinated pipeline/schema releases that support both validation and reliable shipping. |

### Lifecycle labels used in this bridge

| Framework | Phase | Full name (for traceability to [`SDLC.md`](../../../sdlc/SDLC.md) and [`PDLC.md`](../../../pdlc/PDLC.md)) |
|-----------|-------|-----------------------------------------------------------------------------------------------------|
| **PDLC** | P1 | Discover Problem |
| **PDLC** | P2 | Validate Solution |
| **PDLC** | P3 | Plan & Commit |
| **PDLC** | P4 | Launch |
| **PDLC** | P5 | Grow |
| **PDLC** | P6 | Mature / Sunset |
| **SDLC** | A | Discover |
| **SDLC** | B | Specify |
| **SDLC** | C | Design |
| **SDLC** | D | Build |
| **SDLC** | E | Verify |
| **SDLC** | F | Release |

---

## Data engineering across the lifecycle

| Phase | Data engineering role | Key activities | Outputs |
|-------|----------------------|----------------|---------|
| **P1 Discover** | **Data assessor** | Assess existing data landscape; identify data sources for research | Data source inventory, data availability assessment |
| **P2 Validate** | **Data prototype builder** | Build data prototypes for hypothesis testing; quick analytics pipelines | Prototype pipelines, experimental data sets |
| **P3 Plan & Commit** | **Data strategist** | Define data strategy; estimate data infrastructure needs; data architecture options | Data strategy document, infrastructure cost model |
| **A Discover** | **Requirements analyst** | Identify data requirements for features; define data entities and relationships | Data requirements, entity-relationship models |
| **B Specify** | **Data modeler** | Design schemas; define data contracts; specify quality rules; plan migrations | Schema designs, data contracts, quality specifications |
| **C Design** | **Pipeline architect** | Design data flow; select processing patterns (batch/stream); integration architecture | Data flow diagrams, pipeline architecture, integration design |
| **D Build** | **Pipeline builder** | Implement data pipelines; build ETL/ELT jobs; configure data infrastructure | Working pipelines, schema migrations, IaC for data infra |
| **E Verify** | **Data quality gatekeeper** | Run data quality checks; validate schema compliance; reconciliation testing | Quality reports, validation results, data test suites |
| **F Release** | **Migration operator** | Execute data migrations; verify data integrity post-deployment | Migration scripts, integrity verification, rollback plan |
| **P4 Launch** | **Analytics enabler** | Enable production analytics; set up tracking pipelines; configure dashboards | Analytics pipeline, tracking events, launch dashboards |
| **P5 Grow** | **Data platform operator** | Scale data infrastructure; optimize costs; maintain quality; enable experimentation | Capacity plans, cost optimization reports, A/B test infrastructure |
| **P6 Sunset** | **Data archivist** | Data archival; retention compliance; cleanup of deprecated pipelines | Archival plan, retention compliance report |

---

## Role mapping

Data engineering decisions should be explicit at phase boundaries so accountability matches [`SDLC.md`](../../../sdlc/SDLC.md) delivery and [`PDLC.md`](../../../pdlc/PDLC.md) product governance. The table below maps **who typically owns** data engineering judgment to **PDLC roles** and **SDLC role archetypes** from [`roles-archetypes.md`](../../../sdlc/methodologies/roles-archetypes.md).

| Phase | Data engineering decision focus | Typical data engineering owner | PDLC role(s) | SDLC archetype emphasis |
|-------|----------------------------------|-------------------------------|--------------|-------------------------|
| **P1 Discover** | Which sources exist, what is usable for research, legal/ethical constraints | Data engineer or analyst embedded with discovery | PM, UX research | **Demand & value** |
| **P2 Validate** | Fast, disposable pipelines vs production-grade paths for experiments | Data engineer + analyst | PM, experiment owner | **Demand & value** |
| **P3 Plan & Commit** | Target architecture (lakehouse, mesh, batch/stream), cost envelope, governance model | Data architect / DE lead + finance partner | PM, exec sponsor | **Steer & govern**; **Demand & value** |
| **A Discover** | Data entities, relationships, and feature-level data needs | DE lead with product and engineering | PM (priorities) | **Demand & value**; **Build & integrate** |
| **B Specify** | Contracts, schemas, quality rules, migration approach | Data modeler / DE lead | Owner (scope), Implementer | **Build & integrate** |
| **C Design** | ETL/ELT vs streaming, Lambda/Kappa fit, integration boundaries | Pipeline architect / tech lead | Implementer, Architect | **Build & integrate** |
| **D Build** | Pipeline implementation, orchestration, IaC | Data / software engineers | Implementer | **Build & integrate** |
| **E Verify** | Data tests, reconciliation, contract validation in CI/CD | DE + QA | Implementer, QA | **Assure & ship** |
| **F Release** | Migrations, cutover, rollback drills for data paths | DE + release / SRE | Implementer, release | **Assure & ship** |
| **P4 Launch** | Production analytics, event pipelines, dashboard SLAs | Analytics engineer / DE | GTM, PM | **Demand & value** |
| **P5 Grow** | Scale, cost, freshness, experimentation plumbing | Platform DE / data SRE | PM, analytics | **Flow & improvement**; **Demand & value** |
| **P6 Sunset** | Retention, archival, decommissioning pipelines | DE + compliance | PM, legal | **Steer & govern** |

In small teams, one engineer may wear data modeling, pipeline build, and analytics hats; the table still defines **where decisions must be made**, even when the same person carries them across phases.

---

## Artifact flow

### Data engineering → SDLC

| Artifact | SDLC destination | Usage |
|----------|------------------|-------|
| Data requirements, ER views | A–B | Backlog and specification inputs for features touching master or event data |
| Data contracts, schema definitions | B–C | Design-time agreement between producers and consumers; breaking-change policy |
| Pipeline architecture, lineage notes | C–D | Implementation of batch/stream jobs, orchestration, and integration |
| Data test suites, quality reports | E | Gates for correctness, completeness, uniqueness, and timeliness before release |
| Migration scripts, rollback plans | F | Coordinated schema and data movement with application deploy |
| Data lineage and dependency map | C–F | Impact analysis for schema changes; on-call context for pipeline failures |
| Observability spec (alerts, SLOs for freshness) | D–F | DataOps feedback for late partitions, failed loads, and consumer lag |

### Data engineering → PDLC

| Artifact | PDLC destination | Usage |
|----------|------------------|-------|
| Data source inventory, availability assessment | P1 | Grounds problem discovery in what can be measured |
| Prototype pipelines, experiment datasets | P2 | Supports hypothesis tests without over-investing in production paths |
| Data strategy, cost model | P3 | Informs investment and architecture choices at stage gates |
| Analytics pipelines, event specs, dashboards | P4–P5 | Launch metrics and growth loops; A/B infrastructure |
| Archival and retention evidence | P6 | Defensible sunset and compliance |
| Domain ownership matrix (data mesh) | P3 | Clarifies who approves schema and quality bar per bounded context |
| Metric definitions (“single source of truth” spec) | P2–P5 | Aligns experiment readouts and dashboards with conformed dimensions |

### Feedback loops

| Source | Data engineering usage |
|--------|------------------------|
| PDLC P5 metrics and experiment results | Prioritize pipeline features, freshness SLAs, and domain data products |
| SDLC E/F defects tied to data | Feed quality rules, monitoring, and contract tests |
| Incidents and drift alerts | Drive DataOps improvements, retraining of checks, and catalog updates |
| Product sunset decisions | Trigger deprecation of pipelines and datasets per governance policy |
| Customer support data disputes | Surface contract gaps, missing keys, or timezone handling bugs for permanent tests |
| Finance / unit economics reviews | Refine partitioning, tiering, and job schedules to control storage and compute cost |

---

## Calibration

Not every initiative warrants the same depth of data engineering. Calibrate using initiative shape, regulatory exposure, and how central data is to the bet.

### By initiative type

| Initiative type | Data engineering investment | Reasoning |
|-----------------|------------------------------|-----------|
| **Data-heavy product** (recommendations, personalization, fraud, search ranking) | **Heavy** — production contracts, strong quality dimensions, near-real-time or batch SLAs, clear lineage | Wrong or late data directly erodes the core value proposition |
| **Analytics platform** (self-serve BI, metrics store, experimentation hub) | **Heavy** — medallion or equivalent layering, catalog, access control, cost governance | Many consumers amplify the cost of ambiguity and poor metadata |
| **Standard SaaS feature** (CRUD workflows with reporting) | **Medium** — solid event capture, dimensional modeling for key entities, standard ELT | Balance speed with enough structure to avoid one-off extracts |
| **Maintenance / bugfix** | **Light to minimal** — touch pipelines only when schemas or migrations are in scope | Avoid gold-plating pipelines for changes that do not move data boundaries |

### Signals to deepen or lighten

| Signal | Adjust |
|--------|--------|
| Frequent “numbers do not match” escalations | Deepen contracts, reconciliation tests, and catalog investment |
| High privacy or regulatory surface | Deepen governance, retention, and access patterns per DMBOK-style stewardship |
| Low data surface area and stable schema | Lighten ceremony; keep minimal contracts and monitoring |
| Rapid P2 experiments | Prefer disposable pipelines with a defined promotion path to production patterns |

### Regulatory posture and data sensitivity

| Context | Typical adjustment |
|---------|-------------------|
| **Highly regulated** (finance, health, minors’ data) | Stronger stewardship, access logging, retention proofs, and separation of duties on schema change |
| **Internal-only analytics** | Lighter external compliance; still enforce contracts and quality to protect operational decisions |
| **Cross-border residency** | Architecture and pipeline design choices fixed early in P3 and SDLC C; mistakes are expensive to unwind |

### How architecture choices shift the burden

| Pattern | When it helps | Trade-off |
|---------|----------------|-----------|
| **Lakehouse + medallion** | Many consumers need curated, reusable datasets | Operational overhead to maintain bronze/silver/gold contracts |
| **Data mesh** | Scale beyond a central team; domain ownership of data products | Requires mature federated governance and platform enablement |
| **Lambda / Kappa** | Latency-sensitive features or streaming analytics | Higher complexity in operations, testing, and exactly-once semantics |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Data swamp** | Data lake with no governance — everything dumped in, nothing findable | Implement data catalog, quality gates on ingestion, ownership per data domain |
| **Pipeline spaghetti** | Complex, undocumented dependencies between data pipelines | Data lineage tooling; pipeline dependency graphs; modular pipeline design |
| **Schema-on-hope** | No schema enforcement; consumers discover structure through trial and error | Define and enforce contracts; schema registry; breaking change process |
| **All data, no insight** | Collecting everything without defined use cases or consumers | Start from consumer needs; define data products; retire unused pipelines |

---

## Worked example

**Scenario:** A B2C product team wants a **recommendation strip** on the home screen. Success depends on trustworthy behavioral signals, a governed feature store or serving path, and product experimentation to validate lift. The tables below are illustrative; names and tools vary by organization.

### End-to-end artifact trail (representative)

| Lifecycle anchor | Representative data engineering outputs | Who consumes them |
|------------------|----------------------------------------|-------------------|
| P1 | Source inventory, PII and consent constraints | PM, research, legal |
| P2 | Sandbox joins, prototype feature extract | DS / PM, experiment owner |
| P3 | Target architecture note, TCO model, domain ownership sketch | Exec sponsor, finance, platform |
| SDLC A–B | Data requirements packet, contracts, migration plan | Owner, Implementer, QA |
| SDLC C–D | Pipeline design, orchestration code, IaC modules | Implementer, SRE |
| SDLC E–F | Data test reports, migration runbook, post-deploy reconciliation | QA, release manager |
| P4–P5 | Event dictionaries, dashboard datasets, experiment exposure tables | PM, analytics, GTM |
| P6 | Retention evidence, archival manifest, deprecation checklist | Compliance, PM |

### P1–P2 (discover and validate)

Product and research confirm that clickstream and purchase history exist but **event definitions differ** between web and mobile. Data engineering produces a short-lived **prototype pipeline** that joins the two sources for a sandbox cohort. P2 runs an offline evaluation: can a simple collaborative filter beat the baseline? Outcome: hypothesis is promising; gaps in **event completeness** and **timeliness** are documented. The team explicitly decides which **quality dimensions** must improve before production promotion (for example, stricter **validity** rules on item IDs and **uniqueness** on impression keys).

### P3 (plan & commit)

The team chooses a **lakehouse** landing with a **medallion-style** refinement (bronze raw events, silver conformed sessions, gold recommendation-ready features), batch scoring with a path toward near-real-time updates later. Data engineering supplies an **infrastructure cost model** and **data governance** notes: PII handling, retention, and which domains own which datasets. A **Kappa-style** stream path is captured as a **future option** if latency becomes a product constraint; v1 stays batch-first to reduce operational risk.

### SDLC A–B (discover and specify)

Engineering and product specify **data requirements**: impression events, click events, item metadata, and consent flags. Data engineering authors **data contracts** for each event, **quality rules** (e.g. uniqueness of event IDs, validity of timestamps), and a **migration plan** for adding new fields without breaking existing consumers. Non-functional expectations (freshness SLAs, partition strategy) are written so **E Verify** can automate checks rather than rely on manual spot checks.

### SDLC C–D (design and build)

Architecture selects **ELT** into the lakehouse, orchestrated jobs for silver/gold layers, and a **Lambda-leaning** pattern: batch features for training and serving v1, with hooks for a faster layer later. Application teams implement **instrumentation**; data engineering implements **pipelines and IaC** alongside application services. **Lineage** from raw clickstream to scored recommendations is captured so breaking changes surface in review, not only in production.

### SDLC E–F (verify and release)

**Data quality gatekeeper** activities run in CI: schema compatibility, row-count reconciliation between sources and bronze, and sampling for **consistency** across web and mobile. Example checks mapped to dimensions:

| Dimension | Example automated check |
|-----------|-------------------------|
| **Completeness** | Null rate thresholds on mandatory fields; session stitching coverage |
| **Timeliness** | Bronze partition landed within SLA; lag vs application clock |
| **Consistency** | Aggregated CTR from events matches reporting cube within tolerance |
| **Uniqueness** | Duplicate event keys rejected or quarantined |

**Release** includes a **migration operator** checklist: backfill window, rollback for feature table versions, and integrity checks post-deploy.

### P4–P5 (launch and grow)

**Analytics enabler** work wires **launch dashboards** and **experiment assignment** data so PDLC can read lift on recommendation CTR and downstream revenue. In P5, **DataOps** practices monitor **freshness** and **drift**; cost and **capacity** reviews prevent runaway scans. Product uses the same conformed metrics for **growth** experiments, closing the loop from PDLC back to pipeline priorities. If readouts disagree, the team traces through lineage to determine whether the gap is product logic, assignment, or data pipeline regression.

### P6 (mature / sunset)

If the feature retires, **data archivist** activities archive historical training and serving tables per **retention** policy, drop obsolete pipelines, and update the **catalog** so consumers do not attach to deprecated datasets. Lessons feed the next initiative: which contracts prevented incidents, which checks caught drift early, and which prototypes should become platform templates.

---

## Related reading

| Doc | Why |
|-----|-----|
| [`BIGDATA.md`](BIGDATA.md) | Principles, governance, quality, pipeline patterns, DataOps |
| [`architectures/README.md`](architectures/README.md) | Lambda, Kappa, data mesh, data lakehouse |
| [`technologies/README.md`](technologies/README.md) | Processing frameworks, storage systems, orchestration |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, metrics framework |
