---
name: assemble-versona-evidence-pack
description: >
  Collect verify/release evidence into forge/evidence/<pack-id>: index, pointers to logs,
  and optional recipe-driven exports. Cognition layout; heavy file copies may use the paired recipe template.
---

# Assemble Versona evidence pack (Forge)

## When to use

- **Assay Gate**, audit prep, or **§5 evidence_obligations** need a **single pack root**.
- Security / compliance / testing Versonas close a loop with **traceable artifacts**.

## Steps

1. **Choose `pack-id`** — Often Spark id, release id, or ticket slug ([`ARTIFACT-CONTRACTS.md`](../../../../methodologies/forge/versona/ARTIFACT-CONTRACTS.md) §3.7).
2. **Create `forge/evidence/<pack-id>/`** — Add `INDEX.md` (human) listing: artifact path, owner, date, scope.
3. **Register sources** — Link to CI runs, `agents/workspaces/<recipe>/`, session `outputs/`, ADRs — avoid duplicating large binaries; use **hashes** or CI URLs where policy allows.
4. **Optional recipe** — For scripted assembly, copy blueprint template [`versona-evidence-pack-assemble`](../../../../../agents/templates/recipe/versona-evidence-pack-assemble/README.md) into **`agents/recipes/`** and run in CI/local; then point `artifact-manifest.json` at outputs.
5. **Ember Log** — If the pack **records a release or risk acceptance**, append Ember Log per [`record-versona-event`](../record-versona-event/SKILL.md).

## Minimal INDEX.md skeleton

```markdown
# Evidence pack: <pack-id>

| Artifact | Path | Notes |
|----------|------|-------|
| … | … | … |
```

## Install

Copy to **`.cursor/skills/assemble-versona-evidence-pack/`**.

## References

- [`VERSONA-EXECUTION-TASKLETS.md`](../../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md)
- [`export-versona-kitchensink-diagram`](../export-versona-kitchensink-diagram/SKILL.md) — SVG exports into pack or session
