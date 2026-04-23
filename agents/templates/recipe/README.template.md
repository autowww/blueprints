---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Recipe: {{RECIPE_NAME}}

{{ONE_LINE_PURPOSE}}

## Layout

| Path (in container) | Use |
|---------------------|-----|
| `/work` | Repository root (read-only when possible) |
| `/workspaces/{{RECIPE_NAME}}` | Writable output — mirror: `agents/workspaces/{{RECIPE_NAME}}/` on the host |

## Run locally (pattern)

From repository root, with Docker and the base image built (`blueprints/agents/docker/`):

```bash
# Example — adjust image and mounts to match your compose overrides
docker compose -f blueprints/agents/docker/compose.yaml run --rm \
  -v "$PWD:/work:ro" \
  -v "$PWD/agents/workspaces/{{RECIPE_NAME}}:/workspaces/{{RECIPE_NAME}}" \
  agent-base bash agents/recipes/{{RECIPE_NAME}}/run.sh
```

## Environment

| Variable | Required | Description |
|----------|----------|-------------|
| — | — | Add rows as needed |

## CI

Describe which workflow/job invokes this recipe and any required secrets (by name only).
