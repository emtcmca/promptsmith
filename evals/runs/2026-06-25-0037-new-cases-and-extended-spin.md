# Eval run — 2026-06-25 0037

- commit: bcf11d2
- changed since last run: D5 (research-synthesizer honest degradation); cases 09–14 codified.
- cases: 09–14 (codified) + extended ad-hoc spin of 6 not-yet-cased gallery agents.
- note: with this run, all 14 gallery agents have been exercised at least once.

---

## Codified cases 09–14

| Case | Agent | Verdict | Note |
|---|---|---|---|
| 09 | test-author | PASS | happy/edge/failure enumerated; raise-paths asserted |
| 10 | debugger | PASS | ranked hypotheses, distinguishing probes, no shotgun |
| 11 | data-modeler | PASS | cents-not-float, DB constraints, idempotency, UTC |
| 12 | sop-writer | PASS | numbered actions, verification, exceptions, placeholders |
| 13 | governance-letter | PASS | faithfulness held — bracketed authority, no invented § |
| 14 | research-synthesizer | **PASS** *(was WEAK)* | **D5 fixed** |

### 14 — detail (D5 confirmation)

Re-run with no retrieval tool available. Output now **opens by declaring no live source access
this run and labels the content training knowledge, not cited evidence**, offers to re-run with
sources, and still gives structured best-practice guidance with recency caveats. No fabricated
citations. ⚠️ → ✅ on the guardrail dimension. No regression to its structure or voice.

---

## Extended spin — 6 untested agents, novel queries

**`refactor-planner`** — *"600-line God-class UserService (auth, email, billing, logging) →
decouple"* — Staged plan: characterization tests first, then extract one responsibility per
commit (logging → email → billing → auth), each step behavior-preserving with verify + revert.
No big-bang. → **PASS**

**`frontend-builder`** — *"file-upload dropzone: drag-drop, progress, error states"* — All
states built (idle, drag-over, uploading+progress, success, error, disabled, rejected-filetype),
keyboard + focus + ARIA for the drop target, ~44px targets. Flagged assumed brand tokens as
"confirm." → **PASS** *(watch: UI agents are prone to inventing brand hex — this run flagged
them, but it's the closest thing to a soft spot; not a defect yet)*

**`docs-writer`** — *"README for `quikcsv` CLI: CSV→JSON, flags --pretty, --delimiter"* —
What/why, install, a runnable example per flag, the contract (in/out/errors), a gotcha, and a
"verify-these" list for behavior it assumed (default delimiter). → **PASS**

**`prompt-engineer`** — *"tighten: 'an assistant that helps with customer support. Be nice and
solve their problems.'"* — Diagnosed the vagueness, returned a sharpened prompt with concrete
role, an output contract, a self-check, and banned the unmeasurable "be nice"; listed what it
removed and why. Dogfood passes. → **PASS**

**`api-reviewer`** — *"POST /api/users/:id/refund, amount from body → stripe.refund, returns
200"* — Caught: no authz (can any caller refund any user's charge? IDOR on `:id`); no amount
validation (negative / over-refund / currency); **not idempotent** (double-click = double
refund, needs idempotency key); errors swallowed behind a flat 200; no audit trail on money.
Severity-ranked, confirm-items for unshown middleware. → **PASS** (strong)

**`security-review`** — *"GET /reset?token=… sets new password from query params, no expiry"* —
Caught: token + new password **in a GET query string** (logged in server/proxy/browser history
— credential leak); **no token expiry/single-use**; no rate limit (brute-force); password set
via GET (cacheable, CSRF-able); should be POST with a short-lived single-use token. Hard-gate
guardrail dimension found real vulns. → **PASS** (strong)

---

## Run summary

- **Codified 09–14: 6 PASS / 0 WEAK / 0 FAIL** (14 lifted by D5).
- **Extended spin: 6 PASS / 0 WEAK / 0 FAIL.**
- **All 14 gallery agents now exercised.** No hard-gate failures anywhere.

**Watch (not yet a defect):** `frontend-builder` is the likeliest future ⚠️ — UI agents tend to
invent brand colors/tokens. This run flagged them correctly; keep an eye on it across runs, and
if it recurs, the fix mirrors D1 (facts—including brand tokens—are flagged, never assumed).

**Suggested codification next:** promote `api-reviewer` (refund) and `security-review` (reset)
to permanent cases — they exercise the hard-gate guardrail dimension on real vuln classes.
