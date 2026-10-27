---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# OpenSpec — Forge SDLC template pack

Canonical **forge-sdlc** OpenSpec schema and artifact templates for teams **under the Epic execution profile**. Copy into a consuming repository's `openspec/` tree — do not edit consumer copies without bumping the blueprints submodule first.

## Contents

| Path | Role |
|------|------|
| [`schemas/forge-sdlc/schema.yaml`](schemas/forge-sdlc/schema.yaml) | Custom workflow: WBS Epic id → Lite SHALL spec → optional design → non-binding `tasks.md` scratch |
| [`proposal.md`](proposal.md) | Epic proposal template (`## WBS Epic ID` required) |
| [`spec.md`](spec.md) | Lite capability spec — observable **SHALL** / **MUST** + scenarios |
| [`design.md`](design.md) | Optional technical design |
| [`tasks.md`](tasks.md) | **Non-binding** agent scratch (header states this explicitly) |
| [`schemas/forge-sdlc/templates/`](schemas/forge-sdlc/templates/) | Same four templates at paths referenced by `schema.yaml` (for OpenSpec CLI validation) |

**Adoption:** [`../../methodologies/forge/setup/OPENSPEC-ADOPTION.md`](../../methodologies/forge/setup/OPENSPEC-ADOPTION.md)

**Profile canon:** [`../../methodologies/forge/EPIC-EXECUTION-PROFILE.md`](../../methodologies/forge/EPIC-EXECUTION-PROFILE.md)

## Install into a repo

From the **consuming repository root** (after `blueprints/` submodule is present):

```bash
mkdir -p openspec/schemas/forge-sdlc/templates
cp blueprints/sdlc/templates/openspec/schemas/forge-sdlc/schema.yaml openspec/schemas/forge-sdlc/
cp blueprints/sdlc/templates/openspec/proposal.md \
   blueprints/sdlc/templates/openspec/spec.md \
   blueprints/sdlc/templates/openspec/design.md \
   blueprints/sdlc/templates/openspec/tasks.md \
   openspec/schemas/forge-sdlc/templates/
```

Optional default schema in `openspec/config.yaml`:

```yaml
schema: forge-sdlc
```

Create a change for a ready Epic:

```bash
export OPENSPEC_TELEMETRY=0
openspec new change my-epic-slug --schema forge-sdlc
```

## Validate the schema

After installing the OpenSpec CLI (`npm install -g @fission-ai/openspec@latest`):

```bash
cd /path/to/consuming-repo
openspec schema validate forge-sdlc
```

From a **blueprints-only** checkout (structural check of the pack layout):

```bash
cd blueprints/sdlc/templates/openspec/schemas/forge-sdlc
openspec schema validate forge-sdlc --store "$(pwd)/../.."
```

Or validate YAML syntax without the CLI:

```bash
python3 -c "import yaml; yaml.safe_load(open('blueprints/sdlc/templates/openspec/schemas/forge-sdlc/schema.yaml'))"
```

`openspec schema validate` additionally checks template file existence, artifact dependency graph (no cycles), and schema field conformance.

## Workflow summary (forge-sdlc)

| Artifact | Binding? | Notes |
|----------|----------|-------|
| `proposal.md` | Yes | Must include **WBS Epic ID** (e.g. `M1E3`) |
| `specs/**/spec.md` | Yes | Lite observable SHALLs + ≥1 scenario per requirement |
| `design.md` | Optional | Skip for straight single-repo Lite Epics |
| `tasks.md` | **No** | Agent scratch only; apply does not track checkboxes |

## Related

- Epic execution profile — [`EPIC-EXECUTION-PROFILE.md`](../../methodologies/forge/EPIC-EXECUTION-PROFILE.md)
- OpenSpec upstream — [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
