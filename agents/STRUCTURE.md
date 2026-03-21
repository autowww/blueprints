# Agents blueprint — structure & layers

This document is the **canonical Markdown** for the **agents & automation** blueprint (containerized recipes and workspace layout). The **human handbook** in **`blueprints/sdlc/docs/agents.html`** expands the same material for browser reading — including how this fits **agentic** delivery; keep them aligned when you change either.

**Related:** [`README.md`](README.md) · [`POLICY.md`](POLICY.md) · [`blueprints/sdlc/DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md) · [`blueprints/sdlc/SDLC.md`](../sdlc/SDLC.md) §7.

---

## 1. Purpose

| Goal | Means |
|------|--------|
| **Isolation** | Run automation (linters, codegen, browser tests, optional LLM tool loops) in **Linux containers** so host environments stay predictable. |
| **Repeatability** | Same image + same mount points → same behavior in CI and locally. |
| **Separation** | **Frozen** patterns in **`blueprints/agents/`**; **mutable** jobs in **`agents/`**. |

This blueprint does **not** mandate a particular LLM vendor or multi-agent framework. It defines **where** Docker fits and **how** recipes connect to CI.

**Relationship to `blueprints/ide/`:** The agents blueprint covers **containerized execution** (server-side, CI). For **IDE agent instructions** (Cursor rules, Claude skills, commands, plan convention), see [`blueprints/ide/`](../ide/README.md) and handbook [`ide.html`](../sdlc/docs/ide.html).

---

## 2. Conceptual layers (outside → inside)

| Layer | What it is | Typical artifacts |
|-------|------------|-------------------|
| **L1 — Policy** | Immutability + boundaries | [`POLICY.md`](POLICY.md), [`blueprints/sdlc/POLICY.md`](../sdlc/POLICY.md) |
| **L2 — Repository layout** | Frozen blueprint vs mutable workspace | `blueprints/agents/` vs `agents/` |
| **L3 — Container image** | Base OS + runtimes | [`docker/Dockerfile.base`](docker/Dockerfile.base) |
| **L4 — Orchestration** | Build/run wiring | [`docker/compose.yaml`](docker/compose.yaml), optional `agents/compose.override.yaml` |
| **L5 — Recipes** | One folder per job | `agents/recipes/<name>/run.sh` (or Makefile, Node, Python) |
| **L6 — Optional LLM runner** | Tool-calling loop *inside* the container | Small Python/Node app in `agents/runner/` — **only if** you need open-ended automation |

**Rule of thumb:** Most teams use **L1–L5** only. **L6** is optional and increases operational and security surface.

---

## 3. Directory layout (frozen vs mutable)

### 3.1 Frozen (`blueprints/agents/`)

```text
blueprints/agents/
  POLICY.md
  README.md
  STRUCTURE.md
  docker/
    Dockerfile.base
    compose.yaml
    .dockerignore
    README.md
  templates/
    recipe/
    project-agents/
  scripts/
    README.md
  docs/
    README.md
    index.html
    MAINTENANCE.md
```

### 3.2 Mutable (`agents/` — in consuming repo)

```text
agents/
  README.md              # Team conventions
  workspaces/            # Gitignored scratch output (optional)
  recipes/
    <recipe-name>/
      run.sh
      README.md
  compose.override.yaml  # Optional: bind mounts, env_file, profiles
```

---

## 4. Docker specifics

### 4.1 Base image (`Dockerfile.base`)

- **Default stack:** Node 20 (Debian slim) + `git`, `curl`, `jq`.  
- **Playwright:** Either install browser deps in a **derived** Dockerfile, or use Microsoft’s **`mcr.microsoft.com/playwright`** image in a separate recipe-specific Dockerfile — document the choice in `agents/recipes/<name>/README.md`.  
- **Python-heavy tasks:** Prefer a **second** image or multi-stage build so Node-only recipes stay small.

### 4.2 Compose

- **Build context:** `blueprints/agents/` (see [`docker/compose.yaml`](docker/compose.yaml)).  
- **Runtime mounts (pattern):**
  - Repository: **`/work`** read-only when possible.  
  - Writable outputs: **`/workspaces`** → `agents/workspaces/` on the host.  
- **Profiles:** Use Compose [profiles](https://docs.docker.com/compose/how-tos/profiles/) for heavy images (e.g. browser) so default CI stays lean.

### 4.3 Resource hints

- **Chromium / Playwright:** Increase shared memory (`shm_size`) when running headed or heavy pages.  
- **CI:** Match CPU/memory to your worst-case recipe.

---

## 5. Recipes and jobs

| Concern | Guideline |
|---------|-----------|
| **Naming** | `kebab-case` per recipe folder; one primary `run.sh` or documented `Makefile` target. |
| **Inputs** | Read from `/work` (repo); never assume host paths outside mounts. |
| **Outputs** | Write under **`agents/workspaces/`** or CI artifacts directory. |
| **Secrets** | Never bake into images; inject via **environment** in CI or local `env` files (gitignored). |
| **Determinism** | Pin tool versions (`package.json`, `playwright.config`, lockfiles) in the recipe. |

---

## 6. Security and compliance

| Topic | Practice |
|-------|----------|
| **Least privilege** | Run containers as non-root when possible; read-only root FS where supported. |
| **Secrets** | CI secret stores; short-lived tokens; no keys in Compose files committed to Git. |
| **Network** | Restrict outbound in CI if recipes do not need the public internet. |
| **Supply chain** | Pin base image digests in security-sensitive pipelines. |

---

## 7. SDLC mapping

| SDLC phase | How this blueprint shows up |
|------------|---------------------------|
| **Discover / specify** | Decide which automation belongs in **recipes** vs plain CI steps. |
| **Build** | Recipes run locally or in CI using the same image. |
| **Verify** | Browser/E2E recipes attach to **quality gates** (see [`SDLC.md`](../sdlc/SDLC.md) §7). |
| **Release** | Optional release-only recipes (e.g. artifact smoke tests) — document in `docs/development/`. |

---

## 8. Evolution and scaling

| Stage | Approach |
|-------|----------|
| **Single project** | One base image + a few shell recipes. |
| **Growing** | Split images per stack (Node vs Playwright vs Python); use Compose profiles. |
| **Monorepo** | Mount **package subpaths** or run recipes from subdirectory with `WORKDIR` per job. |

---

## 9. Bootstrap and scaffold scripts

**Workspace** — from repository root:

```bash
./blueprints/agents/scripts/init-agents-workspace.sh
```

Creates **`agents/`** with README, **`workspaces/`**, and **`recipes/`** from [`templates/project-agents/`](templates/project-agents/README.md).

**New recipe** — after **`agents/`** exists:

```bash
./blueprints/agents/scripts/new-agent-recipe.sh <kebab-case-name> [--purpose "one line"]
```

Creates **`agents/recipes/<name>/README.md`** and **`run.sh`** from [`templates/recipe/*.template.*`](templates/recipe/README.md).

**Playbook for assistants:** [`ORCHESTRATION.md`](ORCHESTRATION.md). See [`scripts/README.md`](scripts/README.md).

---

## 10. Handbook alignment

When you change this file or [`README.md`](README.md), update **`blueprints/sdlc/docs/agents.html`** and bump footer dates per **`blueprints/sdlc/docs/MAINTENANCE.md`**.

---

*Template — adapt paths and image names to your organization.*
