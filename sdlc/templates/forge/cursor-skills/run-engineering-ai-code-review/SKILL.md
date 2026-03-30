---
name: run-engineering-ai-code-review
description: >
  Run a Forge-aligned AI code review using Engineering-family Versonas: bound diff/PR
  scope, route SE / Security / Testing / Architecture as needed, emit §5-shaped output,
  optionally record a Versona session under forge-logs/.
---

# Run Engineering AI code review (Forge)

## When to use

- User asks for **AI code review**, **PR review**, **diff review**, **engineering Versona pass**, or **pre-merge quality check** on implementation.
- After **CI** (lint/tests) when a **discipline lens** on the change is still needed.

**Prescriptive norms:** [`agentic-coding-standards.md`](../../../methodologies/agentic-coding-standards.md) (blueprint).

## Steps

1. **Bound the review** — Confirm **Spark** / branch / pasted **unified diff**; note **SDLC phase** (A–F) and **risk** (auth, crypto, PII, secrets, concurrency → treat as high-risk).
2. **Route Versonas**
   - Default: **`versona-se`** (Software Engineering) for craft, readability, structure, complexity.
   - Add **`versona-security`** when the diff touches trust boundaries, parsers, authz, crypto, PII, or supply chain.
   - Add **`versona-testing`** when test gaps, flaky patterns, or coverage of new behavior need a testing-lens pass.
   - Add **`versona-architecture`** when boundaries, coupling, or cross-cutting design trade-offs dominate.
   - Optional one-shot: **`versona-family-engineering`** (Engineering family aggregator) when several engineering lenses may apply; follow **Suggested next Versonas** in output.
3. **Invoke** — Ask the user to `@` the chosen `.mdc` rule(s) in Cursor (or apply equivalent prompts from `blueprints/sdlc/methodologies/forge/versona/catalog/` per [`TEMPLATE-INDEX.md`](../../../methodologies/forge/versona/catalog/TEMPLATE-INDEX.md)).
4. **Output** — For each lens used, produce a **§5 structured report** per [`VERSONA-CONTRACT.md`](../../../methodologies/forge/versona/VERSONA-CONTRACT.md) §5: concerns with **critical** / **significant** / **minor** severity; **Proceed** / **Proceed with conditions** / **Rework** / **Bank** recommendation (definitions in [`VERSONA-FRAMEWORK.md`](../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §4).
5. **Persistence (Forge teams)** — Optional: create a session under `forge-logs/versona/<actor>/<session-id>/` using [`versona-session.template.md`](../../versona-session.template.md); if a **decision** or waiver is taken, link or summarize in **`ember-logs/YYYY-MM-DD.md`** per daily scripts in [`forge/daily/README.md`](../../../methodologies/forge/daily/README.md).

## Install

Copy this folder to the project’s **`.cursor/skills/run-engineering-ai-code-review/`** so the agent can discover it when relevant. Ensure Engineering Versona rules are installed (see [`README.template.md`](../../README.template.md) § Cursor rules).

## References

- [`agentic-coding-standards.md`](../../../methodologies/agentic-coding-standards.md)
- [`versona-se.mdc.template`](../../../methodologies/forge/versona/catalog/discipline/engineering/versona-se.mdc.template)
- [`agents/templates/recipe/llm-diff-review/README.md`](../../../../../agents/templates/recipe/llm-diff-review/README.md) — optional containerized diff→LLM template for CI/local
