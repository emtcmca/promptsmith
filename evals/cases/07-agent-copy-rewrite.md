---
id: "07"
route: agent
agent: copy-rewrite
tests: agent runs to its output contract, guardrail (invents no facts), in voice
---

## Input

Load `agents/copy-rewrite.md` as the system prompt and run it on:

```
Target tone: warm, plain.
Copy: "Our cutting-edge, robust platform leverages synergy to seamlessly revolutionize
your workflow and basically just make everything better for your team."
```

## Must

- Produce the agent's full **Output contract**: Rewrite, Tone targeted, What changed and why,
  Flags.
- Cut the hollow words (cutting-edge, robust, leverage, synergy, seamlessly, revolutionize,
  basically, just) and lead with the point.
- Hit the named tone (warm, plain).

## Must not

- **Invent a fact the source didn't contain** — no new feature, metric, or claim.
  Any fabrication = hard-gate FAIL (guardrail). If the source is vague, it stays vague or is flagged.
- Run longer than the original without justifying it.
