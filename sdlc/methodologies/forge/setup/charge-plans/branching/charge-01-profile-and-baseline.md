---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F1
hat: Product
---

# Charge — F1 / setup profile and branching baseline

**Pack:** [branching](README.md) · **Baseline:** [BRANCHING-STRATEGY.md](../../BRANCHING-STRATEGY.md)

Freeze the setup answers that materially change branch behavior and seed the first version of the branching policy.

## Branch context

- **Product Spark:** `PS-BRANCH-01`
- **Preferred parent branch:** `product/PS-BRANCH-01-forge-branching-orchestration` only if the work spans multiple iterations, repos, or a protected pre-main integration lane is needed
- **Working branch for this Charge:** `iter/F1-PS-BRANCH-01`
- **Non-negotiable:** no `charge/*` branches

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E1S1T1 | `discover:` | Answer the Forge setup profile questions that change branching: team size, product stage, iteration length, ceremony weight, CI/CD maturity, AI comfort, and repo topology. Record defaults where the project has not answered yet. | `iter/F1-PS-BRANCH-01` | `planned` |
| 2 | M2E1S1T2 | `specify:` | Decide whether this Product Spark needs a parent integration branch or whether iteration branches can merge directly to `main`. | `iter/F1-PS-BRANCH-01` | `planned` |
| 3 | M2E1S1T3 | `specify:` | Freeze the branch namespace and naming rules for `product/*`, `iter/*`, `spark/*`, `spike/*`, `release/*`, and `hotfix/*`. | `iter/F1-PS-BRANCH-01` | `planned` |
| 4 | M2E1S1T4 | `design:` | Seed `forge/branching.yml` or an equivalent policy doc with the chosen profile, branch prefixes, merge defaults, and the rule that Charge is a view only. | `iter/F1-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Inspect the repo and decide whether it is single-repo, monorepo, polyrepo, or submodule-based. If unknown, stop and run [optional spikes — Spike A](optional-spikes.md) first.
2. Create or check out `iter/F1-PS-BRANCH-01` from `main`, or from `product/PS-BRANCH-01-forge-branching-orchestration` if the parent branch is justified.
3. Record the chosen setup profile inside the policy artifact so later Charges do not keep re-deciding it.
4. Prompt for an Ember Log entry if the team chooses a heavier branch policy than the setup profile would normally suggest.

## Expected outputs

- `forge/branching.yml` or `docs/process/branching-profile.md`
- one explicit decision on whether the Product Spark parent branch is enabled
- one explicit naming convention for all branch classes

## Exit criteria

- the setup profile is frozen for this initiative
- the first iteration branch is known
- the branch namespace is stable enough for implementation Charges

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- If the repo is solo plus PoC, this Charge may also cover the mapping work from [Charge 02](charge-02-forge-to-git-mapping.md).
- Defaults when the project has not decided yet: [pack README — default assumptions](README.md#default-assumptions). Questions: [`QUESTIONNAIRE.md`](../../QUESTIONNAIRE.md). Scale row: [Branching by scaling tier](../../BRANCHING-STRATEGY.md#branching-by-scaling-tier).

## Related

- [`forge.config.template.yaml`](../../forge.config.template.yaml)
- [Work unit hierarchy](../../../process-and-flows.md#2-work-unit-hierarchy)
