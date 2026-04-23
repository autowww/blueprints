---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
date: YYYY-MM-DD
iteration: F3
hat: Governance
---

# Charge — F3 / rollout, migration, and Assay preparation

**Pack:** [branching](README.md) · **Prior:** [Charge 07](charge-07-scenario-verification.md) · **Product Spark:** `PS-BRANCH-01`

Prepare the branching model for adoption inside ForgeSDLC and define the evidence needed to promote it to the default process.

## Branch context

- **Primary integration lane:** `iter/F3-PS-BRANCH-01`
- If your policy uses a release hardening branch, cut `release/PS-BRANCH-01-rc1` only after the F3 evidence is assembled
- This Charge is about release readiness and migration clarity

## Active Sparks

| # | Spark ID | Phase | Intent | Git lane | Status |
|---|----------|-------|--------|----------|--------|
| 1 | M2E3S2T1 | `release:` | Finalize the user-facing branching guide, setup-aware examples, and the summary of which Forge objects do or do not map to branches. | `iter/F3-PS-BRANCH-01` | `planned` |
| 2 | M2E3S2T2 | `release:` | Create a migration guide from any existing branch strategy to the Forge-native model, including what to stop doing. | `iter/F3-PS-BRANCH-01` | `planned` |
| 3 | M2E3S2T3 | `release:` | Prepare the operational handoff for Cursor use: how to start a Charge, bank work, resume work, run review, and handle hotfixes. | `iter/F3-PS-BRANCH-01` | `planned` |
| 4 | M2E3S2T4 | `release:` | Assemble the Assay evidence checklist and final promotion plan for merging the Product Spark into the chosen parent or `main`. | `iter/F3-PS-BRANCH-01` | `planned` |

## Branch Steward in-time actions

1. Assemble evidence first, then decide whether a `release/*` lane is needed for hardening.
2. Make the migration guide explicit about what old branch habits are retired by this policy.
3. Ensure the rollout notes explain how forge-daily and Branch Steward cooperate during a normal day.
4. Prompt for Governance sign-off before promoting the policy to the default branch strategy.

## Expected outputs

- final branching guide and migration guide
- Cursor operating notes for day-to-day use
- Assay evidence checklist and promotion plan

## Exit criteria

- users can adopt the model without guessing
- the evidence for promotion is explicit
- the policy is ready to merge into the project default path

## Blockers

| Spark | Blocker | Action |
|-------|---------|--------|
| | | |

## Banking decisions

| Spark | Reason banked | Restart context |
|-------|---------------|-----------------|
| | | |

## Notes

- If a release hardening branch is used, record why it exists and when it should be skipped. Do not let release branches become a permanent default unless the setup profile truly needs them.

## Related

- [Ceremonies — Assay](../../../ceremonies-prescriptive.md)
- [BRANCHING-STRATEGY.md](../../BRANCHING-STRATEGY.md) · [When to tighten or simplify](../../BRANCHING-STRATEGY.md#when-to-tighten-the-model-escalation)
- [CURSOR-PREAMBLE.md](CURSOR-PREAMBLE.md) · [Branching charge pack index](README.md)
- [forge.md — scaling model](../../../../forge.md#scaling-model)
