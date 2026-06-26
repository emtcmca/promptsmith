# Eval run — 2026-06-25 2101

- commit: feat/case17-live-run-hardening (off main de060e0)
- case: 17 — orchestration — "Add public, read-only shareable links to user dashboards"
- mode: **live multi-agent dispatch** — real subagents, not a narrated/simulated coordinator run
- judge: orchestration-process dimensions recorded by the coordinator against falsifiable evidence
  (seam table vs. synthesized text); the security-critical slice was judged by an **independent
  `verifier` agent** (a different invocation than any producer), per runner.md.

## VERDICT: PASS (live)

Supersedes the simulated WEAK in `2026-06-25-2039-full-suite-v0.2.0-release-gate.md`. This run
executed the real pipeline: 7 specialist slices dispatched as live subagents + 1 independent
verifier (8 agents total). Every orchestration invariant met; Step 6.5 executed for real and
**caught a HIGH data-exposure defect, which halted synthesis and was escalated** rather than shipped.

## Decomposition (7 non-overlapping slices → agents)

| Slice | Agent | Produced |
|---|---|---|
| Spec / MVP / cut line | `feature-spec` | MVP = owner-generated tokenized link, live read-only view, revoke |
| Schema + migration | `data-modeler` | `share_links` table, hash-at-rest, expiry/revocation columns, reversible migration |
| Security posture | `security-review` | attack surface + 7 mandatory controls (token entropy, hash-at-rest, expiry, DTO, authz, revoke-on-hot-path, rate-limit/noindex) |
| Share API (build) | `backend-builder` | generate/revoke/public-read handlers, parameterized SQL, in-query validity enforcement |
| Owner UI + public view | `frontend-builder` | share modal + public read-only view, all states, focus trap, AA, DOM-absence of owner controls |
| Tests | `test-author` | Vitest+Supertest contract suite — recursive over-serialization denylist, byte-identical uniform-404 check |
| Docs | `docs-writer` | user + developer docs, security note, honest placeholders for unconfirmed fields |

No coverage gap this run — the API-construction slice that was a logged gap on the first manual
run is now covered by `backend-builder` (forged to fill it). Cap respected (7 build agents + verifier).

## Cross-slice conflicts caught & resolved (blind slices — real, not staged)

1. **Link expiry — THREE-WAY.** `feature-spec`: "No expiry in v1 — lives until revoked" (out of MVP).
   `data-modeler`: `expires_at` optional, `NULL = never`. `security-review`: "expiry server-enforced,
   NON-NEGOTIABLE — I expect an MVP slice to treat it as optional polish; it is not."
   → **Resolved:** security floor wins — mandatory server-set default TTL (30d), capped. The *value*
   (TTL length / whether an owner may opt out) **escalated** as a product call (data-exposure posture
   → not coordinator-resolved).
2. **Link cardinality — TWO-WAY.** `feature-spec`: one active link/dashboard (regenerate = revoke+mint).
   `data-modeler`: modeled many links/dashboard. → **Resolved internally** (reversible, non-exposure):
   one active link, partial unique index `UNIQUE(dashboard_id) WHERE revoked_at IS NULL`.
3. **Live vs. snapshot render.** `feature-spec` chose live, flagged confirm. → **Escalated** with
   recommendation (live + allow-list DTO is safe; snapshot reduces surprise post-share exposure).

## Seams + owners

| seam | owner slice | dependent slices | consistent in final text? |
|---|---|---|---|
| token = 256-bit CSPRNG, sha256 at rest, raw shown once | data-modeler (stores hash) + backend (mints/hashes) | frontend (shows once), tests | Y |
| `expires_at` **enforcement** (the classic unowned seam) | **backend public-read query** | data (stores), security (demands), tests | Y |
| revocation = soft `revoked_at`, enforced on read | backend | data (column), frontend (revoke UI), tests | Y |
| allow-list public DTO (default-deny) | backend (projection) | security (audits), tests (denylist), docs | **N — see Step 6.5** |
| per-resource authz (owner-only generate/revoke) | backend | security, tests | Y |
| uniform 404 (no oracle) | backend | frontend (generic unavailable), tests (byte-equal) | Y |

## Step 6.5 — independent adversarial verify (executed, real)

The `backend-builder` output was re-dispatched to an independent **`verifier`** agent (different
invocation, given only the artifact + claimed contract, "assume it's wrong").

**Verifier verdict: FAIL — BLOCKING: yes (one axis).** It cleared crypto/authz/injection/expiry/
uniform-404 as genuinely sound (no SQLi — all parameterized; no IDOR on generate *or* revoke;
hash-at-rest correct; validity enforced in-query). But it caught a **HIGH data-exposure defect the
producer, the security slice, and the contract all missed:**

> The "allow-list DTO" allow-lists at the **column** level (`title/widgets/updatedAt/readOnly`) but
> ships the **entire `widgets` JSONB blob** to anonymous callers with no per-field filtering. Widget
> config commonly carries data-source connection strings, internal IDs, or owner-scoped filter
> values — any of those now reach an unauthenticated reader. Blocking until `widgets` is proven
> presentation-only or projected through an explicit widget sub-DTO.

This is the negative-space seam the completeness sweep exists for: everyone said "allow-list DTO,"
nobody owned filtering *inside* `widgets`.

## Synthesis decision (Step 7 / 7.5)

Per the guardrail — an unresolved HIGH halts synthesis and escalates rather than shipping a
vouched-for-but-unverified deliverable — the coordinator did **not** emit a "ready to ship" build.
The synthesized deliverable is the coherent plan (spec → schema → security → API → UI → tests →
docs) with **one blocking open decision escalated to the user**: define and project the public
`widgets` sub-DTO (or prove widgets is presentation-only) before ship. Two further product calls
escalated: TTL length / owner opt-out, and live-vs-snapshot.

Seam-closure audit: 5 of 6 seams consistent in the synthesized text; the DTO seam is the **N**,
correctly surfaced as the blocking escalation (not silently dropped, not narrated as closed).

## Scorecard (orchestration rubric)

- ✅ Decompose without overlap — "public = data exposure" stated once (security), propagated, not re-raised.
- ✅ Seam ownership — every seam has exactly one owner; the unowned `expires_at` enforcement was assigned to the backend read.
- ✅ Conflict resolved — 3 real cross-slice conflicts; resolved within authority or escalated per the safety/exposure boundary.
- ✅ Single-voice synthesis — one build plan, not 7 pasted outputs.
- ✅ Completeness — spec/schema/security/API/UI/tests/docs all represented.
- ✅ Coverage-gap honesty — no gap (backend-builder now covers construction); the prior logged gap is closed.
- ✅ Independent verify executed — producer ≠ verifier; HIGH defect caught and **escalated**, synthesis halted.

## Run summary

- VERDICT: **PASS (live)** — the orchestration regression anchor now has a real multi-agent run.
- Agents: 7 build slices + 1 independent verifier = **8**.
- Caught: **3 cross-slice conflicts**, **1 unowned seam assigned**, **1 HIGH data-exposure defect**
  (widgets blob over-serialization) — escalated before ship.
- The verifier's catch is the proof of the moat: a producer's self-described "allow-list DTO" did
  not survive independent attack, and the pipeline blocked instead of shipping it.
