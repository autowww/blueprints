# {{PROJECT_NAME}} — Claude Code instructions

> This file is loaded by **Claude Code** at the start of every session.
> Edit freely — it is a project file, not part of the frozen blueprint.
> Seeded from `blueprints/ide/templates/CLAUDE.template.md`.

## Build, test, lint

<!-- IMPORTANT: Fill in your project's commands so Claude can verify its work. -->

```bash
# Build
# TODO: e.g. npm run build, ./gradlew assembleDebug

# Test
# TODO: e.g. npm test, ./gradlew test

# Lint / typecheck
# TODO: e.g. npm run lint, ./gradlew lint
```

## Spec-driven workflow

- Start every implementation task from a **named work-unit ID** (e.g. `M1E1S1`, `#123`) that exists in `docs/requirements/` or the issue tracker.
- IMPORTANT: **Acceptance criteria must exist** before large or multi-file changes. If they don't, write them first.
- When behavior changes, **update the spec** (or add an ADR) in the same changeset as the code.
- **Failing tests or unmet criteria are the stop signal** — not "looks fine."

## Commit conventions

- Reference the work unit in the commit subject: `Refs M1E1S1` or `Fixes #123`.
- Describe **what** and **why** in plain language.
- Use `Co-authored-by:` trailers when agent-assisted, per team policy.

## System of record

- **Git** (commits, PRs) and **`docs/requirements/`** are the system of record — not chat.
- If a product or scope decision happens in chat, **persist the minimum** into an ADR, spec note, or issue comment.

## Review contract

- YOU MUST NOT accept scope changes or skip review. You are not the Product Owner.
- **Human review required** for changes touching security, data, or public API.

## Session hygiene

- Use `/clear` between unrelated tasks to keep context clean.
- For large investigations, delegate to subagents so the main context stays focused.
- When compacting, always preserve the list of modified files and any test commands.

## Skills and agents

See `.claude/skills/` for workflow skills (spec-driven, plan-and-verify) and `.claude/agents/` for subagent definitions (spec-reviewer).

See @docs/requirements/ for work-unit specs and acceptance criteria.

<!-- ──────────────────────────────────────────────── -->
<!-- PROJECT-SPECIFIC DECISIONS (fill in as a team) -->
<!-- ──────────────────────────────────────────────── -->

## Project decisions

<!-- Uncomment and fill in when your team agrees: -->
<!-- - Work-unit source of truth: GitHub Issues / docs/requirements/ IDs / both with mapping rule -->
<!-- - Sprint goal storage: milestone field / wiki / dated note under docs/ -->
<!-- - AI commit labeling: same review bar / Co-authored-by policy / bot account -->
