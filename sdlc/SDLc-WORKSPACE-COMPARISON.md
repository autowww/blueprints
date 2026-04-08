# `sdlc/` vs `sdlc.new/` (generated) — comparison notes

**Context:** `sdlc.new/` was produced with:

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "MyProduct" sdlc.new --force
```

It is a **sanity check** that [`templates/sdlc/`](templates/sdlc) matches the intended baseline. **Do not** commit `sdlc.new/` to the main line unless you use it as a fixture; delete it after review or add to `.gitignore` locally.

## What matches

| Artifact | Status |
|----------|--------|
| `TRACKING-FOUNDATION.md` | Identical to **`sdlc/`** and **`templates/sdlc/`** (byte-for-byte after init). |
| `TRACKING-METHODOLOGIES.md` | Same. |
| `TRACKING-CHALLENGES.md` | Same. |

## `README.md` differences (expected)

| Topic | Living `sdlc/README.md` | Generated `sdlc.new/README.md` |
|--------|-------------------------|----------------------------------|
| **Project label** | Footer reflects the **living** repo (named project); table rows assume **full** doc tree (`blueprints/product`, product handbook, etc.). | Footer says **project-only**; several rows are marked **(if adopted)** so greenfield repos can delete unused links. |
| **Engineering intro** | Mentions [`docs/INDEX.md#engineering-tracking`](https://github.com/autowww/blueprints/blob/main/docs/INDEX.md#engineering-tracking) and [`SDLc-WORKSPACE.md`](SDLc-WORKSPACE.md). | Same ideas; wording tuned for repos that may not have `docs/INDEX.md` yet. |

Titles align (e.g. `# SDLC — MyProduct` when that string was passed to `init-sdlc-workspace.sh`). None of this affects the **TRACKING-*** files.

## Possible follow-ups (suggestions)

1. **Trim template rows** after init: remove `blueprints/product` / product handbook lines if the repo only uses `blueprints/sdlc/` + slim `docs/`.
2. **Promote from template to living**: when you change [`templates/sdlc/README.template.md`](templates/sdlc/README.template.md), consider applying the same table wording to the real **`sdlc/README.md`** if you want them identical.
3. **Delete `sdlc.new/`** after verification, or add `/sdlc.new/` to `.gitignore` for local scratch compares.

## Drift control

When you change **`sdlc/TRACKING-*.md`** in the project, **copy or merge** generic updates back into **`blueprints/sdlc/templates/sdlc/`** so the next `init-sdlc-workspace.sh` run stays aligned.
