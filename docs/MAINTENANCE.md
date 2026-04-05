# Maintaining the documentation

## Architecture

Blueprint `.md` files in **this** repository are the single source of truth. They feed three documentation surfaces:

| Surface | Built by | Output |
|---------|----------|--------|
| **blueprints.forgesdlc.com** | **`generator/build-handbook.py`** in the **[blueprints-website](https://github.com/autowww/blueprints-website)** consumer (run from that repo; this repo is vendored as the `blueprints/` submodule there) | `website/` **inside blueprints-website** |
| **GitHub Wiki** | `wiki-source/sync-wiki.sh` | Pushed to `autowww/blueprints.wiki` |
| **forgesdlc.com** | `generator/build-site.py` in the **forgesdlc** repo | Reads `.md` via submodule |

There is **no** `generator/` directory in the **blueprints** repo on its own — the handbook build always runs from **blueprints-website** (or CI there) against a checkout of this Markdown.

**forge-lenses handbook:** The **blueprints-website** build also emits **`website/lenses/`** (hub, **Reference** handbook, tutorial) from the **`forge-lenses`** submodule — merged `docs/**/*.md` and `lenses/website/*.md`. That content is **not** in this repo; edit upstream in [autowww/forge-lenses](https://github.com/autowww/forge-lenses), then bump the submodule in blueprints-website and rebuild.

## Build workflow

### blueprints.forgesdlc.com

Clone **blueprints-website**, initialize submodules, then from the **blueprints-website** root:

```bash
python3 generator/build-handbook.py --all
python3 generator/inject-portal-nav.py
# Output: website/ in the blueprints-website repo
```

CI on **blueprints-website** builds and deploys on push; this repo’s Markdown is pulled via the `blueprints` submodule pointer.

### GitHub Wiki

```bash
bash wiki-source/sync-wiki.sh
```

### Local preview

To preview the website locally, run the build commands above and open `website/index.html` in a browser.

## Generator layout (blueprints-website repo)

The handbook generator lives next to the site output — **not** in this repository:

```
blueprints-website/
├── generator/
│   ├── build-handbook.py       # MD→HTML for blueprints.forgesdlc.com
│   ├── inject-portal-nav.py    # Portal navigation
│   └── …
├── blueprints/                 # submodule → this repo
└── website/                    # generated HTML
```

## Adding a new area

1. Create the area directory with `.md` files **in this (blueprints) repo**.
2. Add the area path to `ALL_AREAS` in **`blueprints-website/generator/build-handbook.py`**.
3. Run the build from **blueprints-website** to verify.
4. Update `wiki-source/sync_markdown.py` if the wiki needs special link handling.

## Content model

See [`DESIGN-PRINCIPLES.md`](DESIGN-PRINCIPLES.md) for:
- Frontmatter metadata schema (`tier`, `surfaces`, `cross_refs`)
- 101/201/301 tiering guidelines
- Cross-referencing policy between surfaces
