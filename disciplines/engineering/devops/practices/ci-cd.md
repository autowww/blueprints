# Continuous Integration & Continuous Delivery / Deployment (blueprint)

**CI/CD** automates the path from code change to production-ready software. Treating the pipeline as a product reduces risk, shortens feedback loops, and makes delivery measurable. This guide is **project-agnostic**; it describes patterns, gates, and metrics teams use regardless of vendor.

---

## 1. CI vs CD: naming and scope

The acronym **CD** is overloaded. Distinguish **continuous delivery** (software is *always releasable*, release may be manual) from **continuous deployment** (every passing change *automatically* reaches production).

| Term | Meaning | Human gate? | Typical outcome |
|------|---------|-------------|-----------------|
| **CI** (Continuous Integration) | Frequent integration to mainline with automated build and test | No for merge; yes for code review | Main branch stays green; fast feedback on defects |
| **CD** (Continuous **Delivery**) | Pipeline produces deployable artifacts; deployment to prod is a business decision | Often yes (approve release) | Any commit *could* go live; release is low ceremony |
| **CD** (Continuous **Deployment**) | Automated promotion to production when quality gates pass | No for routine deploys (policy encodes gates) | Highest automation; requires strong tests and observability |

**Mnemonic:** *Delivery* = “we *can* ship”; *Deployment* = “we *do* ship” when the pipeline says so.

---

## 2. Reference pipeline (conceptual)

The following flow is a **composite** pattern; teams omit or reorder stages by risk profile and regulatory context.

```blueprint-diagram
key: linear
alt: Diagram
```

**Notes:** SAST may run in parallel with unit tests; “approval gate” may be a manual change ticket, policy-as-code, or fully automated in continuous deployment setups.

---

## 3. CI practices

| Practice | Description | Benefit |
|----------|-------------|---------|
| **Trunk-based development** | Small, frequent merges to main; short-lived branches | Reduces merge pain; keeps integration feedback fast |
| **Feature flags** | Decouple deploy from release; toggle behavior without new deploy | Safe incremental rollout; supports CD and experiments |
| **Branch by abstraction** | Introduce large changes behind an abstraction on main | Avoids long-lived feature branches |
| **Build caching** | Cache dependencies, layers, compiler outputs | Cuts pipeline time and cost |
| **Test parallelization** | Shard tests across workers | Scales feedback with codebase size |
| **Artifact versioning** | Immutable, content-addressed or semver-tagged artifacts | Reproducible deploys and rollbacks |

---

## 4. CD practices (deployment and release)

| Practice | Description | When it fits |
|----------|-------------|--------------|
| **Blue-green** | Two identical environments; switch traffic atomically | Need fast rollback; can afford duplicate capacity |
| **Canary** | Route small % of traffic to new version; expand if healthy | Gradual risk reduction; strong metrics required |
| **Rolling updates** | Replace instances incrementally | Common default in orchestrators; balances speed and capacity |
| **Feature flags** | Control user-visible features independently of binary version | Experimentation; kill switches |
| **Dark launches** | Ship code inert in production; enable later | Validate operational behavior before user impact |
| **A/B deployment** | Different versions for cohorts; measure outcomes | Product experimentation; needs routing and analytics |

---

## 5. Pipeline design patterns

| Pattern | Description | Example use |
|---------|-------------|-------------|
| **Fan-in** | Multiple upstream jobs feed one downstream stage | Combine artifacts from several packages before deploy |
| **Fan-out** | One trigger runs many parallel jobs | Matrix across OS, language versions, regions |
| **Matrix builds** | Same workflow, different dimensions | Node 18/20 × Linux/macOS |
| **Monorepo pipelines** | Selective builds via change detection | Only test affected packages in a large repo |
| **Multi-environment promotion** | Dev → staging → prod with same artifact | Immutable artifact promoted; config per environment |

---

## 6. Deployment strategies (comparison)

```blueprint-diagram
key: swimlane
alt: Diagram
```

| Strategy | Blast radius | Rollback | Resource cost |
|----------|--------------|----------|---------------|
| Blue-green | Switched in one step | Revert traffic | High (duplicate stack) |
| Canary | Small, grows with validation | Stop shift or drain canary | Medium |
| Rolling | Per instance | Stop roll or roll forward | Lower extra capacity |

---

## 7. Quality gates by stage

| Stage | Typical checks | Failure means |
|-------|----------------|---------------|
| **Lint / static analysis** | Style, complexity, import rules | Fix before merge or block pipeline |
| **Unit** | Fast, isolated tests | Defect in module contract |
| **Integration** | Services, DB, queues with test doubles or containers | Cross-component breakage |
| **Security scan** | SAST, dependency SBOM, secrets detection | Vulnerability or policy violation |
| **Performance** | Load smoke, regression budgets | Latency or throughput regression |
| **Compliance** | License allow-list, attestations, policy checks | Cannot ship to regulated boundary |

---

## 8. Metrics

| Metric | Definition | Why it matters |
|--------|------------|----------------|
| **Build time** | Wall-clock from trigger to green artifact | Developer flow; infra cost |
| **Deployment frequency** | Deploys to production per unit time | DORA; batch size proxy |
| **Lead time for changes** | Commit to production | DORA; value stream speed |
| **Change failure rate** | Deployments causing incident or rollback / total deploys | DORA; quality of pipeline and culture |
| **MTTR** (recovery) | Detect to restored service | DORA; operational readiness |

See also [`DEVOPS.md`](../DEVOPS.md) for DORA context and maturity framing.

---

## 9. Anti-patterns

| Anti-pattern | Risk | Remedy |
|--------------|------|--------|
| Long-running branches | Integration defects discovered late | Trunk-based development, smaller PRs |
| Manual deployment steps | Drift, slow recovery, human error | Automate; document as code |
| Environment snowflakes | “Works on my machine” in prod | IaC, parity, config management — see [`iac-gitops.md`](iac-gitops.md) |
| No rollback plan | Long outages during failed deploy | Reversible migrations, feature flags, documented rollback |

---

## 10. Technology landscape (illustrative)

| Tool | Model | Strengths | Trade-offs |
|------|--------|-----------|------------|
| **GitHub Actions** | Hosted CI/CD YAML | Ecosystem, GitHub integration | Runner limits; complex org policy |
| **GitLab CI** | Pipeline as code in repo | Integrated DevSecOps, MR workflow | Heavier platform adoption |
| **Jenkins** | Controller + agents, plugins | Flexible, on-prem friendly | Operational overhead |
| **CircleCI** | Cloud/native config | DX, parallelism | Cost at scale |
| **Azure DevOps** | Pipelines + boards + artifacts | Microsoft stack integration | Multi-cloud less native |
| **Argo CD** | Pull Git → cluster | K8s-native GitOps | Kubernetes-centric |
| **Flux** | GitOps controllers | Lightweight, composable | Assembly required |

**CD “last mile”** often pairs a **build CI** (GitHub Actions, GitLab CI, Jenkins) with a **GitOps or deploy controller** (Argo CD, Flux) for cluster state.

---

## 11. External references

| Resource | Notes |
|----------|--------|
| *Continuous Delivery* — Jez Humble & David Farley | Foundational pipeline and deployment discipline |
| *Accelerate* — Nicole Forsgren et al. | DORA metrics and what predicts performance |
| [minimumcd.org](https://minimumcd.org/) | Minimal definitions for CD and related practices |

---

*Keep project-specific DevOps configuration in docs/development/CI-CD.md and infrastructure documentation in docs/operations/, not in this file.*
