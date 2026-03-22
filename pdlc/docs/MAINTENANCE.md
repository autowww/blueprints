# Maintaining the PDLC handbook (`docs/`)

This folder holds **HTML + assets** for people who prefer a browser view over raw Markdown.

## Source of truth

| Canonical (edit first) | Human handbook (update when canonical changes) |
|------------------------|-----------------------------------------------|
| [`../PDLC.md`](../PDLC.md) | [`overview.html`](overview.html), [`phases.html`](phases.html), [`stage-gates.html`](stage-gates.html), [`metrics.html`](metrics.html) |
| [`../PDLC-SDLC-BRIDGE.md`](../PDLC-SDLC-BRIDGE.md) | [`bridge.html`](bridge.html) |
| [`../approaches/*.md`](../approaches/README.md) | [`approaches.html`](approaches.html) (hub), [`approach-dual-track.html`](approach-dual-track.html), [`approach-stage-gate.html`](approach-stage-gate.html), [`approach-design-thinking.html`](approach-design-thinking.html), [`approach-lean-startup.html`](approach-lean-startup.html), [`approach-plm.html`](approach-plm.html), [`approach-ost.html`](approach-ost.html) |
| [`../README.md`](../README.md) | [`index.html`](index.html) intro only if README policy changes |
| [`../POLICY.md`](../POLICY.md) | Governance section (when created) |

**Left nav:** [`assets/docs-nav.js`](assets/docs-nav.js) builds the chapter list from `DOC_NAV`. Add new entries when creating/renaming pages.

**Chapter files** (same layout shell; update `docs-nav.js` when adding/renaming): [`index.html`](index.html) (landing), [`overview.html`](overview.html), [`phases.html`](phases.html), [`bridge.html`](bridge.html), [`stage-gates.html`](stage-gates.html), [`metrics.html`](metrics.html), [`approaches.html`](approaches.html) (hub), `approach-*.html` (sub-chapters).

## When `blueprints/pdlc` changes

1. Edit **`PDLC.md`**, **`PDLC-SDLC-BRIDGE.md`**, **`approaches/*.md`**, or related blueprint files as needed.
2. **Propose or apply matching updates** to the chapter HTML files so the handbook stays accurate.
3. Bump the **"last aligned"** date in every chapter footer and in [`index.html`](index.html).
4. If phases are renamed, added, or removed, update [`phases.html`](phases.html) and [`assets/docs-nav.js`](assets/docs-nav.js).

## Assets

| Asset | Purpose |
|-------|---------|
| [`assets/docs-nav.js`](assets/docs-nav.js) | Sidebar + offcanvas navigation; `DOC_NAV` array defines chapter order |
| [`assets/docs-theme.css`](assets/docs-theme.css) | Typography, layout, phase cards — same as SDLC handbook theme |

## UI stack (handbook)

| Piece | Role |
|-------|------|
| **[Bootstrap 5.3](https://getbootstrap.com/)** (CDN) | Grid, utilities, sidebar, offcanvas, tables |
| [`assets/docs-nav.js`](assets/docs-nav.js) | Shared nav with collapsible Approaches group |
| [`assets/docs-theme.css`](assets/docs-theme.css) | Open Sans body, Proxima Nova / Montserrat display, compact spacing |

## Viewing locally

Open `blueprints/pdlc/docs/index.html` in a browser (`file://` works). For strict relative-path testing, run `python -m http.server` from `docs/`.

---

*This file is for maintainers; it is not part of the frozen process text itself.*
