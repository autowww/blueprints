# Scripts (`blueprints/ide/scripts/`)

Helpers for **consuming repos**. Run from the **repository root** (where `blueprints/ide/` lives).

## `init-ide-workspace.sh`

Creates or refreshes IDE agent instruction files from [`../templates/`](../templates): copies Cursor rules, commands, Claude skills, subagent definitions, plan template, and renders `AGENTS.md` + `CLAUDE.md` at project root with `{{PROJECT_NAME}}` replaced.

**Requires:** `bash`, `sed`.

**Usage:**

```bash
# Full bootstrap (Cursor + Claude)
./blueprints/ide/scripts/init-ide-workspace.sh "My Product Name"

# Cursor only
./blueprints/ide/scripts/init-ide-workspace.sh "My Product Name" --cursor-only

# Claude Code only
./blueprints/ide/scripts/init-ide-workspace.sh "My Product Name" --claude-only

# Overwrite existing files
./blueprints/ide/scripts/init-ide-workspace.sh "My Product Name" --force
```

**Related:** [`../README.md`](../README.md) · [`../STRUCTURE.md`](../STRUCTURE.md) (template → project mapping).

---

*Part of [`blueprints/ide/README.md`](../README.md).*
