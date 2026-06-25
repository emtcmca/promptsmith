---
id: "12"
route: agent
agent: sop-writer
tests: numbered one-action steps, verification per step, exceptions section, placeholders
---

## Input

Load `agents/sop-writer.md` as the system prompt and run it on:

```
Write an SOP for onboarding a new HOA client's governing documents into our system.
```

## Must

- Full contract: Purpose & trigger, Roles, Steps (numbered, one action each, with verification
  where it counts), Exceptions, Confirm-these.
- An exceptions section covering real failure modes (missing docs, illegible scans, duplicates,
  wrong association).
- Placeholders for tools/approvers/thresholds not supplied — not invented values.

## Must not

- Vague verbs ("handle the documents", "process the files") instead of concrete actions.
- Invent a specific system/tool name or approver as if known.
