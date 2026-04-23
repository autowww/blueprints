---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Business Intelligence perspective

How business analysis adapts when the initiative centers on **data**, **analytics**, **reporting**, or **data-driven decision making**. BI initiatives require BA to address data requirements alongside — and often instead of — traditional functional requirements.

**BABOK alignment:** BABOK v3 Business Intelligence perspective.

**Related blueprints:** [`blueprints/pdlc/PDLC.md`](../../../../pdlc/PDLC.md) §5 (Metrics framework) · [`blueprints/product/STRUCTURE.md`](../../../../product/STRUCTURE.md) (data folder in product docs).

---

## 1. How BI changes the BA focus

| Traditional BA Focus | BI BA Focus |
|---------------------|-------------|
| Functional requirements (what the system does) | Data requirements (what data exists, what quality, what insights) |
| User workflows | Data flows and transformations |
| System interactions | Data source integration and lineage |
| Acceptance criteria for features | Data quality criteria and validation rules |
| Solution performance (response time, availability) | Data accuracy, completeness, timeliness, freshness |

---

## 2. Knowledge area shifts

| Knowledge Area | BI Adaptation |
|----------------|---------------|
| **BA Planning & Monitoring** | Stakeholder analysis must include data owners, data stewards, and data consumers. Plan for data quality assessment as a BA activity. |
| **Strategy Analysis** | Current state analysis includes data landscape assessment — what data exists, where, quality, accessibility. Future state defines data-driven capabilities. |
| **Elicitation & Collaboration** | Elicit information needs (what questions do stakeholders need to answer?), not just process needs. Data profiling is an elicitation technique. |
| **Requirements Life Cycle Management** | Data requirements need version control alongside functional requirements. Data dictionaries and lineage documentation require maintenance. |
| **Requirements Analysis & Design Definition** | Data models, ETL specifications, report/dashboard specifications, KPI definitions replace or supplement use cases and process models. |
| **Solution Evaluation** | Evaluate data quality (accuracy, completeness, consistency), report adoption, decision impact — not just functional correctness. |

---

## 3. BI-specific BA activities

### 3.1 Data requirements analysis

| Activity | Description | Output |
|----------|-------------|--------|
| **Information needs analysis** | Identify what questions stakeholders need to answer with data | Information needs catalog |
| **Data source identification** | Inventory available data sources, assess accessibility and quality | Data source inventory |
| **Data profiling** | Statistical analysis of data to understand content, quality, and structure | Data quality assessment |
| **Data modeling** | Conceptual, logical, and physical data models for the analytics solution | Data models (dimensional, star schema, etc.) |
| **KPI definition** | Define measurable indicators with calculation formulas, data sources, and thresholds | KPI specifications |
| **Report/dashboard specification** | Define layout, filters, drill-down paths, data refresh frequency | Report specifications |

### 3.2 Data quality management

| Quality Dimension | Definition | Example Criteria |
|-------------------|------------|------------------|
| **Accuracy** | Data correctly represents the real-world entity or event | Customer email matches actual email address |
| **Completeness** | All required data is present | No null values in mandatory fields |
| **Consistency** | Same data represented the same way across sources | Date formats uniform across systems |
| **Timeliness** | Data is available when needed | Dashboard refreshes within 15 minutes of source update |
| **Uniqueness** | No duplicate records for the same entity | One customer record per customer |
| **Validity** | Data conforms to defined rules and formats | Phone numbers match expected patterns |

---

## 4. BI-specific techniques

| Technique | BI Usage |
|-----------|----------|
| **Data profiling** | Assess quality, patterns, and anomalies in source data |
| **Dimensional modeling** | Design star/snowflake schemas for analytical workloads |
| **KPI decomposition** | Break high-level business metrics into measurable components |
| **Dashboard wireframing** | Visual prototype of report/dashboard layout and interactions |
| **ETL specification** | Define extraction, transformation, and loading rules for data pipelines |
| **Data lineage mapping** | Trace data from source through transformations to consumption |
| **Data dictionary** | Define entities, attributes, domains, and business meanings |
| **Cohort analysis** | Segment users/data by time period or attribute for trend analysis |

---

## 5. BI BA artifacts

| Artifact | Purpose | Where It Lives |
|----------|---------|----------------|
| **Data dictionary** | Canonical definitions for data entities and attributes | `docs/product/data/` |
| **KPI specifications** | Formal definitions of metrics with calculation formulas | `docs/product/metrics/` |
| **Data quality rules** | Validation criteria for each data element | `docs/requirements/` |
| **Report/dashboard specs** | Layout, filters, data sources, refresh rules | `docs/product/features/` |
| **Data source inventory** | Available data sources with quality assessment | `docs/product/data/` or `docs/product/integrations/` |
| **Data lineage diagrams** | Visual representation of data flow from source to consumption | `docs/architecture/` |

---

## 6. Common pitfalls in BI BA

| Pitfall | Description | Remedy |
|---------|-------------|--------|
| **Report factory** | Building every report a stakeholder requests without understanding the decision it supports | Always ask: "What decision will this data support? What action will you take based on the answer?" |
| **Data quality assumed** | Assuming source data is clean; discovering quality issues during development or after launch | Profile data early; include data quality assessment in P1 discovery |
| **Missing business context** | Technical data model without business meaning; analysts can query but can't interpret | Maintain a data dictionary with business definitions, not just technical metadata |
| **Vanity metrics** | Tracking metrics that look good but don't drive decisions (page views, total users) | Use the metrics framework from [`PDLC.md`](../../../../pdlc/PDLC.md) §5 — focus on actionable outcome metrics |
