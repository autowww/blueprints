---
nav_title: "Setup profile: Bootstrap"
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Project setup profile — Bootstrap (steps 1–3)

## What it is

The first phase of the [Project setup profile](SETUP.md): get **`blueprints/`** on disk, **`docs/`** as needed, and a project **`sdlc/`** workspace.

## When to use it

As the first block of the full checklist after [First hour](quickstarts/first-hour.md) or alongside it.

## Prerequisites

- **`blueprints/`** at the **repository root** (see [Prerequisites (project setup checklist)](SETUP.md#prerequisites)).

## Steps

1. **Submodule** — Ensure `blueprints/` is present; `git submodule update --init` so `blueprints/sdlc` exists.
2. **Documentation tree (as needed)** — Create `docs/` per the [layout template on GitHub](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md).
3. **Project `sdlc/` workspace** — From repo root:  
   `./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Project Name"`  
   Context and layout: [`SDLc-WORKSPACE.md`](SDLc-WORKSPACE.md).

## How to verify success

- `test -f blueprints/sdlc/README.md` from repo root.
- Project `sdlc/README.md` exists and describes **your** project (not edits under frozen `blueprints/sdlc/`).

## What to do next

- [Setup profile: Forge and Cursor](setup-profile-forge-cursor.md) (steps 4–11)
- [Project setup profile](SETUP.md) — full overview
