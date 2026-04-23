---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Recipe template

**Automated scaffold** (from repo root):

```bash
./blueprints/agents/scripts/new-agent-recipe.sh <kebab-case-name> [--purpose "one line"]
```

That copies from **`README.template.md`** and **`run.sh.template`** into **`agents/recipes/<name>/`**.

**Manual copy:** duplicate this folder’s ideas into **`agents/recipes/<recipe-name>/`** and adjust `run.sh`.

**Optional AI diff review:** subfolder **[`llm-diff-review/`](llm-diff-review/README.md)** — OpenAI-compatible HTTP API, `curl` + `jq` only; see [`agentic-coding-standards.md`](../../../sdlc/methodologies/agentic-coding-standards.md).

**Optional Playwright E2E:** subfolder **[`playwright-e2e/`](playwright-e2e/README.md)** — `npm` + `@playwright/test` in **[`Dockerfile.playwright`](../../docker/Dockerfile.playwright)**; see [`PLAYWRIGHT-INFRASTRUCTURE.md`](../../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md).

**Optional Versona execution (stubs):** **[`versona-evidence-pack-assemble/`](versona-evidence-pack-assemble/README.md)** (CI/local evidence folder assembly) · **[`versona-kitchensink-diagram-export/`](versona-kitchensink-diagram-export/README.md)** (headless diagram/SVG export). Copy into **`agents/recipes/`** per [`ORCHESTRATION.md`](../../ORCHESTRATION.md); cognition side: [`VERSONA-SKILL-MATRIX.md`](../../../sdlc/methodologies/forge/versona/VERSONA-SKILL-MATRIX.md).

- **`run.sh`** — entrypoint executed **inside** the container; repo is **`/work`** when you mount per [`../../STRUCTURE.md`](../../STRUCTURE.md) §4.  
- Keep recipes **idempotent** where possible; write outputs to **`agents/workspaces/<recipe-name>/`**, not into tracked source unless the recipe is explicit codegen.

**Playbook:** [`../../ORCHESTRATION.md`](../../ORCHESTRATION.md).
