# Public documentation depth guidance

Maintainer-only authoring standards for deepening the **published** Forge handbook (Blueprints site) and **forge-lenses** public guides. These files are **not** emitted to the static handbook.

| File | Purpose |
|------|---------|
| [01-doc-depth-charter.md](01-doc-depth-charter.md) | Depth layers, public boundary, structured-content minimums, definition of done |
| [02-page-archetypes-and-coverage.md](02-page-archetypes-and-coverage.md) | Page archetypes (overview through reference-lite) and required coverage |
| [03-visual-language-and-ks-usage.md](03-visual-language-and-ks-usage.md) | When to use which Kitchen Sink / handbook visuals and tables |
| [04-topic-splitting-rules.md](04-topic-splitting-rules.md) | When to split topics and common split patterns |
| [05-coverage-plan-blueprints.md](05-coverage-plan-blueprints.md) | Backlog: Blueprints handbook pages and execution order |
| [06-coverage-plan-lenses-studio-wizard.md](06-coverage-plan-lenses-studio-wizard.md) | Backlog: Lenses / Studio / Wizard pages and execution order |
| [07-cursor-prompts-sequence.md](07-cursor-prompts-sequence.md) | Cursor prompt sequence (audit through QA) |
| [08-review-checklist.md](08-review-checklist.md) | Pre-publish review checklist |

**Artifacts (audit / outlines / QA snapshots):** [artifacts/](artifacts/) — generated or updated when running the [Cursor prompt sequence](07-cursor-prompts-sequence.md).

**Workspace path:** This directory is also linked from the multi-repo workspace root as [`docs/guidance/`](../../../docs/guidance/) so Cursor `@docs/guidance/` resolves here.

**Workspace rules:** Handbook pages must not use Mermaid fenced blocks; use tables, prose, SVG assets, or Kitchen Sink patterns ([`.cursor/rules/no-mermaid-diagrams.mdc`](../../../.cursor/rules/no-mermaid-diagrams.mdc)).
