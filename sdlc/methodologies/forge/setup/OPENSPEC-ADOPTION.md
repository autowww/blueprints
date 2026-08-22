---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# OpenSpec adoption (Forge Epic execution profile)

Guide for consuming repositories that **opt in** to the [Epic execution profile](../EPIC-EXECUTION-PROFILE.md): Charge lists **Epics**, OpenSpec acceptance defines **L3** scope, and agents decompose **runs** inside the Epic — not WBS Task Charge rows. Core Forge **keeps** Ore → Ingot → **Forge Spark** → Charge on teams that do not adopt this overlay.

## Prerequisites

- Node.js 18+ and a global package manager (`npm`, `pnpm`, `yarn`, or `bun`)
- `blueprints/` submodule (or equivalent path to this pack)
- A repo ready for **L3 Epic** work: one primary repo, reviewable diff, testable SHALLs

## 1. Install OpenSpec CLI (global)

```bash
npm install -g @fission-ai/openspec@latest
openspec --version
```

Prefer `npm` unless your workstation standardizes another global installer. Re-run `openspec update` inside each project after CLI upgrades.

## 2. Disable telemetry (Forge program default)

Forge Epic L3 program sets anonymous CLI telemetry off by default:

```bash
export OPENSPEC_TELEMETRY=0
```

Add to your shell profile or CI env when adopting OpenSpec team-wide. Equivalent: `export DO_NOT_TRACK=1` or `openspec config set telemetry.enabled false`.

## 3. Copy the forge-sdlc schema pack

Canonical templates live in [`../../templates/openspec/`](../../templates/openspec/).

From the **consuming repository root**:

```bash
mkdir -p openspec/schemas/forge-sdlc/templates
cp blueprints/sdlc/templates/openspec/schemas/forge-sdlc/schema.yaml openspec/schemas/forge-sdlc/
cp blueprints/sdlc/templates/openspec/proposal.md \
   blueprints/sdlc/templates/openspec/spec.md \
   blueprints/sdlc/templates/openspec/design.md \
   blueprints/sdlc/templates/openspec/tasks.md \
   openspec/schemas/forge-sdlc/templates/
```

Optional — default schema for new changes:

```yaml
# openspec/config.yaml
schema: forge-sdlc
```

Run `openspec init` once if the repo has no `openspec/` tree yet; then apply the copy steps above (init may scaffold `spec-driven` — replace or add `forge-sdlc` per team choice).

## 4. Validate

```bash
export OPENSPEC_TELEMETRY=0
openspec schema validate forge-sdlc
```

Fix any reported missing templates or dependency errors before Charging Epics.

## 5. Lite vs Full OpenSpec

| Profile | When | Acceptance |
|---------|------|------------|
| **Lite** (default) | Typical feature, UI, or internal behavior in **one repo** | `forge-sdlc` schema: one capability → observable **SHALL** → ≥1 scenario; `tasks.md` non-binding |
| **Full** | API contracts, security-sensitive, or cross-cutting platform work | Human selects stricter OpenSpec layout and review gates at Epic specification time |

Under the Epic execution profile, **Lite is the default**. Upgrade to Full when the size gate or L4 triggers require it — see [Epic execution profile § OpenSpec Lite and Full](../EPIC-EXECUTION-PROFILE.md#openspec-lite-and-full).

## 6. Start an Epic change

Only after the [ready Epic size gate](../EPIC-EXECUTION-PROFILE.md#size-gate-ready-epic) passes:

```bash
export OPENSPEC_TELEMETRY=0
openspec new change <epic-slug> --schema forge-sdlc
```

Fill artifacts in order: `proposal.md` (include **WBS Epic ID**), `specs/**/spec.md` (Lite SHALLs), optional `design.md`, optional `tasks.md` scratch. Humans approve acceptance **before** Charge; agents apply and verify against scenarios.

## Dual profile reminder

Teams **not** on the Epic execution profile continue Spark → Charge unchanged. This guide applies **only under the Epic execution profile**.

## Follow-on integrations (future — out of scope for v1)

Documented for roadmap alignment; **do not** block Epic L3 adoption on these:

| Follow-on | Status | Notes |
|-----------|--------|-------|
| **Graphiti MCP** + knowledge graph | Future | Optional long-horizon memory; not required for OpenSpec Epic flow |
| **Spec Flow board** (Lenses Plan + Today Epic grouping) | Shipped | Seven-column derived lens on WBS + OpenSpec + Charge — [`../SPEC-FLOW-BOARD.md`](../SPEC-FLOW-BOARD.md); Charge remains a view, not a second SoT; **dual wiki on the go** keeps local handbook HTML fresh during Specify/Ready |
| **LevelDB / Lenses `/api/today-charge`** | Future | Program scope excludes unless operator expands |

## Related

| Topic | Location |
|-------|----------|
| Epic execution profile (canon) | [`../EPIC-EXECUTION-PROFILE.md`](../EPIC-EXECUTION-PROFILE.md) |
| Template pack + validate commands | [`../../templates/openspec/README.md`](../../templates/openspec/README.md) |
| Autonomy L3 default | [`../AUTONOMY-LEVELS.md`](../AUTONOMY-LEVELS.md#epic-execution-profile) |
| Forge setup index | [`README.md`](README.md) |
