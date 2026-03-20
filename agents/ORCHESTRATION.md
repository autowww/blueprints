# Orchestration — new agent / recipe

**Canonical instructions** for creating automation under **`agents/recipes/<name>/`** in the consuming repository. Cursor rules, docs, and assistants should **point here** instead of duplicating prose.

**Related:** [`STRUCTURE.md`](STRUCTURE.md) · [`docker/README.md`](docker/README.md) · [`scripts/README.md`](scripts/README.md)

---

## 1. Scope

| Term | Meaning |
|------|---------|
| **Agent** (colloquial) | A **recipe**: one folder with an entry script and README, run in Docker or CI. |
| **Where it lives** | **`agents/recipes/<recipe-name>/`** at repository root (not inside `blueprints/agents/`). |
| **Blueprint** | **`blueprints/agents/`** supplies templates, scripts, and this file — **no project secrets or project recipes** in the blueprint tree. |

---

## 2. Prerequisites

1. Repository root contains **`blueprints/agents/`** (this package).
2. **`agents/`** exists — if not, run from repo root:

   ```bash
   ./blueprints/agents/scripts/init-agents-workspace.sh
   ```

3. Scaffold a new recipe (files only):

   ```bash
   ./blueprints/agents/scripts/new-agent-recipe.sh <kebab-case-name> [--purpose "one line"]
   ```

---

## 3. Guided flow (for humans & AI assistants)

Use this **in order** when someone asks to **create a new agent** or **new recipe**. Do not dump large unreviewed blobs; confirm or infer each step.

### Step A — Intent

- **Recipe name** — `kebab-case` (e.g. `ui-e2e`, `docs-lint`). Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`.
- **One-line purpose** — what it does (e.g. “Run Playwright smoke against staging”).
- **Where it runs** — local, CI, or both.

### Step B — Execution shape

- **Entry** — prefer `run.sh` with `set -euo pipefail` unless Node/Python is clearly better.
- **Image** — default **`agents-blueprint-base:local`** ([`docker/Dockerfile.base`](docker/Dockerfile.base)); use a **Playwright** or other **dedicated image** only when browser/heavy deps are required ([`STRUCTURE.md`](STRUCTURE.md) §4).

### Step C — Inputs and outputs

- **Inputs** — read from repo as **`/work`** when run in Docker; document in recipe README.
- **Outputs** — **`agents/workspaces/<recipe-name>/`** or CI artifacts; do not write into tracked source unless the recipe is explicitly codegen.

### Step D — Secrets

- List **environment variable names** only; never commit values. CI: use the platform secret store.

### Step E — Files

After scaffolding with **`new-agent-recipe.sh`**, edit as needed:

- **`agents/recipes/<name>/README.md`** — fill run instructions, env table, CI pointer.
- **`agents/recipes/<name>/run.sh`** — real commands.
- **`agents/README.md`** — add a one-line entry under **Recipes** (if the project keeps an index).

### Step F — Optional Compose

- **`agents/compose.override.yaml`** — extra mounts, `shm_size`, or image overrides; document in the recipe README.

---

## 4. Out of scope (do not promise without explicit setup)

| Topic | Rule |
|-------|------|
| **Consumer NotebookLM** | No stable public API; do not promise reliable automation unless the user accepts fragile browser automation. |
| **NotebookLM Enterprise** | Only via **Google Cloud** documented APIs; treat as a normal API client recipe with GCP auth. |

---

## 5. Scaffold script contract

**[`scripts/new-agent-recipe.sh`](scripts/new-agent-recipe.sh)** must:

- Run from **repository root** (directory that contains **`blueprints/agents/`** and **`agents/`**).
- Create **`agents/recipes/<name>/`** with **`README.md`** and **`run.sh`** from [`templates/recipe/`](templates/recipe/README.md).
- Refuse invalid names or missing **`agents/`**.

---

## 6. Checklist (copy into PR or issue)

- [ ] Recipe name is kebab-case and unique under `agents/recipes/`.
- [ ] README documents purpose, `/work`, workspaces path, env vars.
- [ ] `run.sh` is executable and safe (`set -euo pipefail` for bash).
- [ ] No secrets in repo; CI documented.
- [ ] `agents/README.md` updated if the team indexes recipes.

---

*Keep this file in **`blueprints/agents/`**; mutable recipe bodies stay in **`agents/`**.*
