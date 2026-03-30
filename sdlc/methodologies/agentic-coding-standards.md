---
slug: agentic-coding-standards
tier: 201
lens: methodology
nav_section: "Agentic Engineering"
---

# Agentic coding standards (cross-cutting)

## Purpose

This guide defines **prescriptive coding and review standards** for teams using **AI-assisted implementation** (IDE assistants, codegen tools, review bots) alongside humans. It applies **with any lifecycle or methodology** (Scrum, Kanban, phased, etc.). Teams running [**Forge SDLC**](forge.md) use the same rules and map them to **Charge**, **Ember Log**, **Versona** sessions, and **Assay** evidence as described in the [Forge overlay](#forge-overlay-optional) below.

**Companion:** principles and risks — [`agentic-sdlc.md`](agentic-sdlc.md). **Specs and durable intent:** [`spec-driven-development.md`](spec-driven-development.md).

---

## Scope and layering

| Layer | What this guide governs |
|-------|-------------------------|
| **Human** | Owns intent, acceptance, release, and policy exceptions. |
| **AI tools** | Generate or refactor code, tests, and drafts **under** team standards, **review**, and **CI**. |
| **Repository** | System of record for what shipped — commits, PRs, tests, and linked work units. |

Forge teams additionally align sessions and logs with [`forge/versona/VERSONA-FRAMEWORK.md`](forge/versona/VERSONA-FRAMEWORK.md) (session layout, §5 structured output when used).

---

## Intent and repository as source of truth

1. **No chat-only specifications** — acceptance criteria, IDs, and constraints live in **tracked artifacts** (issues, specs, `docs/`, SDD inputs) that a reviewer can open without scrolling a thread.  
2. **Link work to intent** — commits or PR descriptions reference backlog / requirement / Spark IDs where your process expects traceability ([`agentic-sdlc.md`](agentic-sdlc.md) engineering-tracking table).  
3. **Prefer spec-first for large AI edits** — for non-trivial scope, written intent leads implementation ([`spec-driven-development.md`](spec-driven-development.md)); reduces rework and silent scope creep.

---

## Generation discipline

1. **Minimal, scoped diffs** — change only what the work unit requires; avoid drive-by refactors, formatting sweeps, or unrelated file churn.  
2. **Match house style** — naming, structure, and patterns consistent with the surrounding module and team directives (e.g. `.cursor/rules/`, `CONTRIBUTING.md`).  
3. **Split when review would suffer** — if agent throughput exceeds review capacity, **smaller PRs** and **lower WIP** beat huge batches ([`agentic-sdlc.md`](agentic-sdlc.md) risks).  
4. **Recoverable steps** — prefer commits that are easy to bisect or revert; avoid squashing unrelated concerns into one change.

---

## Attribution and identity

1. **PR transparency** — state **AI-assisted** work when applicable (tool name optional unless policy requires it); summarize what the human verified.  
2. **Bot and service accounts** — if automation opens PRs or commits, policy should define **labels**, **CODEOWNERS**, and how they appear in history ([`agentic-sdlc.md`](agentic-sdlc.md) Contributor row).  
3. **Audit trail** — reviewers must be able to see **what** changed and **why** without private chat context.

---

## Verification

1. **CI and local gates** — agreed checks (build, lint, tests) **pass** before merge unless a **recorded, time-bounded exception** exists (same bar as non-AI work; see [`SDLC.md`](../SDLC.md) Verify phase).  
2. **Tests are not optional by default** — new behavior needs tests or an explicit, reviewed justification in the work record.  
3. **High-risk areas** — auth, crypto, PII, payments, concurrency, and security-sensitive paths require **human review** and often **extra** discipline passes (e.g. Security Versona, threat-informed checklist); AI review does **not** replace that.  
4. **Regulated contexts** — follow organizational sign-off and evidence rules; automation supplements, not replaces, compliance gates.

---

## Security

1. **LLM application risks** — use [OWASP Top 10 for LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/) as a baseline when models touch prompts, tools, data, or generated code.  
2. **Secure SDLC overlay** — depth for secure design, review, and testing lives under [`disciplines/security/README.md`](../../disciplines/security/README.md) and related practice guides.  
3. **Secrets** — never commit keys, tokens, or production data into prompts, repos, or recipe configs; use secret stores and ephemeral review environments.

---

## AI-assisted code review flow (summary)

1. **Bound the change** — diff or PR scope, SDLC phase, and risk class.  
2. **Automated first** — linters, tests, SAST/SCA as applicable.  
3. **Structured discipline pass** — optional **§5-shaped** reviews via Engineering-family **Versonas** (e.g. Software Engineering, Security, Testing) — see [`forge/versona/catalog/discipline/engineering/versona-se.mdc.template`](forge/versona/catalog/discipline/engineering/versona-se.mdc.template) and [`forge/versona/VERSONA-CONTRACT.md`](forge/versona/VERSONA-CONTRACT.md).  
4. **Human decision** — merge, request changes, or escalate; record material trade-offs in **Ember Log** or ADRs when Forge or your process requires it.

**IDE:** teams may install the blueprint **Cursor skill** [`templates/forge/cursor-skills/run-engineering-ai-code-review/`](../templates/forge/cursor-skills/run-engineering-ai-code-review/SKILL.md). **CI / container:** optional template recipe [`agents/templates/recipe/llm-diff-review/`](../../agents/templates/recipe/llm-diff-review/README.md) (copy to `agents/recipes/` per [`agents/ORCHESTRATION.md`](../../agents/ORCHESTRATION.md)).

---

## Forge overlay (optional)

Use this mapping when **Forge SDLC** is the team’s methodology ([`forge/README.md`](forge/README.md)).

| Standard topic | Forge mapping |
|----------------|---------------|
| **Daily execution** | **Charge** lists Sparks; keep AI work visible in the same pull/PR stream as human work. |
| **Decisions and waivers** | **Ember Log** (`ember-logs/`) for trade-offs, risk acceptance, or scope shifts surfaced during AI-assisted work ([`forge/daily/README.md`](forge/daily/README.md)). |
| **Discipline challenge** | **Versona session** under `forge-logs/versona/<actor>/<session-id>/` when running a formal lens pass ([`forge/versona/VERSONA-FRAMEWORK.md`](forge/versona/VERSONA-FRAMEWORK.md) §7–8). |
| **Iteration quality** | **Review** meeting: discipline review aligns with **C4**-shaped quality intent ([`forge/ceremonies-prescriptive.md`](forge/ceremonies-prescriptive.md)). |
| **Release evidence** | **Assay Gate** checklists include tests, security, and decision hygiene as your gate defines ([`forge/meetings-model.md`](forge/meetings-model.md)). |

---

## Related blueprint guides

- [`agentic-sdlc.md`](agentic-sdlc.md) — agentic principles, ceremonies, risks.  
- [`spec-driven-development.md`](spec-driven-development.md) — durable specs for agentic workflows.  
- [`forge.md`](forge.md) — Forge methodology hub.  
- [`roles-archetypes.md`](roles-archetypes.md) — accountability and Contributor identity.  
- [`blueprints/agents/STRUCTURE.md`](../../agents/STRUCTURE.md) — containerized recipes and optional LLM steps.
