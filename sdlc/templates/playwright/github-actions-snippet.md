# GitHub Actions — Playwright (snippet)

Paste into `.github/workflows/<name>.yaml` or adapt for your CI. Adjust **paths** (`working-directory`, `cache`) to match your repo.

**Linux + Electron:** use `xvfb-run` so the shell can create a display.

```yaml
jobs:
  playwright:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: "20"
          cache: npm
          cache-dependency-path: package-lock.json

      - name: Install Node dependencies
        run: npm ci
        working-directory: . # e.g. desktop/

      - name: Install Playwright browsers
        run: npx playwright install --with-deps
        working-directory: .

      - name: Run Playwright
        run: xvfb-run --auto-servernum -- npm run test:e2e
        working-directory: .
        env:
          CI: "true"
          # Add app-specific env, e.g. workspace root for Electron shells:
          # LENSES_WORKSPACE_ROOT: ${{ github.workspace }}

      - uses: actions/upload-artifact@v4
        if: failure()
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 7
```

**Web-only** (no Electron): you can often omit `xvfb-run` when using fully headless browser projects.

**Python sidecars:** If your Electron app spawns a local server, add `actions/setup-python`, `pip install`, and export `PYTHONPATH` before the Playwright step.

See [`PLAYWRIGHT-INFRASTRUCTURE.md`](../../../disciplines/engineering/testing/PLAYWRIGHT-INFRASTRUCTURE.md) for the full adoption checklist.
