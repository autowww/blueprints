# Blueprints wiki

This wiki is a **Markdown mirror** of the **[blueprints](https://github.com/autowww/blueprints)** repo (everything except `wiki-source/` and `*.template.md`). **Canonical source** is always the code repository on `main`.

## Browse here (wiki pages)

- **SDLC hub:** [sdlc/README](sdlc/README)
- **Phases & DoD (single file):** [sdlc/SDLC](sdlc/SDLC)
- **Methodologies:** [sdlc/methodologies/README](sdlc/methodologies/README)
- **Roles & archetypes:** [sdlc/methodologies/roles-archetypes](sdlc/methodologies/roles-archetypes)
- **Ceremonies (foundation + forks):** [sdlc/methodologies/ceremonies/README](sdlc/methodologies/ceremonies/README)
- **Product-docs blueprint:** [docs/README](docs/README)
- **Agents blueprint:** [agents/README](agents/README)

Use the **sidebar** for the full mirrored tree.

## HTML handbook (not duplicated in the wiki)

The SDLC **handbook** (`sdlc/docs/*.html`, diagrams, nav) is not converted to wiki pages. Open on GitHub or clone the repo and open locally, e.g. [`sdlc/docs/index.html`](https://github.com/autowww/blueprints/blob/main/sdlc/docs/index.html).

## Use in your product repo

**Copy** or **submodule** the blueprint package; bootstrap `sdlc/` with [`sdlc/scripts/init-sdlc-workspace.sh`](https://github.com/autowww/blueprints/blob/main/sdlc/scripts/init-sdlc-workspace.sh) (see [sdlc/SDLc-WORKSPACE](sdlc/SDLc-WORKSPACE)).

## Update this wiki from your machine

From a clone of **`autowww/blueprints`** (with GitHub push access to the wiki):

```bash
./wiki-source/sync-wiki.sh
```

One-time: create the first wiki page named **Home** on GitHub so `blueprints.wiki.git` exists — see [`wiki-source/README.md`](https://github.com/autowww/blueprints/blob/main/wiki-source/README.md).
