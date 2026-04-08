---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Git branching and commit conventions (Forge)

Prescriptive defaults for repos adopting **Forge SDLC**. Branching scales with [team size and ceremony weight](../../forge.md#scaling-model); **commit messages** are structured so humans and **agents** can search history (`git log --grep`, ripgrep, host UI) without opening every diff.

**Baseline:** Generic Git workflow trade-offs and shared practices (merge vs rebase, imperative subjects) stay in [Software engineering — version control](../../../../disciplines/engineering/software-engineering/SOFTWARE-ENGINEERING.md#8-version-control-git). This page adds **Forge-scaled branching** and **commit body/trailer** rules. Work-unit linking aligns with the tracking spine in [`TRACKING-FOUNDATION.md`](../../../templates/sdlc/TRACKING-FOUNDATION.md).

---

## Principles

1. **Default trunk** — One integration branch (`main` or `trunk`) represents the **next releasable** state. **Assay Gate** is the release decision, not a long-lived stabilization branch by default.
2. **Scale by trust, not ceremony weight** — Add branch lanes and review gates when coordination or risk demands them; do not adopt GitFlow “because enterprise.”
3. **Spark ≠ branch** — A [Forge Spark](../process-and-flows.md#2-work-unit-hierarchy) maps to a WBS **task**; traceability lives in **commits and PR titles**, not a rule of one branch per Spark.

---

## Branching by scaling tier

Match `team.scale` in [`forge.config.template.yaml`](forge.config.template.yaml) to your team (see [Scaling model](../../forge.md#scaling-model)).

| Scale | Default model | Branches | PR / review | Release / hotfix |
|-------|----------------|----------|-------------|------------------|
| **Solo** | Direct commit or **same-day** topic branch | `main` + optional `topic/<short-name>` | Self-review optional; commits carry WBS / issue ids | Tag after Assay; hotfix = short branch or direct commit + tag |
| **Small (2–5)** | **GitHub Flow** | Feature/topic off `main`; delete after merge | Lightweight PR (one reviewer or pair); merge when Charge / DoD satisfied | Deploy or tag from `main`; hotfix branch if production is sensitive |
| **Team (5–12)** | **GitHub Flow** or **trunk-based** | Short-lived branches; **protected** `main` | Required review; CI green before merge | Same; optional `release/x.y` only for a **stabilization window** (fixed date, long QA) |
| **Multi-team (12+)** | **Trunk-based** preferred; GitFlow-style only when justified | `main` + short `feature/*` or **team-prefixed** branches (`billing/…`); optional **integration** or **release** branches for train releases | Cross-team merge rules; process changes via retro → directives ([ceremonies](../ceremonies-prescriptive.md)) | Coordinated Assay Gates; document **hotfix** path (cherry-pick to release line *or* trunk-first + backport) |

### What we avoid

- **Environment branches** (`dev` / `staging` / `prod`) as substitutes for releases — prefer **tags**, **deploy from commit SHA**, or configuration per environment.
- **Long-lived personal branches** — integrate frequently to reduce merge risk and keep Assay evidence meaningful.

### When to tighten the model (escalation)

Move toward the **next row** when you see repeated merge pain on `main`, incidents from unreviewed merges, multiple concurrent release trains, or several teams landing in one repo without a clear integration rhythm. If overhead exceeds value, **simplify** again after retro evidence.

**Escalation path (typical):** **Solo** → **Small** → **Team** → **Multi-team** as reviewers, risk, contributor count, or release-train pressure increase. **De-escalation** (e.g. Multi-team → Team) is valid when overhead exceeds value and retro evidence supports simpler branching—there is no requirement to cycle back through every tier.

---

## Commit messages (subjects, body, trailers)

Goals: **stable tokens** for search, **optional Git trailers** for tooling, and a short **body** so agents can summarize history without reading every patch.

### Baseline (all scales)

Align with [Software engineering §8](../../../../disciplines/engineering/software-engineering/SOFTWARE-ENGINEERING.md#8-version-control-git): imperative subject; optional scope; link issues; **separate mechanical refactors from behavior change**.

### Structured conventions

| Element | Rule | Why |
|---------|------|-----|
| **Subject** | Imperative, about ≤72 characters; optional `type(scope): summary` (Conventional Commits–lite: `feat`, `fix`, `docs`, `chore`, `refactor`, …) | Scannable logs; filter by type/scope |
| **Scope** | Repo-defined buckets (`generator`, `handbook`, `kitchensink`, `blueprints-submodule`, …) — list allowed scopes in project `sdlc/` or your fork of this doc | Area keyword search |
| **Work unit** | When applicable, include **WBS / Spark / issue** id in the body’s first line or the subject, e.g. `Refs M1E3S2T4` or `Fixes #123` — same id family as [`TRACKING-FOUNDATION.md`](../../../templates/sdlc/TRACKING-FOUNDATION.md) | Joins git to tracker / requirements |
| **Phase hint** | Optional: **A–F** or [`discover:` / `build:` / …](../../forge.md#mapping-to-this-blueprints-sdlc) in subject or body when it helps Assay forensics — **one** primary phase per commit when a single attribution matters | `git log --grep=build:` |
| **Body** | Blank line after subject; 1–3 short paragraphs: **what**, **why**, **notable paths** or risks (no secrets) | Human + LLM search without diff diving |
| **Trailers** | End with standard Git trailers (`Key: value`, one per line): `Co-authored-by:`, `Refs:`, `Reviewed-by:`; optional **project** trailer only if documented once (e.g. `Forge-Spark: M1E3S2T4`) | `git interpret-trailer`; consistent grep |
| **Mechanical commits** | Submodule bumps, lockfiles, generated sites: `chore(scope):` + body line naming **what** moved (submodule, generator command) | Separates policy/content from bulk regen |
| **PR title** | Mirror the **lead** commit subject or a clear stack summary; keep ids in title or description | Host UI search |

### Scale nuance

- **Solo** — Shorter bodies are acceptable; still keep ids when a Spark or issue exists.
- **Team+** — Non-trivial changes should use the body by default.
- **Multi-team** — Prefer **team or area** in `scope` to keep shared logs readable.

### Anti-patterns

- Vague subjects (`fix stuff`, `updates`).
- Only id buried in a **squash** default message with **no** body.
- Unrelated concerns in **one** commit (harms bisect and agent summaries).

---

## Submodules and multi-repo workspaces

Branching policy applies **per repository**. **Submodule pointer** updates are normal commits on your integration branch (subject/body should name which submodule and why). They are not a separate Forge artifact type — use your workspace **one commit per repo** rule when bumping consumers.

---

## Related

- [Forge overview](../../forge.md) — scaling model, Ore → Spark vocabulary
- [Setup & adoption](README.md) — questionnaire, scaffold, Cursor rules
- [Software engineering — Git](../../../../disciplines/engineering/software-engineering/SOFTWARE-ENGINEERING.md#8-version-control-git)
- [Tracking foundation](../../../templates/sdlc/TRACKING-FOUNDATION.md) — work-unit spine
