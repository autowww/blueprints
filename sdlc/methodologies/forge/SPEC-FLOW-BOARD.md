---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
content_id: forge.docs.blueprints.forge.spec-flow-board
canonical_owner: blueprints
primary_persona: engineering_leader
reader_stage: adopt
maturity: defined
evidence_level: canonical_doc
refresh_policy: on_claim_change
last_reviewed: '2026-08-21'
---

# Spec Flow board

## Introduction

The **Spec Flow board** is a **derived Kanban lens** for teams **under the Epic execution profile**. It visualizes how each **WBS Epic** (`M1E3`) moves from intent through OpenSpec acceptance, Charge, agent apply, verify, and archive — without becoming a second system of record.

> **Dual profile.** Core Forge **keeps** Ore → Ingot → **Forge Spark** → Charge (**Sparks**). The Spec Flow board applies **only** when Charge lists **Epics** (Active Epics in `forge/charge.md`) or the repo adopts the **forge-sdlc** OpenSpec schema. Spark-only Today views stay unchanged on core Forge teams.

> **View, not SoT.** WBS, OpenSpec change folders, and `forge/charge.md` remain authoritative. The board **derives** column placement from those sources; drag actions **write back** to them — they do not mint a parallel backlog JSON or sticker-board SoT.

**One card = one Epic + one OpenSpec change** (`openspec/changes/<slug>/`), linked 1:1. **Product Spark** (`M1`) is the Assay / release horizon — not a board card.

**Where it lives:** Forge Lenses Studio exposes the board at `/plan?tab=spec-board` when the Epic execution profile is detected. See [`setup/OPENSPEC-ADOPTION.md`](setup/OPENSPEC-ADOPTION.md) for adoption steps.

---

## Seven columns

Columns run left to right. A card occupies **exactly one** column at a time (overlays are badges, not columns).

| # | Column | Meaning |
|---|--------|---------|
| 1 | **Intent** | Epic exists on WBS; no OpenSpec change folder yet, or intent-only draft |
| 2 | **Specify** | Change folder present; proposal and specs in progress; `openspec validate --strict` not green |
| 3 | **Ready** | Size gate green — validate strict passes; Epic **not** on Charge |
| 4 | **Charged** | Epic on Active Epics with Charge status **planned** |
| 5 | **Apply** | Active Epics row with status **in progress** (or `in-progress`) — agent/human applies the change |
| 6 | **Verify** | Active Epics row with status **done** — acceptance scenarios under proof |
| 7 | **Archived** | Change moved under `openspec/changes/archive/` (or CLI archive destination); no Active Epics row |

**Specify → Ready is computed, not stored.** Ready appears when validation and the [ready Epic size gate](EPIC-EXECUTION-PROFILE.md#size-gate-ready-epic) pass. Dropping a card onto Ready when validate is not green returns **409** — there is no persisted “ready flag” separate from OpenSpec + WBS state.

**Archive ≠ Released.** Archiving an OpenSpec change closes the **Epic change folder** lifecycle. **Released** still requires **Assay Gate** evidence at **Product Spark** scope. A card in **Archived** is not market-ready by definition.

---

## Derivation table

Do **not** add a sidecar board JSON. Derive each card’s column from WBS + `openspec/` + Charge:

| Column | Derived when | Charge status (if Charged) |
|--------|----------------|----------------------------|
| **Intent** | WBS Epic exists; no matching `openspec/changes/<slug>/` | — |
| **Specify** | Change folder present; `openspec validate --strict` not green (or specs incomplete) | — |
| **Ready** | Validate strict green; Epic **not** on Charge | — |
| **Charged** | Active Epics row present | `planned` |
| **Apply** | Active Epics row present | `in progress` / `in-progress` |
| **Verify** | Active Epics row present | `done` |
| **Archived** | Change under `openspec/changes/archive/` (or CLI archive dest); no Active row | — |

**Match Epic ↔ change** (in order):

1. `proposal.md` **`## WBS Epic ID`** (forge-sdlc schema)
2. Active Epics **OpenSpec change** column in `forge/charge.md`
3. Slug heuristics when unambiguous

---

## Charge status map

When an Epic is on Charge, **only three Charge statuses** map to execution columns:

| Charge status (Active Epics) | Board column |
|------------------------------|--------------|
| `planned` | **Charged** |
| `in progress` / `in-progress` | **Apply** |
| `done` | **Verify** |

Epics not on Charge use **Intent**, **Specify**, or **Ready** per the derivation table. **Charged**, **Apply**, and **Verify** require an Active Epics row.

---

## Overlays (not columns)

These states appear as **badges** on cards; they do not replace column placement:

| Overlay | Source | Behavior |
|---------|--------|----------|
| **blocked** | Charge side table / Blocked Epics | Visible stall; drag rules unchanged unless human moves Charge |
| **banked** | Charge side table / Banked Epics | Intentional pause; distinct from blocked |
| **l4_hold** | Proposal or spec marks **L4.2** / cross-repo / architecture hold | Display badge; agent **stop-and-ask** — human clears before apply |

Overlays align with [`process-and-flows.md`](process-and-flows.md) Blocked vs Banked semantics and [`EPIC-EXECUTION-PROFILE.md`](EPIC-EXECUTION-PROFILE.md#l42-stop-and-ask) L4.2 escalation.

---

## Drag writes (v1)

Drag is permitted only when the operator session has the same **write privilege** as other Lenses markdown mutations (loopback / `LENSES_ALLOW_GIT_ACTIONS`). Illegal moves return **409** with reason.

| From → To | Write |
|-----------|--------|
| **Intent → Specify** | Scaffold `openspec/changes/<slug>/` from [forge-sdlc templates](../../templates/openspec/); set **`## WBS Epic ID`** in proposal; **do not** Charge |
| **Specify → Ready** | **No write** — require validate strict green (computed column) |
| **Ready → Charged** | Upsert Active Epics row: status `planned`, OpenSpec slug, actor |
| **Charged → Apply** | Set Active Epics status `in progress` |
| **Apply → Verify** | Set Active Epics status `done` |
| **Verify → Archived** | `openspec archive <slug>` (or equivalent folder move) + remove Active row. **Archive ≠ Released** |
| **Charged → Ready** (reverse) | Delete Active Epics row |
| **Apply → Charged** (reverse) | Set status `planned` |
| **Verify → Apply** (reverse) | Set status `in progress` |

**Forbidden:**

- Mint `M1E3S2T4` / Spark Charge rows or WBS Task process for Charged Epics
- Skip the size gate into **Charged** without human-approved OpenSpec acceptance
- Archive from **Verify** without passing verify (unless a future operator `force` — not v1)
- Treat board drag as **Released** or Assay completion

Conversational polish (e.g. copilot tightening Lite SHALLs) happens in **Specify**; it must not mint parallel WBS Tasks.

---

## Dual-profile behavior

| Profile | Today / Plan lens |
|---------|-------------------|
| **Core Forge** (Spark Charge) | Plan / Today show **Spark** sections; **no** Spec Flow board tab |
| **Epic execution profile** (Active Epics or `openspec/config.yaml` schema `forge-sdlc`) | **Spec Flow board** tab + Epic grouping on Today when implemented |

Detection is **repo-local**. A workspace may run Spark Charge on one repo and Epic Charge on another.

---

## Relationship to Charge and Epic profile

Under the Epic execution profile, **Charge lists Epics** — a daily **view**, not a Kanban SoT ([`EPIC-EXECUTION-PROFILE.md`](EPIC-EXECUTION-PROFILE.md#charge-of-epics)). The Spec Flow board is the **visual projection** of that view plus OpenSpec phase:

- **Ready → Charged** is the human **Charge** decision (size gate green first)
- **Charged / Apply / Verify** track execution inside the Charged Epic boundary
- Agents decompose **runs** at L1–L3 inside Apply — not Charge-visible WBS Task rows

See also [`process-and-flows.md`](process-and-flows.md) (Charge = view, not board).

---

## Related

| Topic | File |
|-------|------|
| Epic execution profile (canon) | [`EPIC-EXECUTION-PROFILE.md`](EPIC-EXECUTION-PROFILE.md) |
| OpenSpec adoption steps | [`setup/OPENSPEC-ADOPTION.md`](setup/OPENSPEC-ADOPTION.md) |
| forge-sdlc schema + templates | [`../../templates/openspec/README.md`](../../templates/openspec/README.md) |
| Naming: Spec Flow board | [`NAMING-REFERENCE.md`](NAMING-REFERENCE.md) |
| Charge vs board collision | [`CONCEPT-MAP.md`](CONCEPT-MAP.md) |
| Core Spark delivery (default Forge) | [`process-and-flows.md`](process-and-flows.md) · [`daily/README.md`](daily/README.md) |

## Executive capsule

The **Spec Flow board** is a seven-column derived lens (**Intent** through **Archived**) for Epic + OpenSpec work **under the Epic execution profile**. Charge statuses `planned` / `in progress` / `done` map to **Charged** / **Apply** / **Verify**; **Specify → Ready** is computed; **archive ≠ Released**. Core Forge **keeps Spark → Charge**.

## Who this is for

Engineering leaders and operators adopting **OpenSpec Epic L3** delivery with Forge Lenses. Read [`EPIC-EXECUTION-PROFILE.md`](EPIC-EXECUTION-PROFILE.md) first if the dual-profile model is new.

## Trust boundary

Humans own Charge selection, OpenSpec acceptance, merge, Assay, and archive vs release distinction. The board writes markdown and OpenSpec folders only within approved drag rules; it does not dispatch ForgeRun or replace WBS as SoT.

## How to use this page

Adopt OpenSpec per [`setup/OPENSPEC-ADOPTION.md`](setup/OPENSPEC-ADOPTION.md), confirm the size gate, then use the board to Charge ready Epics and track apply/verify — without minting Spark Charge rows under the profile.
