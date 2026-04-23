---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# CRISP-DM: Cross-Industry Standard Process for Data Mining

**Purpose:** Project-agnostic reference for CRISP-DM — the most widely adopted methodology for data mining and applied machine learning. Use it to structure discovery, modeling, and handoff without tying the blueprint to a specific tool stack.

**Audience:** Teams following [`DATA-SCIENCE.md`](../DATA-SCIENCE.md) and [`approaches/README.md`](README.md).

---

## Overview

CRISP-DM (Cross-Industry Standard Process for Data Mining) is a **process model**, not a single algorithm or product. It organizes work from business intent through deployed models with explicit feedback loops. Its strength is **shared vocabulary** across business, analytics, and engineering: everyone can anchor discussions in the same six phases.

The process is **iterative by design**. Evaluation often sends you back to data preparation or modeling; deployment feedback revisits business understanding. Treat phase boundaries as **decision gates**, not linear milestones.

---

## Six phases at a glance

| Phase | Objectives | Key activities | Typical outputs | Typical duration %* |
|-------|------------|----------------|-----------------|---------------------|
| **Business Understanding** | Align analytics with business goals and constraints | Stakeholder interviews; problem framing; success criteria; risk and scope | Problem statement, success metrics, project plan, feasibility note | ~15–20% |
| **Data Understanding** | Know what data exists and whether it can support the goals | Initial collection; EDA; quality checks; hypothesis sketches | Data dictionary, EDA report, quality assessment, gap analysis | ~15–20% |
| **Data Preparation** | Produce analysis-ready datasets and reproducible transforms | Selection, cleaning, integration, feature construction, formatting | Clean datasets, feature specs, transformation code/pipelines | ~25–35% |
| **Modeling** | Fit candidate models and compare approaches | Technique selection; design of experiments; train/validation protocol; tuning | Trained models, experiment logs, comparison tables | ~10–20% |
| **Evaluation** | Judge whether results meet business and technical bars | Metric review vs criteria; error analysis; cost/benefit; deploy decision | Evaluation report, go/no-go, documented limitations | ~10–15% |
| **Deployment** | Put the solution into operation and sustain value | Rollout plan; monitoring; maintenance; documentation; knowledge transfer | Deployed artifact, runbooks, monitoring dashboards, final report | ~5–15% |

\*Percentages are **indicative** only; highly regulated or messy data domains shift time toward understanding and preparation.

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Phase deep dives

### Business Understanding

| Sub-task | What to do | Output |
|----------|------------|--------|
| Problem framing | Translate business language into an analytical or ML problem | Formal problem statement |
| Success criteria | Define measurable business and model-level success | KPIs, acceptance thresholds |
| Data mining goals | Specify modeling type (e.g. classification, forecasting) and constraints | Technical goal doc |
| Project plan | Resources, timeline, data access, ethics/compliance checkpoints | Plan with milestones |

### Data Understanding

| Sub-task | What to do | Output |
|----------|------------|--------|
| Initial collection | Acquire or catalog sources; document lineage where possible | Inventory, access agreements |
| EDA | Univariate/multivariate summaries; visualizations; segment checks | EDA notebook or report |
| Data quality | Missingness, duplicates, outliers, label noise | Quality scorecard |
| Early insights | Hypotheses that inform preparation and modeling | Short insight memo |

### Data Preparation

| Sub-task | What to do | Output |
|----------|------------|--------|
| Selection | Choose rows, columns, time windows aligned to the target | Subset definitions |
| Cleaning | Imputation, deduplication, outlier handling (with rationale) | Cleaning rules |
| Feature construction | Aggregations, ratios, encodings, domain features | Feature definitions |
| Integration | Joins across sources; consistent keys and grain | Integrated tables |
| Formatting | Types, schemas, splits compatible with modeling tools | Model-ready datasets |

### Modeling

| Sub-task | What to do | Output |
|----------|------------|--------|
| Technique selection | Match algorithms to data size, interpretability, latency | Shortlist with rationale |
| Train/test split | Respect leakage rules (time, groups, stratification) | Split protocol |
| Hyperparameter tuning | Search strategy; validation discipline | Tuned configs |
| Model building | Train final candidates; track seeds and code versions | Model artifacts + metadata |

### Evaluation

| Sub-task | What to do | Output |
|----------|------------|--------|
| Business criteria check | Compare metrics to thresholds from Business Understanding | Pass/fail vs criteria |
| Model review | Error analysis, robustness spot checks, fairness slices | Review notes |
| Deployment decision | Go, iterate, or stop — with documented trade-offs | Decision record |

### Deployment

| Sub-task | What to do | Output |
|----------|------------|--------|
| Deployment plan | Rollout, rollback, ownership | Runbook |
| Monitoring | Data drift, performance, latency, business KPIs | Dashboards, alerts |
| Maintenance | Retrain triggers, data refresh, dependency updates | Ops checklist |
| Final report | Lessons learned, limitations, handover | Closing documentation |

---

## CRISP-DM vs other methodologies

| Dimension | **CRISP-DM** | **TDSP** (Microsoft) | **SEMMA** (SAS) | **KDD Process** |
|-----------|--------------|----------------------|-----------------|-----------------|
| Origin / style | Cross-industry standard; phase-oriented | Team roles, agile sprints, code structure | Sample, Explore, Modify, Model, Assess | Research-oriented knowledge discovery |
| Business linkage | Strong explicit phase | Strong (business metrics, backlog) | Weaker; more data-centric | Strong on problem understanding |
| Iteration | Core to the model | Agile loops + phases | Implicit in Assess | Multiple loops |
| Typical audience | General analytics / ML | Enterprise Azure/data teams | SAS-centric shops | Academia / R&D framing |

Use CRISP-DM when you want a **neutral, widely recognized** scaffold; pair it with **MLOps** when production automation is required (see [`mlops.md`](mlops.md)).

---

## CRISP-DM mapped to SDLC (high level)

Generic SDLC letters **A–F** here mean: **A** charter/requirements, **B** design, **C** build/integrate, **D** implementation detail, **E** test/verify, **F** release/operate — adjust to your org’s naming.

```blueprint-diagram
key: swimlane
alt: Diagram
```

- **Business Understanding** → **A/B** (intent, scope, success definition).
- **Data Understanding + Data Preparation** → **C/D** (data products, pipelines, integration).
- **Modeling** → **D** (training code, experiments).
- **Evaluation** → **E** (verification against criteria).
- **Deployment** → **F** (release, monitoring, operations).

---

## Adapting CRISP-DM for modern ML

- **Deep learning:** Modeling and Evaluation expand — longer training cycles, more hardware dependency, and need for **baseline + ablation** discipline. Data Preparation often includes **large-scale labeling** and augmentation policies.
- **MLOps:** Deployment is not a one-time step; it includes **pipelines, registries, and continuous monitoring**. Feedback loops are automated (retrain triggers) rather than only manual project reviews.
- **Feature stores and real-time serving:** Data Preparation and Deployment overlap with **online/offline feature consistency** and **point-in-time** correctness — classic CRISP-DM documents assumed batch analytics unless you extend them explicitly.

---

## Anti-patterns

| Anti-pattern | Why it hurts | Better habit |
|--------------|--------------|--------------|
| Skipping Business Understanding | Optimizes the wrong metric; shelf-ware models | Lock success criteria before heavy modeling |
| Data leakage in preparation | Inflated offline metrics; production failure | Time-safe splits, group splits, pipeline encapsulation |
| Single evaluation metric | Hidden failure modes (e.g. good AUC, bad recall on minority) | Multi-metric dashboards + slice analysis |
| Treating Deployment as “IT handoff” | No monitoring owner; silent drift | Shared SLOs and runbooks from day one |

---

## External references

- CRISP-DM 1.0 — IBM / SPSS consortium process model (widely cited standard document).
- Witten, Frank, Hall, and Pal — *Data Mining: Practical Machine Learning Tools and Techniques* — practical grounding for phases and evaluation.

*Keep project-specific model documentation in docs/product/ and experiment logs in docs/development/, not in this file.*
