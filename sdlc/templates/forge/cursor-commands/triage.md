---
description: Estimate the t-shirt size and cost of the request, and propose an orchestration/model-tiering strategy before executing.
---

Triage the request that follows before doing any work:

1. Emit the `forge-triage.mdc` size line: `Triage: <XS|S|M|L|XL> (~<token order>) · <rationale>`.
2. State the signals that drove the estimate (files touched, search breadth, generation volume, loop count).
3. Apply the gate:
   - XS / S — say you'll execute directly, no strategy step.
   - M — give a one-sentence approach.
   - L / XL — only if `est(strategy) ≲ 10% of est(execution)`, propose a phased strategy: which subagents/models per phase, what to delegate to the cheap tier (`grunt` / Explore / Bash) vs keep on the high-tier orchestrator.
4. Wait for my go-ahead before executing (or I may say "just do it").

Reference: `forge-planning-standards.mdc` (t-shirt rubric + model tiering).

<!-- Install: copy into a consuming repo at `.cursor/commands/triage.md` (manual). -->
