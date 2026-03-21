# Templates (`blueprints/ide/templates/`)

All files that `init-ide-workspace.sh` copies into a consuming project. Files named `*.template.*` have the `.template.` segment stripped during copy and `{{PROJECT_NAME}}` replaced with the project name.

| Directory | Contents | Target in project |
|-----------|----------|-------------------|
| *(root)* | `AGENTS.template.md`, `CLAUDE.template.md` | `AGENTS.md`, `CLAUDE.md` at project root |
| `cursor/rules/` | `.mdc` rule templates | `.cursor/rules/` |
| `cursor/commands/` | Command templates | `.cursor/commands/` |
| `claude/skills/` | Skill templates | `.claude/skills/` |
| `claude/agents/` | Subagent definitions | `.claude/agents/` |
| `plans/` | Plan convention docs + plan template | `.cursor/plans/` (template only) |

See [`../STRUCTURE.md`](../STRUCTURE.md) for the full mapping table.
