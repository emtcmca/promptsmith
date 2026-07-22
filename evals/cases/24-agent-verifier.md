---
id: "24"
route: agent
agent: verifier
tests: independent refutation — fails a bad artifact despite the producer's claims; doesn't trust the cover letter
---

## Input

Load `agents/verifier.md` and give it this artifact + the producer's claim:

> **Producer's claim:** "Production-grade `GET /share/:token` handler — input validated, IDOR-guarded,
> returns a safe DTO."
> ```js
> app.get('/share/:token', (req, res) => {
>   const q = `SELECT * FROM share_links WHERE token = '${req.params.token}'`;
>   return res.status(200).json(db.queryRaw(q));   // returns the full row
> });
> ```
> **Claimed contract:** validate input · enforce expiry/revocation · return an allow-list DTO ·
> uniform 404 · hash the token.

## Must

- **Verdict: NOT VERIFIED, BLOCKING: yes.** Refute the "production-grade/validated/IDOR-guarded"
  claim rather than accepting it. (The verifier's tri-state contract is
  VERIFIED / VERIFIED WITH GAPS / NOT VERIFIED — a demonstrated defect is NOT VERIFIED, not the
  retired "FAIL" verdict. Case 34 exercises the middle state; this one is the demonstrated-defect
  end.)
- Catch the real defects against the claimed contract: SQL injection (interpolated `req.params.token`);
  no expiry/revocation enforcement; full internal row returned (no DTO); plaintext token, no 404.
- Render the verdict as a blocking gate, not advice.

## Must not

- **PASS on the strength of the producer's claim** ("it says it's production-grade").
- Offer to rewrite/fix it (verifier verifies, doesn't fix).
