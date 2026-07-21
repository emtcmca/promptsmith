---
id: "36"
route: grade
command: /promptsmith:grade
tests: --against comparison — per-dimension deltas, and naming a regression even when the revision wins overall
---

## Input

```
/promptsmith:grade --against
```

**Version B (the revision, under grade):**

```
You are a senior support engineer for Northwind Tools, a warehouse inventory SaaS.

Answer questions about orders, returns, and shipping using only the order record supplied in
the conversation. Reply in under 120 words, plain text, no bullet lists.

Success: the customer can act on your answer without a follow-up question.
```

**Version A (the original, `--against`):**

```
You are a support engineer for Northwind Tools, a warehouse inventory SaaS.

Answer questions about orders, returns, and shipping using only the order record supplied in
the conversation. Never state a refund amount, delivery date, or policy detail that is not in
that record — say you'll escalate instead. Escalate any refund over $500 to a human.

Keep replies short.
```

## Must

- Score **both** on the same rubric and report per-dimension deltas.
- Judge B stronger **overall** — it gains a measurable success criterion and a concrete output
  format ("under 120 words, plain text") where A had only "keep replies short."
- **Name the regressions explicitly, despite B winning:** B dropped the prohibition against
  stating unverifiable refund amounts / dates / policy details, and dropped the $500 escalation
  rule. **Prohibitions** and **Bounded** regressed; **Grounded** weakened.
- State the winner and why in one line.
- Note that the two versions differ in more than one respect, so the improvement cannot be
  attributed to a single change.

## Must not

- **Report B as an unqualified improvement.** Surfacing the regression under an overall win is
  the entire purpose of the route and the reason to measure rather than eyeball.
- Merge the two into a single blended score, or grade only B.
- Rewrite either version, or emit a merged "best of both" prompt — that's `/sharpen`.
- Attribute the overall gain to one specific edit when several changed at once.
