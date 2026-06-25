# Coverage gaps — slices no gallery agent covers

Append-only. The Layer 2 coordinator (`/promptsmith:orchestrate`) writes here whenever a request
slice falls outside every existing agent's purview. A **recurring** gap is the spec for the next
gallery agent — forge it with `/promptsmith:forge-agent` and drop it in `agents/`.

Format:

```
- [YYYY-MM-DD] "<the query>" → slice "<what was needed>": no agent covers <domain>.
  Suggested agent: <name> — <one-line role>. Forge when the gap recurs.
```

---

<!-- entries below, newest last -->

- [2026-06-25] "Add public read-only shareable dashboard links" → slice "implement the share
  API (generate/revoke handlers + the public read endpoint that enforces expiry/revocation and
  projects an allow-list DTO)": no agent covers backend *construction*. The gallery has
  `api-reviewer` (reviews an endpoint) and `data-modeler` (schema) but nothing that *writes* a
  route handler. Suggested agent: `backend-builder` — builds an endpoint/service to contract,
  with validation, authz, idempotency, and error shape baked in. Forge when the gap recurs.
