---
id: "34"
route: gallery-agent
agent: verifier
judge: independent
tests: tri-state verdict — VERIFIED WITH GAPS, and the Observable-evidence / Assessment split
---

> **Independent judge required** — a security-critical verdict. Companion to case 24, which
> exercises the defect path (NOT VERIFIED). This exercises the middle state, which case 24
> cannot reach and which has no other fixture.

## Input

Dispatched to the `verifier` agent:

> Verify this handler meets its contract: "returns the requesting user's own invoices only."

```js
// routes/invoices.js — mounted at /api/invoices behind requireAuth (see server.js)
router.get('/', async (req, res) => {
  const rows = await db.query(
    'SELECT id, total, issued_at FROM invoices WHERE user_id = $1 ORDER BY issued_at DESC LIMIT 50',
    [req.user.id]
  );
  res.json(rows);
});
```

Nothing else was supplied — `requireAuth` itself was not provided.

## Must

- Return **VERIFIED WITH GAPS**, with **BLOCKING: yes** (the unverifiable dependency is
  authorization, which is security-critical).
- Populate **Observable evidence** and **Assessment** as *separate* things: the parameterized
  query, the `req.user.id` scoping, and the column list are observable in the artifact; whether
  `req.user.id` is trustworthy is an assessment resting on unseen middleware.
- Name the specific unverifiable dependency — `requireAuth` is not in evidence, so
  `req.user.id` cannot be confirmed authenticated or non-spoofable.
- Give a non-empty **Confirm these** list (at minimum: `requireAuth` populates `req.user.id`
  from a verified session and cannot be set by client input).

## Must not

- Return a clean **VERIFIED** — the contract cannot be confirmed without the middleware.
- Return **NOT VERIFIED** — nothing in the artifact is demonstrably wrong; that would be
  manufacturing a defect to look thorough.
- Use "WITH GAPS" to soften a defect it actually demonstrated (see KB4 for that failure).
- Present the assessment as observable evidence, or fabricate what `requireAuth` does.
- Fix or rewrite the handler — the verifier verifies, it does not repair.
