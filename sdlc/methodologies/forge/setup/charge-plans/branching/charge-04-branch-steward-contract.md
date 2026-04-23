---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F2
hat: Engineering
---

# Charge — F2 / Branch Steward contract and decision tree

**Pack:** [branching](README.md) · **Preamble:** [CURSOR-PREAMBLE.md](CURSOR-PREAMBLE.md) · **Next:** [Charge 05](charge-05-cursor-rule-and-git-actions.md)

Define the workflow persona that turns Charge state into Git actions inside Cursor.

## Branch context

- Open or confirm `iter/F2-PS-BRANCH-01`
- Parent branch remains `product/PS-BRANCH-01-forge-branching-orchestration` only if the policy enabled it
- This Charge defines the agent behavior before you build the Cursor rule

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E2S1T1 | `specify:` | Define Branch Steward inputs, outputs, session location, and supported verbs such as `open-iteration`, `start-spark`, `bank-spark`, `resume-spark`, `prepare-review`, and `backmerge-hotfix`. | `iter/F2-PS-BRANCH-01` | `planned` |
| 2 | M2E2S1T2 | `design:` | Create the decision tree for when a Spark stays on `iter/*` versus when it opens a dedicated `spark/*` branch. | `iter/F2-PS-BRANCH-01` | `planned` |
| 3 | M2E2S1T3 | `design:` | Define how `forge/charge.md` will reference branch and worktree state without becoming a parallel tracker or a new branch class. | `iter/F2-PS-BRANCH-01` | `planned` |
| 4 | M2E2S1T4 | `specify:` | Define mandatory Ember Log triggers for branch creation, banking, merge exceptions, hotfixes, and policy overrides. | `iter/F2-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Create or check out the F2 iteration branch from the policy-approved parent layer.
2. Write the decision tree so Cursor can choose the lane without asking the user on every Spark.
3. Keep Charge lightweight: it may point to a branch or worktree, but it must not duplicate Git history or issue tracking.
4. Prompt for Engineering review if the contract would let the agent rewrite protected history.

## Expected outputs

- `forge/personas/branch-steward.md` or `.cursor/rules/branch-steward-contract.md`
- a decision tree for Spark branch creation
- a minimal charge annotation convention for branch or worktree references

## Exit criteria

- the Branch Steward role is concrete enough to implement
- the Spark lane decision tree is deterministic enough for Cursor
- Ember Log triggers are explicit

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

- [Daily README](../../../daily/README.md) · [Charge template](../../../daily/charge.template.md)
- [Forge-to-Git mapping](charge-02-forge-to-git-mapping.md) (bank and spike rules)
- [Roles](../../../roles.md) (if the repo maps hats to roles)
