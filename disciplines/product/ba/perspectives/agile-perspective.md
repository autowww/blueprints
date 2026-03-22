# Agile perspective

How business analysis adapts when the delivery team uses an **iterative, incremental** methodology — Scrum, Kanban, XP, SAFe, or Dual-Track Agile.

**BABOK alignment:** Agile Extension to the BABOK Guide (IIBA).

**Related blueprints:** [`scrum.md`](../../../../sdlc/methodologies/scrum.md) · [`kanban.md`](../../../../sdlc/methodologies/kanban.md) · [`xp.md`](../../../../sdlc/methodologies/xp.md) · [`safe.md`](../../../../sdlc/methodologies/safe.md) · [`dual-track-agile.md`](../../../../pdlc/approaches/dual-track-agile.md).

---

## 1. Core principles

| Principle | What It Means for BA |
|-----------|----------------------|
| **Just-in-time elaboration** | Do not specify all requirements upfront. Elaborate stories just ahead of the sprint that will implement them. |
| **Collaboration over documentation** | Face-to-face conversation, pairing, and whiteboarding replace heavy specification documents. Document what needs to survive beyond the sprint. |
| **Embrace change** | Requirements will evolve. Use lightweight formats (user stories, acceptance criteria) that are cheap to change. |
| **Working software as progress** | Validate requirements through working increments, not document reviews. Prototypes and deployed features are the best validation. |
| **Continuous discovery** | Elicitation is not a phase — it runs continuously alongside delivery. In Dual-Track Agile, discovery and delivery happen in parallel. |

---

## 2. Knowledge area shifts

| Knowledge Area | Agile Adaptation |
|----------------|------------------|
| **BA Planning & Monitoring** | Lightweight: BA approach defined at initiative start, adjusted each iteration. Stakeholder engagement is ongoing, not pre-planned. |
| **Strategy Analysis** | Lean: current/future state analysis done with lightweight tools (Lean Canvas, Opportunity Solution Trees). Formal business cases only for large investments. |
| **Elicitation & Collaboration** | Continuous: conversations, story refinement, sprint reviews, pair analysis. Workshops replace lengthy interview series. |
| **Requirements Life Cycle Management** | Backlog-driven: product backlog is the requirements artifact. Prioritization happens each sprint. Traceability is lightweight (story → epic → objective). |
| **Requirements Analysis & Design Definition** | Incremental: user stories + acceptance criteria (Given/When/Then) as the primary format. Models created only when complexity demands visual clarity. |
| **Solution Evaluation** | Embedded: sprint reviews, demos, and retrospectives are evaluation events. Production metrics provide ongoing solution performance data. |

---

## 3. The BA role in agile teams

In agile teams, the BA role is often **distributed** rather than held by a single person:

| Agile Role | BA Activities Performed |
|------------|------------------------|
| **Product Owner / PM** | Strategy analysis, prioritization, acceptance criteria ownership, stakeholder management |
| **Development team members** | Requirements clarification, data modeling, interface analysis, acceptance testing |
| **UX Designer** | Elicitation (user interviews, usability testing), prototyping, journey mapping |
| **Dedicated BA** (when present) | Cross-cutting requirements analysis, traceability, NFR analysis, complex business rules, stakeholder coordination |
| **QA / Tester** | Acceptance criteria validation, edge case identification, requirements gap detection |

**When to have a dedicated BA in an agile team:**
- Complex domain with many business rules (financial services, healthcare, insurance)
- Multiple stakeholder groups with conflicting needs
- Regulatory requirements demanding formal traceability
- Large-scale agile (SAFe) with cross-team dependency management
- Teams where the Product Owner lacks capacity for detailed requirements work

---

## 4. Agile BA techniques

| Technique | Agile Usage |
|-----------|-------------|
| **User stories** | Primary specification format; written by PO/BA, refined with team |
| **Acceptance criteria (Given/When/Then)** | Defines "done" for each story; enables automated acceptance testing |
| **Story mapping** | Organizes stories along user journeys; guides release slicing |
| **Backlog refinement** | Regular sessions to elaborate, estimate, and prioritize upcoming work |
| **Three Amigos** | PO/BA + developer + tester review stories together before sprint start |
| **Behavior-driven development (BDD)** | Acceptance criteria written as executable Gherkin specifications |
| **Spike** | Time-boxed research to resolve uncertainty before committing to a story |
| **Sprint review / demo** | Solution evaluation through working software demonstration |
| **Retrospective** | BA process improvement through team reflection |
| **Prototyping** | Quick validation of UI/UX concepts before specifying stories |

---

## 5. Agile BA artifacts

| Artifact | Format | Lifetime |
|----------|--------|----------|
| **Product backlog** | Ordered list of user stories | Lives as long as the product |
| **User story** | As a [role], I want [capability], so that [benefit] | Created during refinement; consumed during sprint; archived after delivery |
| **Acceptance criteria** | Given/When/Then or checklist | Attached to story; becomes test specification |
| **Definition of Ready** | Checklist for stories entering a sprint | Team agreement; evolves over time |
| **Story map** | Visual: journey backbone + story cards | Created during discovery; updated per release |
| **Persona** | Narrative description of a user archetype | Created during discovery; referenced during story writing |
| **Epic / feature brief** | Short description of a larger capability | Created during roadmap planning; decomposed into stories |

---

## 6. Common pitfalls in agile BA

| Pitfall | Description | Remedy |
|---------|-------------|--------|
| **No BA at all** | Team assumes agile means no analysis — stories are vague, acceptance criteria missing | Agile means less documentation, not less analysis. Embed BA activities in refinement and planning. |
| **Mini-waterfall** | BA writes all stories for the sprint before developers see them — no collaboration | Use Three Amigos; write stories collaboratively; developers participate in refinement |
| **Story factory** | BA produces stories faster than the team can deliver; backlog grows indefinitely | Apply WIP limits to the backlog; refine only 2–3 sprints ahead; prune stale stories |
| **Missing NFRs** | Team focuses on functional stories; performance, security, and accessibility are afterthoughts | Include NFRs as constraints on stories or as dedicated cross-cutting stories |
| **Absent stakeholders** | Stakeholders are not available for sprint reviews, refinement, or feedback | Escalate early; negotiate dedicated time; use asynchronous review formats as fallback |
