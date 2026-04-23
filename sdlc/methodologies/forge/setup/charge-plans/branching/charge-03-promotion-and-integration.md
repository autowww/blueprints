---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F1
hat: Governance
---

# Charge — F1 / promotion, parent integration, and protected flow

**Pack:** [branching](README.md) · **Baseline:** [BRANCHING-STRATEGY.md](../../BRANCHING-STRATEGY.md)

Define how work moves upward through the branch layers and how the policy changes by repo topology and CI maturity.

## Branch context

- **Primary working branch:** `iter/F1-PS-BRANCH-01`
- Tabletop the following promotion ladder: `spark/*` -> `iter/*` -> `product/*` or `main` -> `release/*` or `main`
- If the parent branch is disabled, document the direct `iter/*` -> `main` path

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E1S3T1 | `design:` | Define the promotion ladder for normal work, including Spark close, iteration review, Product Spark integration, and release promotion. | `iter/F1-PS-BRANCH-01` | `planned` |
| 2 | M2E1S3T2 | `design:` | Define how the policy differs for single repo, monorepo, polyrepo, and submodule setups. | `iter/F1-PS-BRANCH-01` | `planned` |
| 3 | M2E1S3T3 | `specify:` | Define protected branch, PR, and evidence rules by CI/CD maturity: none, basic, standard, advanced. | `iter/F1-PS-BRANCH-01` | `planned` |
| 4 | M2E1S3T4 | `verify:` | Tabletop one standard delivery flow and one hotfix plus back-merge flow. Capture gaps instead of improvising around them. | `iter/F1-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Write one happy-path merge flow and one emergency hotfix flow end to end.
2. If the repo is polyrepo or submodule-based, spell out where manifest or SHA updates happen and on which branch layer.
3. If CI maturity is low, replace automated gates with explicit human review checkpoints rather than leaving the rule ambiguous.
4. Prompt for Governance review if release or hotfix promotion can bypass normal checks.

## Expected outputs

- `docs/process/branch-promotion.md`
- `docs/process/branch-protection-matrix.md` or an equivalent section in the policy doc
- one documented hotfix and back-merge route

## Exit criteria

- promotion paths are defined for normal work and hotfixes
- parent and main integration rules are setup-aware
- protected branch expectations are explicit enough for implementation work

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- If [Spike B or Spike C](optional-spikes.md) was needed, fold its conclusions into this Charge before calling the policy done.

## Related

- [Ceremonies — Assay](../../../ceremonies-prescriptive.md) (release decision)
- [Branching by scaling tier](../../BRANCHING-STRATEGY.md#branching-by-scaling-tier)
- [CONTRIBUTING.md](../../../../../../CONTRIBUTING.md) (example Team-tier pattern for the blueprints repo)
