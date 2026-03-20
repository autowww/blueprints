# Security policy

## Supported versions

Security-sensitive fixes apply to the latest default branch (`main`). There are no numbered releases; consume at a specific commit if you need a fixed baseline.

## Reporting a vulnerability

**Please do not** open a public issue for undisclosed security problems.

1. Prefer **[GitHub private vulnerability reporting](https://github.com/autowww/blueprints/security/advisories/new)** for this repository if it is enabled for the org/repo.
2. If that is unavailable, contact repository maintainers through a **private channel** they publish for this org (e.g. org security contact), or ask in an existing private maintainer thread—do not post exploit details in public issues or discussions.

Include enough detail to reproduce or understand the risk (affected paths, scenario, and impact). We will work with you on a coordinated disclosure timeline when practical.

## Scope

This repository is primarily **documentation, templates, and shell scripts**. Reports about hypothetical risks in consuming applications should go to those projects’ security contacts unless the flaw is clearly in blueprint content distributed here (e.g. an unsafe default in a published script).
