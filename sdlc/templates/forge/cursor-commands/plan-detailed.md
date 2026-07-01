---
description: Produce a detailed, cost-aware implementation plan (no code yet) using the Forge planning standards.
---

Produce a detailed implementation plan for the request that follows. Do **not** write code yet.

Follow the structure in `forge-planning-standards.mdc`:

1. Goal & success criteria (measurable).
2. Clarifying questions + assumptions ledger.
3. Affected surface (files/modules/contracts, blast radius; respect submodule read-only rules).
4. Phased breakdown — small, independently verifiable increments; one commit per increment.
5. Test strategy per change (unit / integration / e2e / regression) + a negative "what proves this wrong" check.
6. Dual wiki updates — in-repo docs AND handbook source.
7. Prompt-chains / sub-agents + Versona(s) per phase.
8. Remediation loops (PDCA) — acceptance evidence defined before each phase.
9. Drift prevention — final code ↔ tests ↔ docs consistency gate.
10. Risks & rollback.

Also emit the `forge-triage.mdc` size line first, and propose model tiering (cheap subagents for grep/scripts/mechanical, high-tier for reasoning). Bias toward incremental improvement loops that raise final quality.

<!-- Install: copy into a consuming repo at `.cursor/commands/plan-detailed.md` (manual). -->
