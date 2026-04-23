---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona skill and tasklet matrix

**Purpose:** Map every **catalog** Versona template to **reusable** Cursor **Skills**, **cognition tasklets**, and **execution recipe** stubs so enriched Versonas **call into** shared capabilities instead of duplicating long prose in `.mdc` rules. **Normative** rule shape remains [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md); **paths** remain [`ARTIFACT-CONTRACTS.md`](ARTIFACT-CONTRACTS.md).

**Source layout:** Skill templates live under [`../../../templates/forge/cursor-skills/`](../../../templates/forge/cursor-skills/) (copy to `.cursor/skills/<name>/`). Tasklet templates live under [`../tasklets/tasklet-*.mdc.template`](../tasklets/) (install via [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh)). Execution stubs live under [`../../../../agents/templates/recipe/`](../../../../agents/templates/recipe/) (copy to consuming repo **`agents/recipes/<name>/`** per [`../../../../agents/ORCHESTRATION.md`](../../../../agents/ORCHESTRATION.md)).

---

## 0. Orchestration vs discipline boundaries

| Rule / lens | Owns | Does **not** own |
|-------------|------|-------------------|
| **`versona-all`** | Cross-family **routing** (which `@versona-*` to invoke next) | Phase **plans**, discipline **§5** judgment, **merge** of parallel specialists |
| **`versona-forge-sdlc`** | **A–F** execution order, **P/S** steps, **merge owner**, trace checklist | Specialist findings — those stay in discipline §5 |
| **`versona-family-*`** | **Merge coordinator** for **one domain** after parallel child passes | Cross-domain routing when unclear — use **`versona-all`** first |
| **`versona-pm`** (Governance) | **Delivery** feasibility: scope baseline, schedule/critical path, cost/capacity, **RAID**, gate readiness | **Product** strategy, roadmap **prioritization**, market fit → **`versona-product-management`** |
| **`versona-product-management`** | **Product** strategy, roadmap/OKR fit, prioritization **rationale**, PMF signals | **Project** schedule/critical-path baselines → **`versona-pm`** |
| **`versona-ba`** | **Requirements**, AC, elicitation, needs ↔ solution fit | Portfolio **why now** → **product-management**; **delivery plan** mechanics → **pm** |

**Companion:** [`../orchestration/README.md`](../orchestration/README.md) — SDLC orchestration hub + links to `FORGE-SDLC-ORCHESTRATION.md`.

---

## 1. Pack legend (shorthand)

| ID | Includes |
|----|----------|
| **pack-session** | Skills: `start-versona-session`, `record-versona-event`, `close-versona-session` · Tasklets: `bootstrap-session`, `log-event` |
| **pack-standards** | Skills: `resolve-versona-standards` · Tasklet: `check-standards` |
| **pack-handoff** | Skill: `build-versona-handoff` |
| **pack-merge** | Skill: `merge-parallel-versona-results` · Tasklet: `merge-outputs` |
| **pack-evidence** | Skill: `assemble-versona-evidence-pack` · Tasklet: `summarize-evidence` · Recipe template: `versona-evidence-pack-assemble` |
| **pack-diagram** | Skill: `export-versona-kitchensink-diagram` · Recipe template: `versona-kitchensink-diagram-export` |
| **pack-route** | Tasklet: `route-request` |

**Specialist skills** (domain-shaped flows, not universal):

| Skill folder | Use |
|--------------|-----|
| `run-product-versona-session` | Product family / PM / multi-lens shallow pass |
| `run-engineering-ai-code-review` | Diff/PR, Engineering-family routing |

---

## 2. Matrix by template

**Columns:** **Packs** = routine invocation order (session + standards + handoff baseline for most disciplines). **Specialist** = optional domain Skill. **Orchestration** = who sequences work. **Trace / evidence** = typical §5.1, Ember Log, `forge/evidence/` obligations.

| Template (`.mdc`) | Packs | Specialist Skill | Orchestration | Trace / evidence |
|-------------------|-------|-------------------|---------------|------------------|
| `versona-se` | session, standards, handoff | `run-engineering-ai-code-review` | Human invokes; may parallelize with other eng lenses then **pack-merge** | §5.1 when policy surface; Ember Log on craft **decisions** that affect scope |
| `versona-architecture` | session, standards, handoff, **diagram** | `run-engineering-ai-code-review` | Human / family aggregator | §5.1 for NFRs; ADR pointers; diagram exports to session or `docs/architecture` |
| `versona-devops` | session, standards, handoff, **evidence** | `run-engineering-ai-code-review` | Human / CI handoff | §5.1 for controls; **evidence** for pipelines, incidents, SRE claims |
| `versona-testing` | session, standards, handoff, **evidence** | `run-engineering-ai-code-review` | Human; often after recipe outputs | §5.1; **evidence** packs for Assay; `artifact-manifest.json` for recipe runs |
| `versona-frontend` | session, standards, handoff | `run-engineering-ai-code-review` | Human | §5.1 when a11y / policy; WCAG matrix row |
| `versona-mobile` | session, standards, handoff | `run-engineering-ai-code-review` | Human | Same as frontend where applicable |
| `versona-iot` | session, standards, handoff, evidence | `run-engineering-ai-code-review` | Human | §5.1; safety evidence pointers |
| `versona-bigdata` | session, standards, handoff, evidence | — | Human | §5.1; data-governance evidence |
| `versona-datascience` | session, standards, handoff, evidence | — | Human | §5.1; model risk / lineage evidence |
| `versona-product-management` | session, standards, handoff | `run-product-versona-session` | Human / roadmap gate | §5.1 when commercial or policy; strategy **decisions** → Ember Log |
| `versona-ba` | session, standards, handoff | `run-product-versona-session` | Human | §5.1 when obligations; specs under `docs/requirements/` |
| `versona-ux` | session, standards, handoff, **diagram** | `run-product-versona-session` | Human | §5.1 a11y; UX diagram exports |
| `versona-marketing` | session, standards, handoff | `run-product-versona-session` | Human | §5.1 when brand/legal surface |
| `versona-cs` | session, standards, handoff | `run-product-versona-session` | Human | §5.1 when SLAs / privacy |
| `versona-pm` | session, standards, handoff, evidence | — | Human / governance | §5.1; **evidence** for gates, RAID, compliance plans |
| `versona-security` | session, standards, handoff, **evidence** | — | Human; often post-recipe | §5.1 **always** when in scope; **evidence** packs, waivers |
| `versona-compliance` | session, standards, handoff, **evidence** | — | Human / GRC | §5.1; **evidence** primary |
| `versona-family-engineering` | session, standards, handoff, **merge**, route | `run-engineering-ai-code-review` | **Aggregator** runs children or suggests; **pack-merge** required | Merge child §5.1 summaries per contract |
| `versona-family-data` | session, standards, handoff, merge, route | — | Aggregator | Merge discipline traces |
| `versona-family-product` | session, standards, handoff, merge, route | `run-product-versona-session` | Aggregator | Merge; Ember Log for cross-cutting **decisions** |
| `versona-all` | route, standards (light), session (optional) | — | **Router** — no §5 by default | Points to sinks; optional `routing-decision.json` |
| `versona-sampling` | route, merge (via tasklets), session (optional) | — | **Meta** — runs tasklet chain | Teaching/demo; align with Sampling template |
| `versona-project-setup` | session, standards (light), route | — | **Workflow** checklist | Records setup **decisions** → Ember Log |
| `versona-roadmap-gate` | session, standards, handoff, merge, **evidence** | `run-product-versona-session` | **Workflow** gate | Gate **evidence**; phase alignment |
| `versona-forge-sdlc` | route, session, merge (phase reports) | — | **Workflow** SDLC phases | Links to orchestration docs |
| `versona-cursor-rules-sync` | session (optional) | — | **Workflow** tooling | Change log in PR / journal |
| `versona-generic` | session (optional) | — | **Baseline** companion only | N/A — no §5 |

**`versona-generic`:** Layer-0 baseline; pair with a discipline rule. Use **pack-session** only when the user opts into persisted sessions.

---

## 3. Separation: tasklets vs recipes

| Plane | Location | Use |
|-------|----------|-----|
| **Cognition** | `.cursor/rules/forge-tasklet-*.mdc` | Single-operation **LLM** output shapes (route, bootstrap, check, log, merge, summarize) |
| **Execution** | `agents/recipes/<recipe>/run.sh` (mutable repo) | Docker/CI, file copies, generators — **stubs** in blueprint [`agents/templates/recipe/`](../../../../agents/templates/recipe/) |

Details: [`agents/docs/VERSONA-EXECUTION-TASKLETS.md`](../../../../agents/docs/VERSONA-EXECUTION-TASKLETS.md), [`../tasklets/TASKLET-TAXONOMY.md`](../tasklets/TASKLET-TAXONOMY.md).

---

## 4. Authoring rule (slim `.mdc`)

Discipline templates SHOULD **name** packs in **`## Artifact I/O`** (see [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §2a) with **one line**: “Invoke Skills: pack-session, pack-standards, …” and link **here** instead of pasting Skill steps.

---

## 5. Related

- [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §3 — interfaces and handoffs  
- [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) §3 — Rules vs Skills vs recipes  
- [`../tasklets/README.md`](../tasklets/README.md) — install tasklets
