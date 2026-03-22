# Data engineering techniques (blueprint)

**Purpose:** Deep, **project-agnostic** guides for data engineering techniques. Each guide covers principles, implementation patterns, trade-offs, and tooling so teams can reuse patterns without copying project-specific schemas or pipelines.

**Audience:** Teams adopting [`blueprints/disciplines/data/bigdata/`](../README.md); project-specific data configuration stays in **`docs/product/data/`** where that convention exists.

Techniques here complement **architecture** and **product** docs: modeling and quality rules apply regardless of whether you run Lambda, Kappa, or a lakehouse. Planned guides will extend pipeline and validation topics without duplicating [`BIGDATA.md`](../BIGDATA.md).

---

| Technique | Focus | Guide |
|-----------|-------|-------|
| **Operational data modeling** | Relational modeling (normalization, ER), indexing strategies, query plan analysis, transaction isolation, schema migration, NoSQL modeling (document, key-value, graph, time-series), polyglot persistence | [`operational-data-modeling.md`](operational-data-modeling.md) |
| **Pipeline patterns** | ETL/ELT, CDC, idempotency, orchestration integration | *(planned)* |
| **Data quality** | Validation layers, testing data pipelines, observability for freshness and volume | *(planned)* |

**How to use this section:** Read [`operational-data-modeling.md`](operational-data-modeling.md) when designing schemas, choosing indexes, or comparing relational vs NoSQL shapes. When pipeline-pattern and data-quality guides exist, use them alongside ADRs for **project-specific** pipeline layout and SLAs.

Suggested reading order for new practitioners:

1. [`BIGDATA.md`](../BIGDATA.md) §1–2 for vocabulary and governance framing.
2. [`operational-data-modeling.md`](operational-data-modeling.md) before locking physical schemas.
3. [`architectures/README.md`](../architectures/README.md) when choosing batch vs stream vs mesh posture.

**Core knowledge:** [`BIGDATA.md`](../BIGDATA.md) — data engineering principles, governance, pipeline patterns, DataOps.

**Bridge:** [`BIGDATA-SDLC-PDLC-BRIDGE.md`](../BIGDATA-SDLC-PDLC-BRIDGE.md) — how data engineering maps to delivery and product lifecycles.

**Architectures & engines:** [`architectures/README.md`](../architectures/README.md), [`technologies/README.md`](../technologies/README.md) (including [`processing-engines.md`](../technologies/processing-engines.md)).

**Cross-reference:** [`BIGDATA.md`](../BIGDATA.md) §2 (governance and quality dimensions) and §5 (competencies) align with the techniques catalog; mesh-specific ownership is covered in [`architectures/data-mesh.md`](../architectures/data-mesh.md).

**Scope boundary:** Blueprint technique guides stay **pattern-level** (what to consider, how to trade off). Concrete DDL, DAG definitions, and environment-specific connection strings belong in **`docs/development/`** or your pipeline repo, with ADRs for durable decisions.

**Related blueprints:** For end-to-end data discipline context, start at [`../README.md`](../README.md), then drill into architectures and technologies as needed.

---

*Keep project-specific data architecture decisions in docs/adr/ and pipeline documentation in docs/development/, not in this file.*
