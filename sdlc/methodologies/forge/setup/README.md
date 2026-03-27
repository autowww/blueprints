# Setup & adoption

A guided flow for consuming repos to adopt Forge SDLC. Includes a questionnaire to determine team configuration, a scaffold script to create directories and files, and a Cursor rule for conversational setup.

## Adoption steps

1. **Answer the questionnaire** — determine team size, roles, product stage, and active disciplines.
2. **Run the scaffold script** — creates `forge/`, `ember-logs/`, and initial configuration.
3. **Install Cursor rules** — `bash blueprints/sdlc/methodologies/forge/setup/install-versona-cursor-rules.sh` (and `--with-standard-forge-rules` as needed); or copy templates manually per [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md).
4. **Validate** — `bash blueprints/sdlc/methodologies/forge/setup/check-forge-cursor-alignment.sh`; after blueprint updates, `diff-versona-cursor-rules.sh` then install with `--force` if appropriate.
5. **Start working** — first refinement, first Charge, first Ember Log entry.

**Full checklist (submodule → Cursor alignment):** see [`../../../SETUP.md`](../../../SETUP.md). **Project Setup Versona** (orchestrated gap analysis; trigger **`setup`**): copy [`../versona/catalog/workflow/versona-project-setup.mdc.template`](../versona/catalog/workflow/versona-project-setup.mdc.template) to `.cursor/rules/versona-project-setup.mdc`. For interactive YAML and team choices, use [`forge-setup.mdc.template`](forge-setup.mdc.template) as `@forge-setup`.

## Files

| File | Purpose |
|------|---------|
| [`QUESTIONNAIRE.md`](QUESTIONNAIRE.md) | Questions to determine Forge configuration |
| [`forge-init.sh`](forge-init.sh) | Scaffold script — creates workspace directories and seed files |
| [`forge.config.template.yaml`](forge.config.template.yaml) | Configuration template |
| [`forge-setup.mdc.template`](forge-setup.mdc.template) | Cursor rule for guided setup (questionnaire) |
| [`../versona/catalog/workflow/versona-project-setup.mdc.template`](../versona/catalog/workflow/versona-project-setup.mdc.template) | Cursor rule — **Project setup** Versona (`setup` / `@versona-project-setup`); checklist + commands |
| [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh) | Copy example **tasklets** + **Sampling Versona** into `.cursor/rules/` |
| [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) | Map `forge.config.yaml` `versona.*` flags → expected `versona-*.mdc` files |
| [`versona_cursor_rules.py`](versona_cursor_rules.py) | Shared map: `forge.config.yaml` → templates; CLI `check` \| `install` \| `diff` |
| [`install-versona-cursor-rules.sh`](install-versona-cursor-rules.sh) | Copy Versonas (and optional Forge rules) into `.cursor/rules/` |
| [`diff-versona-cursor-rules.sh`](diff-versona-cursor-rules.sh) | SHA256 compare installed `.mdc` vs blueprints sources |
| [`check-forge-cursor-alignment.sh`](check-forge-cursor-alignment.sh) | Wrapper: `versona_cursor_rules.py check` (needs PyYAML) |

## Quick start

From the consuming repository root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

This creates the minimal Forge workspace. Then configure using the questionnaire or the Cursor rule.
