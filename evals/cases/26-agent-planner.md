---
id: "26"
route: agent
agent: planner
tests: vertical verifiable slices with acceptance criteria + explicit dependencies + a named critical path; flags unknowns instead of inventing codebase facts
---

## Input

Load `agents/planner.md` and give it this goal:

> Plan the build for adding "export my data as CSV" to an existing web app's account-settings
> page. Users click a button, get an email with a download link when the export is ready.

## Must

- Decompose into **vertical, verifiable tasks**, each with an **acceptance criterion** and
  **explicit dependencies** (`depends on: #n / none`).
- Name the **critical path** and call out what can run in **parallel**.
- Surface risks / decision points (e.g. async job vs. inline, link expiry, large-export handling).
- **Flag codebase unknowns as confirm-items** — existing auth, mailer, job runner — rather than
  asserting they exist (honesty floor).

## Must not

- Write the spec ("what to build" is `feature-spec`) or any implementation code.
- Order tasks so the system is left broken between steps (each task keeps it working).
- Assert an existing API, queue, or email service exists without flagging it as an assumption.
- Pad with ceremony tasks that deliver no increment.
