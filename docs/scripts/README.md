# Scripts — documentation blueprint

| Script | Purpose |
|--------|---------|
| [`init-docs-workspace.sh`](init-docs-workspace.sh) | Bootstrap the full `docs/` tree from templates. |

## Usage

From the **repository root** (where `blueprints/docs/` lives):

```bash
./blueprints/docs/scripts/init-docs-workspace.sh "Project Name"
```

**Options:**

- `--force` — overwrite existing files (default: skip if file exists).
- `-h`, `--help` — show usage.

The script:

1. Copies all `*.template.*` files from `blueprints/docs/templates/` into `docs/`, stripping the `.template.` segment from filenames.
2. Also seeds `docs/ROADMAP.md` from `blueprints/sdlc/templates/ROADMAP.template.md`.
3. Replaces `{{PROJECT_NAME}}` and `{{DATE}}` placeholders with the provided name and current date.
4. Creates empty scaffold directories (`milestones/M1/epics`, `risks/items`).

**Companion scripts:** [`blueprints/sdlc/scripts/init-sdlc-workspace.sh`](../../sdlc/scripts/init-sdlc-workspace.sh) (bootstrap `sdlc/`) · [`blueprints/ide/scripts/init-ide-workspace.sh`](../../ide/scripts/init-ide-workspace.sh) (bootstrap IDE agent files).
