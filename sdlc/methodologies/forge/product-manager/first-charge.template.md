---
date: YYYY-MM-DD
iteration: F1
hat: Product
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Charge — Product Bootstrap (F1)

This is a pre-defined first Charge for bootstrapping a new product. It contains discovery and specification Sparks that produce the foundational product artifacts. Adjust, reorder, or skip Sparks based on what already exists.

## Active Sparks

| # | Spark ID | Phase | Intent | Status |
|---|----------|-------|--------|--------|
| 1 | M1E1S1 | `discover:` | Define problem statement and target audience — produce or update VISION.md | `planned` |
| 2 | M1E1S2 | `discover:` | Conduct market analysis — produce MARKET-ANALYSIS.md (TAM/SAM/SOM, segmentation, dynamics) | `planned` |
| 3 | M1E1S3 | `discover:` | Map competitive landscape — produce COMPETITIVE-ANALYSIS.md (competitors, differentiation, moats) | `planned` |
| 4 | M1E2S1 | `specify:` | Draft business case — produce business-case.md (costs, benefits, risks, recommendation) | `planned` |
| 5 | M1E2S2 | `specify:` | Define product vision and success metrics — produce PRODUCT-VISION.md and PRODUCT-METRICS.md | `planned` |
| 6 | M1E2S3 | `specify:` | Create high-level roadmap — produce ROADMAP.md (NOW/NEXT/LATER themes) | `planned` |
| 7 | M1E3S1 | `specify:` | Decompose WBS — produce WBS.md (Themes → Epics → Stories → Tasks) | `planned` |
| 8 | M1E3S2 | `design:` | Define first Product Spark scope — select PoC/MVP/Phase approach, create plan, define Assay criteria | `planned` |

## Templates referenced

| Spark | Template source |
|-------|----------------|
| M1E1S1 | `blueprints/product/templates/VISION.template.md` or `blueprints/pdlc/templates/PRODUCT-VISION.template.md` |
| M1E1S2 | `blueprints/pdlc/templates/MARKET-ANALYSIS.template.md` |
| M1E1S3 | `blueprints/pdlc/templates/COMPETITIVE-ANALYSIS.template.md` |
| M1E2S1 | `blueprints/disciplines/product/ba/templates/business-case.template.md` |
| M1E2S2 | `blueprints/pdlc/templates/PRODUCT-VISION.template.md` + `blueprints/pdlc/templates/PRODUCT-METRICS.template.md` |
| M1E2S3 | `blueprints/sdlc/templates/ROADMAP.template.md` |
| M1E3S1 | `blueprints/pdlc/templates/WBS.template.md` |
| M1E3S2 | `blueprints/sdlc/methodologies/forge/planning/poc-plan.template.md` / `mvp-plan.template.md` / `phase-plan.template.md` |

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

<!-- This Charge is designed for a single-day or multi-day product bootstrap session.
     Work through Sparks sequentially (discover → specify → design).
     Hat: Product throughout. Switch to Challenge hat after completing each
     discovery Spark to invoke Product Management Versona for validation.
     After completing this Charge, transition to implementation Charges
     using the standard charge.template.md. -->