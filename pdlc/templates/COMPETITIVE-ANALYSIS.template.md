---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Competitive analysis — [Product / Initiative Name]

<!--
  Copy this template into docs/product/discovery/ (or equivalent).
  Complete during P1 Discover; update quarterly and before major launches (P4).
  See blueprints/pdlc/PDLC.md Phase P1 for context.
  See blueprints/disciplines/product/product-management/PRODUCT-MANAGEMENT.md §5 for guidance.
-->

## 1. Overview

| Field | Detail |
|-------|--------|
| **Product / initiative** | |
| **Market / category** | |
| **Analysis date** | YYYY-MM-DD |
| **Owner** | |
| **Review cadence** | Quarterly / Per-launch / Annual |

---

## 2. Competitor inventory

### Direct competitors

<!-- Solve the same problem for the same audience. -->

| Competitor | Description | Target segment | Pricing model | Est. market share | Funding / stage |
|-----------|-------------|----------------|---------------|-------------------|-----------------|
| | | | | | |
| | | | | | |

### Indirect competitors

<!-- Solve the same problem differently (spreadsheets, manual processes, different category). -->

| Competitor / alternative | How they solve it | Why customers choose them |
|--------------------------|-------------------|--------------------------|
| | | |
| | | |

### Potential competitors

<!-- Adjacent players who could enter (platform expansion, acqui-hires, large companies adding features). -->

| Potential entrant | Why they might enter | Timeline risk |
|-------------------|---------------------|---------------|
| | | |
| | | |

---

## 3. Feature comparison matrix

<!-- List the features that matter to your ICP. Score: ✅ Available, ⚠️ Partial, ❌ Missing, 🔜 Announced. -->

| Feature / capability | Our product | Competitor A | Competitor B | Competitor C |
|---------------------|-------------|-------------|-------------|-------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

## 4. Positioning map

<!-- Plot competitors on two axes that matter to your ICP.
     Examples: ease-of-use vs depth, price vs specialization, self-serve vs enterprise.
     Include a visual (ASCII, diagram-as-code, or image reference). -->

```blueprint-diagram
key: quadrant
alt: Competitive positioning quadrant sketch
title: Competitive positioning quadrant
summary: Plots competitors and our product on two ICP-critical axes to surface relative position and white space.
node: High [Axis Y]
detail: Upper bound of the vertical axis you define for your ICP.
more: Name the Y dimension in the axis table below—examples include depth, specialization, or enterprise readiness.
node: Competitor B
detail: Positioned high on the Y axis in this sketch.
more: Ground placement in the feature matrix and per-competitor assessment so the map stays reviewable.
node: ● Our product
detail: Marks where we intend to sit relative to named competitors.
more: Revisit this position quarterly and before major launches as evidence accumulates.
node: Competitor A
detail: Plotted lower on Y and left of center on X.
more: Cross-check against win/loss patterns and pricing comparison in later sections.
node: Low
detail: Lower bound of the vertical positioning axis.
more: Pair with the X-axis Low and High labels so both dimensions read clearly for stakeholders.
node: Low
detail: Left end of the horizontal axis scale.
more: Define what low means on the X dimension in the axis table—e.g., price, self-serve, or ease of use.
node: High
detail: Right end of the horizontal axis scale.
more: The X-axis label and white-space notes below explain why this end matters to buyers.
node: [Axis X]
detail: Names the horizontal dimension that segments competitors.
more: Choose axes that matter to your ICP; the section comment suggests ease versus depth or price versus specialization.
fallback_ascii: |
          High [Axis Y]
               │
               │    Competitor B
               │
               │         ● Our product
               │
               │  Competitor A
               │
          Low  ├──────────────────────
               Low                High
                     [Axis X]
```

| Axis | What it represents | Why it matters to ICP |
|------|-------------------|----------------------|
| **X** | | |
| **Y** | | |

**White space identified:** <!-- Underserved quadrants or positions -->

---

## 5. Pricing comparison

| Competitor | Pricing model | Entry price | Mid-tier | Enterprise | Free tier? |
|-----------|---------------|-------------|----------|-----------|------------|
| Our product | | | | | |
| Competitor A | | | | | |
| Competitor B | | | | | |

**Pricing strategy implications:** <!-- Are we competing on price, value, or differentiation? -->

---

## 6. Strengths, weaknesses, and differentiation

### Per-competitor assessment

#### Competitor A

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | |
| **Weaknesses** | |
| **Where we win against them** | |
| **Where they win against us** | |

#### Competitor B

| Dimension | Assessment |
|-----------|-----------|
| **Strengths** | |
| **Weaknesses** | |
| **Where we win against them** | |
| **Where they win against us** | |

### Our differentiation

| # | Differentiator | Why it matters | Evidence |
|---|---------------|----------------|----------|
| 1 | | | |
| 2 | | | |

---

## 7. Competitive moats

| Moat type | Our product | Strongest competitor |
|-----------|-------------|---------------------|
| **Network effects** | | |
| **Data advantages** | | |
| **Switching costs** | | |
| **Brand / trust** | | |
| **Economies of scale** | | |
| **Regulatory / IP** | | |

**Moat assessment:** <!-- How defensible is our position? What can we invest in to strengthen it? -->

---

## 8. Win/loss patterns

<!-- Populate from sales data, customer interviews, or churned customer analysis. Skip if pre-revenue. -->

| Pattern | Frequency | Root cause | Action |
|---------|-----------|-----------|--------|
| **We win when...** | | | |
| **We lose when...** | | | |
| **We lose to [competitor] because...** | | | |

---

## 9. Competitive risks

| # | Risk | Likelihood | Impact | Mitigation |
|---|------|-----------|--------|------------|
| 1 | | | | |
| 2 | | | | |

---

## 10. Strategic implications

<!-- What does this analysis mean for the product roadmap?
     - Features to build or not build
     - Segments to prioritize
     - Positioning changes needed
     - Moats to invest in
     - Pricing adjustments -->

---

*Last updated: YYYY-MM-DD · Owner: [name/role]*
