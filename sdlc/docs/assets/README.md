# Handbook static assets (`docs/assets/`)

This folder holds **CSS**, **JavaScript**, and **diagrams** for the **SDLC blueprint HTML handbook** (`blueprints/sdlc/docs/*.html`).

## Audit status (references vs files)

| Referenced in HTML | File | Status |
|--------------------|------|--------|
| [`phases.html`](../phases.html) | `phases-flow.svg` | Present — phases A–F |
| [`documentation.html`](../documentation.html) | `repo-layout.svg` | Present — repo / blueprints / `docs/` |
| [`dod.html`](../dod.html) | `story-dod.svg` | Present — story DoD checklist |
| [`cicd.html`](../cicd.html) | `cicd-gates.svg` | Present — conceptual CI gate chain |
| [`change.html`](../change.html) | `change-control-flow.svg` | Present — visible scope path vs hidden scope |
| [`methodologies-roles.html`](../methodologies-roles.html) | — | No figure — archetype & title tables inline |
| [`methodologies-ceremonies.html`](../methodologies-ceremonies.html) | — | No figure — intent types + fork links inline |
| [`methodologies-scrum.html`](../methodologies-scrum.html) | `methodology-scrum-sprint.svg` | Present — Sprint event chain |
| [`methodologies-kanban.html`](../methodologies-kanban.html) | `methodology-kanban-board.svg` | Present — pull / board flow |
| [`methodologies-phased.html`](../methodologies-phased.html) | `methodology-phased-gates.svg` | Present — phased gates |
| [`methodologies-xp.html`](../methodologies-xp.html) | `methodology-xp-loop.svg` | Present — XP practices (linearized) |
| [`methodologies-agile.html`](../methodologies-agile.html) | `methodology-agile-umbrella.svg` | Present — Agile vs frameworks |
| [`methodologies-agentic.html`](../methodologies-agentic.html) | `methodology-agentic-flow.svg` | Present — intent → review → repo |
| *(all pages)* | `docs-theme.css` | Present |
| *(all pages)* | `docs-nav.js` | Present |
| *(documentation + agents)* | `docs-toc-scrollspy.js` | Present |

**Broken links:** none — every `<img src="assets/…">` points to an existing file.

**Other blueprints:** `blueprints/docs/docs/` uses only `assets/docs-theme.css` (no raster/SVG images yet).

## Non-image assets

| File | Role |
|------|------|
| [`docs-theme.css`](docs-theme.css) | Typography, layout, sidebar, TOC, external-link summaries |
| [`docs-nav.js`](docs-nav.js) | Chapter + sub-chapter nav (`DOC_NAV`) |
| [`docs-toc-scrollspy.js`](docs-toc-scrollspy.js) | “On this page” scroll spy (`documentation.html`, `agents.html`, `change.html`) |

## Optional / future diagrams (not referenced yet)

Ideas if you want more visuals later (same style as existing SVGs: `#f6f3ed` background, `#2c5f4e` titles):

| Suggested file | Chapter | Purpose |
|----------------|---------|---------|
| `overview-roles.svg` | `overview.html` | Simple roles / RACI (PO, SM, Dev) — only if text stays stable |
| `change-adr-flow.svg` | `change.html` | Proposal → decision → ADR / record |
| `tracking-spine.svg` | `methodologies.html` or project `sdlc/` | contributor → events → work units (matches ASCII tree today) — distinct from `methodology-agentic-flow.svg` (agentic intent flow) |

Redraw `phases-flow.svg` and `cicd-gates.svg` when phase names or gate steps change materially — see [`../MAINTENANCE.md`](../MAINTENANCE.md).
