# Versona-owned execution tasklets (Docker / browser / API)

**Cognition tasklets** (Cursor rules) live under Forge [`tasklets/`](../../sdlc/methodologies/forge/tasklets/README.md). **Execution tasklets** are **recipes** or wrappers that run **outside** the IDE LLM and return **artifacts** (files, logs, exit codes) for a Versona or human to review.

## Pattern

1. **Versona or meta-agent** defines **inputs**, **success criteria**, and **expected artifacts** (e.g. `export.pdf`, `screenshots/`, `run.log`).
2. **Recipe** under `agents/recipes/<name>/` implements the run (see [`ORCHESTRATION.md`](../ORCHESTRATION.md)).
3. **Cursor / CI** invokes the recipe; the **LLM** does not replace the container — it **interprets** outputs.

```blueprint-diagram
key: swimlane
alt: Pattern
title: Execution tasklet swimlanes
summary: Cognition defines criteria and artifacts; recipes run outside the IDE and return reviewable outputs.
node: Pattern
detail: The split between cognition tasklets and execution recipes on this page.
more: Cognition tasklets live under Forge tasklets in Cursor; execution tasklets are recipes that run outside the IDE LLM.
node: Lane A
detail: The execution plane where bounded recipes produce concrete artifacts.
node: handoff
detail: Cursor or CI invokes the recipe with project-specific inputs.
more: The LLM does not replace the container; it passes inputs and later interprets returned files and exit codes.
node: shared outcome
detail: Expected artifacts land as files, logs, or exit codes for review.
more: Versona or meta-agent defined inputs, success criteria, and expected paths before the run.
node: Lane B
detail: The review plane where Versona or human interprets run outputs.
node: inspect / adapt
detail: Reviewers read artifacts against the defined success criteria.
more: The LLM interprets outputs rather than re-running the recipe; gaps trigger bounded adaptation.
node: feedback
detail: Findings fold back into inputs, criteria, or the next recipe invocation.
fallback_ascii: |
  Pattern

  Lane A ──► handoff ──► shared outcome
  Lane B ──► inspect / adapt ──► feedback
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

After the run, register concrete paths in a session **`artifact-manifest.json`** when the team adopts optional schemas — see [`../../sdlc/methodologies/forge/schemas/artifact-manifest.schema.json`](../../sdlc/methodologies/forge/schemas/artifact-manifest.schema.json) and [`../../sdlc/methodologies/forge/VERSONA-OPERATING-MODEL.md`](../../sdlc/methodologies/forge/VERSONA-OPERATING-MODEL.md) §2.

## Security

- **No secrets** in blueprint Markdown. Use CI secrets and **gitignored** `.env` patterns per [`POLICY.md`](../POLICY.md).
- **Network** and **browser** recipes are **high risk** — restrict images, cap runtime, log URLs.

## Related

- [`STRUCTURE.md`](../STRUCTURE.md) — L5 recipes, L6 optional runner
- [`sdlc/methodologies/forge/tasklets/TASKLET-TAXONOMY.md`](../../sdlc/methodologies/forge/tasklets/TASKLET-TAXONOMY.md) — execution plane row
- [`sdlc/methodologies/forge/versona/VERSONA-SKILL-MATRIX.md`](../../sdlc/methodologies/forge/versona/VERSONA-SKILL-MATRIX.md) — which Versona uses which Skill vs recipe
- Blueprint **stub templates** (copy to `agents/recipes/`): [`../templates/recipe/versona-evidence-pack-assemble/`](../templates/recipe/versona-evidence-pack-assemble/README.md), [`../templates/recipe/versona-kitchensink-diagram-export/`](../templates/recipe/versona-kitchensink-diagram-export/README.md)
