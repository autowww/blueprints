# Feature engineering & feature stores

**Purpose:** Project-agnostic reference for turning **raw data** into **model inputs** — encodings, scaling, temporal and text features, selection, and **feature store** architecture for train/serve consistency.

**Audience:** Teams following [`DATA-SCIENCE.md`](../DATA-SCIENCE.md) and [`techniques/README.md`](README.md). Pairs with [`model-evaluation.md`](model-evaluation.md) for validation discipline.

---

## Overview

Feature engineering is the **bridge** between domain data and learning algorithms. Good features compress signal, respect causality and leakage rules, and behave consistently in **training** and **serving**. Poor features waste capacity, invite leakage, or break silently when distributions shift.

```blueprint-diagram
key: linear
alt: Diagram
```

---

## Feature types and encoding strategies

| Type | Examples | Encoding / representation notes |
|------|----------|----------------------------------|
| **Numerical — continuous** | Price, temperature | Scaling often helps linear models; tree models may be less sensitive |
| **Numerical — discrete** | Count of events | Treat as count or bucket; watch heavy tails |
| **Categorical — nominal** | Country, SKU | One-hot, hashing, embeddings for high cardinality |
| **Categorical — ordinal** | Survey Likert (if truly ordered) | Integer with care, or ordered target encoding with leakage controls |
| **Temporal** | Timestamps | Lags, rolling stats, cyclical encodings |
| **Text** | Reviews, tickets | TF-IDF, embeddings, topic features |
| **Spatial** | Lat/long, polygons | Binning, distance-to-poi, geohash |
| **Image** | Pixels | CNN embeddings or handcrafted descriptors |

---

## Numerical feature techniques

| Technique | When to use | Impact / caveat |
|-----------|-------------|-----------------|
| **Min–max scaling** | Bounded inputs; neural nets sensitive to scale | Sensitive to outliers |
| **Standard scaling (z-score)** | Linear models, SVM, k-NN | Assumes roughly Gaussian-ish tails |
| **Robust scaling** | Outlier-heavy data | Uses median/IQR; more stable |
| **Binning** | Nonlinear effects; interpretability | Information loss; bin boundaries matter |
| **Log / power transforms** | Heavy-tailed positives | Handle zeros with log1p or offset |
| **Polynomial features** | Low-dimension interactions | Explodes dimensionality |
| **Interaction features** | Known multiplicative effects | Combine with regularization |

---

## Categorical encoding comparison

| Method | Cardinality handling | Information preservation | Leakage risk | Model compatibility |
|--------|----------------------|--------------------------|--------------|---------------------|
| **One-hot** | Poor for very high cardinality | High for low/medium | Low if fit on train only | Linear, NN, many trees |
| **Label / integer** | Scales | Arbitrary order risk | Low | Trees; risky for linear |
| **Target encoding** | Good | High signal | **High** if not nested CV / proper regularization | Gradient boosting, linear with care |
| **Frequency** | Good | Moderate | Lower than target | Trees, NN |
| **Binary / hashing** | Very high | Collision trade-off | Low | Linear, NN |
| **Embedding** | Very high | High in data-rich settings | Medium (train carefully) | NN, some two-stage pipelines |

---

## Temporal feature engineering

| Technique | Description | Typical use |
|-----------|-------------|-------------|
| **Lag features** | Value at t−k | Autoregressive patterns |
| **Rolling statistics** | Mean, std, min/max over window | Short-term trends, volatility |
| **Cyclical encoding** | sin/cos of hour, day-of-week | Seasonality without arbitrary ordering |
| **Time since event** | Days since last purchase | Recency signals |
| **Trend / seasonality decomposition** | STL, classical decomposition | Baseline features for forecasting |
| **Calendar features** | Holidays, business day flags | Regime changes |

Always enforce **temporal splits** and **point-in-time** feature availability when labels are forward-looking.

---

## Text feature techniques

| Approach | Idea | Trade-off |
|----------|------|-----------|
| **Bag-of-words** | Word counts per document | Simple; loses order |
| **TF-IDF** | Down-weight common terms | Strong baseline for linear models |
| **Word embeddings (Word2Vec, GloVe)** | Dense vectors from co-occurrence | Transfer limited context |
| **Sentence embeddings (BERT, sentence-transformers)** | Contextual vectors | Heavier compute; strong semantics |
| **Topic features (LDA, NMF)** | Soft cluster memberships | Interpretable topics; tuning needed |

---

## Feature selection methods

| Family | Method examples | Pros | Cons |
|--------|-----------------|------|------|
| **Filter** | Correlation, mutual information, chi-square | Fast; model-agnostic | Ignores feature interactions |
| **Wrapper** | Forward / backward / stepwise selection | Adapts to model | Expensive; risk of overfitting to validation |
| **Embedded** | Lasso, tree importance, SHAP-based pruning | Joint with training | Model-specific; may need stability checks |

---

## Feature store architecture

```blueprint-diagram
key: swimlane
alt: Diagram
```

- **Offline:** Historical backfills, training snapshots, analytics.
- **Online:** Serving path for live keys; must match **definitions** and **freshness** used in training.

---

## Feature store tools comparison

| Platform | Notable strengths | Deployment model | Cost considerations |
|----------|-------------------|------------------|---------------------|
| **Feast** | Open source; Kubernetes; multi-cloud | Self-hosted / vendor bundles | Ops overhead; infra costs |
| **Tecton** | Managed feature platform; streaming | SaaS / enterprise | Platform subscription |
| **Hopsworks** | Integrated FS + lakehouse patterns | Managed or self-hosted | Cluster sizing |
| **Databricks Feature Store** | Tight Unity Catalog / Delta integration | Databricks cloud | Databricks consumption |
| **Vertex AI Feature Store** | GCP-native serving | Google Cloud | GCP pricing model |

---

## Automated feature engineering

| Library | Capabilities | Limitations |
|---------|--------------|-------------|
| **Featuretools** | Deep Feature Synthesis for relational data | Can explode feature count; needs pruning |
| **tsfresh** | Many time-series statistics | Compute cost; correlation filtering advised |
| **autofeat** | Symbolic / polynomial feature expansion | Dimensionality; validation discipline required |

Use automation **with** domain constraints and **leakage-aware** validation — not as a black box.

---

## Anti-patterns

| Anti-pattern | Why it hurts |
|--------------|--------------|
| **Leakage via features** | Future information in training (e.g. aggregates including test rows) |
| **High-cardinality one-hot** | Sparse huge matrices; unstable generalization |
| **Ignoring feature drift** | Silent performance decay |
| **Train/serve skew** | Different imputation, encoding, or join logic in batch vs online |

---

## External references

- Zheng & Casari — *Feature Engineering for Machine Learning* — systematic patterns and pitfalls.
- [Feast documentation](https://docs.feast.dev/) — concepts for offline/online stores and registry.
- Kaggle feature engineering courses and notebooks — practical patterns (always validate for leakage).

*Keep project-specific model documentation in docs/product/ and experiment logs in docs/development/, not in this file.*
