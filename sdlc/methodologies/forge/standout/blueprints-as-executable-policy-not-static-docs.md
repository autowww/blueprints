---
public_publish: true
audience: public
handbook_area: blueprints
learning_level: reference
hydration_source: forge-agentic-sdlc-standout-pack
---

# Blueprints as Executable Policy, Not Static Docs

## Core Thesis

Blueprints stand out because they turn methodology knowledge into a policy substrate for agentic SDLC. They define what should be judged, which Versonas apply, which evidence is expected, and which recipes or rules shape a run.

The core message is: **the wiki should not merely describe the process; it should supervise the process.**

## Condensed Thought

Traditional SDLC documentation is often passive. It sits in a wiki, and humans may or may not remember to consult it. Agents may read fragments of it, but usually without a reliable contract for how the information governs action.

Forge's Blueprint idea is more active. Blueprints provide canonical policy, recipes, Versonas, and evidence expectations. They do not execute jobs or store live run state, but they define the discipline knowledge that other products consume.

## Why It Stands Out

This is a practical way to bridge methodology and runtime. Instead of embedding policy separately into every agent, UI, workflow, and runner, Forge can maintain Blueprints as a reusable knowledge source. Lenses can display expectations, LCDL can use contracts shaped by policy, workcells can receive scoped context, and evidence packets can be evaluated against the expected standard.

The innovation is not merely having good documentation. It is making documentation operational without turning it into an opaque runtime.

## Forge Ecosystem Hooks

- **Blueprints** own canonical policy, recipes, Versonas, and evidence expectations.
- **ForgeSDLC** provides the methodology and vocabulary that Blueprints express.
- **Lenses** consumes Blueprint expectations in the control plane.
- **LCDL** can use Blueprint-driven contracts and verification flows.
- **Workcells** receive context and constraints derived from Blueprints.
- **EvidencePacket** can be checked against evidence expectations defined by Blueprints.

## Architecture Implications

Blueprints as executable policy require careful boundaries:

1. Blueprints define what should be judged; they do not execute jobs.
2. Blueprints should be versioned and addressable.
3. Policy should be machine-readable enough for tools and human-readable enough for governance.
4. Changes to policy should be reviewable like code.
5. Products should consume Blueprint contracts rather than copy policy into private forks.
6. Evidence expectations should map to autonomy levels and Versonas.
7. Blueprint resolution should be visible in the run record.

This keeps policy centralized while preserving clear ownership.

## Blog Post Seed Paragraph

Most engineering organizations already have process knowledge. It lives in wikis, checklists, architecture rules, testing standards, security policies, and team habits. The problem is that this knowledge is passive. Forge's Blueprints make methodology knowledge operational. They define what should be judged, which discipline lenses apply, and what evidence is expected, while leaving execution and state to the appropriate products. The result is a policy layer agents can respect and humans can inspect.

## Idea Evolution Questions

- What parts of a Blueprint should be machine-readable versus prose?
- How should Blueprints version policy changes across long-running ForgeRuns?
- Can Blueprint recipes be tested against sample runs?
- How should teams customize Blueprints without breaking canonical governance?
- What is the relationship between Blueprints, AGENTS.md, Cursor rules, and LCDL contracts?

## Risks And Counterarguments

Executable policy can become brittle if it is over-specified. Forge should distinguish strict gates from advisory guidance. The most effective Blueprints will preserve human judgment while giving agents and tools enough structure to act safely.

## Related

- [Forge concept map](../CONCEPT-MAP.md)
- [Autonomy levels](../AUTONOMY-LEVELS.md)
- [Respecting resources](../RESPECTING-RESOURCES.md)
