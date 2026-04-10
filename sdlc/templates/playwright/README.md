# Playwright templates

Copy these files into a repository that already embeds **`blueprints/`** as a submodule. **Do not** commit generated `node_modules` or Playwright output into the blueprint repo.

## Contents

| File | Destination (typical) |
|------|------------------------|
| `playwright.config.ts.template` | Repository root → rename to `playwright.config.ts` |
| `e2e/example-web.spec.ts.template` | `e2e/example-web.spec.ts` |
| `e2e/example-electron.spec.ts.template` | `e2e/example-electron.spec.ts` (adjust `appDir` / env) |
| `github-actions-snippet.md` | Paste into `.github/workflows/` or internal CI docs |

## Bootstrap (recommended)

From the **application repository root** (parent of `blueprints/`):

```bash
./blueprints/sdlc/scripts/init-playwright-e2e.sh
```

Then:

```bash
npm install -D @playwright/test
npx playwright install
# Linux CI: npx playwright install --with-deps
```

Remove or edit the **web** vs **Electron** example spec you do not need.

## Reference

[`../../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md`](../../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md)
