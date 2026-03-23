# Agents blueprint (automation)

This folder is a **reusable, product-agnostic** package for **engineering automation**: **foundational Docker images**, **Compose patterns**, and **templates** for isolated, repeatable jobs (shell scripts, browser runners, optional LLM tool loops). It is the **execution layer** for work that fits the repo’s **agentic** and **CI** policies — not the place for SDLC process prose (see **`blueprints/sdlc/`**, including [**`methodologies/agentic-sdlc.md`**](../sdlc/methodologies/agentic-sdlc.md)) or product functional specs (see **`blueprints/product/`**).

**Governance:** read [`POLICY.md`](POLICY.md) — **do not change** this directory unless explicitly updating the baseline. Project automation lives in **`agents/`** (mutable) at repository root when you adopt this blueprint.

| Deliverable | Purpose |
|-------------|---------|
| [**POLICY.md**](POLICY.md) | Immutability rules for this blueprint. |
| [**STRUCTURE.md**](STRUCTURE.md) | Layers (conceptual → Docker → recipes → CI), security, adoption. |
| [**ORCHESTRATION.md**](ORCHESTRATION.md) | **Canonical** steps to create recipes under **`agents/`**; assistants and Cursor rules should point here. |
| [**docker/**](docker/README.md) | Foundational **`Dockerfile.base`**, **`compose.yaml`**, ignore rules. |
| [**templates/**](templates/README.md) | **Recipe** stub and **mutable `agents/`** workspace seed. |
| [**scripts/**](scripts/README.md) | **`init-agents-workspace.sh`**, **`new-agent-recipe.sh`** — see [`scripts/README.md`](scripts/README.md). |
| [**docs/**](docs/README.md) | Maintainer notes for handbook generation (`website/agents--*.html` via **`generator/build-handbook.py`**). |

## What does *not* belong here

- API keys, tokens, `.env` with secrets, or project-specific URLs — use **`agents/`** (gitignored patterns) and CI secret stores.  
- Application source code — stays in your product tree (`app/`, `src/`, etc.).  
- Frozen SDLC text — **`blueprints/sdlc/`** only.

## How to adopt

1. Keep this folder at **repository root** as **`blueprints/agents/`** (or copy the subtree).  
2. Add **`agents/`** (mutable): run **`./blueprints/agents/scripts/init-agents-workspace.sh`** from repo root, or copy [`templates/project-agents/`](templates/project-agents/README.md) manually.  
3. New recipes: follow [**`ORCHESTRATION.md`**](ORCHESTRATION.md); scaffold with **`./blueprints/agents/scripts/new-agent-recipe.sh <name> [--purpose "..."]`**.  
4. From **`docs/INDEX.md`** (or root `README.md`) and **`blueprints/sdlc/README.md`**, link to **`blueprints/agents/README.md`**.  
5. **Handbook (browser):** generated under **`blueprints/website/`** (e.g. `agents--index.html`) by **`generator/build-handbook.py`**; canonical Markdown: [`STRUCTURE.md`](STRUCTURE.md), [`DOCUMENTATION-STRUCTURE.md`](../sdlc/DOCUMENTATION-STRUCTURE.md).  
6. **Build** the base image: `docker compose -f blueprints/agents/docker/compose.yaml build` (from repo root).

---

*Blueprint — no project-specific content.*
