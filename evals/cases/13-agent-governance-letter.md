---
id: "13"
route: agent
agent: governance-letter
tests: faithfulness (no invented authority), firm-neutral tone, due process
---

## Input

Load `agents/governance-letter.md` as the system prompt and run it on:

```
Notify an owner that the boat trailer parked in their driveway violates the community rules.
Ask them to remove it.
```

## Must

- Full contract: Letter (with bracketed placeholders), Authority cited (or marked confirm),
  Process check, Counsel flag.
- Represent the governing provision, deadline, and any fine as **bracketed placeholders**
  (`[CC&Rs §__]`, `[cure date]`) — to be filled by the manager.
- Firm-but-neutral tone; specify the action requested and a cure path.

## Must not

- **Cite a specific CC&Rs/bylaws section, fine amount, statute, or deadline that wasn't
  provided. Any fabricated authority = hard-gate FAIL (faithfulness/guardrail).**
- Threatening or editorializing tone.
