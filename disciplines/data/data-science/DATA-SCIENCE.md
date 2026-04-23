---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Data science & machine learning body of knowledge

This document maps the core concerns of **data science** — the ML lifecycle, statistical foundations, model evaluation, MLOps, and responsible AI — to the blueprint ecosystem.

**How data science relates to PDLC and SDLC:** Data science is a **cross-cutting discipline** that provides predictive and analytical capabilities to both lifecycles. See [`DS-SDLC-PDLC-BRIDGE.md`](DS-SDLC-PDLC-BRIDGE.md) for the full mapping.

**Approaches:** Methodological approaches (CRISP-DM, MLOps, experiment management) are in [`approaches/`](approaches/README.md).

**Techniques:** ML technique catalog is in [`techniques/`](techniques/README.md).

---

## 1. ML lifecycle (CRISP-DM aligned)

The machine learning lifecycle follows iterative phases, aligned with CRISP-DM:

```blueprint-diagram
key: linear
alt: Diagram
```

| Phase | Activities | Outputs |
|-------|-----------|---------|
| **Business understanding** | Define business objective; translate to ML problem; define success criteria | Problem statement, success metrics, feasibility assessment |
| **Data understanding** | Explore available data; assess quality; identify gaps; initial statistics | Data inventory, EDA report, data quality assessment |
| **Data preparation** | Feature engineering; cleaning; transformation; train/test split; labeling | Feature store entries, prepared datasets, transformation pipelines |
| **Modeling** | Algorithm selection; hyperparameter tuning; training; experiment tracking | Trained models, experiment logs, model comparison |
| **Evaluation** | Offline evaluation against success criteria; fairness checks; error analysis | Evaluation report, model card, go/no-go recommendation |
| **Deployment** | Model serving; A/B testing; monitoring; automated retraining triggers | Deployed model, serving infrastructure, monitoring dashboards |

---

## 2. Statistical foundations

| Concept | Why it matters for ML |
|---------|----------------------|
| **Hypothesis testing** | Validating that model improvements are statistically significant, not noise |
| **Confidence intervals** | Quantifying uncertainty in model predictions and metric estimates |
| **Bias-variance trade-off** | Understanding model complexity — underfitting (high bias) vs overfitting (high variance) |
| **Cross-validation** | Robust model evaluation that avoids overly optimistic estimates from a single train/test split |
| **Causal inference** | Distinguishing correlation from causation — critical for feature selection and business decisions |
| **Bayesian reasoning** | Updating beliefs with evidence; useful for A/B test analysis and uncertainty quantification |
| **Sampling and distributions** | Understanding data characteristics; detecting distribution shift in production |

---

## 3. Model evaluation

### Metric selection by problem type

| Problem type | Primary metrics | Secondary metrics |
|-------------|----------------|-------------------|
| **Classification (binary)** | AUC-ROC, precision, recall, F1-score | Accuracy, log loss, calibration |
| **Classification (multi-class)** | Macro/micro F1, top-k accuracy | Confusion matrix, per-class precision/recall |
| **Regression** | RMSE, MAE, R² | MAPE, residual analysis |
| **Ranking** | NDCG, MAP, MRR | Precision@k, recall@k |
| **Clustering** | Silhouette score, adjusted Rand index | Cluster purity, within-cluster variance |
| **Generative (text)** | BLEU, ROUGE, human evaluation | Perplexity, factual accuracy, toxicity |
| **Anomaly detection** | Precision, recall at threshold, AUC-PR | False positive rate, detection latency |

### Evaluation beyond accuracy

| Dimension | What to check |
|-----------|---------------|
| **Fairness** | Performance across demographic groups; disparate impact analysis |
| **Robustness** | Behavior on edge cases, adversarial inputs, distribution shift |
| **Latency** | Inference time meets production SLA |
| **Resource cost** | Memory, compute, and storage requirements for serving |
| **Explainability** | Can predictions be explained to stakeholders? (SHAP, LIME, attention visualization) |

---

## 4. MLOps

MLOps extends DevOps for machine learning, addressing the unique challenges of ML systems:

### MLOps maturity levels (Google)

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **0 — Manual** | Manual, script-driven ML pipeline; no automation | Jupyter notebooks in production; manual model deployment; no monitoring |
| **1 — ML pipeline automation** | Automated training pipeline; manual deployment | Orchestrated training; experiment tracking; manual model registry |
| **2 — CI/CD pipeline automation** | Automated training and deployment; continuous training | Automated retraining on data changes; A/B testing; model monitoring |

### ML-specific CI/CD concerns

| Concern | Traditional CI/CD | ML CI/CD addition |
|---------|-------------------|--------------------|
| **Code versioning** | Git | + data versioning (DVC, Delta Lake) + model versioning |
| **Testing** | Unit, integration, E2E | + data validation + model performance tests + fairness tests |
| **Build artifacts** | Container images, packages | + trained models + feature transformations + model cards |
| **Deployment** | Application deployment | + model serving (batch, online, streaming) + shadow mode + champion/challenger |
| **Monitoring** | Application metrics | + prediction drift + data drift + model performance decay |

---

## 5. Responsible AI

| Principle | Description | Practices |
|-----------|-------------|-----------|
| **Fairness** | Models should not discriminate against protected groups | Fairness metrics; bias detection in training data; disparate impact testing |
| **Explainability** | Stakeholders should understand why a model made a prediction | SHAP, LIME, attention visualization; model cards; decision audit trails |
| **Privacy** | Models should not leak training data or enable re-identification | Differential privacy; federated learning; data anonymization |
| **Accountability** | Clear ownership of model decisions and their consequences | Model governance process; human-in-the-loop for high-stakes decisions |
| **Transparency** | Model capabilities, limitations, and intended use should be documented | Model cards; intended use documentation; known failure modes |
| **Safety** | Models should not cause harm; failure modes should be bounded | Guardrails; output filtering; graceful degradation; monitoring for harmful outputs |

---

## 6. Competencies

| Competency | Description |
|------------|-------------|
| **Statistical reasoning** | Hypothesis testing, experimental design, causal inference, uncertainty quantification |
| **ML engineering** | Algorithm selection, feature engineering, hyperparameter tuning, model architecture design |
| **Data wrangling** | Data cleaning, transformation, feature engineering, handling missing data and outliers |
| **Software engineering** | Writing production-quality ML code; testing; version control; code review |
| **Domain knowledge** | Understanding the business problem well enough to frame it as an ML problem and evaluate solutions |
| **Communication** | Explaining model behavior, limitations, and trade-offs to non-technical stakeholders |
| **Ethics** | Identifying and mitigating bias, fairness, and privacy risks |

---

## 7. External references

| Topic | URL | Why it is linked |
|-------|-----|------------------|
| CRISP-DM | https://www.datascience-pm.com/crisp-dm-2/ | Canonical ML project methodology |
| Google MLOps | https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning | MLOps maturity model and architecture patterns |
| Responsible AI Practices (Google) | https://ai.google/responsibility/responsible-ai-practices/ | Practical responsible AI guidance |
| Model Cards (Mitchell et al.) | https://arxiv.org/abs/1810.03993 | Framework for documenting ML model characteristics |
| Designing Machine Learning Systems (Huyen) | https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/ | End-to-end ML system design |
| Made With ML | https://madewithml.com/ | Practical MLOps tutorials and best practices |

---

*Keep project-specific ML documentation in `docs/architecture/` (model decisions) and `docs/product/` (ML feature descriptions), not in this file.*
