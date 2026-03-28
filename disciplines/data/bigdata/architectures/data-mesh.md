# Data mesh: domain-oriented decentralized architecture

**Purpose:** Project-agnostic guide to **data mesh** — treating analytical data as **domain-owned products** on a **self-serve platform** under **federated governance**.

**Audience:** Teams using [`blueprints/disciplines/data/bigdata/`](../README.md). See [`BIGDATA.md`](../BIGDATA.md) for principles, governance, and pipeline patterns that mesh implementations must still satisfy.

---

## 1. Overview

Data mesh is both **organizational** and **technical**. Instead of one central data team owning all pipelines and marts, **domain teams** publish **data products** with explicit **contracts**, **SLOs**, and **lifecycle ownership**. A **platform** removes undifferentiated toil (provisioning, CI templates, observability baselines); **governance** stays **federated** — global rules where they matter, **autonomy** where domains differ.

It is not “microservices for tables” without standards: without **interoperability** and **enforcement**, mesh becomes **distributed chaos**.

---

## 2. Four principles

| Principle | Definition | Benefit | Implementation challenge |
|-----------|------------|---------|---------------------------|
| **Domain ownership** | The team closest to the business context owns the **data product** end-to-end | Contextual quality; faster feedback loops | Skill gaps; competing priorities with product roadmaps |
| **Data as a product** | Consumers get discoverable, reliable, documented interfaces — not raw dumps | Reuse; trust; fewer ad-hoc extracts | Defining SLAs; support burden; product management discipline |
| **Self-serve data platform** | Golden paths for ingestion, transformation, publishing, and observability | Scale without central bottleneck | Platform product ownership; preventing one-off snowflakes |
| **Federated computational governance** | Global policies (security, privacy, interoperability) + **automated** checks | Consistency without central approval for every change | Policy-as-code maturity; cross-domain standards negotiation |

---

## 3. Topology (conceptual)

```blueprint-diagram
key: swimlane
alt: Diagram
```

---

## 4. Data product anatomy

A **data product** is more than a table: it is an **operated interface** with explicit boundaries.

```blueprint-diagram
key: swimlane
alt: Diagram
```

**Input ports** declare upstream expectations (schema, volume, SLAs). **Output ports** are versioned consumer contracts. **Discovery** combines catalog metadata and human-readable intent. **Observability** covers freshness, volume anomalies, and failed publishes. **SLOs** make reliability negotiable.

---

## 5. Comparison: mesh vs warehouse vs lake vs lakehouse

| Dimension | Data mesh | Data warehouse | Data lake | Data lakehouse |
|-----------|-----------|----------------|-----------|----------------|
| **Ownership** | Federated by domain | Often centralized analytics | Often centralized platform team | Platform + domain mix (varies) |
| **Governance** | Federated + automated | Strong central modeling | Often weak without discipline | Improving via table formats + catalogs |
| **Scalability** | Organizational scale-out | Team bottleneck risk | Storage scale; curation risk | Storage + engine scale |
| **Agility** | High when platform mature | Slower change for unrelated domains | Fast landing; slow trust | Faster trusted consumption |
| **Complexity** | High coordination surface | Lower concept count | Medium; can become swamp | Medium–high tooling |
| **Maturity required** | Product + platform + governance | Mature SQL/analytics practice | Data engineering maturity | Lake + warehouse skills combined |

Mesh can **use** a lakehouse as **implementation**; the differentiator is **ownership and operating model**.

---

## 6. Self-serve data platform capabilities

| Capability | What “good” looks like |
|------------|-------------------------|
| **Storage provisioning** | Namespaces, encryption, retention defaults; cost guardrails |
| **Pipeline orchestration** | Templates, env promotion, secrets handling |
| **Schema registry** | Compatibility modes; contract tests in CI |
| **Access control** | ABAC/RBAC integration; column/row policies where needed |
| **Catalog** | Ownership, lineage, PII tags, deprecation workflow |
| **Monitoring** | Freshness, volume, schema drift alerts; SLO dashboards |
| **Data quality** | Reusable expectations; quarantine/DLQ patterns; scorecards |

---

## 7. Federated governance

- **Global policies**: legal retention, residency, identity standards, naming conventions, PII handling.
- **Domain autonomy**: internal model choices that do not break interoperability.
- **Interoperability standards**: event schemas, identifier strategy, mesh-wide glossary links.
- **Computational governance**: policy checks in CI/CD, automated blocking of breaking publishes, audit evidence from pipelines rather than ticket theater.

---

## 8. Data product lifecycle

```blueprint-diagram
key: decision
alt: Diagram
```

---

## 9. Organizational readiness

**Favors data mesh:** Large org, many domains, central data team is a **gating** bottleneck, strong **engineering culture**, willingness to fund a **platform** as a product.

**Premature mesh:** Small team, no catalog or CI basics, leadership expects mesh to **replace** governance investment, or domains lack **data engineering** capacity and **product** discipline.

---

## 10. Implementation patterns

| Pattern | Description |
|---------|-------------|
| **One domain pilot** | One credible domain builds 1–3 data products on golden paths; harden platform from real pain |
| **Strangler from centralized lake** | Domains gradually **own** curated layers; central team shifts to platform + standards |
| **Incremental platform** | Start with catalog + access + CI templates; add quality and lineage as adoption grows |

---

## 11. Anti-patterns

| Anti-pattern | Symptom |
|--------------|---------|
| **Mesh without platform** | Every domain builds bespoke fragile stacks |
| **No governance** | Incompatible schemas, duplicative entities, compliance risk |
| **Every table is a “data product”** | Catalog noise; no real SLOs or owners |
| **Premature decomposition** | Operational cost exceeds value; weak observability |

---

## 12. External references

| Reference | Notes |
|-----------|--------|
| Zhamak Dehghani, *Data Mesh: Delivering Data-Driven Value at Scale* (O’Reilly) | Foundational book |
| [datamesh-architecture.com](https://www.datamesh-architecture.com/) | Community site and pattern language |
| [ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar) | Tracks mesh-related techniques and maturity |

---

*Keep project-specific data architecture decisions in docs/adr/ and pipeline documentation in docs/development/, not in this file.*
