# Discipline exploration spike — lifecycle and anchors

This document defines **discipline exploration spikes** in Forge: time-boxed learning work that any discipline may run before committing to delivery scope. It complements [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) (session kinds, manifest fields) and [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) (§5 report shape when a spike closes with a Versona pass).

**Related:** [`../process-and-flows.md`](../process-and-flows.md) (Forge Spark vs exploration spike) · [`../planning/PLANNING-FLOW.md`](../planning/PLANNING-FLOW.md) (Product Spark) · [`../../../templates/sdlc/TRACKING-FOUNDATION.md`](../../../templates/sdlc/TRACKING-FOUNDATION.md) (backlog tree in the consuming repo) · templates [`../../../templates/forge/discipline-spike-open.template.md`](../../../templates/forge/discipline-spike-open.template.md) · [`../../../templates/forge/discipline-spike-close.template.md`](../../../templates/forge/discipline-spike-close.template.md)

---

## 1. Definitions

| Term | Meaning |
|------|---------|
| **Exploration spike** (also **discipline spike**) | Time-boxed work to **answer an unknown** (feasibility, UX risk, compliance gap, architecture choice). Outcome is **learning** and a **record**; code or designs may be throwaway. |
| **Forge Spark** | The smallest **delivery** unit in the Ore → Ingot → **Spark** → Charge pipeline — maps to a **task** in the WBS. Not the same noun as an exploration spike. |
| **Product Spark** | A **product-level** iteration slice (PoC / MVP / phase) in planning — see [PLANNING-FLOW.md](../planning/PLANNING-FLOW.md). |

**Prescriptive rule:** In prose, say **exploration spike** or **discipline spike** when ambiguity with **Forge Spark** or **Product Spark** would confuse readers.

**Informal speech:** Teams sometimes say **“product spike.”** That is **not** a fourth official type. Prefer **exploration spike** or **discipline spike** with product anchors and, when the lens is product strategy, **Product Management** as the owning discipline (`spike_discipline`). The [**Product Management Versona**](catalog/discipline/product/versona-product-management.mdc.template) is often invoked at **spike close** for a structured §5 review (report includes **Suggested next Versonas** per [`VERSONA-CONTRACT.md`](VERSONA-CONTRACT.md) §5). It remains distinct from a [**Product Spark**](../planning/PLANNING-FLOW.md) (planning slice: PoC / MVP / phase).

---

## 2. Who runs it

Any **discipline** (or cross-functional pair) may propose or own an exploration spike. **Versona** use is optional during the spike (e.g. routing or a discipline lens on partial findings) and common at **close** when the team wants a structured review of conclusions before promoting work to Ingots or the backlog.

Session manifest `work_item_kind` values (see [VERSONA-FRAMEWORK.md](VERSONA-FRAMEWORK.md) §7.4):

| Value | Use |
|-------|-----|
| `spike_discipline` | Spike owned by or reviewed through a **named** discipline lens (maps to a bridge under `blueprints/disciplines/`). |
| `spike_general` | Lens **unknown**, **multi-discipline**, or **exploratory** until the team narrows ownership. |

Blueprints do **not** introduce a separate global spike ID scheme. Use **team conventions** in `work_item_refs` (e.g. `SPIKE-ARCH-3`, tracker issue id, or the same id as an **Ore** if the spike is tracked as raw intake).

---

## 3. Where the id and description live

| Element | Typical storage |
|---------|-----------------|
| **Stable folder id** | `forge-logs/versona/<actor>/<session-id>/` — `session_id` matches folder name ([VERSONA-FRAMEWORK.md](VERSONA-FRAMEWORK.md) §7). |
| **Team spike label / external id** | `work_item_refs` in `SESSION.md` YAML frontmatter. |
| **Short description** | `SESSION.md` **Summary** section. |
| **Hypothesis, time box, success criteria** | Open checklist (template) in `SESSION.md` and/or `inputs/` companion file. |
| **Findings and closure** | `outputs/SPIKE-CLOSE.md` (or equivalent under `outputs/`). |
| **Decisions / trade-offs** | `ember-logs/YYYY-MM-DD.md` — set `ember_log_ref` on the session when applicable ([VERSONA-FRAMEWORK.md](VERSONA-FRAMEWORK.md) §8). |
| **Backlog traceability** | Consuming repo: `docs/requirements/` (WBS), `docs/ROADMAP.md`, or tracker — per [TRACKING-FOUNDATION.md](../../../templates/sdlc/TRACKING-FOUNDATION.md). |

---

## 4. Anchors (optional multi-link)

Exploration spikes may attach to zero or more of:

- **Product** — initiative or product name (prose + optional `docs/product/` paths).
- **Roadmap / WBS** — stable ids from `docs/ROADMAP.md`, `docs/requirements/WBS.md` (or CSV), or external epic/story keys.
- **Forge** — **Ore** (why explore), **Ingot** (refined question), **Spark** only if the spike produces **same-day committed execution** work; **Charge** is incidental (today’s view), not a spike anchor.

**Prescriptive rule:** Prefer linking **Ore** or WBS/tracker ids in `work_item_refs` when they exist so closure commits stay traceable.

---

## 5. No roadmap or WBS yet

Two allowed paths (cross-links only — do not duplicate full bootstrap text here).

**Preferred — create anchors before or during the spike**

1. If `docs/`, `forge/`, or blueprints layout is missing: follow the **Project setup** workflow — [`catalog/workflow/versona-project-setup.mdc.template`](catalog/workflow/versona-project-setup.mdc.template) (`@versona-project-setup`).
2. Create roadmap and WBS via the **Product Manager** path:
   - [`../product-manager/product-bootstrap-flow.md`](../product-manager/product-bootstrap-flow.md) **Steps 6–7** — `docs/ROADMAP.md` from [`../../../templates/ROADMAP.template.md`](../../../templates/ROADMAP.template.md), `docs/requirements/WBS.md` from [`../../../../pdlc/templates/WBS.template.md`](../../../../pdlc/templates/WBS.template.md), **or**
   - Equivalent Sparks in [`../product-manager/first-charge.template.md`](../product-manager/first-charge.template.md) (roadmap / WBS rows).
   - Between roadmap and deep WBS: apply **Roadmap Definition of Ready**, run **Product Management Versona** (expect **Suggested next Versonas** in output), or use [`catalog/workflow/versona-roadmap-gate.mdc.template`](catalog/workflow/versona-roadmap-gate.mdc.template) as a playbook.

**Minimal — time-box or product layer not ready**

- Anchor on **product name + Ore (or prose equivalent) + hypothesis** in the session and open template.
- **Close** must list explicit **follow-up** to run bootstrap Steps 6–7 (or add WBS rows) so the next increment has stable ids.
- Still **commit** session `outputs/` (and Ember Log lines for decisions) per team git policy.

---

## 6. Initiation → close

1. **Open** — Create a Versona session folder (e.g. [`../../../scripts/forge-versona-session.sh`](../scripts/forge-versona-session.sh)) from [`../../../templates/forge/versona-session.template.md`](../../../templates/forge/versona-session.template.md). Set `work_item_kind` to `spike_discipline` or `spike_general`. Fill optional manifest hints ([VERSONA-FRAMEWORK.md](VERSONA-FRAMEWORK.md) §7.4). Complete the open checklist template.
2. **Execute** — Time-boxed work; artifacts under `inputs/` and `outputs/`.
3. **Close** — Write `outputs/SPIKE-CLOSE.md`: findings, recommendation (promote to Ingot / new Ore / no-go), follow-up ids, links to any new WBS lines or ADRs.
4. **Decisions** — Append Ember Log entries when scope, risk acceptance, or trade-offs are decided ([`../scripts/forge-ember.sh`](../scripts/forge-ember.sh)).
5. **Git** — Commit traceable changes (session tree, WBS, roadmap, specs). Suggested message pattern:

   `spike(close): <discipline-or-general> <short-ref> — <one-line outcome>`

   Example: `spike(close): architecture SPIKE-ARCH-3 — warehouse path rejected; operational store + async rollups`.

6. **Journal** — Optional row in `forge/journal/YYYY-MM-DD.md` pointing at the session path ([VERSONA-FRAMEWORK.md](VERSONA-FRAMEWORK.md) §8.2).

---

## 7. Phase flavor

Exploration spikes often align with **`discover:`** or **`design:`** Spark prefixes when follow-up work is planned, but they are **not** required to be expressed as Forge Sparks until the team promotes them. Outcomes typically feed **new Ore**, **Ingots**, or WBS updates rather than shipping as production increments.

---

## 8. References

- [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) — session layout, manifest, Ember Log alignment
- [`../process-and-flows.md`](../process-and-flows.md) — work unit hierarchy
- [`../foundation-connection.md`](../foundation-connection.md) — tracking spine
- [`../product-manager/product-bootstrap-flow.md`](../product-manager/product-bootstrap-flow.md) — roadmap and WBS creation
