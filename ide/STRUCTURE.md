# IDE agent instructions — structure & mapping

This document is the **canonical Markdown** for the IDE agent instruction blueprint. The **human handbook** chapter at `blueprints/sdlc/docs/ide.html` expands the same material for browser reading — keep them aligned when you change either.

**Related:** [`README.md`](README.md) · [`POLICY.md`](POLICY.md) · [`blueprints/sdlc/methodologies/agentic-sdlc.md`](../sdlc/methodologies/agentic-sdlc.md) · [`blueprints/sdlc/methodologies/spec-driven-development.md`](../sdlc/methodologies/spec-driven-development.md)

---

## 1. Purpose

| Goal | Means |
|------|-------|
| **Agent alignment** | IDE agents (Cursor, Claude Code) receive SDLC methodology as native instructions they can act on, not prose they must discover. |
| **Consistency** | Every project bootstrapped from this blueprint starts with the same spec-driven, plan-first, verify-before-commit workflow. |
| **Customizability** | Templates are copied into the project; teams adjust freely without touching the frozen blueprint. |

---

## 2. Vendor feature matrix

| Concept | Cursor | Claude Code |
|---------|--------|-------------|
| **Always-on project instructions** | `AGENTS.md` (root, nested) | `CLAUDE.md` (root, nested) |
| **Conditional rules** | `.cursor/rules/*.mdc` (frontmatter: globs, description, alwaysApply) | `.claude/skills/*/SKILL.md` (frontmatter: name, description) |
| **Reusable commands** | `.cursor/commands/*.md` (invoked via `/command-name`) | Skills with `disable-model-invocation: true` (invoked via `/skill-name`) |
| **Plan artifacts** | `.cursor/plans/*.md` (saved from Plan Mode) | Plan Mode output (manual save) |
| **Subagents** | Built-in (Task tool, worktrees) | `.claude/agents/*.md` (separate context, scoped tools) |
| **Hooks** | `.cursor/hooks.json` | `.claude/settings.json` (hooks section) |
| **Context management** | New chat per task; `@Past Chats`, `@Branch` | `/clear`, `/compact`, `/rewind`; subagents for investigation |

---

## 3. Template → project file mapping

The init script (`scripts/init-ide-workspace.sh`) copies templates into the project, stripping the `.template.` segment from filenames and replacing `{{PROJECT_NAME}}` with the project name.

### 3.1 Vendor-neutral

| Template | Project file | Role |
|----------|-------------|------|
| `AGENTS.template.md` | `AGENTS.md` (root) | Cursor always-on instructions |
| `CLAUDE.template.md` | `CLAUDE.md` (root) | Claude Code always-on instructions |

### 3.2 Cursor-specific

| Template | Project file | Activation |
|----------|-------------|------------|
| `cursor/rules/spec-driven.template.mdc` | `.cursor/rules/spec-driven.mdc` | Globs: `docs/requirements/**/*` + description |
| `cursor/rules/agentic-workflow.template.mdc` | `.cursor/rules/agentic-workflow.mdc` | Description-based |
| `cursor/rules/commit-conventions.template.mdc` | `.cursor/rules/commit-conventions.mdc` | `alwaysApply: true` |
| `cursor/rules/plan-and-verify.template.mdc` | `.cursor/rules/plan-and-verify.mdc` | Description-based |
| `cursor/commands/plan.template.md` | `.cursor/commands/plan.md` | `/plan` |
| `cursor/commands/pr.template.md` | `.cursor/commands/pr.md` | `/pr` |
| `cursor/commands/review-spec.template.md` | `.cursor/commands/review-spec.md` | `/review-spec` |

### 3.3 Claude Code-specific

| Template | Project file | Activation |
|----------|-------------|------------|
| `claude/skills/spec-driven/SKILL.template.md` | `.claude/skills/spec-driven/SKILL.md` | Auto (by description) or `/spec-driven` |
| `claude/skills/plan-and-verify/SKILL.template.md` | `.claude/skills/plan-and-verify/SKILL.md` | Auto or `/plan-and-verify` |
| `claude/agents/spec-reviewer.template.md` | `.claude/agents/spec-reviewer.md` | Explicit delegation |

### 3.4 Plan convention

| Template | Project file | Role |
|----------|-------------|------|
| `plans/PLAN.template.md` | `.cursor/plans/PLAN.template.md` | Template for individual plan artifacts |
| `plans/README.md` | Stays in blueprint (reference) | Convention documentation |

---

## 4. Content derivation

IDE instructions **condense** existing blueprint methodology prose — they do not replace it. The canonical source of truth for each topic remains in `blueprints/sdlc/`.

| Instruction | Derived from |
|-------------|-------------|
| Spec-driven rules/skills | [`sdlc/methodologies/spec-driven-development.md`](../sdlc/methodologies/spec-driven-development.md) |
| Agentic workflow rules | [`sdlc/methodologies/agentic-sdlc.md`](../sdlc/methodologies/agentic-sdlc.md) |
| Commit conventions | [`sdlc/SDLC.md`](../sdlc/SDLC.md) (traceability), spec-driven (work-unit IDs) |
| Plan-and-verify | Synthesized from Cursor/Claude Code best practices + blueprint phases A–F |
| Context/session hygiene | Synthesized from vendor guidance (Cursor: new chat per task; Claude: `/clear`, subagents) |

---

## 5. Adoption notes

- **Single vendor:** use `--cursor-only` or `--claude-only` with the init script if your team uses only one tool.
- **Existing rules:** the init script does not delete existing `.cursor/rules/` files. Your project rules coexist with blueprint-derived ones.
- **Customization after bootstrap:** edit the generated files freely. They are mutable project files, not blueprint text.
- **Upgrading:** re-run the init script with `--force` to overwrite with newer template versions. Diff before committing to preserve local customizations.

---

*Blueprint — no project-specific content.*
