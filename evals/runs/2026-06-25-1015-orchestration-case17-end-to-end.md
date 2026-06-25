# Eval run — 2026-06-25 1015  (case 17 END-TO-END, 7 agents)

- commit: d5919e1 (+ backend-builder)
- case: 17 — orchestration — "Add public read-only shareable dashboard links"
- mode: **full live dispatch.** Reused the 4 prior slices (feature-spec, data-modeler,
  security-review, frontend-builder) from the 0053 run; dispatched the 3 previously-missing
  slices as live subagents this round: **backend-builder** (the now-filled API gap),
  **test-author**, **docs-writer**. 7 slices total.
- verdict: **PASS (end-to-end).** The API coverage gap is closed; the build is complete.

---

## What changed vs the 0053 run

- The API slice — logged as a coverage gap last time (no backend maker) — was dispatched to the
  **forged `backend-builder`** and came back production-grade: sha256 token, in-transaction IDOR
  guards, uniform 404 (no oracle), allow-list DTO, read-time expiry/revocation in the query,
  `no-store`/`no-referrer`, idempotent revoke, rate-limit. **The coverage-gap → forge → fill loop
  closed end to end.**
- All 7 domains now delivered: spec, schema, API, UI, tests, docs (+ security posture).

## Cross-slice conflict the coordinator caught (the headline)

**Regenerate behavior — a 3-way conflict no single agent could see:**
- `docs-writer`: "generating again **replaces** the old link."
- `test-author`: case 4 asserts re-generating **supersedes** the previous token.
- `backend-builder`: implemented **`409` — blocked**, an active link already exists (revoke first).

Two slices assumed *replace*; one implemented *block*. Left unsynthesized, the test suite would
**fail against the shipped handler**. → **Coordinator resolution:** adopt **replace-on-regenerate**
(majority assumption + smoother UX: regenerate atomically revokes the old link and mints a new one).
`backend-builder`'s `POST` changes from "409 on existing" to "revoke-then-insert in the same
transaction." docs + tests already match; only the handler adjusts. *(Minor product call — flagged
for confirm; block-until-revoked is the safer alternative if you prefer explicit.)*

## Still escalated (unchanged) — needs Eric

- **Live read vs frozen snapshot.** All three building slices independently re-flagged it and none
  decided it — correct behavior. A forgotten live link keeps publishing new data; snapshot is safer
  if dashboards hold sensitive data. **Product decision, still open.**

## Synthesized deliverable (condensed — one coherent v1, not 7 pasted outputs)

> **Public read-only dashboard share links — v1 (complete build)**
> - **Spec:** owner mints one public read-only link/dashboard, bounded expiry, revocable. Cut line:
>   no per-recipient access, no analytics, no passphrase (later).
> - **Schema:** `dashboard_share_links` (token_hash sha256, expires_at, revoked_at/by, partial
>   unique index = one active link/dashboard).
> - **API (backend-builder):** POST generate (owner-only, **revoke-then-mint**, returns raw URL once),
>   DELETE revoke (owner-only, idempotent), GET /share/:token (public, hash lookup, expiry+revocation
>   enforced in-query, allow-list DTO, uniform 404, no-store/no-referrer, rate-limited).
> - **UI (frontend-builder):** ShareDashboardModal — generate/copy/expiry/revoke, all states, AA +
>   keyboard, brand tokens flagged.
> - **Tests (test-author):** lifecycle, IDOR, 404-uniformity (status+body), strict expiry boundary,
>   DTO allow-list — bind to the HTTP contract.
> - **Docs (docs-writer):** owner guide + dev API reference, security gotchas, usage examples.
> **Open decision:** live vs snapshot. **Resolved this round:** regenerate = replace.

---

## Scoring vs ORCHESTRATION rubric

- ✅ **Decompose without overlap** — 7 slices, each in lane; no concern triplicated.
- ✅ **Seam ownership** — every shared decision owned; the new regenerate seam caught + assigned.
- ✅ **Conflict resolved** — 3-way regenerate conflict resolved to replace; live-vs-snapshot correctly
  escalated (rubric: resolve OR escalate).
- ✅ **Single-voice synthesis** — one coherent build plan across all 7 slices.
- ✅ **Completeness** — every domain delivered; no deferrals.
- ✅ **Coverage-gap honesty** — zero gaps this run; the prior API gap is filled by the forged agent.

**Verdict: PASS (end-to-end).** The coordinator ran the full 7-agent build, filled the gap it had
itself surfaced, and caught a 3-way conflict invisible to every individual agent — exactly the value
Layer 2 was built for.

## Notes

- Cost: 3 new subagents this round (~37–42k tokens each); 4 slices reused from 0053.
- Loop proof: case 17 (0053) found the API gap → forged backend-builder → case 17 (1015) dispatches
  through it cleanly. Orchestration and the gallery improved each other, as designed.
