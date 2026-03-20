# Maintaining the human handbook (`docs/`)

This folder holds **HTML + assets** for people who prefer a browser view over raw Markdown.

## Source of truth

| Canonical (edit first) | Human handbook (update when canonical changes) |
|------------------------|-----------------------------------------------|
| [`../SDLC.md`](../SDLC.md) | [`phases.html`](phases.html), [`dod.html`](dod.html), [`change.html`](change.html), [`review.html`](review.html), [`cicd.html`](cicd.html) — matching sections |
| [`../DOCUMENTATION-STRUCTURE.md`](../DOCUMENTATION-STRUCTURE.md) | [`documentation.html`](documentation.html) (incl. §2.1 work hierarchy); [`assets/repo-layout.svg`](assets/repo-layout.svg) if tree meaning changes |
| [`../../agents/STRUCTURE.md`](../../agents/STRUCTURE.md) (when present) | [`agents.html`](agents.html) |
| [`../README.md`](../README.md) | [`overview.html`](overview.html) / [`index.html`](index.html) intro only if README policy changes |
| [`../POLICY.md`](../POLICY.md) | [`governance.html`](governance.html) |
| [`../methodologies/*.md`](../methodologies/README.md) | [`methodologies.html`](methodologies.html) (hub + cards) · [`methodologies-roles.html`](methodologies-roles.html) · [`methodologies-scrum.html`](methodologies-scrum.html) · [`methodologies-kanban.html`](methodologies-kanban.html) · [`methodologies-phased.html`](methodologies-phased.html) · [`methodologies-xp.html`](methodologies-xp.html) · [`methodologies-agile.html`](methodologies-agile.html) · [`methodologies-agentic.html`](methodologies-agentic.html) — summaries; **canonical depth** stays in Markdown |
| **—** | **Left nav:** [`assets/docs-nav.js`](assets/docs-nav.js) builds the chapter list from **`DOC_NAV`**: each item is a **leaf** `{ href, label }` or a **group** `{ hubHref, label, groupId, children: [...] }` for any chapter that has sub-chapter HTML pages. **Methodologies** is the first group; add more groups when you add `phases-*.html` (or similar). Keep empty [`#doc-sidebar-nav`](index.html) / [`#doc-offcanvas-nav`](index.html) placeholders in each HTML shell. |

**Chapter files** (same layout shell; **update [`assets/docs-nav.js`](assets/docs-nav.js)** when adding/renaming a nav entry): [`index.html`](index.html) (landing), [`overview.html`](overview.html), [`phases.html`](phases.html), [`dod.html`](dod.html), [`change.html`](change.html), [`review.html`](review.html), [`cicd.html`](cicd.html), [`documentation.html`](documentation.html), [`agents.html`](agents.html), [`methodologies.html`](methodologies.html), [`methodologies-roles.html`](methodologies-roles.html), [`methodologies-scrum.html`](methodologies-scrum.html), [`methodologies-kanban.html`](methodologies-kanban.html), [`methodologies-phased.html`](methodologies-phased.html), [`methodologies-xp.html`](methodologies-xp.html), [`methodologies-agile.html`](methodologies-agile.html), [`methodologies-agentic.html`](methodologies-agentic.html), [`governance.html`](governance.html).

**Optional project extension (not blueprint text):** [`methodologies.html`](methodologies.html) links to **deep guides** in [`../methodologies/`](../methodologies/README.md) and to the consuming repo’s `sdlc/` tracking files — [`../../../sdlc/TRACKING-FOUNDATION.md`](../../../sdlc/TRACKING-FOUNDATION.md), [`TRACKING-METHODOLOGIES.md`](../../../sdlc/TRACKING-METHODOLOGIES.md), [`TRACKING-CHALLENGES.md`](../../../sdlc/TRACKING-CHALLENGES.md). If those files are absent, the `sdlc/` links 404; add or remove when forking.

Optional visuals (redraw if the **meaning** of the process changes):

| Asset | Purpose |
|-------|---------|
| [`assets/phases-flow.svg`](assets/phases-flow.svg) | Phases A–F |
| [`assets/repo-layout.svg`](assets/repo-layout.svg) | Repo layout (blueprint vs project vs docs) |
| [`assets/story-dod.svg`](assets/story-dod.svg) | Story definition of done (redraw if DoD items change) |
| [`assets/cicd-gates.svg`](assets/cicd-gates.svg) | Conceptual CI gate chain (trigger → static → tests → build → merge gate) |
| [`assets/change-control-flow.svg`](assets/change-control-flow.svg) | Visible scope path vs hidden scope ([`change.html`](change.html)) |

Inventory and future diagram ideas: [`assets/README.md`](assets/README.md).

## External links (methodologies)

Authoritative **https** targets for methodology guides are listed in [`../methodologies/REFERENCE-LINKS.md`](../methodologies/REFERENCE-LINKS.md), each with an **executive summary** (what it is, why this blueprint links to it). After editing [`../methodologies/*.md`](../methodologies/README.md), **sync** the same URLs **and blurbs** into the matching [`methodologies-*.html`](methodologies.html) “Authoritative sources” / “External reading” blocks (use `.doc-external-summary` in [`assets/docs-theme.css`](assets/docs-theme.css)), then spot-check with `curl -L -o /dev/null -w '%{http_code}' <url>` (expect **200**). Sites reorganize paths often; prefer stable home pages (standards bodies, scrumguides.org) over deep blog permalinks when a link breaks.

## When `blueprints/sdlc` changes

1. Edit **`SDLC.md`**, **`DOCUMENTATION-STRUCTURE.md`**, **`README.md`**, or **`POLICY.md`** as needed.  
2. **Propose or apply matching updates** to the **chapter HTML files** above, SVGs, and (if layout/theme changes) **`assets/docs-theme.css`** so the handbook stays accurate.  
3. Bump the **“last aligned”** date in **every** chapter footer (and [`index.html`](index.html)) and in this file if you keep a changelog here.  
4. If phases are renamed, added, or removed, **redraw** `phases-flow.svg` and adjust [`phases.html`](phases.html).

## UI stack (handbook)

| Piece | Role |
|-------|------|
| **[Bootstrap 5.3](https://getbootstrap.com/)** (CSS + `bootstrap.bundle.js` from CDN in each HTML page) | Grid, utilities, components (sidebar + **offcanvas** on small screens), tables, alerts, **collapse** for methodology sub-nav. |
| [`assets/docs-nav.js`](assets/docs-nav.js) | Injects identical **Chapters** nav into `#doc-sidebar-nav` and `#doc-offcanvas-nav`; **collapsible groups** in `DOC_NAV` expand when the current page is that chapter’s hub or any listed sub-page. |
| [`assets/docs-toc-scrollspy.js`](assets/docs-toc-scrollspy.js) | On pages with `nav.doc-toc` (**Documentation layout**, **Agents & automation**, **Change control**, **Roles & archetypes**), highlights the **On this page** link for the section in view. |
| **`assets/docs-theme.css`** | Typography (Open Sans body, Proxima Nova Black for `.font-display`, Courier New for `code`), compact spacing, smooth scroll, scroll-margin, tables, skip-link, phase cards, **`.doc-nav-*`** sidebar group styles. |
| **Fonts** | **Open Sans** + **Montserrat** (900, Black fallback) from Google Fonts; **Proxima Nova** from [CDNFonts](https://www.cdnfonts.com/proxima-nova-2.font) (replace with a licensed self-hosted `@font-face` or Adobe Fonts if your policy requires it). **Courier New** for monospace (system). |

If you **change Bootstrap version** or add heavy customization, update **`docs-theme.css`** when custom classes need to stay aligned (e.g. `--bs-*` variables).

## Viewing locally

Open `blueprints/sdlc/docs/index.html` in a browser (`file://` works). Images load from `assets/`. For strict relative-path testing, run `python -m http.server` from `docs/`.

---

*This file is for maintainers; it is not part of the frozen process text itself.*
