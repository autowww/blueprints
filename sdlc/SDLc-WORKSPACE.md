# Initializing the project `sdlc/` workspace

This blueprint ships **canonical copies** of the engineering-tracking Markdown files and a **`README` template** under [`templates/sdlc/`](templates/sdlc). Use them to create a **mutable** `sdlc/` folder at the **repository root** (next to `blueprints/sdlc/`), without copying project-specific prose from another repo by hand.

## What gets created

| Path (repo root) | Source |
|------------------|--------|
| `sdlc/README.md` | From [`templates/sdlc/README.template.md`](templates/sdlc/README.template.md) with `{{PROJECT_NAME}}` replaced |
| `sdlc/TRACKING-FOUNDATION.md` | Copy of [`templates/sdlc/TRACKING-FOUNDATION.md`](templates/sdlc/TRACKING-FOUNDATION.md) |
| `sdlc/TRACKING-METHODOLOGIES.md` | Copy of [`templates/sdlc/TRACKING-METHODOLOGIES.md`](templates/sdlc/TRACKING-METHODOLOGIES.md) |
| `sdlc/TRACKING-CHALLENGES.md` | Copy of [`templates/sdlc/TRACKING-CHALLENGES.md`](templates/sdlc/TRACKING-CHALLENGES.md) |

## Prerequisites

- Repository root contains **`blueprints/sdlc/`** (this package).
- You plan to add **`docs/`** (or equivalent) per [`DOCUMENTATION-STRUCTURE.md`](DOCUMENTATION-STRUCTURE.md); paths in `README.md` assume the usual layout.

## Option A — script (recommended)

From the **repository root**. Full flags and prerequisites: [`scripts/README.md`](scripts/README.md).

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name"
```

Optional second argument: target directory (default `sdlc`):

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name" sdlc
```

If `README.md` already exists in the target, the script **refuses to overwrite** unless you pass `--force` (overwrites only `README.md`; tracking files are always copied).

## Option B — manual

1. `mkdir -p sdlc`
2. Copy the three `TRACKING-*.md` files from `blueprints/sdlc/templates/sdlc/` into `sdlc/`.
3. `sed 's/{{PROJECT_NAME}}/Your Project/g' blueprints/sdlc/templates/sdlc/README.template.md > sdlc/README.md` (or edit by hand).
4. Link `sdlc/README.md` from the root `README.md` and [`docs/INDEX.md`](DOCUMENTATION-STRUCTURE.md) as you adopt `docs/`.

## After init

- **Customize** `sdlc/README.md`: remove table rows for paths you do not use yet (e.g. `blueprints/docs/`, `docs/product/`) if the repo is slimmer than the template.
- **Link** the handbook: [`docs/index.html`](docs/index.html) already references `../../../sdlc/TRACKING-*.md` when those files exist.
- **Do not** edit the frozen blueprint for project-only notes; keep them in `sdlc/` or `docs/`.

## Drift

When tracking content in the **living** `sdlc/` folder is improved, consider **backporting** the generic parts into `blueprints/sdlc/templates/sdlc/` so the next project gets the same baseline.

## Compare with an existing `sdlc/`

After generating a scratch folder (e.g. `sdlc.new/`), see [`SDLc-WORKSPACE-COMPARISON.md`](SDLc-WORKSPACE-COMPARISON.md) for what should match and what differs in `README.md` only.
