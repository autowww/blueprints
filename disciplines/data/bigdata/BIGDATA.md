# Big data & data engineering body of knowledge

This document maps the core concerns of **data engineering** — data architecture, pipelines, governance, quality, and lifecycle management — to the blueprint ecosystem.

**How data engineering relates to PDLC and SDLC:** Data engineering is a **cross-cutting discipline** that provides data infrastructure for both lifecycles. See [`BIGDATA-SDLC-PDLC-BRIDGE.md`](BIGDATA-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Architectures:** Data architecture patterns (Lambda, Kappa, data mesh, etc.) are in [`architectures/`](architectures/README.md).

**Technologies:** Processing framework and tooling guidance is in [`technologies/`](technologies/README.md).

---

## 1. Data engineering principles

| Principle | Description |
|-----------|-------------|
| **Data as a product** | Treat data sets as products with defined consumers, SLOs, documentation, and ownership |
| **Automation first** | Automate data pipelines, quality checks, and provisioning; minimize manual data handling |
| **Schema on read vs write** | Choose schema enforcement strategy based on use case — strict schemas for operational data, flexible for exploratory |
| **Idempotency** | Data pipelines should produce the same result when run multiple times with the same input |
| **Lineage and observability** | Track data from source to consumption; understand transformations; detect anomalies |
| **Least privilege** | Restrict data access to what each consumer needs; classify data by sensitivity |
| **Cost awareness** | Data storage and processing costs scale with volume; optimize for cost-efficiency without sacrificing quality |

---

## 2. Data governance

### DMBOK knowledge areas (relevant subset)

| Knowledge area | Core question | Key outputs |
|----------------|---------------|-------------|
| **Data governance** | Who owns data, and how are data decisions made? | Data governance charter, stewardship roles, decision rights |
| **Data quality** | Is the data fit for its intended use? | Quality rules, profiling results, quality dashboards |
| **Metadata management** | What does the data mean, and where does it come from? | Data catalog, glossary, lineage graphs |
| **Data security** | Who can access what data, and how is it protected? | Access policies, encryption standards, audit logs |
| **Data architecture** | How is data organized, integrated, and made available? | Data models, integration patterns, reference architecture |
| **Data integration** | How does data flow between systems? | ETL/ELT pipelines, API contracts, CDC streams |

### Data quality dimensions

| Dimension | Definition | Measurement example |
|-----------|-----------|---------------------|
| **Accuracy** | Data correctly represents the real-world entity or event | % of records matching authoritative source |
| **Completeness** | Required data elements are present and not null | % of non-null values for required fields |
| **Consistency** | Same data is represented the same way across systems | Cross-system reconciliation match rate |
| **Timeliness** | Data is available when needed; freshness meets SLA | Data age at consumption time vs SLA |
| **Validity** | Data conforms to defined business rules and formats | % of records passing validation rules |
| **Uniqueness** | No unintended duplicate records | Duplicate detection rate |

---

## 3. Data pipeline patterns

| Pattern | Description | Best fit |
|---------|-------------|----------|
| **Batch ETL** | Extract, transform, load on a schedule (hourly, daily) | Reporting, data warehousing, low-latency not required |
| **Batch ELT** | Extract, load raw, then transform in-place | Cloud data warehouses (BigQuery, Snowflake, Redshift) where compute is elastic |
| **Stream processing** | Process events in real-time or near-real-time as they arrive | Real-time analytics, alerting, event-driven architectures |
| **Change data capture (CDC)** | Capture row-level changes from source databases | Database replication, keeping derived stores in sync |
| **Micro-batch** | Small, frequent batch jobs (seconds to minutes) | Near-real-time needs without full streaming complexity |
| **Data virtualization** | Query data in place without moving it | Federation across multiple sources without ETL overhead |

---

## 4. DataOps

DataOps applies DevOps principles to data:

| DevOps practice | DataOps equivalent |
|-----------------|---------------------|
| **CI/CD** | Automated pipeline deployment; schema migration CI; data transformation testing |
| **Infrastructure as Code** | Data infrastructure provisioning (databases, warehouses, streaming clusters) via IaC |
| **Automated testing** | Data quality checks in pipeline; schema validation; reconciliation tests |
| **Monitoring/alerting** | Data freshness monitoring; pipeline health; quality metric dashboards |
| **Incident management** | Data incident process — stale data, quality degradation, pipeline failure |
| **Version control** | Schema versioning; transformation code in git; dbt models versioned |

---

## 5. Competencies

| Competency | Description |
|------------|-------------|
| **Data modeling** | Designing logical and physical data models — relational, dimensional, graph, document |
| **Distributed systems** | Understanding partitioning, replication, consistency, and fault tolerance |
| **SQL and query optimization** | Writing efficient queries; understanding query plans; index design |
| **Pipeline engineering** | Building reliable, idempotent, observable data pipelines |
| **Cloud platforms** | Working with cloud data services (storage, compute, streaming, analytics) |
| **Data governance** | Implementing classification, access control, lineage, and quality |

---

## 6. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| DAMA DMBOK | https://www.dama.org/cpages/body-of-knowledge | Canonical data management body of knowledge |
| Data Mesh (Zhamak Dehghani) | https://www.datamesh-architecture.com/ | Domain-oriented, product-thinking approach to analytical data |
| Fundamentals of Data Engineering (Reis, Housley) | https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ | Modern data engineering lifecycle and practices |
| The Data Warehouse Toolkit (Kimball) | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/ | Dimensional modeling — the standard reference |
| Designing Data-Intensive Applications (Kleppmann) | https://dataintensive.net/ | Distributed data systems — storage, replication, partitioning, batch/stream processing |

---

*Keep project-specific data documentation in `docs/product/data/` and data architecture decisions in `docs/adr/`, not in this file.*
