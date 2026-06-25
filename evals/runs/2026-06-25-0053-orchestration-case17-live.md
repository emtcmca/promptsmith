# Eval run — 2026-06-25 0053  (LIVE multi-agent dispatch)

- commit: 5d5a60c (Layer 2 coordinator v0)
- case: 17 — orchestration — "Add public read-only shareable dashboard links"
- mode: **real subagent dispatch.** The coordinator (host) ran the orchestration pipeline and
  dispatched 4 gallery agents as live parallel subagents: feature-spec, data-modeler,
  security-review, frontend-builder. Each returned its output contract; the coordinator
  synthesized. (api-build, tests, docs slices not dispatched this run — see coverage gap + notes.)
- verdict: **PASS** (case 17 lifts from N/A-blocked now that a coordinator exists).

---

## Seams the coordinator resolved (the synthesis)

| Seam / conflict | Raised by | Resolution | Owner |
|---|---|---|---|
| Raw token vs hash at rest | security + data-modeler (converged) | Store `sha256(token)` as `token_hash UNIQUE`; raw token only in the URL; look up by hash | API (generate), schema (store hash) |
| Expiry/revocation enforcement | data-modeler (stored) ↔ security (demanded) | Enforce in the read query: `WHERE revoked_at IS NULL AND (expires_at IS NULL OR expires_at > now())`; no cached render survives revocation | API read path |
| One vs many active links/dashboard | spec (one) ↔ schema (many) ↔ frontend (one) | MVP = one active link/dashboard → partial unique index `(dashboard_id) WHERE revoked_at IS NULL` | schema |
| Over-fetch | security | Public response is an explicit allow-list DTO, never the internal entity | API serializer |
| Token entropy | security | ≥256-bit CSPRNG token | API |
| Leak surface | security | `Referrer-Policy: no-referrer`, `Cache-Control: no-store, private`, scrub token from logs | API/infra |
| Uniform not-viewable state | spec + security (converged) | Single 404/410 for invalid/expired/revoked — no oracle | API |
| "Never expires" (NULL) vs bounded | data (allowed) ↔ security (bounded) | MVP: bounded default TTL; "never" deferred/admin-gated | API/policy |

## Escalated — needs Eric's decision (coordinator did NOT silently pick)

- **Live read vs frozen snapshot.** feature-spec's sharpest objection: a forgotten live link keeps
  publishing whatever later lands on the dashboard; expiry/revocation only bound *time*, not
  *content*. If dashboards can hold sensitive/PII data, a snapshot-at-share-time may be the safer
  default than a live read. This is a product/risk call above the coordinator's authority — flagged,
  not auto-resolved. **Decision needed before build.**

## Coverage gap found (logged)

- No agent **builds** the API endpoint (gallery has api-reviewer = review, data-modeler = schema,
  but no backend maker). Logged to `agents/coverage-gaps.md`; suggested new agent `backend-builder`.
  This is the coverage-gap mechanism working: orchestration surfaced a real roster hole.

## Synthesized deliverable (condensed — one coherent build plan, not 4 pasted outputs)

> **Public read-only dashboard share links — v1 build plan**
> 1. **Schema** (`dashboard_share_links`): id, dashboard_id FK CASCADE, created_by FK RESTRICT,
>    `token_hash` UNIQUE (sha256), `expires_at` (bounded), `revoked_at`/`revoked_by` (paired CHECK),
>    partial unique index for one-active-link/dashboard, partial active-token index.
> 2. **API** (the gap — needs backend-builder): `POST` generate (mint ≥256-bit token, store hash,
>    return raw URL once), `DELETE` revoke, `GET /share/:token` public read — looks up by hash,
>    enforces expiry+revocation in the query, returns an allow-list DTO, uniform 404 for all
>    not-viewable states, `no-referrer` + `no-store`, rate-limited.
> 3. **UI** (ShareDashboardModal): generate/copy/expiry/revoke, all states, AA + keyboard, brand
>    tokens flagged for the owner to supply.
> 4. **Deferred slices:** api-reviewer to audit the endpoint once built; test-author for the
>    lifecycle + access tests; docs-writer for the feature doc. (Agents exist; not run this round.)
> **Open decision:** live read vs snapshot (above).

---

## Scoring vs ORCHESTRATION rubric

- ✅ **Decompose without overlap** — each slice stayed in lane; the "exposure" concern wasn't triplicated.
- ✅ **Seam ownership** — every shared decision assigned one owner (table above).
- ✅ **Conflict resolved** — one-vs-many, raw-vs-hash, never-vs-bounded all resolved; live-vs-snapshot
  correctly *escalated* (rubric allows resolve OR escalate).
- ✅ **Single-voice synthesis** — one build plan, deduped, in one voice.
- ✅ **Completeness** — all domains represented or honestly deferred; the unbuildable slice flagged as a gap.
- ✅ **Coverage-gap honesty** — the missing backend-maker logged, not faked.

**Verdict: PASS.** The coordinator did the thing the manual cross-over test said it must.

## Defect found — D6 (coordinator)

The live-vs-snapshot conflict was surfaced by a *slice agent* (feature-spec) **after** dispatch,
not caught at Step 4 (pre-dispatch conflict ID). The SKILL's Step 7 (assemble) resolves conflicts
but doesn't explicitly say "catch and resolve/escalate conflicts that only emerge from slice
outputs." → Add to `skills/orchestration/SKILL.md` Step 7: surface agent-emergent conflicts, not
just the pre-identified ones. Small wording fix; tune next.

## Notes

- Real dispatch cost: 4 subagents, ~37k tokens each. Bounded intentionally (4 of 7 slices).
- All 4 agents held their guardrails live: frontend-builder flagged every brand token (no
  invention); data-modeler + security-review independently converged on token-hashing.
