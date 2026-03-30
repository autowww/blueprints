# Template recipe: `llm-diff-review`

**Purpose:** Optional **repeatable** job that sends a **unified diff** to an **OpenAI-compatible** chat-completions HTTP API and writes a **Markdown review** to a file or stdout. Use for **CI artifacts** or **local** pre-review when an IDE assistant is not available.

**Aligned with:** [`blueprints/sdlc/methodologies/agentic-coding-standards.md`](../../../../sdlc/methodologies/agentic-coding-standards.md) — this template does **not** replace human review, CI gates, or Forge Versona judgment.

## Non-goals

- Not a full **L6** tool-calling agent ([`STRUCTURE.md`](../../STRUCTURE.md) §2).  
- Not vendor-locked to OpenAI — any API that accepts a similar JSON body works if you set `LLM_API_URL`.  
- Does **not** post PR comments; wire that in your CI if needed.

## Adoption

1. Copy this folder into **`agents/recipes/llm-diff-review/`** at the consuming repo root (or use [`new-agent-recipe.sh`](../../scripts/new-agent-recipe.sh) and merge these files).  
2. Provide secrets via **environment** or CI secret store — **never** commit API keys.  
3. Mount the repo at **`/work`** per [`docker/compose.yaml`](../../docker/compose.yaml) and run from the recipe directory or set paths accordingly.

## Environment

| Variable | Required | Default |
|----------|----------|---------|
| `LLM_API_KEY` or `OPENAI_API_KEY` | Yes | — |
| `LLM_API_URL` | No | `https://api.openai.com/v1/chat/completions` |
| `LLM_MODEL` | No | `gpt-4o-mini` |

## Usage

```bash
# From a git repo
git diff origin/main...HEAD | ./run.sh --out agents/workspaces/llm-diff-review/report.md

# From a file
./run.sh --diff-file /tmp/changes.patch --out report.md
```

**Stack:** [`Dockerfile.base`](../../docker/Dockerfile.base) includes **`curl`** and **`jq`** only (no Python in the default image).

## Output

Plain **Markdown** suitable to attach as a CI artifact or paste into a PR. Reviewers should treat it as **input**, not approval.

## See also

- [`ORCHESTRATION.md`](../../ORCHESTRATION.md) — recipe conventions.  
- Forge **Cursor** flow: [`blueprints/sdlc/templates/forge/cursor-skills/run-engineering-ai-code-review/SKILL.md`](../../../../sdlc/templates/forge/cursor-skills/run-engineering-ai-code-review/SKILL.md).
