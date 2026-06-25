---
id: "08"
route: agent
agent: feature-spec
tests: agent runs to contract, states MVP cut line + sharpest objection, no scope inflation
---

## Input

Load `agents/feature-spec.md` as the system prompt and run it on:

```
We want users to be able to share their dashboards with people outside the company.
```

## Must

- Produce the agent's full **Output contract**: Problem, Primary user + job, MVP slice,
  Requirements, Out of scope / later, Risks & open questions, Success criteria, Sharpest objection.
- Name a real MVP slice and an explicit cut line (what's deferred).
- Surface the genuine risks here (external auth, link security/expiry, data exposure, permissions).
- State a sharpest objection — e.g. external sharing is a security surface that may need a
  decision before any build.

## Must not

- Inflate into a full sharing/permissions platform; one feature, one MVP slice.
- Invent product facts (existing auth model, stack) as known — flag them as assumptions.
