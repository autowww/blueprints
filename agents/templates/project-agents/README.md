---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Mutable `agents/` workspace (seed)

Copy the contents of this folder to **`agents/`** at repository root (sibling to `blueprints/agents/`).

| File / path | Purpose |
|-------------|---------|
| `README.md` | Local conventions: naming, secrets, CI pointers. |
| `workspaces/.gitkeep` | Writable scratch; gitignore large artifacts. |
| `recipes/` | One folder per automation job (from [`../recipe/`](../recipe/README.md)); seeded with `.gitkeep`. |
| `compose.override.yaml` (optional) | Project-specific Compose overrides; **do not** commit secrets. |

Add **`agents/`** to `.gitignore` only if you treat automation as local-only; most teams **commit** `recipes/` and **ignore** `workspaces/*` except `.gitkeep`.
