# Blueprints wiki

Human-friendly **entry point**. Canonical sources live in the **[code repository](https://github.com/autowww/blueprints)** (`main`).

## Start here

| Topic | In-repo |
|--------|---------|
| **SDLC blueprint** (policy, phases, DoD) | [`sdlc/README.md`](https://github.com/autowww/blueprints/blob/main/sdlc/README.md) |
| **Single-file overview** | [`sdlc/SDLC.md`](https://github.com/autowww/blueprints/blob/main/sdlc/SDLC.md) |
| **HTML handbook** (clone repo and open locally, or browse on GitHub) | [`sdlc/docs/index.html`](https://github.com/autowww/blueprints/blob/main/sdlc/docs/index.html) |
| **Methodologies** | [`sdlc/methodologies/README.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/README.md) |
| **Roles & archetypes** | [`sdlc/methodologies/roles-archetypes.md`](https://github.com/autowww/blueprints/blob/main/sdlc/methodologies/roles-archetypes.md) · [handbook chapter](https://github.com/autowww/blueprints/blob/main/sdlc/docs/methodologies-roles.html) |
| **Product docs blueprint** | [`docs/README.md`](https://github.com/autowww/blueprints/blob/main/docs/README.md) |
| **Agents & automation** | [`agents/README.md`](https://github.com/autowww/blueprints/blob/main/agents/README.md) |

## Use in your product repo

**Copy** or **submodule** this package next to your project tree. Bootstrap a project `sdlc/` workspace with [`sdlc/scripts/init-sdlc-workspace.sh`](https://github.com/autowww/blueprints/blob/main/sdlc/scripts/init-sdlc-workspace.sh) (see [`sdlc/SDLc-WORKSPACE.md`](https://github.com/autowww/blueprints/blob/main/sdlc/SDLc-WORKSPACE.md)).

## Maintain this wiki

Source pages live under **`wiki-source/`** in the main repo. After a one-time **Create the first page** on GitHub (see [`wiki-source/README.md`](https://github.com/autowww/blueprints/blob/main/wiki-source/README.md)), run **`wiki-source/publish-wiki.sh`** from a clone of `autowww/blueprints`, or copy `Home.md` / `_Sidebar.md` into a clone of `https://github.com/autowww/blueprints.wiki.git`.
