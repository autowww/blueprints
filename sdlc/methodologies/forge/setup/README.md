# Setup & adoption

A guided flow for consuming repos to adopt Forge SDLC. Includes a questionnaire to determine team configuration, a scaffold script to create directories and files, and a Cursor rule for conversational setup.

## Adoption steps

1. **Answer the questionnaire** — determine team size, roles, product stage, and active disciplines.
2. **Run the scaffold script** — creates `forge/`, `ember-logs/`, and initial configuration.
3. **Configure Versonas** — copy relevant Versonas templates to `.cursor/rules/`.
4. **Configure Cursor rules** — copy daily and planning rules to `.cursor/rules/`.
5. **Start working** — first refinement, first Charge, first Ember Log entry.

**Full checklist (submodule → Cursor alignment):** see [`../../../SETUP.md`](../../../SETUP.md). **Project Setup Versona** (orchestrated gap analysis; trigger **`setup`**): copy [`../versona/versona-project-setup.mdc.template`](../versona/versona-project-setup.mdc.template) to `.cursor/rules/versona-project-setup.mdc`. For interactive YAML and team choices, use [`forge-setup.mdc.template`](forge-setup.mdc.template) as `@forge-setup`.

## Files

| File | Purpose |
|------|---------|
| [`QUESTIONNAIRE.md`](QUESTIONNAIRE.md) | Questions to determine Forge configuration |
| [`forge-init.sh`](forge-init.sh) | Scaffold script — creates workspace directories and seed files |
| [`forge.config.template.yaml`](forge.config.template.yaml) | Configuration template |
| [`forge-setup.mdc.template`](forge-setup.mdc.template) | Cursor rule for guided setup (questionnaire) |
| [`../versona/versona-project-setup.mdc.template`](../versona/versona-project-setup.mdc.template) | Cursor rule — **Project setup** Versona (`setup` / `@versona-project-setup`); checklist + commands |
| [`../tasklets/install-tasklets.sh`](../tasklets/install-tasklets.sh) | Copy example **tasklets** + **Sampling Versona** into `.cursor/rules/` |
| [`CURSOR-RULES-ALIGNMENT.md`](CURSOR-RULES-ALIGNMENT.md) | Map `forge.config.yaml` `versona.*` flags → expected `versona-*.mdc` files |
| [`check-forge-cursor-alignment.sh`](check-forge-cursor-alignment.sh) | Script: list missing Versona rules under `.cursor/rules/` (needs PyYAML) |

## Quick start

From the consuming repository root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

This creates the minimal Forge workspace. Then configure using the questionnaire or the Cursor rule.
