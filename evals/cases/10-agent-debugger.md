---
id: "10"
route: agent
agent: debugger
tests: ranked hypotheses with distinguishing probes, no shotgun fixes, reproduction demanded
---

## Input

Load `agents/debugger.md` as the system prompt and run it on:

```
Users intermittently see stale data right after they save a record. A manual refresh fixes
it. Happens maybe 1 in 5 saves. React frontend, REST API, Postgres with a read replica.
```

## Must

- Full contract: Failure (expected vs actual + trigger), Reproduction, Hypotheses (ranked,
  each with a distinguishing probe), Most likely + why.
- Hypotheses ranked by likelihood × ease-of-test; each probe must *distinguish* between causes
  (e.g. read-after-write against primary to test replica lag).
- Surface the strong candidates: client cache not invalidated on write; read-replica lag;
  optimistic UI not reconciled with server response.

## Must not

- Propose a fix before a cause is identified ("try adding a cache-bust and see").
- Give a generic "try this and see" list where probes don't separate hypotheses.
