---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Data architectures (blueprint)

**Purpose:** Catalog of **data architecture patterns** — structural approaches to organizing data storage, processing, and access at scale. Each pattern describes its structure, trade-offs, and fitness criteria.

**Why it matters:** Data architecture is the **foundation of data strategy**. It constrains what latency, consistency, ownership, and cost profiles are achievable before tool selection. Patterns here are **reference models**; a concrete system often blends ideas (for example, lakehouse storage with mesh-style ownership).

**Audience:** Teams adopting [`blueprints/disciplines/data/bigdata/`](../README.md); architecture choices for a specific project are documented as ADRs in **`docs/adr/`**.

### Architecture evolution (conceptual timeline)

```blueprint-diagram
key: linear
alt: Process flow
title: Architecture pattern selection flow
summary: How teams move from data-strategy constraints to a documented reference architecture choice from this catalog.
node: Process flow
detail: Frames the path from constraints to a reviewable architecture decision.
more: Patterns here are reference models; concrete systems often blend ideas such as lakehouse storage with mesh-style ownership.
node: Start
detail: Clarify latency, volume, team structure, and analytics use cases.
more: Selection depends on these factors plus operational maturity before comparing rows in the table below.
node: Core steps (see walkthrough below)
detail: Review each pattern's core idea, trade-offs, and linked deep guides.
more: Use linked guides for comparison matrices, decision flowcharts, technology mapping, and anti-patterns beyond one-line summaries.
node: Outcome
detail: A bounded architecture choice captured for the project.
more: Record project-specific decisions in docs/adr/ and pipeline documentation in docs/development/, not in this catalog.
node: Note: operating model
detail: Some patterns govern ownership and federation, not storage technology alone.
more: Data mesh is primarily an operating model that can sit on lakehouse or warehouse technology; it is not a strict successor to either.
fallback_ascii: |
  Process flow

  Start
      |
      v
  Core steps (see walkthrough below)
      |
      v
  Outcome

  Note: operating model
```

Mesh is not a strict successor to lakehouse — it is primarily an **operating model** that can sit on top of lakehouse or warehouse technology.

Use the linked guides when you need **comparison matrices**, **decision flowcharts**, **technology mapping**, and **anti-patterns** beyond the one-line summaries in the table.

---

| Architecture | Core idea | Best fit | Guide |
|-------------|-----------|----------|-------|
| **Lambda** | Dual path — batch layer for completeness + speed layer for low latency; serving layer merges | Systems needing both historical accuracy and real-time views; complex but flexible | [`lambda-kappa.md`](lambda-kappa.md) |
| **Kappa** | Single stream-processing path; reprocess by replaying the event log | Stream-first systems where batch reprocessing from the log is sufficient | [`lambda-kappa.md`](lambda-kappa.md) |
| **Unified streaming / lakehouse** | One engine and/or table-centric storage for batch + stream + serving (e.g., Flink, Delta/Iceberg/Hudi) | Reducing dual-path cost while keeping reprocessing and analytics | [`lambda-kappa.md`](lambda-kappa.md) |
| **Data mesh** | Domain-oriented, decentralized data ownership; data as a product; federated governance | Large organizations with multiple domains; autonomous teams; data product thinking | [`data-mesh.md`](data-mesh.md) |
| **Data lakehouse** | Unified storage combining data lake flexibility with data warehouse reliability (Delta Lake, Iceberg, Hudi) | Organizations wanting to eliminate separate lake + warehouse; ML and BI on same storage | [`lambda-kappa.md`](lambda-kappa.md) |
| **Medallion (bronze/silver/gold)** | Layered data quality — raw ingestion (bronze), cleaned/conformed (silver), business-ready (gold) | Lakehouse and data lake environments; progressive quality refinement | [BIGDATA.md §3](../BIGDATA.md#3-data-pipeline-patterns) |
| **Data warehouse (Kimball)** | Dimensional modeling — facts and dimensions; star/snowflake schemas; bottom-up | BI and reporting; well-understood business processes; SQL-centric analytics | [BIGDATA.md §1](../BIGDATA.md#1-data-engineering-principles) |
| **Data warehouse (Inmon)** | Enterprise data warehouse — normalized; top-down; single source of truth | Enterprise-wide integration; strict consistency requirements | [BIGDATA.md §1](../BIGDATA.md#1-data-engineering-principles) |

**Decision guidance:** Architecture selection depends on latency requirements, data volume, team structure, analytics use cases, and operational maturity. See [`BIGDATA.md`](../BIGDATA.md) §1 (principles) for the decision framework and governance/quality context in later sections.

**Cross-reference:** For pipeline patterns (batch ETL/ELT, CDC, micro-batch) and DataOps practices that implement these architectures, use [`BIGDATA.md`](../BIGDATA.md) §§3–4. Processing engine trade-offs are summarized in [`technologies/processing-engines.md`](../technologies/processing-engines.md).

Medallion and dimensional warehouse rows link to the relevant body-of-knowledge sections in [`BIGDATA.md`](../BIGDATA.md); add project-specific star schemas and conformed dimensions in **`docs/adr/`** or modeling appendices as your repo convention requires.

---

*Keep project-specific data architecture decisions in docs/adr/ and pipeline documentation in docs/development/, not in this file.*
