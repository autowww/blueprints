# Crystal

## What it is

**Crystal** is a **family** of Agile methodologies created by Alistair Cockburn, scaled by two dimensions: **team size** and **system criticality**. Each variant is named by a color — **Crystal Clear** (1–6 people, low criticality), **Crystal Yellow** (7–20), **Crystal Orange** (21–40), **Crystal Red** (40–80), and so on. The "heavier" the color, the more ceremony and documentation the method prescribes.

Crystal's core insight is that **no single process fits all projects** — the right methodology depends on the number of people who must coordinate and the consequences of failure. All Crystal variants share **seven properties**: frequent delivery, reflective improvement, osmotic communication, personal safety, focus, easy access to expert users, and a technical environment with automated tests, configuration management, and frequent integration.

## Process diagram (handbook)

![Crystal family — size × criticality](../docs/assets/methodology-crystal-family.svg)

*Color variants on a grid of team size (x) and criticality (y). Lighter colors = lighter process.*

---

## Authoritative sources (external)

| Resource | Executive summary (why it's linked here) |
|----------|------------------------------------------|
| [**Wikipedia — Crystal Clear (software development)**](https://en.wikipedia.org/wiki/Crystal_Clear_(software_development)) | **Stable overview** of Crystal Clear — the most commonly adopted variant. |
| [Agile Alliance — Crystal](https://www.agilealliance.org/glossary/crystal/) | **Short definition** in the Agile glossary. |

**Books:** Cockburn, *Crystal Clear: A Human-Powered Methodology for Small Teams* (2004); Cockburn, *Agile Software Development: The Cooperative Game* (2006).

---

## Seven properties (shared across all variants)

| Property | Meaning |
|----------|---------|
| **Frequent delivery** | Ship working software regularly (weekly to quarterly depending on variant). |
| **Reflective improvement** | Regular reflection workshops (retros) to tune the process. |
| **Osmotic communication** | Team members overhear useful information naturally (co-location or equivalent). |
| **Personal safety** | People can speak up without fear; trust enables honest feedback. |
| **Focus** | Minimize interruptions and context-switching during work periods. |
| **Easy access to expert users** | Quick feedback from real users or domain experts. |
| **Technical environment** | Automated tests, CI, configuration management — foundational engineering. |

---

## Crystal variants overview

| Variant | Team size | Typical formality |
|---------|-----------|-------------------|
| **Crystal Clear** | 1–6 | Minimal docs; informal communication; 1–3 month iterations |
| **Crystal Yellow** | 7–20 | Slightly more docs; cross-team coordination; shorter iterations |
| **Crystal Orange** | 21–40 | More documentation; defined roles; formal reviews |
| **Crystal Red / higher** | 40–80+ | Substantial governance; resembles phased delivery with Agile principles |

---

## Mapping to this blueprint's SDLC

| Crystal idea | Blueprint touchpoint |
|--------------|----------------------|
| Frequent delivery | Phases D–F: iterative build, verify, release. |
| Reflective improvement | Phase F: retrospectives, process tuning. |
| Seven properties | Cross-phase: technical environment = CI/CD; osmotic communication = team practices. |
| Scaling by variant | Methodology selection: Crystal Clear for small teams, heavier variants for larger/regulated contexts. |

---

## Agentic SDLC: Crystal + agents

| Topic | Guidance |
|-------|----------|
| **Osmotic communication** | Agents can supplement human communication (summaries, context retrieval) but cannot replace the trust and nuance of osmotic communication. |
| **Personal safety** | Agent-generated code reviews should be **constructive**; agents amplify volume, so human review culture matters more. |
| **Scaling** | As agent throughput increases team "effective size," consider whether a heavier Crystal variant's coordination practices are needed. |

---

## Further reading

- [Wikipedia — Crystal Clear](https://en.wikipedia.org/wiki/Crystal_Clear_(software_development)) — **Overview** of the most common variant.
- Companion: [Scrum](scrum.md), [XP](xp.md), [Agile umbrella](agile.md)
