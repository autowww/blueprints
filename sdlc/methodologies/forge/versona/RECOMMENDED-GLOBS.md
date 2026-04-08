---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Recommended Cursor `globs` for Product Versonas

Forge Versona templates ship with **empty `globs:`** so each repo opts in. For **product-led** work, consider attaching rules when product or PDLC docs are in context.

These are **defaults** — narrow or widen to match your tree.

| Rule (installed name) | Suggested `globs` (comma-separated in `.mdc` frontmatter) |
|-----------------------|------------------------------------------------------------|
| `versona-product-management.mdc` | `docs/product/**/*`, `docs/requirements/**/*`, `**/PRODUCT*.md`, `forge/**/*` |
| `versona-ba.mdc` | `docs/requirements/**/*`, `docs/product/**/*`, `**/*requirements*.md` |
| `versona-ux.mdc` | `docs/product/journeys/**/*`, `docs/**/*ux*`, `**/*.figma.md`, `**/design/**/*` |
| `versona-marketing.mdc` | `docs/product/**/*`, `**/GTM*.md`, `**/marketing/**/*` |
| `versona-cs.mdc` | `docs/product/**/*`, `**/support/**/*`, `**/onboarding/**/*` |
| `versona-family-product.mdc` | `docs/product/**/*`, `docs/requirements/**/*`, `forge/**/*` |

**Family aggregator:** use the **union** of the above or a single broad pattern such as `docs/**/*` if your repo is doc-centric (higher noise).

**Tasklets** (`forge-tasklet-*.mdc`): e.g. `docs/**/*.md`, `forge/**/*`, or leave empty for manual `@` invocation.

See also: Cursor rule format in [`.cursor/skills-cursor/create-rule`](https://github.com/getcursor/cursor) (user environment) and [`../tasklets/README.md`](../tasklets/README.md).
