# Triage + planning effectiveness test

An **isolated, iteratable** harness to check whether `forge-triage.mdc` and `forge-planning-standards.mdc` actually change agent behavior, and to improve them via a PDCA loop. No general rule-testing harness exists in Cursor, so this is a prompt-pack pattern (borrowed from the Cockpit `.cursor-packs/` PDCA convention): a fixed test prompt, a scoring rubric, and a run protocol.

## Files

- [`test-prompt.md`](test-prompt.md) — two synthetic requests (one L-sized feature, one S-sized change) fed to the agent in a clean chat.
- [`rubric.md`](rubric.md) — the scored checklist and pass/fail acceptance gate.

## Why "in isolation"

Effectiveness must be **attributable to the rules**, so measure the same prompt **rules-on vs rules-off**. If both look the same, the rules are not doing work; if rules-on scores higher against the rubric, the delta is the rules' contribution.

## Run protocol

1. **Rules-off baseline.** Temporarily remove the two rules from context (rename `forge-triage.mdc` and `forge-planning-standards.mdc` to `*.mdc.off`, or run in a scratch repo without them). Open a **new chat** to avoid carryover context. Paste Scenario A, then Scenario B from `test-prompt.md`. Save the transcript.
2. **Rules-on run.** Restore the rules. Open a **new chat**. Paste the same scenarios. Save the transcript.
3. **Score both** transcripts against `rubric.md`. Do this with a fresh evaluator (a subagent with a narrow output contract works well: "score this transcript against this rubric, return the table + total"). Keep the evaluator separate from the agent that produced the transcript.
4. **Gate.** Rules-on must meet the acceptance gate in `rubric.md` and beat rules-off by the stated margin.

## PDCA improvement loop

If the gate fails or the delta is small:

1. **Plan** — identify which rubric rows failed (e.g. no triage line, plan missing the drift-prevention section).
2. **Do** — refine the wording of the specific rule that owns that behavior (be surgical; keep the always-apply `forge-triage.mdc` lean).
3. **Check** — re-run steps 2-3 above (rules-on) and re-score.
4. **Act** — when the gate passes, record the before/after scores in the effectiveness table of `COST-AWARE-PLANNING-AND-MODEL-TIERING.md`, and sync the refined rule to consumers with `--with-cost-tiering-rules --force`.

## Notes

- Sizing is heuristic; the rubric checks that a size **and rationale** are emitted and are *plausible*, not that a specific number is hit.
- Keep the test prompt fixed across runs so scores are comparable over time. Version any prompt change alongside the rule change that motivated it.
