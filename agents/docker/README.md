# Docker — foundational files

| File | Role |
|------|------|
| [`Dockerfile.base`](Dockerfile.base) | Default **automation base**: Node LTS on Debian slim + `git`, `curl`, `jq`; `WORKDIR /work`. Extend for Playwright or Python. |
| [`compose.yaml`](compose.yaml) | Builds/tags **`agents-blueprint-base:local`**; documents bind-mount pattern for repo + writable workspace. |
| [`.dockerignore`](.dockerignore) | Keeps build context small when the build context is `blueprints/agents/`. |

**Build context** is **`blueprints/agents/`** (parent of `docker/`). From repository root:

```bash
docker compose -f blueprints/agents/docker/compose.yaml build
```

Override image name or add bind mounts in the mutable **`agents/compose.override.yaml`** (see [`../STRUCTURE.md`](../STRUCTURE.md) §4).
