# Maintaining the documentation

## Architecture

Blueprint `.md` files are the single source of truth. They feed three documentation surfaces:

| Surface | Built by | Output |
|---------|----------|--------|
| **blueprints.forgesdlc.com** | `generator/build-handbook.py` in this repo | `website/` directory |
| **GitHub Wiki** | `wiki-source/sync-wiki.sh` | Pushed to `autowww/blueprints.wiki` |
| **forgesdlc.com** | `generator/build-site.py` in the `forgesdlc` repo | Reads `.md` via submodule |

## Build workflow

### blueprints.forgesdlc.com

```bash
python3 generator/build-handbook.py --all
python3 generator/inject-portal-nav.py
# Output: website/
```

CI automatically builds and deploys on push to `main` via `.github/workflows/deploy-blueprints-site.yml`.

### GitHub Wiki

```bash
bash wiki-source/sync-wiki.sh
```

### Local preview

To preview the website locally, run the build commands above and open `website/index.html` in a browser.

## Generator structure

```
generator/
├── build-handbook.py       # Main MD→HTML generator for blueprints.forgesdlc.com
├── inject-portal-nav.py    # Adds portal navigation to generated pages
├── migrate-to-forge.py     # Theme migration helper (one-time use)
├── build_methodology_chapters.py  # SDLC methodology chapters
└── templates/
    ├── __init__.py
    ├── components.py       # Atomic UI components
    ├── layouts.py          # Page layout shells
    ├── transforms.py       # HTML post-processing
    ├── forge-theme.css     # Canonical CSS
    └── theme.css           # Legacy CSS (deprecated)
```

## Adding a new area

1. Create the area directory with `.md` files.
2. Add the area path to `ALL_AREAS` in `generator/build-handbook.py`.
3. Run the build to verify.
4. Update `wiki-source/sync_markdown.py` if the area needs special link handling.

## Content model

See [`DESIGN-PRINCIPLES.md`](DESIGN-PRINCIPLES.md) for:
- Frontmatter metadata schema (`tier`, `surfaces`, `cross_refs`)
- 101/201/301 tiering guidelines
- Cross-referencing policy between surfaces
