# Public documentation depth charter

## Goal

Public documentation should not only tell a reader what to click next. It should give enough context, structure, examples, and visual explanation that a reader can understand the topic in one sitting without having to reverse-engineer intent from source files or GitHub history.

The goal is **full-information reading** for public topics:

- the reader understands the purpose of the topic
- the reader knows when to use it and when not to use it
- the reader sees the main workflow or conceptual model visually
- the reader gets one successful path end to end
- the reader sees common branches, options, and edge cases
- the reader gets verification criteria
- the reader gets next steps and nearby topics

## Public boundary

Keep these public docs product- and usage-oriented.

Allowed in public docs:

- purpose and value
- role-based guidance
- setup and prerequisites
- tutorials and workflows
- examples and worked scenarios
- comparisons that help a user choose correctly
- troubleshooting and FAQs
- minimal operator settings required to use the product

Not allowed in public docs unless absolutely necessary for basic use:

- architecture internals
- ADRs
- raw file maps
- implementation plans
- generator/build-system mechanics
- contributor workflow
- source-path tours
- route inventories as reference dumps
- internal naming that only matters to maintainers

## Depth standard

Every mature public page should cover five layers where relevant:

1. **Orientation** — what this topic is and why it exists
2. **Mental model** — how the topic works conceptually
3. **Execution** — how to do it successfully
4. **Judgment** — how to choose between options or paths
5. **Recovery** — what goes wrong and how to fix it

Pages do not need equal weight on all five layers, but a page should not ship with only orientation and execution if the topic also requires judgment or recovery.

## Reader-experience standard

Each page should feel skimmable first, rich second.

That means:

- short intro and quick summary near the top
- clear sectioning
- at least one primary visual for any topic with flow, comparison, or system shape
- structured data presentation where it helps: tables, matrices, checklists, timelines
- callouts only for genuinely important caveats
- examples that are concrete and short
- previous/next navigation plus a small “related topics” area

## Structured-content rule

Every page should include at least **two** structured elements from this list, unless the page is intentionally tiny:

- comparison table
- decision matrix
- checklist
- step table
- glossary table
- role matrix
- examples table
- FAQ list
- flow diagram
- lifecycle/timeline visual

For any page longer than roughly 900–1200 words, include at least **one visual** and at least **three** structured elements.

## Visual rule

Use visuals to clarify thinking, not decorate pages.

Every visual must answer one of these jobs:

- show sequence
- show branching
- show ownership or role boundaries
- show hierarchy or containment
- show comparison
- show time
- show status/health
- show a worked example

If a visual does not reduce reading effort, do not include it.

## Example density rule

Tutorial and workflow pages should contain:

- one “happy path” example
- one “variation” or branch example if the topic commonly forks
- one “what good looks like” verification example

Concept pages should contain:

- at least one worked scenario or mini-case
- one “do / avoid” table if misuse is common

## Splitting rule

A topic should split into subtopics when any of the following becomes true:

- the page serves more than one primary user intent
- the page serves more than one audience with materially different questions
- the page contains two or more workflows that can each stand alone
- the page combines concept explanation with long operational instructions
- the page starts to require more than one major visual to stay readable
- the page becomes a long wall of headings with little narrative continuity

Split by reader job, not by internal source layout.

## Writing rule

Prefer:

- task language
- outcome language
- examples grounded in real repo workflows
- direct “why / when / how / verify” structure

Avoid:

- vague abstract prose
- file-path exposition unless operationally necessary
- internal-only jargon without explanation
- giant undifferentiated code dumps
- “see README/GitHub” as the main way to learn the topic

## Definition of done for a strong page

A public page is done when:

- a first-time reader can explain the topic back in plain language
- a practitioner can complete the task or apply the concept without opening internal docs
- the page includes at least one visual or structured summary where the topic benefits from it
- the page points to the correct next steps
- the page stays inside the public boundary
