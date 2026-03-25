# Forge design system (Kitchen Sink)

This handbook uses the **Forge design system** from the shared [forgesdlc-kitchensink](https://github.com/autowww/forgesdlc-kitchensink) repository: Bootstrap&nbsp;5 dark theme, design tokens, Python **components** and **layouts**, HTML **transforms**, and reusable **SVG diagram templates**.

## Where it lives

| Piece | Role |
|--------|------|
| `forge-theme.css` | Blueprints handbook look (nav, ToC, prose, callouts) |
| `docs-theme.css` | Optional chapter-style pages |
| `forge-theme.js` | Theme behavior |
| `components/` (Python) | `handbook_page()`, callouts, nav fragments, table transforms |
| `assets/svg/` | Diagram archetypes (flows, charts, boards) |

Build copies CSS/JS and SVGs into `website/assets/` when you run `generator/build-handbook.py`.

## Design tokens (summary)

- **Background:** deep space (`#0A0E17` family)  
- **Accents:** cyan (`#06B6D4`), amber (`#F59E0B`)  
- **Fonts:** Inter (body), JetBrains Mono (code), Space Mono (labels)

Use semantic HTML and existing component classes from the generator rather than ad-hoc styles.

## Page layouts

Kitchen Sink defines full-page **layouts** (showcase, handbook, product, landing, …). The blueprints site uses **`handbook_page`**: sidebar + article + optional right ToC. See the Kitchen Sink **Page Layouts** documentation for schematics and live previews.

## Diagram templates (examples)

Below are a few SVG templates shipped with Kitchen Sink. They illustrate the visual language for methodology docs; replace placeholders with your own labels.

![Linear flow](assets/template-linear-flow.svg)

![Gate chain](assets/template-gate-chain.svg)

![Swimlane](assets/template-swimlane.svg)

**Reference:** the Kitchen Sink repo includes a built **diagram gallery** under `showcase/` (run `python3 generator/build-showcase.py` locally, or see [forgesdlc-kitchensink](https://github.com/autowww/forgesdlc-kitchensink) for sources).

## Authoring guidance

1. Prefer **` ```ks-diagram `** / **` ```ks-diagram-expand `** fences for figures on the **handbook** and **forgesdlc.com** sites: they render static Kitchen Sink SVG templates (Forge palette) with optional click-to-expand legend.  
2. Put **bespoke** figures in blueprint `sdlc/docs/assets/` (or site `assets/svg/`) and reference them with `src:` in the fence when needed.  
3. **Mermaid** remains available only in the **Kitchen Sink showcase** (`mermaid-examples.html`, diagram parallels) as diagram-as-code reference—not loaded on handbook or product pages.  
4. Keep tables and headings so **`transforms`** (e.g. table wrappers) run consistently.

## KS diagram fences (handbook + product)

- **Catalog keys** (`linear`, `swimlane`, `sequence`, `state`, `gantt`, …) and SVG filenames live in **`generator/pages/_diagram_gallery.py`** (`_FAMILIES`).  
- **Legend text** for the modal is shipped to sites as **`ks-diagram-catalog.js`** (extracted from the showcase `DIAGRAM_DETAILS` object); keep it in sync when you add templates.  
- **Live Mermaid reference** (grammar catalog, theme): build the KS **`showcase/`** and open **`mermaid-examples.html`** and **`diagrams.html`** — not part of blueprints-website or forgesdlc runtime.

### Inline (no expand)

```ks-diagram
key: swimlane
alt: Cross-team handoffs
```

### Click-to-expand (lightbox + legend)

```ks-diagram-expand
key: linear
alt: End-to-end flow
```

### Custom asset under `assets/`

```ks-diagram-expand
src: svg/my-flow.svg
alt: Program-specific figure
expand: true
```

GitHub does not render `ks-diagram` fences; readers should use the published HTML site or link to **diagrams** / **Mermaid examples** on the KS showcase for live previews.

### Consuming the catalog in another repository

1. Add **forgesdlc-kitchensink** as a **submodule** (or vendor the pieces you need).  
2. Copy **`assets/svg/template-*.svg`**, **`ks-diagram-catalog.js`**, **`ks-diagram-modal.js`**, and theme CSS/JS in your site build the same way **blueprints-website** and **forgesdlc** do.  
3. **Python:** import **`handbook_page`**, **`render_ks_diagram_block`**, **`apply_all`** / **`convert_ks_diagram_blocks`** from Kitchen Sink `components` with your `PYTHONPATH` set like the existing generators.  
4. **Interactive gallery** (bento thumbs + `openDiagramWithDetail`): ship **`showcase.js`** on KS showcase pages only, or **link out** to the published KS showcase.  
5. **Modal legend** on consumer sites uses **`forge-theme.js`** + **`ks-diagram-modal.js`** (not full `showcase.js`).

## Related links

- [Documentation structure](./DOCUMENTATION-STRUCTURE.md) — how SDLC docs are organized  
- Maintenance (generator / CI) — see `sdlc/docs/MAINTENANCE.md` in the blueprints repository  
