---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F1
hat: Architecture
---

# Charge — F1 / Forge-to-Git mapping and exceptions

**Pack:** [branching](README.md) · **Baseline:** [BRANCHING-STRATEGY.md](../../BRANCHING-STRATEGY.md) · **Spark ≠ branch:** [principles](../../BRANCHING-STRATEGY.md#principles)

Map Forge planning and execution objects to Git objects or non-objects, with special attention to Sparks, Charge, and exploration spikes.

## Branch context

- Stay on `iter/F1-PS-BRANCH-01`
- Only open a `spike/*` branch if a real unknown appears; do not use spike branches for normal delivery design work
- This Charge defines what each Forge noun means in Git

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E1S2T1 | `specify:` | Map Ore, Ingot, Product Spark, Forge iteration, Forge Spark, Charge, Bank, Review, and Assay Gate to Git objects or explicit non-objects. | `iter/F1-PS-BRANCH-01` | `planned` |
| 2 | M2E1S2T2 | `specify:` | Define phase-sensitive branch heuristics for `discover:`, `specify:`, `design:`, `build:`, `verify:`, and `release:` Sparks. | `iter/F1-PS-BRANCH-01` | `planned` |
| 3 | M2E1S2T3 | `design:` | Define how exploration spikes differ from delivery Sparks, including when `spike/*` branches or worktrees are allowed and when force-push is acceptable. | `iter/F1-PS-BRANCH-01` | `planned` |
| 4 | M2E1S2T4 | `design:` | Define bank and resume behavior, including restart context, minimum checkpoint expectations, and when an Ember Log entry is mandatory. | `iter/F1-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Keep all work on the iteration branch unless a genuine unknown forces an exploration spike.
2. Write the branch heuristics so that `build:` and `verify:` are usually branchable, while `discover:` and `specify:` are usually not.
3. Make the Banking rules explicit enough that Cursor can bank and resume work without inventing new workflow objects.
4. Prompt for Architecture and Governance review if the mapping creates new protected branch types.

## Expected outputs

- `docs/process/forge-git-mapping.md`
- phase-specific Spark branching heuristics
- bank and resume rules with restart-context guidance

## Exit criteria

- Charge is explicitly treated as a daily view, not a branch
- every official Forge object in scope has a Git interpretation or explicit non-Git interpretation
- spike handling is separate from delivery Spark handling

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- Use the Ember Log for non-trivial branch decisions, policy exceptions, and any risk accepted during this Charge.
- Exploration spikes (discipline spikes): [DISCIPLINE-SPIKE.md](../../../versona/DISCIPLINE-SPIKE.md). WBS / commit ids: [`TRACKING-FOUNDATION.md`](../../../../../templates/sdlc/TRACKING-FOUNDATION.md).

## Related

- [Naming reference](../../../NAMING-REFERENCE.md)
- [Charge template](../../../daily/charge.template.md)
- [Submodules and multi-repo workspaces](../../BRANCHING-STRATEGY.md#submodules-and-multi-repo-workspaces)
