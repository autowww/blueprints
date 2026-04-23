---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F3
hat: Challenge
---

# Charge — F3 / scenario verification across setup profiles

**Pack:** [branching](README.md) · **Profile switches:** [README — profile switches](README.md#profile-switches) · **Next:** [Charge 08](charge-08-rollout-and-assay.md)

Stress-test the branching model against the setups most likely to expose hidden assumptions.

## Branch context

- **Primary integration lane:** `iter/F3-PS-BRANCH-01`
- Use dedicated verification branches where the scenario write-up or test harness could destabilize the main F3 lane
- The goal is evidence, not more policy invention

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E3S1T1 | `verify:` | Run the solo plus PoC scenario and confirm the policy collapses gracefully without forcing unnecessary branch types. | `spark/M2E3S1T1-solo-poc-scenario` | `planned` |
| 2 | M2E3S1T2 | `verify:` | Run the small-team MVP scenario and confirm the iteration plus conditional Spark branch model works cleanly. | `spark/M2E3S1T2-small-team-mvp-scenario` | `planned` |
| 3 | M2E3S1T3 | `verify:` | Run the multi-team or polyrepo scenario and confirm the parent, iteration, Spark, and hotfix rules still compose. | `spark/M2E3S1T3-multi-team-polyrepo-scenario` | `planned` |
| 4 | M2E3S1T4 | `specify:` | Capture gaps, false complexity, and rules to bank for later instead of forcing them into this Product Spark. | `iter/F3-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Run each scenario against the same core policy and only add a rule if a real failure appears.
2. Prefer banking non-essential complexity over expanding the branch taxonomy.
3. Capture scenario evidence in a compact matrix that can be reviewed later.
4. Prompt for Challenge or Governance review if a scenario requires bypassing earlier policy decisions.

## Expected outputs

- `docs/process/branching-scenario-matrix.md`
- one list of validated rules and one list of banked enhancements
- evidence that the policy scales down as well as up

## Exit criteria

- at least three setup profiles have been tested conceptually or in a sample repo
- false complexity has been removed or banked
- the remaining rules still fit Forge instead of replacing it

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- If the project only needs one setup profile right now, still run at least one stress scenario at a different scale to expose hidden assumptions.

## Related

- [VERSONA-VERIFICATION.md](../../VERSONA-VERIFICATION.md) (broader Forge + Cursor verification)
- [Charge 06](charge-06-multi-repo-banking-hotfix.md) (bank, hotfix, multi-repo)
