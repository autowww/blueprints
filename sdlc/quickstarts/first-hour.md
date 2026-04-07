---
nav_title: First hour in your repository
nav_group: onboarding
public_publish: true
audience: public
handbook_area: blueprints
learning_level: overview
---

# First hour in your repository

## What it is

A single sitting (~**60 minutes**) to get **`blueprints/`**, a project **`sdlc/`** workspace, a minimal **Forge** layout, and **Cursor** rules aligned with the recommended preset. Each numbered step below ends with something you can verify before moving on.

## When to use it

Use this guide after you intend to use Blueprints at the **repository root** (next to `sdlc/`, `docs/`, `forge/`). For *which adoption story* matches you first, see [**Adopting Blueprints**](../adopting-blueprints.md).

**Not covered here:** choosing an ICP adopter path (solo vs team vs org) — see [**Adopting Blueprints**](../adopting-blueprints.md). Maintainer plans and milestones — on GitHub: [Roadmap](https://github.com/autowww/blueprints/blob/main/docs/ROADMAP.md).

### First-hour sequence (visual)

```blueprint-diagram
key: linear
alt: First hour — submodule in place, then project sdlc, Forge, Cursor rules, optional Forge Studio
```

## Prerequisites

- **Git** and **bash** available.
- A **repository checkout** where you can run commands from the **repository root** (the folder that will contain `blueprints/`).
- **Python 3** available (used by Forge init and Cursor rule sync scripts).

## Steps

### Before you start

Decide that **`blueprints/` will live at the repository root** next to `sdlc/`, `docs/`, and (after this guide) `forge/`. The stock scripts assume that layout.

**Why this layout:** scripts such as `init-sdlc-workspace.sh` and `forge-init.sh` resolve paths from the **repository root**. Nesting `blueprints/` elsewhere would require custom wrappers not covered here.

### 1. Get the blueprint on disk

If you have not already, add Blueprints as a **git submodule** at `blueprints/` (or ensure a copy of the tree exists there). Initialize submodules so `blueprints/sdlc/` is present:

```bash
git submodule update --init --recursive
```

### 2. Create the project `sdlc/` workspace

From the **repository root**, run (replace the quoted name with your project label):

```bash
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "Your project name"
```

### 3. Initialize Forge

Still from the repo root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

Edit `forge/forge.config.yaml` later when you are ready; the [full setup checklist](../SETUP.md) lists questionnaire and alignment steps.

### 4. Install Cursor rules (recommended preset)

From the repo root:

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended
```

For preset options and YAML-only installs, use the handbook page for [Cursor rules — quickstart](../methodologies/forge/setup/CURSOR-RULES-QUICKSTART.md).

Optional audit:

```bash
bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check
```

### 5. Optional: Forge Studio (local workspace UI)

**Forge Studio** is the product name for **Lenses Studio** — the React UI at `/studio/` on the **forge-lenses** server. It is a **separate** public repository ([**autowww/forge-lenses**](https://github.com/autowww/forge-lenses)); it does not ship inside `blueprints/`. The same project’s **user guides** (Lenses, Forge Studio, Blueprints Wizard) are published read-only at [blueprints.forgesdlc.com/lenses](https://blueprints.forgesdlc.com/lenses/index.html); the runnable app stays on your machine.

**Next:** Follow [**Forge Studio quickstart**](forge-studio.md) — clone or submodule, Python venv, run the server, open `/studio/`.

## Example repo (generic)

| | |
|--|--|
| **Starting situation** | New monorepo root `acme-api/`; no `blueprints/` yet; you want Forge + Cursor aligned in one sitting. |
| **Action taken** | Submodule add `blueprints/`, run `init-sdlc-workspace.sh`, `forge-init.sh`, `sync-forge-cursor-rules.sh sync --preset recommended`. |
| **Expected result** | `blueprints/sdlc/README.md`, `sdlc/README.md`, `forge/forge.config.yaml`, and `.cursor/rules` (or synced rules path) exist from the stock scripts. |
| **What to check** | From repo root: `test -f blueprints/sdlc/README.md && test -f sdlc/README.md && test -f forge/forge.config.yaml`; optional Studio only after this passes. |

## How to verify success

| After step | Check |
|------------|--------|
| 1. Get the blueprint | From the repo root, `test -f blueprints/sdlc/README.md` exits `0`. |
| 2. Project `sdlc/` | `sdlc/README.md` exists and describes **your** project — not edits under `blueprints/sdlc/` (frozen baseline). |
| 3. Forge | `forge/forge.config.yaml` exists and `ember-logs/` (or paths created by the script) are present. |
| 4. Cursor rules | The sync script completes without error; optional: `… check` passes. |
| 5. Optional Forge Studio | With the server running on the default port, [http://127.0.0.1:8080/studio/](http://127.0.0.1:8080/studio/) should load (see the Forge Studio quickstart if it does not). `GET /api/workspace-state` returns JSON for a quick check. |

## Common mistakes

| Mistake | What to do |
|---------|------------|
| Running scripts from a subfolder of the repo | `cd` to the **repository root** (the directory that will list `blueprints/`, `sdlc/`, …) and re-run |
| Editing files under `blueprints/` for product-specific wording | Move that text to project **`sdlc/`** or **`docs/`**; see [Policy](../POLICY.md) |
| Skipping `git submodule update` after clone | Run `git submodule update --init --recursive` so `blueprints/sdlc/` exists |
| Expecting Forge Studio inside `blueprints/` | Forge Studio is the **forge-lenses** app — see [Forge Studio quickstart](forge-studio.md) |

### Worked example (generic)

| Stage | Situation | Action | What to check |
|-------|-----------|--------|----------------|
| Start | Fresh clone; `blueprints/` empty | `git submodule update --init --recursive` | `test -f blueprints/sdlc/README.md` |
| Middle | Forge init done | Open `forge/forge.config.yaml`; fill questionnaire when ready | YAML parses; paths exist |
| Done | Team wants Cursor help | `sync-forge-cursor-rules.sh sync --preset recommended` | `… check` passes if you gate on it |

## What to do next

- **Full ordered checklist** (submodule through optional product flows): [Project setup profile](../SETUP.md).
- **ICP paths** (which adoption story matches you): [**Adopting Blueprints**](../adopting-blueprints.md).
- **Documentation layout** in the consuming repo — full template reference on GitHub: [`sdlc/DOCUMENTATION-STRUCTURE.md`](https://github.com/autowww/blueprints/blob/main/sdlc/DOCUMENTATION-STRUCTURE.md).