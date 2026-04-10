---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
---

# Docker — foundational files

| File | Role |
|------|------|
| [`Dockerfile.base`](Dockerfile.base) | Default **automation base**: Node LTS on Debian slim + `git`, `curl`, `jq`; `WORKDIR /work`. |
| [`Dockerfile.playwright`](Dockerfile.playwright) | Adds **Chromium system dependencies** via `playwright install-deps` for browser/Electron-style jobs; image **`agents-blueprint-playwright:local`**. |
| [`compose.yaml`](compose.yaml) | Builds **`agents-blueprint-base:local`** and **`agents-blueprint-playwright:local`**; bind-mount repo at **`/work`**. |
| [`.dockerignore`](.dockerignore) | Keeps build context small when the build context is `blueprints/agents/`. |

**Build context** is **`blueprints/agents/`** (parent of `docker/`). From repository root:

```bash
docker compose -f blueprints/agents/docker/compose.yaml build
```

Override image name or add bind mounts in the mutable **`agents/compose.override.yaml`** (see [`../STRUCTURE.md`](../STRUCTURE.md) §4).
