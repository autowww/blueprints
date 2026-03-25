# Versona-owned execution tasklets (Docker / browser / API)

**Cognition tasklets** (Cursor rules) live under Forge [`tasklets/`](../../sdlc/methodologies/forge/tasklets/README.md). **Execution tasklets** are **recipes** or wrappers that run **outside** the IDE LLM and return **artifacts** (files, logs, exit codes) for a Versona or human to review.

## Pattern

1. **Versona or meta-agent** defines **inputs**, **success criteria**, and **expected artifacts** (e.g. `export.pdf`, `screenshots/`, `run.log`).
2. **Recipe** under `agents/recipes/<name>/` implements the run (see [`ORCHESTRATION.md`](../ORCHESTRATION.md)).
3. **Cursor / CI** invokes the recipe; the **LLM** does not replace the container — it **interprets** outputs.

```ks-diagram
key: swimlane
alt: Diagram
```

## Example manifest (conceptual)

Project-specific JSON or env file passed to the recipe (not frozen in blueprints):

```json
{
  "recipe": "notebooklm-export",
  "inputs": { "source_dir": "docs/product/vision", "template": "exec-brief" },
  "outputs_expected": ["artifacts/deck-spec.json", "artifacts/run.log"],
  "secrets": "env:NOTEBOOKLM_SESSION"
}
```

## Security

- **No secrets** in blueprint Markdown. Use CI secrets and **gitignored** `.env` patterns per [`POLICY.md`](../POLICY.md).
- **Network** and **browser** recipes are **high risk** — restrict images, cap runtime, log URLs.

## Related

- [`STRUCTURE.md`](../STRUCTURE.md) — L5 recipes, L6 optional runner
- [`sdlc/methodologies/forge/tasklets/TASKLET-TAXONOMY.md`](../../sdlc/methodologies/forge/tasklets/TASKLET-TAXONOMY.md) — execution plane row
