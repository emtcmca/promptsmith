---
id: "11"
route: agent
agent: data-modeler
tests: money-not-float, DB-enforced constraints, idempotency, UTC, migration safety
---

## Input

Load `agents/data-modeler.md` as the system prompt and run it on:

```
Model a subscription billing system: plans, customers, subscriptions, invoices. Postgres.
```

## Must

- Full contract: Entities & relationships, Schema (DDL), Invariants→constraints, Migration,
  Flags.
- **Amounts in integer minor units (cents) with a currency column — never float.**
- Invariants enforced in the DB: PK/FK/UNIQUE/CHECK; status values as CHECK or enum.
- Invoice/charge idempotency via a unique key; timestamps UTC.

## Must not

- Store money as a floating-point type.
- Leave a core invariant (e.g. one active subscription per customer per plan) to app code only
  when the DB could enforce it.
