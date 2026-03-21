# Cursor rule templates

`.mdc` files copied to `.cursor/rules/` by `init-ide-workspace.sh`. Each uses Cursor's frontmatter format (`description`, `globs`, `alwaysApply`).

| Template | Rule purpose | Activation |
|----------|-------------|------------|
| `spec-driven.template.mdc` | Spec-driven development workflow | Globs + description |
| `agentic-workflow.template.mdc` | Agentic SDLC governance | Description-based |
| `commit-conventions.template.mdc` | Commit messages and work-unit traceability | Always apply |
| `plan-and-verify.template.mdc` | Plan-first workflow and verification contract | Description-based |

After copying, teams should customize rules for their stack and conventions.
