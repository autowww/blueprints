---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F2
hat: Engineering
---

# Charge — F2 / Cursor rule and Git action scaffolding

**Pack:** [branching](README.md) · **Preamble:** [CURSOR-PREAMBLE.md](CURSOR-PREAMBLE.md) · **Prior:** [Charge 04](charge-04-branch-steward-contract.md)

Implement the Branch Steward behavior in Cursor and add the minimum helper commands needed for day-to-day Git choreography.

## Branch context

- **Primary integration lane:** `iter/F2-PS-BRANCH-01`
- Use dedicated Spark branches for the implementation Sparks in this Charge
- Merge each completed Spark branch back into `iter/F2-PS-BRANCH-01` before starting the next risky implementation item

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E2S2T1 | `build:` | Create the Cursor rule or prompt template that combines forge-daily behavior with Branch Steward Git decisions. | `spark/M2E2S2T1-branch-steward-rule` | `planned` |
| 2 | M2E2S2T2 | `build:` | Create helper scripts or tasklets for `open-product-spark`, `open-iteration`, `start-spark`, `bank-spark`, `close-spark`, and `sync-parent`. | `spark/M2E2S2T2-branch-helper-actions` | `planned` |
| 3 | M2E2S2T3 | `build:` | Add example `forge/charge.md` annotations and any archive or helper notes needed so the rule can keep state without inventing a second tracker. | `spark/M2E2S2T3-charge-annotations` | `planned` |
| 4 | M2E2S2T4 | `verify:` | Dry-run the normal flow on a clean repo: open iteration, start Spark, close Spark, bank Spark, and resume Spark. | `spark/M2E2S2T4-dry-run-flow` | `planned` |

## Branch Steward in-time actions

1. Create each dedicated Spark branch from `iter/F2-PS-BRANCH-01`, not from `main`.
2. Merge the Spark branches back into the iteration branch as each unit stabilizes; do not let them drift unnecessarily.
3. Keep script behavior idempotent where possible so Cursor can re-run safe operations without damage.
4. Prompt for an Ember Log entry if the dry run exposes a rule gap or a surprising manual step.

## Expected outputs

- `.cursor/rules/branch-steward.mdc` or equivalent
- `scripts/` or `tasklets/` for the core Branch Steward verbs
- an example annotated Charge that Cursor can follow reliably

## Exit criteria

- Cursor can execute the core lane-management verbs
- the core implementation branches merge cleanly back into the iteration lane
- at least one dry run proves the contract is executable

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- If the project is solo and low-risk, you may collapse T2 and T3 onto the iteration branch, but keep T1 and T4 isolated if the rule is still unstable.

## Related

- [Branch Steward contract](charge-04-branch-steward-contract.md)
- [BRANCHING-STRATEGY.md — commit messages](../../BRANCHING-STRATEGY.md#commit-messages-subjects-body-trailers)
- [CURSOR-RULES-QUICKSTART.md](../../CURSOR-RULES-QUICKSTART.md) · [CURSOR-RULES-ALIGNMENT.md](../../CURSOR-RULES-ALIGNMENT.md)
- [Markdown canonical — AGENTS template](../../../../../templates/forge/cursor-rules/markdown-canonical/AGENTS.template.md)
