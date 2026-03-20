# Human handbook (HTML)

- **Open in a browser:** [`index.html`](index.html) — landing + links to chapters; **[`methodologies.html`](methodologies.html)** (hub) + **`methodologies-*.html`** sub-chapters (roles &amp; archetypes, Scrum, Kanban, phased, XP, Agile, agentic) + links to **`../methodologies/*.md`** and project **`sdlc/TRACKING-*.md`**. **`documentation.html`** — work hierarchy (milestones → tasks). **`change.html`** — scope management, time tracking, ADRs, diagram. **`agents.html`** — **Agents & automation** (agentic context + optional **`blueprints/agents/`** Docker layers, recipes, CI). Other chapters: **`overview.html`**, **`phases.html`**, **`dod.html`**, **`review.html`**, **`cicd.html`**, **`governance.html`**.  
- **UI:** Responsive **sidebar navigation** (mobile **offcanvas**), **Bootstrap 5** (CDN), custom [`assets/docs-theme.css`](assets/docs-theme.css).  
- **Maintainers:** [`MAINTENANCE.md`](MAINTENANCE.md) — keep HTML/SVG/CSS in sync when `blueprints/sdlc/*.md` changes.
- **Bootstrap project `sdlc/`:** [`../scripts/README.md`](../scripts/README.md) (`init-sdlc-workspace.sh`) · [`../SDLc-WORKSPACE.md`](../SDLc-WORKSPACE.md).

This `docs/` folder lives **inside** `blueprints/sdlc/` and is part of the reusable blueprint package (update it when the Markdown sources change).

## CSS framework note

- **[Bootstrap 5 vs Tailwind — comparison](COMPARISON-BS5-TAILWIND.md)** — table + when to pick which (the handbook is implemented with **Bootstrap 5**).
