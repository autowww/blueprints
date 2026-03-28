---
slug: methodology-spec-driven
tier: 201
lens: methodology
nav_section: "Methodology Comparisons"
---

# Spec-driven development

## What we mean

**Spec-driven development** means **written intent** (requirements, acceptance criteria, scenarios, constraints) is the **primary input** to design and implementation—not an afterthought. “Spec” includes **story files**, **epic briefs**, **acceptance tests** (examples or automated), **API contracts**, **ADRs** for decisions, and **checklists** your team treats as binding before calling work *done*.

It is **compatible with any methodology** in this blueprint (Scrum, Kanban, phased, XP): the difference is *discipline about when prose and criteria exist*, not which ceremony you use.

---

## Why it matters

| Outcome | How specs help |
|---------|----------------|
| **Shared understanding** | Owner, implementers, and reviewers align on *done* before deep coding. |
| **Traceability** | Stable work-unit IDs ([`DOCUMENTATION-STRUCTURE.md`](../DOCUMENTATION-STRUCTURE.md)) link commits, tests, and releases to explicit intent. |
| **Less rework** | Ambiguity surfaces in cheap conversations and short documents, not after merge. |
| **Agentic workflows** | LLMs and CI bots need **durable context in the repo**; chat alone is not a spec ([`agentic-sdlc.md`](agentic-sdlc.md)). |
| **Regulated / audited delivery** | Evidence chains (req → design → test → release) assume specs exist and change through control, not only through code diffs. |

---

## Minimal artifact set (typical)

Adjust names to your `docs/` layout; the **pattern** is what counts.

| Stage of thinking | Artifact | Usually owned by |
|-------------------|----------|------------------|
| **Shape** | Milestone / epic narrative, WBS or backlog slice | Owner / PM |
| **Specify** | Story + **acceptance criteria** (and non-functional notes) | Owner + implementers (refine) |
| **Design** | ADR or short design section in epic/story when cross-cutting | Tech lead / team |
| **Implement** | Tasks, PRs; code comments only for *why*, not duplicate specs | Implementers |
| **Verify** | Tests tied to criteria; manual checklist if needed | Implementers + Owner |
| **Release** | Release notes referencing requirement or story IDs | Team |

**Rule:** If implementers cannot point to a **spec sentence or test** that justifies a change, the change is either **too speculative** or the spec needs updating first.

---

## Lifecycle loop (docs ↔ code)

1. **Draft** — Rough intent in milestone/epic/story; IDs assigned early ([`change`](../docs/change.html) / scope management).  
2. **Refine** — Acceptance criteria testable and agreed (Definition of Ready, in Scrum terms).  
3. **Implement** — Small batches; each PR traces to a work unit.  
4. **Inspect** — Review checks spec fit; CI checks executable specs where they exist.  
5. **Adapt** — If reality invalidates the spec, **update the spec** (or add an ADR) in the same change set as the code when possible.

This mirrors Phases A–F in [`SDLC.md`](../SDLC.md): discovery and specification stay **visible in the repo**, not only in meetings.

---

## Specs and agents (brief)

Agents amplify **execution**; they do not replace **acceptance** or **prioritization**. Effective spec-driven + agentic teams:

- Keep **stories, criteria, and IDs** in `docs/requirements/` (or equivalent) **before** large automated edits.  
- Require **human review** for changes that touch security, data, or public API.  
- Treat **failing tests or unmet criteria** as the stop signal—not “looks fine in chat.”

See [`agentic-sdlc.md`](agentic-sdlc.md) and handbook [`agents.html`](../docs/agents.html).

---

## Anti-patterns

| Anti-pattern | Fix |
|--------------|-----|
| **Code-first, spec-later** | Block “done” until story criteria and traceability match what shipped. |
| **Specs in chat only** | Move decisions into Markdown (or tracker with export) linked from the tree. |
| **Brittle prose** | Prefer **examples**, **given/when/then** (BDD), or **checklists** over vague adjectives. |
| **Specs never updated** | Use CR / PR discipline: changing behavior without updating spec is **scope drift**. |
| **One giant spec doc** | Prefer **hierarchy** (milestone → epic → story) so diffs stay reviewable. |

---

## Related in this repo / blueprint

- [`DOCUMENTATION-STRUCTURE.md`](../DOCUMENTATION-STRUCTURE.md) — where files live.  
- Handbook [`documentation.html`](../docs/documentation.html) — work hierarchy and IDs.  
- Handbook [`dod.html`](../docs/dod.html) — Definition of Done.  
- Handbook [`change.html`](../docs/change.html) — stable IDs and scope.  
- Project example: [`sdlc/SCOPE-WORK-REPO-AND-CURSOR.md`](../../../sdlc/SCOPE-WORK-REPO-AND-CURSOR.md) — work units, commits, Cursor.  
- [`docs/requirements/STRUCTURE-PROPOSAL.md`](../../../docs/requirements/STRUCTURE-PROPOSAL.md) (this monorepo) — concrete ID and folder rules.

---

## External reading (starting points)

| Topic | URL | Why link |
|-------|-----|----------|
| Specification by example | [Martin Fowler (Bliki)](https://martinfowler.com/bliki/SpecificationByExample.html) | Short expert framing: examples as the contract between roles. |
| BDD (context) | [Wikipedia — Behavior-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) | Stable overview of scenario-style specs and tests. |
| Agile + requirements | [Agile Alliance — glossary](https://www.agilealliance.org/agile101/agile-glossary/) | Shared vocabulary (user story, acceptance criteria, etc.). |

---

## SDD I/O subchapters (ceremonies & process)

Structured **inputs, outputs, preconditions**, **artifact registers**, and **filled examples** in Spec-Driven Development (SDD) format:

| Topic | Markdown | Handbook |
|-------|----------|----------|
| Schema & quality rules | [`spec-driven/SDD-IO-SCHEMA.md`](spec-driven/SDD-IO-SCHEMA.md) | [`spec-driven-sdd-schema.html`](../docs/spec-driven-sdd-schema.html) |
| Ceremony intents C1–C6 | [`spec-driven/ceremonies-sdd.md`](spec-driven/ceremonies-sdd.md) | [`spec-driven-sdd-ceremonies.html`](../docs/spec-driven-sdd-ceremonies.html) |
| Process slots P1–P6 | [`spec-driven/process-slots-sdd.md`](spec-driven/process-slots-sdd.md) | [`spec-driven-sdd-process.html`](../docs/spec-driven-sdd-process.html) |

**Templates** (copy into your repo): [`templates/sdd/`](../templates/sdd/README.md) — `CEREMONY-INTENT.template.md`, `PROCESS-SLOT.template.md`.

---

*Handbook hub (HTML): [`spec-driven.html`](../docs/spec-driven.html) — sidebar lists Overview + SDD subchapters.*
