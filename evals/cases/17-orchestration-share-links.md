---
id: "17"
route: orchestration
status: deferred-target
blocked-on: Layer 2 (no coordinator exists yet)
expected-agents: [feature-spec, data-modeler, security-review, api-reviewer, frontend-builder, test-author, docs-writer]
tests: multi-agent decomposition, seam ownership, conflict resolution, single-voice synthesis
---

> **This case is a forward target, not yet runnable.** promptsmith has no coordinator today
> (Layer 2, deferred — see ROADMAP). Until then its verdict is **N/A — blocked**. It exists to
> give the orchestration layer a concrete thing to pass when built, and to pin the requirements
> the manual cross-over test surfaced.

## Input

```
Add public, read-only shareable links to user dashboards.
```

A genuinely multi-domain build request: it crosses spec, data, security, API, UI, tests, docs.

## Must (when a coordinator runs it)

- **Decompose** into slices that cover the domains with **no overlap** — the "public link =
  data-exposure" concern is stated **once**, not re-raised by three agents.
- **Assign every seam an owner.** Specifically: `expires_at` is *stored* by data-modeler but
  enforcement must be explicitly owned (the API/read slice), not left as "someone checks it."
- **Resolve cross-agent conflicts before output** — e.g. feature-spec's "no expiry in the MVP
  cut line" vs. security-review's "expiry is mandatory." The coordinator decides; it doesn't
  paste both and move on.
- **Synthesize to one coherent deliverable in one voice** — a plan a person can act on, not a
  concatenation of seven agent outputs in seven formats.
- **Completeness:** spec, schema, security posture, endpoint contract, UI, tests, and docs are
  each represented or explicitly deferred with a reason.
- **Coverage-gap honesty:** any slice that no existing agent covers is **logged as an unmet
  gap** (what was asked, why nothing fits) and surfaced — not silently dropped or fake-covered.
  Recurring gaps become the spec for a new forged agent.

## Must not

- Emit raw concatenated agent outputs (a pile is not a deliverable).
- Leave any seam unowned or any cross-agent conflict unresolved.
- Silently drop a domain that the request clearly implies.

## Reference

Manual stand-in-coordinator run of this exact query (the seams it exposed) is documented in
`ROADMAP.md` → Layer 2 → "Worked example: shareable dashboard links."
