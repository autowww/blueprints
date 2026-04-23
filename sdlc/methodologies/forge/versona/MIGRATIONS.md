---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Versona migrations

When **blueprints** changes Versona **session** layouts, **manifest** fields, or **§5 report** shapes, consuming repos may need to adjust existing `forge-logs/versona/**` trees or local conventions.

## Cursor rules (`.mdc`)

- **No automatic rewrite** of `.cursor/rules/` — after `git submodule update`, run [`../setup/sync-forge-cursor-rules.sh`](../setup/sync-forge-cursor-rules.sh) `diff --preset recommended` (or `status`) before `sync … --force`. See [`../setup/CURSOR-RULES-QUICKSTART.md`](../setup/CURSOR-RULES-QUICKSTART.md).
- Local **globs** or edits in installed `.mdc` files are overwritten by `--force`; re-apply custom globs after sync if needed.

## Session folders and manifests

- Optional field **`versona_session_schema_version`** (see [`VERSONA-FRAMEWORK.md`](VERSONA-FRAMEWORK.md) §7.4) lets teams and tools record which manifest/session shape a folder uses.
- When blueprints publishes a **breaking** change, this file should gain a short **versioned** subsection: what changed, how to patch `SESSION.md` / `session.manifest.yaml`, and whether AI-assisted migration is appropriate (**human review** required).

### Playbook (generic)

1. Identify sessions under `forge-logs/versona/<actor>/<session-id>/`.
2. Compare folder contents to current templates: [`../../templates/forge/versona-session.template.md`](../../templates/forge/versona-session.template.md), [`../../templates/forge/session.manifest.yaml.template`](../../templates/forge/session.manifest.yaml.template).
3. Update frontmatter / YAML to match; set or bump `versona_session_schema_version` if your team adopts it.
4. Commit with a message referencing the blueprint commit or release.

## Operating model and JSON schemas (optional)

[`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) adds **optional** paths under `forge-logs/versona-track/` and JSON files next to existing `SESSION.md` trees. **No migration** is required for teams that do not adopt them. When adopting:

1. Create `forge-logs/versona-track/` (or monthly shards per operating model §1.2).
2. Add `session.manifest.json` only for **new** or **actively maintained** sessions if desired; old folders remain valid with `SESSION.md` only.
3. Set `versona_session_schema_version` when pinning to a schema revision.

Schema files live under [`../schemas/`](../schemas/); breaking JSON Schema changes should add a row below.

## Changelog entries

Add a row here when session or manifest **contracts** change in a way that affects existing files:

| Blueprint change (summary) | Affected artifacts | Migration hint |
|----------------------------|-------------------|----------------|
| **Setup / presets** — **`recommended`** preset includes **`versona-sampling.mdc`**; **`forge-init.sh`** creates **`forge-logs/`** and **`forge-logs/versona-track/`**; optional **`.forge/versona-adoption-manifest.json`** via **`sync --write-adoption-manifest`**; docs **`setup/VERSONA-PROCESS-MODEL-MIGRATION.md`**, **`setup/VERSONA-VERIFICATION.md`** | Installed `.mdc`; empty dirs in repo; optional manifest | Re-run **`sync --preset recommended`** (review **`status`** / **`diff`** first). Expect **`versona-sampling.mdc`** added. Commit **`forge-logs/**` **`.gitkeep`** trees if your team tracks them. Use **`--write-adoption-manifest`** once if you want the companion JSON for onboarding automation. |
| **Estimation Versona** — new `versona-estimation.mdc.template` (Governance); **`versona-pm`** gains explicit **out-of-scope** line for estimation **method** (Fibonacci/t-shirt/tokens, `ESTIMATES.md` calibration); templates `forge/estimation/ESTIMATION-RULES.template.md`, `requirements/ESTIMATES.template.md`, `forge-estimation-bootstrap.prompt.md`; **standards matrix** adds `versona-estimation` | Installed `.mdc`; teams sizing in Markdown | Optionally install `versona-estimation`; copy estimation templates to `forge/estimation/` and `docs/requirements/`; re-sync rules if PM template updated. |
| **Specialist Versona alignment** — Engineering, Data, Security, Compliance, and **`versona-generic`** templates gain **specialist standards profile**, **Artifact I/O**, **trace/Skills/parallel-work**, **handoff.json** hooks, **merge compatibility**, and **§5** blocks (**Standards traceability**, **Suggested next Versonas**); Security/Compliance **precedence override** over L3–L6 methodology | Installed specialist `.mdc` | Re-sync rules; optional adoption of `handoff.json` in CI. |
| **Orchestration / product governance template alignment** — `versona-all`, `versona-forge-sdlc`, family aggregators, `versona-pm`, product-family disciplines, workflow rules gain **Artifact I/O**, **standards/trace**, **merge/routing**, explicit **PM vs Product Management vs BA** boundaries; `VERSONA-SKILL-MATRIX.md` §0 + `orchestration/README.md` table | Installed `.mdc` from listed templates | Re-sync Cursor rules from blueprints; no session file migration. |
| **Skill / tasklet layer** — `versona/VERSONA-SKILL-MATRIX.md`; eight **Skills** under `sdlc/templates/forge/cursor-skills/`; six new **cognition tasklets** (`route-request`, `bootstrap-session`, `check-standards`, `log-event`, `merge-outputs`, `summarize-evidence`); recipe **stub templates** `versona-evidence-pack-assemble`, `versona-kitchensink-diagram-export` under `agents/templates/recipe/`; Layer 0 baseline + templates gain **Reusable capabilities** paragraph | Copied `.cursor/skills/`; `install-tasklets.sh` installs new `.mdc` | Copy new Skills; re-run tasklet installer (`--force` if replacing); copy recipe stubs to `agents/recipes/` when using execution plane. |
| **Artifact contracts** — `versona/ARTIFACT-CONTRACTS.md` (canonical `docs/`, `forge/`, `forge-logs/`, `forge/evidence/`); **VERSONA-CONTRACT** §2a **Artifact I/O** required for new/updated discipline templates; **RECOMMENDED-GLOBS** aligned to canonical tree | Installed `.mdc` globs; new `forge/evidence/` optional | Re-tune `globs:` when syncing rules; add `## Artifact I/O` when editing a template. Existing sessions and specs paths unchanged until teams migrate. |
| **Forge SDLC orchestration** — `versona-forge-sdlc.mdc.template` (workflow); `forge/orchestration/` (FORGE-SDLC-ORCHESTRATION.md, `workflows/phases.json`); **recommended** preset now includes `versona-forge-sdlc.mdc` | Installed `.mdc`; teams using `--preset recommended` | Re-sync Cursor rules; invoke `@versona-forge-sdlc` for phase-aware plans. No change to discipline §5 contracts. |
| **Standards resolution** — `forge/standards/` (precedence, matrix, registry/waiver schemas); **§5.1** traceability fields; **Standards resolution** paragraph in Layer 0 baseline (`GENERIC-VERSONA-BASELINE.md` + all `versona-*.mdc.template` + packaged `forge-versona.mdc`) | Installed `.mdc` rules; §5 session exports | Re-sync Versona rules from blueprints. Add optional `forge/standards-registry.yaml` in consuming repo; use Team Rules for L1–2. Historical §5 reports without §5.1 remain valid. |
| **Versona operating model** — canonical `versona-track/` tree; optional `session.manifest.json`, `outputs/handoff.json`, `routing-decision.json`, `artifact-manifest.json`, `diagrams/`; JSON Schemas under `forge/schemas/` | Consuming repos that opt in to machine-readable artifacts | Opt-in only; existing `forge-logs/versona/**` without JSON remains valid. Backfill ledger/graph lines when enabling analytics. |
| Terminology: “Versona challenge” → sessions / §5 structured output; example heading `## {Discipline} Versona — structured output`; **Review depth** replaces “Challenge intensity”; Cursor skill folder `run-product-versona-challenge` → `run-product-versona-session` | Installed `.mdc` rules; day journal / planning templates; copied skills; historical session markdown under `outputs/` | Old headings in saved logs are still readable; optional rename for consistency. Re-copy skill from `sdlc/templates/forge/cursor-skills/run-product-versona-session/`. Re-sync Versona rules from blueprints. |
