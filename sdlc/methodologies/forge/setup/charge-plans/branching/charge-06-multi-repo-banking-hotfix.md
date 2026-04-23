---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F2
hat: Architecture
---

# Charge — F2 / multi-repo, banking, and hotfix flows

**Pack:** [branching](README.md) · **Spikes:** [optional-spikes.md](optional-spikes.md) · **Promotion:** [Charge 03](charge-03-promotion-and-integration.md)

Extend the implementation to the hard cases: mirrored branch names across repos, banking and resume hygiene, and production hotfix back-merges.

## Branch context

- **Primary integration lane:** `iter/F2-PS-BRANCH-01`
- Open dedicated Spark branches for the implementation and verification work in this Charge
- If the repo is single-repo only, keep the multi-repo parts as documented examples rather than forced code

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E2S3T1 | `build:` | Define or implement mirrored Product Spark and iteration naming across child repos, submodules, or manifest-based assemblies. | `spark/M2E2S3T1-multi-repo-naming` | `planned` |
| 2 | M2E2S3T2 | `build:` | Implement or document the parent-to-child integration steps, including manifest updates or submodule SHA bumps as explicit work. | `spark/M2E2S3T2-parent-child-integration` | `planned` |
| 3 | M2E2S3T3 | `verify:` | Test bank and resume behavior on an interrupted Spark, including branch name retention, restart context, and optional worktree cleanup. | `spark/M2E2S3T3-bank-resume-test` | `planned` |
| 4 | M2E2S3T4 | `verify:` | Test a hotfix and back-merge path from production or release line into the active iteration and Product Spark lanes. | `spark/M2E2S3T4-hotfix-backmerge-test` | `planned` |

## Branch Steward in-time actions

1. Only implement multi-repo automation if the repo topology actually needs it; otherwise keep the examples and decision notes.
2. Treat submodule or manifest updates as first-class Sparks with evidence, not as invisible cleanup.
3. When testing banking, leave enough restart context that a future session can resume without re-discovery.
4. When testing hotfix flow, document exactly which branches receive the fix and in what order.

## Expected outputs

- multi-repo or submodule branching notes, helpers, or examples
- a bank and resume demonstration with restart context
- a documented hotfix and back-merge recipe

## Exit criteria

- the policy can handle interruption without branch chaos
- the policy can handle hotfixes without orphaning the active iteration
- multi-repo behavior is clear enough for the repo topology in play

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

## Related

- [Forge-to-Git mapping — bank and resume](charge-02-forge-to-git-mapping.md)
- [Submodules and multi-repo workspaces](../../BRANCHING-STRATEGY.md#submodules-and-multi-repo-workspaces)
- [Charge template — Banking](../../../daily/charge.template.md)
- [CONTRIBUTING.md](../../../../../../CONTRIBUTING.md) · [SETUP.md](../../../../../SETUP.md)
