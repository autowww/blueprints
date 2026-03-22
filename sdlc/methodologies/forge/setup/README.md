# Setup & adoption

A guided flow for consuming repos to adopt Forge SDLC. Includes a questionnaire to determine team configuration, a scaffold script to create directories and files, and a Cursor rule for conversational setup.

## Adoption steps

1. **Answer the questionnaire** — determine team size, roles, product stage, and active disciplines.
2. **Run the scaffold script** — creates `forge/`, `ember-logs/`, and initial configuration.
3. **Configure Bellows** — copy relevant Bellows templates to `.cursor/rules/`.
4. **Configure Cursor rules** — copy daily and planning rules to `.cursor/rules/`.
5. **Start working** — first refinement, first Charge, first Ember Log entry.

## Files

| File | Purpose |
|------|---------|
| [`QUESTIONNAIRE.md`](QUESTIONNAIRE.md) | Questions to determine Forge configuration |
| [`forge-init.sh`](forge-init.sh) | Scaffold script — creates workspace directories and seed files |
| [`forge.config.template.yaml`](forge.config.template.yaml) | Configuration template |
| [`forge-setup.mdc.template`](forge-setup.mdc.template) | Cursor rule for guided setup |

## Quick start

From the consuming repository root:

```bash
./blueprints/sdlc/methodologies/forge/setup/forge-init.sh
```

This creates the minimal Forge workspace. Then configure using the questionnaire or the Cursor rule.
