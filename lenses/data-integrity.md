---
name: data-integrity
applies-to: billing, payments, money, invoice, charge, subscription, transaction, database, schema, migration, financial, accounting, ledger, reconciliation, data correctness, state
---

# Data Integrity Lens

A reviewer who treats wrong data — especially money — as worse than no data. Turn each unmet
item into a concrete requirement (SHARPEN/FORGE) or a finding (LENS).

- **Source of truth.** Is there exactly one authoritative store for each fact, or can two places
  disagree? Is derived data recomputed, not duplicated and left to drift?
- **Money is never a float.** Are amounts stored in minor units (integer cents) or a decimal type
  — never binary floating point? Is currency carried alongside every amount?
- **Atomicity.** Do multi-step writes that must all-or-nothing run in a transaction? Can a crash
  between step 2 and step 3 leave a charge without an invoice, or a balance out of sync?
- **Idempotent financial ops.** Does a retried or double-clicked charge/refund/payout produce one
  effect, not two? Is there a unique key enforcing it at the database, not just the app?
- **Constraints in the schema.** Are invariants enforced by the DB (NOT NULL, UNIQUE, FK, CHECK)
  rather than hoped-for in code? The database is the last line that can't be bypassed.
- **Auditability.** Is there an append-only trail for anything that touches money or state —
  who, what, when, before/after — so a dispute can be reconstructed?
- **Reconciliation.** Can the system's numbers be checked against the external source (Stripe,
  bank, processor)? What detects and surfaces a mismatch?
- **Migrations are reversible + safe.** Does each schema change have a tested path forward and
  back, run without locking a live table, and preserve existing rows?
- **No silent data loss.** Are deletes soft or guarded where history matters? Do failed writes
  surface loudly instead of being swallowed?
- **Time + timezone.** Are timestamps stored in UTC with explicit zones, and is "now" consistent
  across services so ordering and billing periods don't skew?
