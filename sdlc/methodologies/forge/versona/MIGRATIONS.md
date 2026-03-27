# Versona migrations

When **blueprints** changes Versona **session** layouts, **manifest** fields, or **challenge report** shapes, consuming repos may need to adjust existing `forge-logs/versona/**` trees or local conventions.

## Cursor rules (`.mdc`)

- **No automatic rewrite** of `.cursor/rules/` — use [`../setup/install-versona-cursor-rules.sh`](../setup/install-versona-cursor-rules.sh) after `git submodule update`, then [`../setup/diff-versona-cursor-rules.sh`](../setup/diff-versona-cursor-rules.sh) before `--force`.
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
| *(none yet)* | — | — |
