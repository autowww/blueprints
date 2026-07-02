---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Cost-aware planning and model tiering

Forge planning should raise final quality **and** control token cost without re-typing the same instructions each turn. This page defines the reusable pattern: a lean **triage** rule that sizes every request, a **planning-standards** rule that enforces detailed plans, and a **model-tiering** convention that reserves expensive models for reasoning while pushing token-heavy, low-judgment work to cheaper tiers.

Companion rules: [`forge-triage.mdc`](../../templates/forge/cursor-rules/forge-triage.mdc) and [`forge-planning-standards.mdc`](../../templates/forge/cursor-rules/forge-planning-standards.mdc). Install: see [`setup/CURSOR-RULES-QUICKSTART.md`](setup/CURSOR-RULES-QUICKSTART.md) (`--with-cost-tiering-rules`). Where these sit relative to Rules / AGENTS.md / Skills / subagents / recipes: [`VERSONA-OPERATING-MODEL.md`](VERSONA-OPERATING-MODEL.md) §3.

## Why

Cursor gives no pre-execution token meter (the context ring reports usage only afterward), and there is no way to scope a rule to Plan Mode alone. So the practical levers are: (1) rules that are in context during planning and shape plan output, (2) deliberate model selection, and (3) subagents that isolate token-heavy work on cheaper models. This pattern packages all three.

## 1. Triage every request

`forge-triage.mdc` (lean, always-apply) emits one compact line before non-trivial work:

```
Triage: <XS|S|M|L|XL> (~<rough token order>) · <1-3 word rationale>
```

The size is a **heuristic self-estimate** from visible signals (files touched, search breadth, generation volume, loop count), not a measured number. Calibrate against the context ring over time.

## 2. T-shirt sizing rubric

| Size | Signals | ~Token order | Triage depth | Model / orchestration response |
|---|---|---|---|---|
| **XS** | 1 file, direct answer, no search | <5k | none | current model, no subagents |
| **S** | 2-4 files, simple edit, narrow grep | 5-25k | 1-line header | Auto; Explore only if needed |
| **M** | multi-file feature, 1 repo, moderate reasoning | 25-100k | header + approach | Auto/mid main; Explore for search, Bash for runs |
| **L** | cross-cutting, iterative loops, or multi-repo | 100-400k | invest: strategy step | high-tier orchestrator + cheap subagents; plan before executing |
| **XL** | migration, many files, long multi-tier loops | >400k | invest + split | full tiered plan, checkpoints, split across sessions |

## 3. The gate (the key economic rule)

Strategy investment scales with size, so a trivial request never pays orchestration overhead:

1. **XS / S** — execute directly. Do **not** spawn a strategy subagent; triage stays inline.
2. **M** — one-sentence approach, then execute.
3. **L / XL** — invest a strategy step **only if** `est(strategy) ≲ 10% of est(execution)`. The strategy pass (cheap) returns which subagents/models per phase and what to delegate.

Recursion trap to avoid: a subagent that "decides the strategy" is itself a token cost. Keep triage an **inline heuristic** (a few tokens by the current model); only at L/XL is the task big enough to amortize a spawned strategy pass.

## 4. Model tiering

| Tier | Work | Model |
|---|---|---|
| Orchestrator (main) | planning, architecture, synthesis | high-tier or Auto |
| Search / read | codebase Q&A, "where is X" | built-in **Explore** (auto, faster model) |
| Scripts / shell | tests, builds, git | built-in **Bash** (auto) |
| Mechanical edits | rename, boilerplate, apply-a-pattern | cheap `grunt` subagent (`composer-2.5`) |

The `grunt` subagent template lives at [`cursor-agents/grunt.md`](../../templates/forge/cursor-agents/grunt.md); copy it into `.cursor/agents/` manually (like Skills).

### Cost math (so tiering actually saves money)

- Each subagent carries its own context window: **N parallel subagents ≈ N x tokens**. Savings come from a *cheap model* doing the bulk-token work in a **sequential** tier (grep/mechanical → report back → high-tier reasons), not from fan-out.
- On **legacy request-based plans**, a subagent's `model:` is ignored and it runs on Composer; **token-based plans** honor it.
- Prefer **Auto/Composer** for everyday turns (larger included allowance; Teams plans are exempt from the Cursor Token Rate). Reserve **Max Mode** for tasks that genuinely need the larger context — it bills at the model's full API rate.

### Fast-variant policy

Quality-first default: when the **agent** selects a model for a subagent or delegated Task, use the **standard** variant of a tier, not a speed-tier `*-fast` variant (e.g. `composer-2.5`, never `composer-2.5-fast`), unless the user explicitly asks for speed. If a `-fast` model would otherwise be the natural pick, flag it and use the standard variant.

Capability boundary: a rule is prompt context — it **cannot** override Cursor's model router. It only governs models the agent itself chooses (subagent `model:` fields, Task-tool model requests). The main-chat model remains the user's picker/Auto choice, which a rule cannot veto. So this policy is "don't *delegate* to fast variants," plus a reminder to the user, not a hard router block.

## 5. Testing rule effectiveness

Rules are prompts; treat their effectiveness as testable. The reusable, isolated harness lives beside the templates at [`cursor-rules/tests/triage-planning-effectiveness/`](../../templates/forge/cursor-rules/tests/triage-planning-effectiveness/README.md):

1. Run a synthetic request **rules-on vs rules-off** so measured behavior is attributable to the rules.
2. Score each transcript against a rubric (triage header present and correctly sized? plan has the required sections? model tiering proposed? gate respected?).
3. PDCA loop: run → score → refine rule wording on gaps → re-run → until the acceptance gate passes.

### Effectiveness results

Latest run of the isolated harness (rules-on vs rules-off), scored by a separate evaluator against [`rubric.md`](../../templates/forge/cursor-rules/tests/triage-planning-effectiveness/rubric.md):

| Scenario | Rules off | Rules on | Max | Notes |
|---|---|---|---|---|
| A — detailed plan (E2EE feature) | 8 | 23 | 24 | rules-off emitted no triage line, no PDCA/drift gate, no model tiering |
| B — small rename (S) | 6 | 10 | 10 | rules-off over-explained without sizing; rules-on gated correctly, no over-planning |
| **Total** | **14** | **33** | **34** | **delta +19** |

**Acceptance gate: PASS** (A ≥ 20 with 10/10 plan rows; B = 10 with the two anti-over-planning rows maxed; delta ≥ 8).

**PDCA action taken:** the first rules-on run sized Scenario A as `M` while acknowledging the feature was `L` (rubric row A2 = partial). `forge-triage.mdc` was refined to size the **underlying work, not just the current turn** ("just plan it" for a large feature is still L/XL). A follow-up check confirmed the triage line then read `L`, closing the gap.

## Relationship to other Forge planning docs

- **Product planning** (Business Driver → Product Spark → iterations) stays in [`planning/PLANNING-FLOW.md`](planning/PLANNING-FLOW.md) and `forge-planning.mdc`. This page is about **how any implementation plan is produced and sized**, not the product-planning hierarchy.
- **File token bands** for source analyzability are separate: `code-footprint.mdc` and [`../agentic-coding-standards.md`](../agentic-coding-standards.md).
- **Autonomous / bounded execution** (unattended loops, autonomy ladder, local-first routing): [`RESPECTING-RESOURCES.md`](RESPECTING-RESOURCES.md) and [`AUTONOMY-LEVELS.md`](AUTONOMY-LEVELS.md). For the autonomous counterpart to this interactive triage, see the [bounded execution examples](BOUNDED-EXECUTION-EXAMPLES.md) — real L1/L2 runs showing what each level spends.
