---
id: "20"
route: agent
agent: backend-builder
tests: boundary validation, per-resource authz/IDOR, idempotency, DTO projection, read-time invariants
---

## Input

Load `agents/backend-builder.md` as the system prompt and run it on (this is the API slice the
case-17 orchestration run found uncovered):

```
Build the share-link API for public read-only dashboard links, against this schema:
dashboard_share_links(id, dashboard_id, created_by, token_hash UNIQUE, expires_at, revoked_at, revoked_by).
Endpoints: POST (owner generates a link), DELETE (owner revokes), GET /share/:token (public read).
```

## Must

- Full contract: Contract, Implementation, Safety notes, Assumptions/confirm-these, Tests needed.
- Validate inputs at the boundary; authorize generate/revoke to the dashboard **owner** (guard IDOR).
- Generate a ≥256-bit token, store only `sha256(token)`, return the raw token once.
- Public read looks up by hash and **enforces expiry + revocation in the query**
  (`revoked_at IS NULL AND (expires_at IS NULL OR expires_at > now())`).
- Return an explicit allow-list **DTO**, not the internal entity; uniform 404 for all not-viewable states.

## Must not

- Trust client input or assume an auth layer it wasn't given (flag assumptions instead).
- Return the raw internal model, or leak which not-viewable reason applied.
