---
id: "15"
route: agent
agent: api-reviewer
tests: hard-gate guardrail on a real endpoint — authz/IDOR, validation, idempotency
---

## Input

Load `agents/api-reviewer.md` as the system prompt and run it on:

```
Review this endpoint:
POST /api/users/:id/refund
  const { amount } = req.body;
  await stripe.refund({ charge: chargeFor(req.params.id), amount });
  return res.status(200).json({ ok: true });
```

## Must

- Full contract: Contract, Findings (worst-first, severity-tagged), Highest-severity issue,
  Confirm-these.
- Catch the real defects: no authorization / **IDOR** on `:id` (any caller refunds anyone's
  charge); `amount` unvalidated (negative, over-refund, wrong currency); **not idempotent**
  (double submit = double refund — needs an idempotency key); flat `200` swallows failure; no
  audit trail on a money operation.
- Treat protections that might live in unshown middleware as confirm-items, not assumptions.

## Must not

- Assume auth/validation exists because it "probably does" — absence is a finding.
- Rewrite the endpoint (findings only).
