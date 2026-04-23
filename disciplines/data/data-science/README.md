---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Data science & machine learning

Reusable, **project-agnostic** blueprint for **data science and machine learning** — the discipline of extracting knowledge from data and building predictive or generative models that create value.

Data science answers **"how do we extract knowledge and build predictive models from data?"** — a question that bridges PDLC hypothesis validation (P2) with SDLC model engineering (Build/Verify) and production model management (Operate).

| Document | Purpose |
|----------|---------|
| [**DATA-SCIENCE.md**](DATA-SCIENCE.md) | ML lifecycle, statistical foundations, experiment design, model evaluation, responsible AI, competencies |
| [**DS-SDLC-PDLC-BRIDGE.md**](DS-SDLC-PDLC-BRIDGE.md) | How data science maps across SDLC phases A–F and PDLC phases P1–P6 — discovery, training, validation, monitoring |
| [**approaches/**](approaches/README.md) | Methodological approaches: CRISP-DM, MLOps maturity model, experiment management, A/B testing |
| [**techniques/**](techniques/README.md) | ML technique catalog: supervised, unsupervised, deep learning, NLP, computer vision, time series, recommender systems |

## Relationship to other packages

| Package | How Data Science relates |
|---------|--------------------------|
| [`blueprints/sdlc/`](../../../sdlc/README.md) | ML models are software artifacts — they go through SDLC phases (design, build, test, deploy). Model training happens in Build; validation in Verify; model serving in Release. ML adds unique concerns (data versioning, experiment tracking, model registry) that extend standard SDLC. |
| [`blueprints/pdlc/`](../../../pdlc/README.md) | PDLC P2 (Validate) may use ML prototypes for hypothesis testing. P5 (Grow) uses ML models for personalization, recommendation, and prediction. ML model performance metrics feed PDLC outcome measurement. |
| [`blueprints/disciplines/product/ba/`](../../product/ba/README.md) | BA defines the business problems that ML may solve. Business understanding (CRISP-DM phase 1) maps directly to BA Strategy Analysis. BA acceptance criteria may include model performance thresholds. |
| [`blueprints/disciplines/engineering/testing/`](../../engineering/testing/README.md) | ML models require specialized testing — data validation, model performance testing, fairness testing, adversarial testing. Traditional software testing (unit, integration) still applies to ML infrastructure code. |
| [`blueprints/disciplines/engineering/devops/`](../../engineering/devops/README.md) | MLOps extends DevOps for ML — CI/CD for models, model monitoring, automated retraining, model registry. |
| [`blueprints/disciplines/data/bigdata/`](../bigdata/README.md) | Data engineering provides the data infrastructure that data science depends on — feature stores, training data pipelines, data quality, and governance. |

## Scope

This package covers **data science as a discipline** — not just model training notebooks. It includes:

- **ML lifecycle** — problem framing, data understanding, feature engineering, model training, evaluation, deployment, monitoring
- **Statistical foundations** — hypothesis testing, experimental design, causal inference
- **Model evaluation** — metrics selection, cross-validation, bias-variance trade-off, model comparison
- **MLOps** — model versioning, experiment tracking, automated retraining, model serving, monitoring
- **Responsible AI** — fairness, explainability, privacy, bias detection, governance
- **Experiment management** — A/B testing, multi-armed bandits, online experimentation platforms

Reference bodies of knowledge: CRISP-DM, MLOps maturity model (Google), Responsible AI practices.

---

*Keep project-specific ML documentation in `docs/architecture/` (model architecture decisions) and `docs/product/` (ML feature descriptions), not in this file.*
