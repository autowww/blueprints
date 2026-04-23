---
name: export-versona-kitchensink-diagram
description: >
  Produce kitchen-sink compatible diagram artifacts: blueprint-diagram IR in session diagrams/,
  SVG exports for handbooks/sites — not Mermaid as the normative path.
---

# Export Versona kitchen-sink diagram (Forge)

## When to use

- Architecture, UX, or process **diagrams** must ship in **handbook / product site** pipelines that use **Kitchen Sink** assets.
- Session **`diagrams/`** should hold **source + export** per [`VERSONA-OPERATING-MODEL.md`](../../../../methodologies/forge/VERSONA-OPERATING-MODEL.md) §5.

## Steps

1. **Author IR** — In Markdown body or `diagrams/*.md`, use fenced **`blueprint-diagram`** blocks (see [`VERSONA-FRAMEWORK.md`](../../../../methodologies/forge/versona/VERSONA-FRAMEWORK.md) §6).
2. **Render SVG** — Use the consuming repo’s **Kitchen Sink** generator or approved toolchain to emit **`.svg`** under `forge-logs/versona/.../diagrams/exported/` (or team path); do **not** rely on Mermaid for **canonical** Forge artifacts unless the repo explicitly allows a legacy exception.
3. **Register** — List exports in `SESSION.md` and optional `artifact-manifest.json`.
4. **Optional recipe** — Stub template [`versona-kitchensink-diagram-export`](../../../../../agents/templates/recipe/versona-kitchensink-diagram-export/README.md) for **CI** that runs `build-showcase` or site generator headlessly in **`agents/recipes/`** after copy.

## Rules

- Prefer **reusable** diagram **templates** in Kitchen Sink + **instance** SVG in product/blueprint content trees per workspace asset rules.

## Install

Copy to **`.cursor/skills/export-versona-kitchensink-diagram/`**.

## References

- [`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) — diagram classes
- Workspace rule: no Mermaid in handbook/product docs; KS showcase exception only
