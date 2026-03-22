# Data Science ↔ SDLC ↔ PDLC bridge

## Purpose

This document maps **data science and machine learning** practices to the two lifecycle frameworks:

- **PDLC** — "Are we building the **right product**?"
- **SDLC** — "Are we building the product **right**?"
- **Data Science** — "Can we **learn from data** to create value?"

Data science extends both lifecycles with predictive capabilities, experimental validation, and data-driven decision-making.

**Canonical sources:** [`DATA-SCIENCE.md`](DATA-SCIENCE.md) (this package) · [`PDLC.md`](../../../pdlc/PDLC.md) · [`SDLC.md`](../../../sdlc/SDLC.md).

---

## Document map

| Section | Contents |
|---------|----------|
| [Purpose](#purpose) | Why this bridge exists; how DS relates to PDLC and SDLC |
| [Comparison: Data Science, SDLC, and PDLC](#comparison-data-science-sdlc-and-pdlc) | Core questions, scope, ownership, metrics, artifacts, risks |
| [When one is missing](#when-one-is-missing) | Consequences of practicing one domain without the others |
| [Data science across the lifecycle](#data-science-across-the-lifecycle) | PDLC P1–P6 and SDLC A–F: roles, activities, outputs |
| [CRISP-DM ↔ SDLC mapping](#crisp-dm--sdlc-mapping) | Internal ML workflow vs delivery phases |
| [Role mapping](#role-mapping) | Who owns DS decisions; alignment with PDLC/SDLC roles and archetypes |
| [Artifact flow](#artifact-flow) | Handoffs DS → PDLC, DS → SDLC, and feedback loops |
| [Calibration](#calibration) | When to invest more or less in data science by initiative type |
| [Anti-patterns](#anti-patterns) | Common failures when the bridge is weak |
| [Worked example](#worked-example) | End-to-end ML capability from discovery through production monitoring |
| [Related reading](#related-reading) | Package and lifecycle references |

---

## Comparison: Data Science, SDLC, and PDLC

| Dimension | Data Science | SDLC | PDLC |
|-----------|--------------|------|------|
| **Core question** | Can we learn from data to create value (prediction, personalization, automation, insight)? | Are we building the product right (quality, feasibility, release readiness)? | Are we building the right product (desirability, viability, strategy)? |
| **Scope** | Problem framing, data, modeling, evaluation, deployment patterns, monitoring, responsible AI | Requirements through release: specify, design, build, verify, ship | Problem discovery through growth and sunset: validate, strategize, launch, evolve |
| **Primary owner** | Data scientist / ML engineer (often with research or analytics lead); MLOps for production path | Engineering / delivery team; QA; release management | Product manager / product trio; leadership at stage gates |
| **Timeline** | Experiment cycles and model iterations (days to weeks); retraining and drift cadence (ongoing) | Sprint / iteration / release train | Product lifetime (quarters to years) |
| **Success metric** | Predictive quality plus business lift (precision/recall, calibration, uplift), latency/cost SLAs, fairness and explainability targets | Defect rate, CI/CD health, DORA, on-time release, non-functional compliance | Adoption, retention, revenue, experiment win rate, strategic outcomes |
| **Key artifacts** | Problem statements, datasets and feature definitions, experiment tracking, model registry entries, model cards, evaluation reports, serving configs, monitoring dashboards | Specs, designs, code, tests, release notes, runbooks | Research synthesis, hypotheses, roadmap, launch metrics, growth dashboards |
| **Risk focus** | Data quality, leakage, drift, bias, opaque models, operational ML debt, vendor/model lock-in | Technical debt, security, performance, integration failures | Wrong problem, weak validation, misaligned incentives, sunsetting debt |
| **Failure mode** | Great models that nobody uses, or models that harm trust when they fail silently | Shipping fast without measurable product impact | Validated ideas that never become reliable, governed production systems |

---

## When one is missing

| Scenario | What happens |
|----------|----------------|
| **Data science without PDLC** | Technically sound models optimize the wrong objective — strong offline metrics, weak or negative product outcomes; no clear hypothesis or stage-gate for when ML is worth the cost |
| **Data science without SDLC** | Prototypes stall in notebooks; no path to testing, release, or operability — experiment tracking and model registry exist only informally |
| **PDLC without data science (when ML is material)** | Product bets rely on opinion or shallow analytics; missed personalization, ranking, or automation opportunities; late discovery that data cannot support the vision |
| **SDLC without data science (when ML is material)** | Engineering treats the model as a black-box binary artifact — weak contracts for features, latency, and monitoring; releases without A/B design or rollback strategy |
| **PDLC + SDLC without disciplined DS** | Features ship with ad hoc scoring rules or one-off models — no MLOps, no drift detection, no responsible-AI review |
| **All three practiced** | Hypotheses are tested with data; models are specified, built, verified, and released with governance; product metrics and model health co-evolve in P5 |

---

## Data science across the lifecycle

| Phase | Data science role | Key activities | Outputs |
|-------|-------------------|----------------|---------|
| **P1 Discover** | **Pattern finder** | Exploratory data analysis on existing data; identify ML opportunities; assess data availability | EDA reports, ML opportunity assessment |
| **P2 Validate** | **Hypothesis tester** | Build ML prototypes to validate product hypotheses; feasibility spikes for ML-powered features | Prototype models, feasibility assessment, data gap analysis |
| **P3 Strategize** | **ML strategist** | Define ML success metrics; estimate data/compute requirements; build-vs-buy for ML capabilities | ML requirements, resource estimates, vendor assessment |
| **A Discover** | **Problem framer** | Translate business requirements into ML problems; define features and labels; success criteria | ML problem definition, feature candidates, evaluation plan |
| **B Specify** | **Data specifier** | Specify training data requirements; define feature engineering pipeline; model performance SLA | Data specifications, feature definitions, model SLA |
| **C Design** | **Model architect** | Select model architecture; design training pipeline; plan experiment infrastructure | Model architecture, training pipeline design, experiment plan |
| **D Build** | **Model builder** | Feature engineering; model training; hyperparameter tuning; experiment tracking | Trained models, experiment logs, feature pipelines |
| **E Verify** | **Model evaluator** | Offline evaluation; fairness testing; A/B test design; model card creation | Evaluation report, model card, A/B test plan |
| **F Release** | **Model deployer** | Model serving deployment; shadow mode testing; champion/challenger setup | Deployed model, serving configuration, monitoring setup |
| **P4 Launch** | **Experiment runner** | Run A/B tests; measure model impact on product metrics | A/B test results, impact analysis |
| **P5 Grow** | **Model guardian** | Monitor model performance; detect drift; automated retraining; continuous improvement | Drift reports, retraining logs, model performance dashboards |
| **P6 Sunset** | **Model retirer** | Decommission models; archive artifacts; document lessons learned | Model retirement plan, archived model cards |

---

## CRISP-DM ↔ SDLC mapping

| CRISP-DM phase | SDLC phase(s) | Notes |
|----------------|----------------|-------|
| Business understanding | P1–P3, A | Maps to PDLC discovery and SDLC scope definition |
| Data understanding | A, B | Exploratory analysis informs requirements |
| Data preparation | B, C | Feature engineering is both specification and design |
| Modeling | D | Training is the ML equivalent of "build" |
| Evaluation | E | Offline evaluation is the ML equivalent of "verify" |
| Deployment | F | Model serving is the ML equivalent of "release" |

**Key difference from standard SDLC:** ML projects are more iterative within phases — modeling often loops back to data preparation multiple times before evaluation. The SDLC provides the governance envelope; CRISP-DM provides the internal ML workflow.

---

## Role mapping

### Across PDLC, SDLC, and data science

| Phase(s) | Data science focus | PDLC roles (typical) | SDLC roles (typical) | Archetype emphasis |
|----------|-------------------|----------------------|----------------------|-------------------|
| **P1–P2** | Opportunity scan, prototypes, feasibility | PM, UX research, analytics | — (upstream of delivery) | Demand & value |
| **P3** | ML strategy, resourcing, build-vs-buy | PM, leadership, GTM | Owner entering delivery | Demand & value; Steer & govern |
| **A** | ML problem framing, labels, evaluation plan | PM (intent), DS lead | Owner, architect (constraints) | Demand & value; Build & integrate |
| **B** | Data/feature specs, SLAs, contracts for inference | — | Implementer, data/platform | Build & integrate |
| **C** | Architecture of training/serving, experiment platform | — | Architect, MLOps, DS | Build & integrate |
| **D** | Training, feature pipelines, experiment tracking | — | Implementer, ML engineer | Build & integrate |
| **E** | Offline metrics, fairness, explainability, A/B design | — | QA, DS, security/compliance | Assure & ship |
| **F** | Deployment, shadow/champion-challenger, observability | — | Release, SRE, MLOps | Assure & ship; Flow & improvement |
| **P4** | Experiment execution, causal readouts | PM, GTM | — (downstream feedback) | Demand & value |
| **P5** | Drift monitoring, retraining, continuous experiments | PM, analytics | Owner (iteration), SRE | Demand & value; Flow & improvement |
| **P6** | Retirement, archival, lessons for future models | PM, exec sponsor | — | Steer & govern |

### Decision ownership (practical split)

| Decision | Primary owner | Collaborators |
|----------|---------------|---------------|
| Whether ML is appropriate for the bet | Product (PDLC) with DS input | Engineering (feasibility), compliance |
| Target metric and guardrails (fairness, latency) | Product + DS | Legal/privacy, SRE |
| Data access, PII, retention | Data governance / security | DS, platform |
| Model selection and hyperparameters | DS / ML lead | MLOps (operability), architect |
| Release go/no-go for model change | Engineering release + product | DS (evidence), QA |
| Production monitoring thresholds | MLOps / SRE | DS, product |

### Flow & improvement (ML operations)

The **Flow & improvement** archetype appears once models are in production: retros on model incidents, CI for training pipelines, latency and cost optimization, and standardized experiment templates. It is not a separate PDLC phase; it runs continuously across **F** and **P5**.

| Practice | Primary home | Typical owners |
|----------|--------------|----------------|
| Training pipeline CI and data validation gates | D–E (and recurring) | MLOps, DS, data platform |
| SLOs for inference latency and error budgets | F, P5 | SRE, MLOps, DS |
| Blameless postmortems after model incidents | P5, SDLC hardening | SRE, DS, product |
| Shared experiment templates and feature patterns | Cross-cutting | DS lead, MLOps |

---

## Artifact flow

### Data science → PDLC

| DS artifact | Destination (PDLC) | Usage |
|-------------|---------------------|-------|
| EDA and opportunity assessment | P1–P2 | Evidence for problem worth solving and data realism |
| Prototype results and data-gap analysis | P2 | Input to pivot/persevere decisions |
| ML requirements and cost estimates | P3 | Investment and roadmap decisions |
| A/B results and impact analysis | P4–P5 | Validates lift to product metrics; informs scaling or rollback |
| Drift and incident summaries | P5 | Triggers retraining, feature changes, or product UX adjustments |
| Retirement plan and archived model cards | P6 | Clean sunset; knowledge retention |

### Data science → SDLC

| DS artifact | Destination (SDLC) | Usage |
|-------------|---------------------|-------|
| ML problem definition, label schema, evaluation plan | A–B | Bases specs and acceptance criteria |
| Data and feature specifications | B | Contracts for pipelines and APIs |
| Training pipeline design, experiment plan | C | Shapes implementation and environments |
| Trained model artifacts, feature code, experiment logs | D–E | Build, regression, and audit trail |
| Model card, evaluation report, A/B protocol | E | Release gate and risk disclosure |
| Serving config, monitoring dashboards, runbooks | F | Operable release and on-call |

### Feedback loops

| Loop | Mechanism |
|------|-----------|
| **PDLC → DS** | New hypotheses and metric targets reshape labels, features, and success criteria (especially P2, P4, P5) |
| **SDLC → DS** | Production incidents, latency budgets, and schema changes force model and pipeline updates |
| **DS → DS (MLOps)** | Experiment tracking and model registry link training runs to deployed versions; champion/challenger and shadow deployments reduce release risk |

### PDLC and SDLC inputs back to data science

| Source | Typical artifact or signal | DS response |
|--------|----------------------------|-------------|
| **PDLC** | Updated success metrics, segment strategy, ethical red lines | Revisit labels, re-weight objectives, fairness analyses |
| **SDLC** | Schema migrations, API deprecation, infra cost pressure | Refactor features, change serving path, simplify model |
| **Assure & ship** | Pen-test findings, audit requests | Document lineage; restrict features; add monitoring |

---

## Calibration

| Initiative type | When to invest more in DS | When a lighter touch suffices |
|-------------------|---------------------------|-------------------------------|
| **ML-powered product** (core differentiator) | Dedicated DS/MLOps, feature store, strong offline + online evaluation, continuous retraining, formal model cards | — |
| **Analytics feature** (insights, recommendations in-app) | Clear product metrics, experiment design, dashboards for P5; guardrails for explainability where users see outputs | Reuse existing pipelines; limit custom modeling if lift is incremental |
| **Traditional SaaS** (ML optional) | Only after simpler rules/SQL fail a cost–benefit test | Prefer heuristics, reporting, and descriptive analytics until data volume and repeat decisions justify ML |
| **Experimentation platform** | Shared tooling for assignment, metrics, and power analysis; DS partners with PM on design | Centralize infra once; avoid one-off experiment code per feature |

Use **CRISP-DM iteration** deliberately: shallow loops early in P2 and A; deeper modeling investment only after product and data feasibility are credible.

### Signals to deepen or lighten investment

| Signal | Lean toward |
|--------|-------------|
| Decisions are high-volume, costly when wrong, and stable enough to learn from | More DS: personalization, ranking, fraud, routing |
| Outcomes depend on fast feedback loops and online experiments | More DS + platform: A/B infra, experiment tracking, sequential testing discipline |
| Data is sparse, biased, or cannot be labeled reliably | Less bespoke modeling until P1–P2 closes data gaps |
| Regulatory or reputational risk is high | More governance: model cards, explainability, human oversight hooks—may slow iteration deliberately |

---

## Anti-patterns

| Anti-pattern | Description | Fix |
|--------------|-------------|-----|
| **Notebook-to-production** | Jupyter notebooks deployed directly as production services | Refactor to production code; use ML frameworks; apply software engineering practices |
| **Accuracy tunnel vision** | Optimizing model accuracy while ignoring latency, fairness, cost, and maintainability | Define holistic success criteria (see [`DATA-SCIENCE.md`](DATA-SCIENCE.md) §3); model evaluation beyond accuracy |
| **Data leakage** | Training data inadvertently contains information from the future or test set | Strict train/test/validation splits; time-based splitting for temporal data; feature audit |
| **ML for everything** | Using ML when simpler solutions (rules, heuristics, SQL queries) would suffice | Start with the simplest solution; use ML only when it demonstrably outperforms simpler approaches |
| **Set and forget** | Deploying a model and never monitoring or retraining it | Model monitoring for drift; automated retraining triggers; performance decay alerting |
| **Shadow AI** | ML models developed and deployed without governance, documentation, or review | ML model registry; model cards; review process for production models |

---

## Worked example

**Scenario:** A B2B SaaS team adds a **churn-risk score** surfaced to Customer Success, with optional automated playbooks later.

| Stage | PDLC / SDLC | Data science in practice |
|-------|-------------|-------------------------|
| **P1** | Discover churn drivers in interviews and usage data | EDA on historical accounts; baseline churn rate; identify features (usage depth, support tickets, billing signals) |
| **P2** | Validate that early warning changes outcomes | Train a simple prototype classifier; measure precision/recall on backtest; confirm CS can act on top decile |
| **P3** | Decide build vs buy (vendor risk score vs internal) | Cost, latency, and data residency comparison; ML requirements and staffing |
| **A** | Frame prediction target (e.g., 30-day churn) and fairness constraints | Label definition; cohort rules; agreement on definitions with finance and CS |
| **B** | Specify data pipelines and SLA (score freshness, API latency) | Feature catalog entries; contract for missing data; model performance floor |
| **C** | Design batch vs online scoring, experiment hooks for future playbooks | Serving architecture; shadow scoring alongside rules |
| **D** | Build features, train model, track experiments | Experiment tracking; versioned datasets; registered candidate models |
| **E** | Offline evaluation + holdout; pilot A/B or before/after readout | Model card; fairness checks across segments; A/B plan if automating interventions |
| **F** | Deploy scoring job + API; feature flags | Champion/challenger or shadow; monitoring on score distribution and drift |
| **P4** | Launch to CS with training; measure retention and playbook usage | Compare treatment vs control groups where applicable |
| **P5** | Monitor calibration as product mix changes; schedule retrains | Drift alerts; refresh cadence tied to data velocity; feed learnings to roadmap |
| **P6** | If strategy shifts away from score, retire model and archive card | Document what worked; preserve lineage for compliance |

**Variant — home-page recommendations:** The same spine applies with heavier **P4–P5** emphasis. P1–P3 validate that recommendations move a north-star metric (engagement, revenue, diversity). **A–B** define impression/click logs, item metadata, and exploration/exploitation policy. **C–D** implement retrieval + ranking, **feature stores** for low-latency vectors, and **offline replay** or counterfactual estimates where live randomization is limited. **E** covers ranking metrics (nDCG, calibration), slice fairness, and **A/B** power. **F** ships shadow traffic and **champion/challenger**; **P5** tracks **model drift**, catalog shifts, and cold-start behavior, with **retraining** tied to data freshness.

| Stage | Emphasis for ranking / recsys |
|-------|------------------------------|
| **P2** | Offline prototype on historical logs; sanity-check coverage and popularity bias |
| **P3** | Capacity planning for near-real-time features; vendor vs in-house retrieval |
| **B–C** | Feature store contracts; latency budget per stage (retrieval vs ranker) |
| **E** | Holdout sets with temporal split; abuse and manipulation scenarios |
| **F** | Gradual ramp; kill switches; logging for attribution |
| **P5** | Drift in query/item distributions; periodic full retrains vs incremental updates |

---

## Related reading

| Doc | Why |
|-----|-----|
| [`DATA-SCIENCE.md`](DATA-SCIENCE.md) | ML lifecycle, statistics, evaluation, MLOps, responsible AI |
| [`approaches/README.md`](approaches/README.md) | CRISP-DM, MLOps, experiment management |
| [`techniques/README.md`](techniques/README.md) | ML technique catalog |
| [`SDLC.md`](../../../sdlc/SDLC.md) | Delivery phases A–F, DoD |
| [`PDLC.md`](../../../pdlc/PDLC.md) | Product phases P1–P6, metrics framework |
| [`blueprints/disciplines/data/bigdata/README.md`](../bigdata/README.md) | Data infrastructure that ML depends on |
