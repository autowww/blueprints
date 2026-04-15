---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Setup & adoption

A guided flow for consuming repos to adopt Forge SDLC. Includes a questionnaire to determine team configuration, a scaffold script to create directories and files, and a Cursor rule for conversational setup.

## Adoption steps

1. **Answer the questionnaire** — determine team size, roles, product stage, and active disciplines.
2. **Run the scaffold script** — creates `forge/`, `ember-logs/`, and initial configuration.
3. **Install Cursor rules** — `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh sync --preset recommended` (quick ref: [`CURSOR-RULES-QUICKSTART.md`](CURSOR-RULES-QUICKSTART.md)); or copy templates manually per [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md).
4. **Validate** — `bash blueprints/sdlc/methodologies/forge/setup/sync-forge-cursor-rules.sh check`; after blueprint updates, `sync-forge-cursor-rules.sh status --preset recommended` or `diff --preset recommended`, then `sync … --force` if appropriate. Full walkthrough: [`VERSONA-VERIFICATION.md`](VERSONA-VERIFICATION.md).
5. **Start working** — first refinement, first Charge, first Ember Log entry.

**Optional — enriched Versona tracking:** canonical tree, JSON schemas, and Rules vs recipes split: [`../VERSONA-OPERATING-MODEL.md`](../VERSONA-OPERATING-MODEL.md) · [`../schemas/README.md`](../schemas/README.md).

**Process-first adoption (from older Versona-only installs):** [`VERSONA-PROCESS-MODEL-MIGRATION.md`](VERSONA-PROCESS-MODEL-MIGRATION.md).

**Optional — standards precedence & registries:** [`../standards/README.md`](../standards/README.md) (Team Rules + `forge/standards-registry.yaml` pattern).

**Full checklist (submodule → Cursor alignment):** see [Project setup checklist](../../../SETUP.md). **Project Setup Versona** (orchestrated gap analysis; trigger **`setup`**): copy [`../versona/catalog/workflow/versona-project-setup.mdc.template`](../versona/catalog/workflow/versona-project-setup.mdc.template) to `.cursor/rules/versona-project-setup.mdc`. For interactive YAML and team choices, use [`forge-setup.mdc.template`](forge-setup.mdc.template) as `@forge-setup`.

## Files

| File | Purpose |
|------|---------|
| [`QUESTIONNAIRE.md`](QUESTIONNAIRE.md) | Questions to determine Forge configuration |
| [`BRANCHING-STRATEGY.md`](BRANCHING-STRATEGY.md) | Git branching by Forge scale + commit message/body rules (agents & search) |
| [`charge-plans/branching/README.md`](charge-plans/branching/README.md) | **Branching charge pack** — Forge-native Charges (F1–F3), Branch Steward, Cursor preamble; copy to `forge/charge-plans/branching/` in consumers |
| [`forge-init.sh`](forge-init.sh) | Scaffold script — creates workspace directories and seed files |
| [`forge.config.template.yaml`](forge.config.template.yaml) | Configuration template |
| [`forge-setup.mdc.template`](forge-setup.mdc.template) | Cursor rule for guided setup (questionnaire) |
| [`../versona/catalog/workflow/versona-project-setup.mdc.template`](../versona/catalog/workflow/versona-project-setup.mdc.template) | Cursor rule — **Project setup** Versona (`setup` / `@versona-project-setup`); checklist + commands |
| [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh) | Copy example **tasklets** + **Sampling Versona** into `.cursor/rules/` |
| [`CURSOR-RULES-QUICKSTART.md`](CURSOR-RULES-QUICKSTART.md) | Short onboarding: `sync`, `status`, `diff`, presets |
| [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) | Map `forge.config.yaml` `versona.*` flags → expected `versona-*.mdc` files |
| [`versona_cursor_rules.py`](versona_cursor_rules.py) | Shared map: `forge.config.yaml` → templates; CLI `check` \| `install` \| `diff` \| `status` |
| [`sync-forge-cursor-rules.sh`](sync-forge-cursor-rules.sh) | One entry: `sync` \| `diff` \| `status` \| `check` |
| [`VERSONA-PROCESS-MODEL-MIGRATION.md`](VERSONA-PROCESS-MODEL-MIGRATION.md) | Move from discipline-rules-only to process-first (artifacts, Skills, ledger, diagrams) |
| [`VERSONA-VERIFICATION.md`](VERSONA-VERIFICATION.md) | End-to-end verification + optional Cloud Agent notes |
| [`install-versona-cursor-rules.sh`](install-versona-cursor-rules.sh) | Thin wrapper → `sync sync` |
| [`diff-versona-cursor-rules.sh`](diff-versona-cursor-rules.sh) | Thin wrapper → `sync diff` |
| [`check-forge-cursor-alignment.sh`](check-forge-cursor-alignment.sh) | Thin wrapper → `sync check` |
| [`VERSIONING-AND-RELEASES.md`](VERSIONING-AND-RELEASES.md) | Shared semver + changelog policy; optional post-commit automation |
| [`install-version-release-hook.sh`](install-version-release-hook.sh) | Installs `.git/hooks/post-commit` → `hooks/version-release-post-commit.py` |
| [`templates/version-release.manifest.example.json`](templates/version-release.manifest.example.json) | Copy to repo root `.forge/version-release.json` |

## Quick start

From the consuming repository root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

This creates the minimal Forge workspace. Then configure using the questionnaire or the Cursor rule.
