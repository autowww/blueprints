# Public documentation depth review checklist

Use this before publishing.

## Coverage

- Does the page explain what the topic is?
- Does it explain when to use it and when not to use it?
- Does it give a mental model, not only steps?
- Does it include at least one example if the topic would otherwise feel abstract?
- Does it include verification criteria?
- Does it address common mistakes, branches, or recovery paths where relevant?

## Structure

- Is the page skimmable before it becomes detailed?
- Are headings meaningful and reader-oriented?
- Are long sections broken up by structured content?
- Does the page avoid a wall of prose?

## Visuals

- Does the page include a primary visual when flow, hierarchy, time, roles, or comparison matter?
- Is the visual actually clarifying something?
- Is the page using the simplest correct visual?
- Are tables or matrices used where precision matters?

## Boundary

- Does the page stay public/user-facing?
- Did any maintainer-only internals leak in?
- Are raw source paths, build scripts, or implementation details exposed unnecessarily?

## Navigation

- Does the page point to the correct next topic?
- If the topic has child pages, does the parent page act as a good chooser?
- Are previous/next links still coherent after splitting?

## Quality bar

- Could a first-time reader understand the topic in one sitting?
- Could a returning practitioner use the page during actual work?
- Would the page still make sense if the reader never opened the repo?
