# Elicitation & Collaboration

The knowledge area responsible for **gathering information** from stakeholders and sources, **confirming** that information is understood correctly, and **maintaining ongoing collaboration** throughout the initiative. Elicitation is not a one-time activity — it recurs whenever new understanding is needed.

**BABOK alignment:** Knowledge Area 4 (Elicitation and Collaboration).

**Lifecycle mapping:** Heaviest during **PDLC P1–P2** (discovery, validation) and **SDLC A–B** (discover, specify), but active whenever new information is needed throughout the lifecycle.

---

## 1. Tasks

### 1.1 Prepare for elicitation

Plan what information is needed, select appropriate techniques, identify participants, and prepare materials.

| Input | Output |
|-------|--------|
| BA approach, stakeholder register, information need | Elicitation plan (technique, participants, logistics, prepared materials) |

**Preparation checklist:**
- Define the objective: what specific information or confirmation is needed?
- Select technique(s) appropriate to the objective (see §2)
- Identify and invite the right participants (from stakeholder register)
- Prepare supporting materials (current state docs, prototypes, data samples)
- Schedule logistics (time, location/platform, duration)
- Define expected outputs and how they will be documented

### 1.2 Conduct elicitation

Execute the planned elicitation activities to gather information.

| Input | Output |
|-------|--------|
| Elicitation plan, prepared materials, participants | Elicitation results (raw) — notes, recordings, observations, prototypes feedback |

**Elicitation technique families:**

| Family | Techniques | Best For |
|--------|------------|----------|
| **Interactive** | Interviews, workshops, focus groups, brainstorming | Deep understanding, exploring unknowns, building consensus |
| **Research** | Document analysis, interface analysis, data mining | Understanding existing systems, regulations, data patterns |
| **Observational** | Observation, job shadowing, contextual inquiry | Understanding actual (vs stated) workflows and pain points |
| **Experimental** | Prototyping, proof of concept, simulations | Validating solution concepts, testing assumptions |
| **Survey-based** | Questionnaires, surveys | Reaching large groups, quantifying opinions, confirming patterns |

### 1.3 Confirm elicitation results

Verify that gathered information is correctly understood, complete, and consistent. Resolve conflicts and ambiguities.

| Input | Output |
|-------|--------|
| Elicitation results (raw) | Confirmed elicitation results |

**Confirmation activities:**
- Review notes with participants for accuracy
- Cross-reference findings across multiple sources
- Identify and resolve contradictions between stakeholder inputs
- Distinguish facts from opinions and assumptions
- Document open questions for follow-up elicitation

### 1.4 Communicate BA information

Ensure stakeholders receive the right BA information at the right time in the right format.

| Input | Output |
|-------|--------|
| BA artifacts, stakeholder communication plan | Delivered communications (presentations, reports, reviews) |

**Communication considerations:**
- Audience: tailor depth and vocabulary (executives need summaries; developers need specifications)
- Format: match organizational norms (some teams prefer Markdown in git; others need slide decks)
- Timing: align with ceremonies and decision points (sprint planning, stage gates, design reviews)
- Feedback: make communication bi-directional — invite questions, corrections, additions

### 1.5 Manage stakeholder collaboration

Build and maintain productive working relationships with stakeholders to support ongoing BA work.

| Input | Output |
|-------|--------|
| Stakeholder register, engagement plan | Sustained stakeholder engagement, resolved conflicts |

**Collaboration challenges and approaches:**

| Challenge | Approach |
|-----------|----------|
| Conflicting stakeholder needs | Facilitate negotiation; use prioritization techniques (MoSCoW, value/effort) |
| Disengaged stakeholders | Understand their motivations; demonstrate value of their input; escalate if critical |
| Geographically distributed teams | Use asynchronous techniques (surveys, document reviews); scheduled video calls |
| Domain knowledge gaps | Pair with SMEs; use observation and document analysis before interviews |
| Power dynamics | Separate elicitation sessions for different authority levels; anonymous input collection |

---

## 2. Techniques commonly used

| Technique | When to Use | PDLC/SDLC Phase |
|-----------|-------------|------------------|
| **Interviews** | Deep exploration of individual perspectives; understanding context | P1, P2, A |
| **Workshops / facilitated sessions** | Building consensus; complex problem-solving; multiple viewpoints | P1, P2, A, B |
| **Observation / job shadowing** | Understanding actual workflows vs stated processes | P1 |
| **Document analysis** | Understanding existing systems, contracts, regulations | P1, A |
| **Prototyping** | Validating solution concepts; surfacing implicit requirements | P2, B, C |
| **Surveys / questionnaires** | Quantifying patterns across large groups | P1, P5 |
| **Focus groups** | Exploring reactions to concepts with representative groups | P1, P2 |
| **Brainstorming** | Generating solution ideas; exploring possibilities | P2, A |
| **Interface analysis** | Understanding integration points and data flows | A, B |
| **Data mining / analytics** | Identifying patterns in existing usage data | P1, P5 |
| **Benchmarking** | Comparing against industry standards or competitors | P1 |
| **Mind mapping** | Organizing and exploring related concepts | P1, A |

Full technique catalog: [`techniques/README.md`](../techniques/README.md).

---

## 3. Relationship to PDLC and SDLC

| Elicitation Task | PDLC Mapping | SDLC Mapping |
|-----------------|--------------|--------------|
| Prepare for elicitation | P1 preparation: research plan, participant selection | A preparation: sprint planning, backlog refinement |
| Conduct elicitation | P1–P2: user interviews, observation, prototyping | A–B: requirements workshops, story writing, acceptance criteria definition |
| Confirm results | P2: validation with stakeholders, experiment results review | B: specification review, story walkthrough |
| Communicate BA information | Across all: stage gate presentations, experiment reports | Across all: sprint review, design review, DoD verification |
| Manage collaboration | Across all: product trio engagement, stakeholder alignment | Across all: cross-functional team collaboration |

### Overlap with PDLC discovery

Elicitation & Collaboration and PDLC P1–P2 share many techniques (interviews, prototyping, observation). The distinction:

| Concern | Elicitation (BA) | Discovery (PDLC PM) |
|---------|------------------|----------------------|
| Goal | Gather and confirm **all** stakeholder requirements | Validate that a **problem exists** and a **solution is viable** |
| Scope | Full stakeholder landscape including internal, regulatory, operational | Primarily end-users and market |
| Output | Confirmed requirements, stakeholder analysis | Research synthesis, experiment results, validation evidence |
| When done | When requirements are sufficient for the current iteration | When evidence supports a go/kill/pivot decision at stage gate |

In practice, BA and PM elicitation activities often overlap — the same interview may surface both market validation data (PDLC) and detailed requirements (BA).
