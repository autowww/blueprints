# First hour in your repository

**Time to complete:** about 60 minutes  

**You’ll have:** `blueprints/` on disk, a project **`sdlc/`** workspace, a minimal **Forge** layout, and **Cursor** rules aligned with the recommended preset — each step ends with something you can verify.

**Not covered here:** choosing an ICP adopter path (solo vs team vs org) — see [Adopting Blueprints](../../docs/ADOPTION.md). Maintainer plans and milestones — see [Roadmap](../../docs/ROADMAP.md).

## Prerequisites

- **Git** and **bash** available.
- A **repository checkout** where you can run commands from the **repository root** (the folder that will contain `blueprints/`).
- **Python 3** available (used by Forge init and Cursor rule sync scripts).

## Before you start

Decide that **`blueprints/` will live at the repository root** next to `sdlc/`, `docs/`, and (after this guide) `forge/`. The stock scripts assume that layout.

## 1. Get the blueprint on disk

If you have not already, add Blueprints as a **git submodule** at `blueprints/` (or ensure a copy of the tree exists there). Initialize submodules so `blueprints/sdlc/` is present:

```bash
git submodule update --init --recursive
```

**Verify:** From the repo root, `test -f blueprints/sdlc/README.md` exits `0`.

## 2. Create the project `sdlc/` workspace

From the **repository root**, run (replace the quoted name with your project label):

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Your project name"
```

**Verify:** `sdlc/README.md` exists. Optionally open it and confirm it describes **your** project — not edits under `blueprints/sdlc/` (that tree stays the frozen baseline).

## 3. Initialize Forge

Still from the repo root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

**Verify:** `forge/forge.config.yaml` exists and `ember-logs/` (or the paths created by the script) are present. Edit `forge/forge.config.yaml` later when you are ready; the [full setup checklist](../SETUP.md) lists questionnaire and alignment steps.

## 4. Install Cursor rules (recommended preset)

From the repo root:

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended
```

**Verify:** The script completes without error. Optional audit:

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check
```

For preset options and YAML-only installs, use the handbook page for [Cursor rules — quickstart](../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md).

## Go deeper

- **Full ordered checklist** (submodule through optional product flows): [Project setup profile](../SETUP.md).
- **ICP paths** (which adoption story matches you): [Adopting Blueprints](../../docs/ADOPTION.md).
- **Documentation layout** in the consuming repo: [Documentation structure](../DOCUMENTATION-STRUCTURE.md).
