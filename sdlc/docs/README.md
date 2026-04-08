# Human handbook (HTML)

- **Open in a browser:** [`index.html`](index.html) — landing + links to chapters; **[`methodologies.html`](methodologies.html)** (hub) + **`methodologies-*.html`** sub-chapters (roles &amp; archetypes, **ceremonies**, Scrum, Kanban, phased, XP, Agile, agentic) + links to **`../methodologies/*.md`**, **`../methodologies/ceremonies/`**, and project **`sdlc/TRACKING-*.md`**. **`documentation.html`** — work hierarchy (milestones → tasks). **`change.html`** — scope management, time tracking, ADRs, diagram. **`agents.html`** — **Agents & automation** (agentic context + optional **`blueprints/agents/`** Docker layers, recipes, CI). Other chapters: **`overview.html`**, **`phases.html`**, **`dod.html`**, **`review.html`**, **`cicd.html`**, **`governance.html`**.  
- **UI:** Responsive **sidebar navigation** (mobile **offcanvas**), **Bootstrap 5** (CDN), custom [`assets/docs-theme.css`](assets/docs-theme.css).  
- **Maintainers:** [`MAINTENANCE.md`](MAINTENANCE.md) — keep HTML/SVG/CSS in sync when `blueprints/sdlc/*.md` changes.
- **Bootstrap project `sdlc/`:** [`../scripts/README.md`](../scripts/README.md) (`init-sdlc-workspace.sh`) · [`../SDLc-WORKSPACE.md`](../SDLc-WORKSPACE.md).

This `docs/` folder lives **inside** `blueprints/sdlc/` and is part of the reusable blueprint package (update it when the Markdown sources change).

## Workspace policy (synced)

- **[WORKSPACE-LOCALIZATION-SCOPE.md](WORKSPACE-LOCALIZATION-SCOPE.md)** — supported locales and i18n policy for Forge workspace products; canonical copy at workspace `docs/`; run `sync-workspace-localization-scope.sh` after edits.
- **[L10N-ARCHITECTURE.md](L10N-ARCHITECTURE.md)** — manifest schema, handbook/site generator flags (`build-handbook.py`, `build-site.py`), delta translation workflow, and Kitchen Sink chrome bundles.

## CSS framework note

- **[Bootstrap 5 vs Tailwind — comparison](COMPARISON-BS5-TAILWIND.md)** — table + when to pick which (the handbook is implemented with **Bootstrap 5**).
