---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Big data & data engineering

Reusable, **project-agnostic** blueprint for **big data and data engineering** — the discipline of designing, building, and maintaining the systems and infrastructure for collecting, storing, processing, and governing data at scale.

Data engineering answers **"how do we engineer, govern, and process data at scale?"** — a question that intersects SDLC delivery (building data pipelines) and PDLC strategy (data as a product asset).

| Document | Purpose |
|----------|---------|
| [**BIGDATA.md**](BIGDATA.md) | Data engineering principles, data governance, data quality dimensions, data lifecycle, DMBOK alignment, competencies |
| [**BIGDATA-SDLC-PDLC-BRIDGE.md**](BIGDATA-SDLC-PDLC-BRIDGE.md) | How data engineering maps across SDLC phases A–F and PDLC phases P1–P6 — schema in Specify, pipelines in Build, validation in Verify, analytics in Grow |
| [**architectures/**](architectures/README.md) | Data architecture patterns: Lambda, Kappa, data mesh, data lakehouse, medallion architecture |
| [**technologies/**](technologies/README.md) | Processing framework taxonomy, storage systems, streaming platforms, orchestration tools |
| [**techniques/**](techniques/README.md) | Operational data modeling — relational, NoSQL, indexing, transactions, migration, polyglot persistence |

## Relationship to other packages

| Package | How Big Data relates |
|---------|----------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | Data pipelines are software — they go through SDLC phases (design, build, test, deploy). Schema design happens in Specify; pipeline implementation in Build; data validation in Verify. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P1–P3 (Discover, Validate, Plan & Commit) define data strategy and analytics requirements. P5 (Grow) relies on data infrastructure for usage analytics, A/B testing, and outcome measurement. |
| [`blueprints/disciplines/product/ba/`](../../product/ba/README.md) | BA Business Intelligence perspective covers data requirements, analytics, and data quality. Data engineering provides the infrastructure that makes BI possible. |
| [`blueprints/disciplines/engineering/software-architecture/`](../../engineering/software-architecture/README.md) | Data architecture is a subset of system architecture. Storage choices, processing patterns, and data flow design are architectural decisions. |
| [`blueprints/disciplines/engineering/devops/`](../../engineering/devops/README.md) | DataOps applies DevOps principles to data pipelines — CI/CD for data, data quality gates, pipeline observability, infrastructure as code for data infrastructure. |
| [`blueprints/disciplines/data/data-science/`](../data-science/README.md) | Data engineering provides the infrastructure and data preparation that data science depends on. Feature stores, training data pipelines, and model serving infrastructure bridge the two disciplines. |

## Scope

This package covers **data engineering as a discipline** — not just database administration or ETL scripting. It includes:

- **Data architecture** — storage systems, processing patterns, data flow design
- **Data pipelines** — batch processing, stream processing, ELT/ETL patterns
- **Data governance** — data ownership, classification, lineage, cataloging, access control
- **Data quality** — accuracy, completeness, consistency, timeliness, validity, uniqueness
- **Data lifecycle** — creation, storage, usage, archival, deletion, compliance (GDPR, retention)
- **DataOps** — CI/CD for data, automated testing of data pipelines, data observability

Reference bodies of knowledge: DAMA DMBOK (Data Management Body of Knowledge), data mesh principles (Zhamak Dehghani).

---

*Keep project-specific data documentation in `docs/product/data/` and data architecture decisions in `docs/adr/`, not in this file.*
