# Recipe template

**Automated scaffold** (from repo root):

```bash
./blueprints/agents/scripts/new-agent-recipe.sh <kebab-case-name> [--purpose "one line"]
```

That copies from **`README.template.md`** and **`run.sh.template`** into **`agents/recipes/<name>/`**.

**Manual copy:** duplicate this folder’s ideas into **`agents/recipes/<recipe-name>/`** and adjust `run.sh`.

- **`run.sh`** — entrypoint executed **inside** the container; repo is **`/work`** when you mount per [`../../STRUCTURE.md`](../../STRUCTURE.md) §4.  
- Keep recipes **idempotent** where possible; write outputs to **`agents/workspaces/<recipe-name>/`**, not into tracked source unless the recipe is explicit codegen.

**Playbook:** [`../../ORCHESTRATION.md`](../../ORCHESTRATION.md).
