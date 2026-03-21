---
name: spec-driven
description: Spec-driven development workflow — work-unit IDs, acceptance criteria, and spec lifecycle.
---

# Spec-driven development

When implementing features or editing requirements:

1. **Work-unit IDs first** — every story, epic, and task has a stable ID (e.g. `M1E1S1`). Reference it in commits, PRs, and plan files. Specs live under `docs/requirements/`.
2. **Acceptance criteria before code** — if the spec lacks testable criteria, write or refine them before implementing. Prefer given/when/then, checklists, or concrete examples.
3. **Lifecycle loop** — Draft → Refine (criteria agreed) → Implement (small batches, PR traces to work unit) → Inspect (review checks spec fit) → Adapt (update spec if reality invalidates it).
4. **Failing tests or unmet criteria are the stop signal** — not "looks fine."
5. **Update specs when behavior changes** — changing code without updating the spec is scope drift. Do both in the same changeset.

Anti-patterns: code-first spec-later, specs in chat only, specs never updated, one giant spec doc.

Reference: `blueprints/sdlc/methodologies/spec-driven-development.md`.
