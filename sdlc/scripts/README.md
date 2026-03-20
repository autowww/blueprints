# Scripts (`blueprints/sdlc/scripts/`)

Small helpers for **consuming repos** (not required to *use* the SDLC process text). Run from the **repository root** (where `blueprints/sdlc/` lives).

## `init-sdlc-workspace.sh`

Creates or refreshes a project **`sdlc/`** folder from [`../templates/sdlc/`](../templates/sdlc): copies `TRACKING-*.md` and renders `README.md` from `README.template.md` with the project name.

**Requires:** `bash`, **`python3`** (for safe `{{PROJECT_NAME}}` substitution).

**Usage:**

```bash
# Default target directory: ./sdlc
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name"

# Custom target (e.g. scratch compare folder)
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name" sdlc.new

# Overwrite existing README.md in target (TRACKING files are always copied)
./blueprints/sdlc/scripts/init-sdlc-workspace.sh "My Product Name" sdlc --force
```

**Human-oriented steps** (manual copy, no script): see [`../SDLc-WORKSPACE.md`](../SDLc-WORKSPACE.md).

---

*Part of [`blueprints/sdlc/README.md`](../README.md).*
