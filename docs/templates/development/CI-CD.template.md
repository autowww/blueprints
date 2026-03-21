# CI/CD — {{PROJECT_NAME}}

**Purpose:** Where automation runs, which **quality gates** block merges, and how that ties to [`blueprints/sdlc/SDLC.md`](../../blueprints/sdlc/SDLC.md) §7.

## Pipeline

| Item | Detail |
|------|--------|
| **Host** | <!-- e.g. GitHub Actions, GitLab CI, Jenkins --> |
| **Workflow** | <!-- link to workflow file --> |
| **Triggers** | <!-- e.g. push and PR to main --> |

## Quality gates (required for merge)

<!-- List the checks that must pass before a PR can merge. -->

| Step | Command | Purpose |
|------|---------|---------|
| Compile | <!-- e.g. ./gradlew build --> | Ensures the project builds |
| Lint | <!-- e.g. eslint, Android Lint --> | Static analysis |
| Unit tests | <!-- e.g. npm test --> | JVM / Node / etc. unit tests |

## Branch protection (recommended)

In the repository **Settings → Branches**, require the CI check to pass before merging to the default branch.

## Release automation

<!-- Document release workflow when configured. Keep secrets in CI provider settings only. -->

## Related

- Test plans: [`docs/testing/README.md`](../testing/README.md) · blueprint template [`blueprints/sdlc/templates/TEST-PLAN.template.md`](../../blueprints/sdlc/templates/TEST-PLAN.template.md)

---

*Update this file when workflows or required checks change.*
