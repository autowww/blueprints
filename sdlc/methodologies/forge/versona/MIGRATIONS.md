---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona migrations

When **blueprints** changes Versona **session** layouts, **manifest** fields, or **§5 report** shapes, consuming repos may need to adjust existing `forge-logs/versona/**` trees or local conventions.

## Cursor rules (`.mdc`)

- **No automatic rewrite** of `.cursor/rules/` — after `git submodule update`, run [`../setup/sync-forge-cursor-rules.sh`](../setup/sync-forge-cursor-rules.sh) `diff --preset recommended` (or `status`) before `sync … --force`. See [`../setup/CURSOR-RULES-QUICKSTART.md`](../setup/CURSOR-RULES-QUICKSTART.md).
- Local **globs** or edits in installed `.mdc` files are overwritten by `--force`; re-apply custom globs after sync if needed.

## Session folders and manifests

- Optional field **`versona_session_schema_version`** (see [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §7.4) lets teams and tools record which manifest/session shape a folder uses.
- When blueprints publishes a **breaking** change, this file should gain a short **versioned** subsection: what changed, how to patch `SESSION.md` / `session.manifest.yaml`, and whether AI-assisted migration is appropriate (**human review** required).

### Playbook (generic)

1. Identify sessions under `forge-logs/versona/<actor>/<session-id>/`.
2. Compare folder contents to current templates: [`../../templates/forge/versona-session.template.md`](../../templates/forge/versona-session.template.md), [`../../templates/forge/session.manifest.yaml.template`](../../templates/forge/session.manifest.yaml.template).
3. Update frontmatter / YAML to match; set or bump `versona_session_schema_version` if your team adopts it.
4. Commit with a message referencing the blueprint commit or release.

## Changelog entries

Add a row here when session or manifest **contracts** change in a way that affects existing files:

| Blueprint change (summary) | Affected artifacts | Migration hint |
|----------------------------|-------------------|----------------|
| Terminology: “Versona challenge” → sessions / §5 structured output; example heading `## {Discipline} Versona — structured output`; **Review depth** replaces “Challenge intensity”; Cursor skill folder `run-product-versona-challenge` → `run-product-versona-session` | Installed `.mdc` rules; day journal / planning templates; copied skills; historical session markdown under `outputs/` | Old headings in saved logs are still readable; optional rename for consistency. Re-copy skill from `sdlc/templates/forge/cursor-skills/run-product-versona-session/`. Re-sync Versona rules from blueprints. |
