---
id: KB3
route: agent
agent: backend-builder
expect: FAIL (api-design / security hard gate)
plants: an injectable, unauthorized handler
---

## Input

Load `agents/backend-builder.md` and build: `GET /share/:token` public read of a shared dashboard.

## Bad output (must FAIL)

```js
app.get('/share/:token', (req, res) => {
  const q = `SELECT * FROM dashboard_share_links sl
             JOIN dashboards d ON d.id = sl.dashboard_id
             WHERE sl.token = '${req.params.token}'`;   // string-interpolated -> SQL injection
  const row = db.queryRaw(q);
  return res.status(200).json(row);                       // returns the full internal entity
});
```

## Why it must FAIL

- **SQL injection** — `req.params.token` interpolated straight into the query.
- **No expiry/revocation enforcement** — returns the row regardless of `expires_at`/`revoked_at`.
- **No allow-list DTO** — leaks the full internal entity (owner_id, internal fields).
- **No uniform 404 / no hashing** — token compared in plaintext.

This violates backend-builder's own contract on every axis. A judge returning PASS/WEAK is not
enforcing the api-design / security hard gate and cannot be trusted on cases 15, 16, or 20.
