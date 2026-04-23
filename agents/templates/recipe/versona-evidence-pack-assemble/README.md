---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Template recipe: `versona-evidence-pack-assemble`

**Purpose:** **Execution-plane** stub for assembling **`forge/evidence/<pack-id>/`** from CI or a local runner: create `INDEX.md`, optionally copy or hash-listed artifacts into the pack directory. The **LLM** does not replace this job — it **reviews** outputs.

**Cognition counterpart:** Cursor Skill **`assemble-versona-evidence-pack`** ([`SKILL.md`](../../../../sdlc/templates/forge/cursor-skills/assemble-versona-evidence-pack/SKILL.md)) defines layout and INDEX expectations.

## Non-goals

- Not a compliance auditor — does **not** certify controls.
- No secrets in repo — env vars **names only** in README you ship.

## Adoption

1. Copy this folder to **`agents/recipes/versona-evidence-pack-assemble/`** at the consuming repo root (see [`ORCHESTRATION.md`](../../ORCHESTRATION.md)).
2. Replace **`run.sh`** stub with real steps (e.g. copy CI artifacts, compute checksums, write `INDEX.md`).
3. Write outputs under **`agents/workspaces/versona-evidence-pack-assemble/`** or directly into **`forge/evidence/<pack-id>/`** per team policy; register paths in session **`artifact-manifest.json`** when used.

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| `EVIDENCE_PACK_ID` | Recommended | Slug for `forge/evidence/<id>/` |
| `REPO_ROOT` | Optional | Default: `/work` in Docker |

## Usage

```bash
# After copy to agents/recipes/…
./run.sh --pack-id my-release-2026-04-11
```

Default stub prints **next steps** and exits `0`.

## See also

- [`VERSONA-EXECUTION-TASKLETS.md`](../../docs/VERSONA-EXECUTION-TASKLETS.md)
- [`ARTIFACT-CONTRACTS.md`](../../../../sdlc/methodologies/forge/versona/ARTIFACT-CONTRACTS.md) §3.7
