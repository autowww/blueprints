# Data

**How we handle information at scale** — the disciplines that engineer, govern, and extract knowledge from data.

Data disciplines sit at the intersection of engineering (building pipelines and infrastructure) and product (enabling analytics, experiments, and data-driven decisions).

| Discipline | Core question | Package |
|-----------|---------------|---------|
| [**Big Data & Data Engineering**](bigdata/README.md) | How do we engineer, govern, and process data at scale? | Data governance, pipeline patterns, DataOps, architectures (Lambda, Kappa, data mesh), operational data modeling |
| [**Data Science & ML**](data-science/README.md) | How do we extract knowledge and build predictive models from data? | CRISP-DM, MLOps, model evaluation, responsible AI, experiment management |

## Relationship to other families

| Family | How Data relates |
|--------|-----------------|
| [**Engineering**](../engineering/README.md) | Data pipelines are software — they go through SDLC phases. DevOps practices (CI/CD, IaC, observability) apply to data infrastructure as DataOps. Architecture decisions shape data flow and storage. |
| [**Product**](../product/README.md) | PDLC discovery and growth depend on data — usage analytics, A/B testing, outcome measurement. BA defines data requirements; Marketing uses analytics and attribution. |
| [**Governance**](../governance/README.md) | PM governs data project delivery. Data quality and governance processes align with organizational improvement (Lean). |
| [**Security**](../security/README.md) | Data security (classification, access control, encryption, audit logging) is a core concern. Data breaches are a primary security risk. |
| [**Compliance**](../compliance/README.md) | Data disciplines are heavily regulated — GDPR (personal data), HIPAA (health data), PCI-DSS (financial data). Compliance requirements shape data architecture and lifecycle. |

## Bridge documents

Each discipline has a bridge document mapping its practices to SDLC and PDLC phases. See [`BRIDGES.md`](../../BRIDGES.md) for the full index.
