# Scoring rubric

Score each scenario independently. Each row is 0 (absent), 1 (partial), or 2 (fully present and correct). Record the transcript source (rules-on / rules-off) with each score.

## Scenario A — L-sized feature

| # | Criterion | 0 / 1 / 2 |
|---|---|---|
| A1 | A triage line is emitted with a size **and** a short rationale | |
| A2 | The size is plausible (L or XL for a cross-cutting migration) | |
| A3 | Plan has Goal & success criteria | |
| A4 | Plan surfaces clarifying questions / assumptions | |
| A5 | Plan lists affected surface / blast radius | |
| A6 | Plan is broken into phased, independently verifiable increments | |
| A7 | Plan states a test strategy per change (+ a negative check) | |
| A8 | Plan calls for dual wiki/docs updates | |
| A9 | Plan includes PDCA remediation loops with acceptance evidence | |
| A10 | Plan includes a drift-prevention / consistency gate | |
| A11 | Plan includes risks & rollback | |
| A12 | Model tiering is proposed (cheap tier for mechanical work, high-tier for reasoning) | |

**Scenario A max: 24.**

## Scenario B — S-sized change (over-planning is a failure)

| # | Criterion | 0 / 1 / 2 |
|---|---|---|
| B1 | A triage line is emitted with a size + rationale | |
| B2 | The size is plausible (XS or S) | |
| B3 | The agent says it will execute directly (no strategy subagent) | |
| B4 | The agent does **not** emit a heavyweight 10-section plan | |
| B5 | The agent does **not** spawn a strategy/planning pass for this small task | |

**Scenario B max: 10.** (B3-B5 test that the *gate* prevents over-investment — the expensive failure mode.)

## Acceptance gate

Rules-on passes when **all** of the following hold:

1. **Scenario A ≥ 20/24** and at least 8 of the 10 plan-structure rows (A3-A12) score 2.
2. **Scenario B ≥ 8/10**, with **B4 and B5 both = 2** (no over-planning, no wasted strategy pass).
3. **Delta:** rules-on total (A+B) beats rules-off total by **≥ 8 points**, confirming the behavior is attributable to the rules.

If the gate fails, follow the PDCA loop in [`README.md`](README.md): fix the rule that owns the failing rows, re-run rules-on, re-score.
