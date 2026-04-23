# Maintaining the documentation

## Architecture

Blueprint `.md` files in **this** repository are the single source of truth. They feed three documentation surfaces:

| Surface | Built by | Output |
|---------|----------|--------|
| **blueprints.forgesdlc.com** | **`generator/build-handbook.py`** in the **[blueprints-website](https://github.com/autowww/blueprints-website)** consumer (run from that repo; this repo is vendored as the `blueprints/` submodule there) | `website/` **inside blueprints-website** |
| **GitHub Wiki** | `wiki-source/sync-wiki.sh` | Pushed to `autowww/blueprints.wiki` |
| **forgesdlc.com** | `generator/build-site.py` in the **forgesdlc** repo | Reads `.md` via submodule |

There is **no** `generator/` directory in the **blueprints** repo on its own — the handbook build always runs from **blueprints-website** (or CI there) against a checkout of this Markdown.

**Consumers (repos that embed `blueprints/`):** baseline edit rules and **`blueprints/`** vs project **`sdlc/`** are summarized for readers in [`sdlc/POLICY.md`](../sdlc/POLICY.md).

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

- **Public handbook governance** — blueprints.forgesdlc.com is a **curated** handbook, not a mirror of every `.md` file; `public_publish`, audience, tier, `nav_title`, `product_area`
- **Manifest** — [`handbook-publish-manifest.yaml`](https://github.com/autowww/blueprints-website/blob/main/generator/handbook-publish-manifest.yaml) in **blueprints-website** (`include_globs` / `exclude_globs` relative to the `blueprints/` submodule)
- 101/201/301 tiering and cross-surface linking

Migration phases: [`PUBLIC-HANDBOOK-MIGRATION.md`](PUBLIC-HANDBOOK-MIGRATION.md).

Optional CI: `python3 generator/validate_handbook_public_metadata.py` from **blueprints-website** (validates required frontmatter when `public_publish: true`).
