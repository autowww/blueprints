# Scripts

| Script | Purpose |
|--------|---------|
| [**`init-agents-workspace.sh`**](init-agents-workspace.sh) | Create **`agents/`** at repo root from [`../templates/project-agents/`](../templates/project-agents/README.md). |
| [**`new-agent-recipe.sh`**](new-agent-recipe.sh) | Create **`agents/recipes/<name>/`** (`README.md` + `run.sh`) from [`../templates/recipe/*.template.*`](../templates/recipe/README.md). See [**`../ORCHESTRATION.md`**](../ORCHESTRATION.md). |

**Usage (from repository root):**

```bash
./blueprints/agents/scripts/init-agents-workspace.sh
./blueprints/agents/scripts/init-agents-workspace.sh my-automation-dir
./blueprints/agents/scripts/init-agents-workspace.sh --force   # overwrite README and template files
```

Additional **helpers** may live here — e.g. `print-compose-run.sh` that echoes a `docker compose run` line with correct mounts — without storing project secrets.

Consuming repos may symlink or copy scripts into **`scripts/`** at repo root.

**Suggested conventions**

- Scripts accept **`REPO_ROOT`** (default: current directory) and **`IMAGE`** (default: `agents-blueprint-base:local`).  
- Never print secrets; read tokens from the environment inside CI only.
