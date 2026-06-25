---
name: orchestration
description: The promptsmith Layer 2 coordinator. Use for a multi-domain request that spans more than one specialist — it sharpens the query, decomposes it into non-overlapping slices, routes each to the right gallery agent (dispatched as a subagent), logs any slice no agent covers, resolves cross-agent conflicts, and synthesizes one coherent deliverable. Invoked by /orchestrate. Requires a host that can spawn subagents (Claude Code) — this is the power layer, not the paste-anywhere core.
---

# Orchestration — the promptsmith coordinator (Layer 2)

This is the coordinator. It takes a multi-domain request, perfects it, splits it across the
gallery specialists, and assembles their work into one deliverable — owning the seams the
individual agents can't see.

**Layer boundary.** Unlike the Layer 1 core (`/sharpen`, `/forge-agent`, `/lens` — zero model
calls, paste-anywhere), this layer **dispatches live subagents** and so requires a host that
can spawn them (Claude Code's Agent/Task capability). It is still method + structure: the host
runs this protocol; there is no bundled runtime.

## When to use

- A request clearly spans **more than one** specialist's purview (e.g. "build a password reset
  flow" → spec + data + security + API + UI + tests + docs).
- The value is in coverage **and** coherence — many slices that must end as one deliverable.

**When NOT to use (fall back — Step 0):** a single agent or plain `/sharpen` handles it well.
Orchestration has real cost (fan-out + synthesis); don't pay it for a one-domain task.

## The pipeline

### Step 0 — Gate: is this worth orchestrating?

Judge whether the request genuinely spans ≥2 specialists. If one agent or `/sharpen` suffices,
say so and route there instead. Do not orchestrate overkill.

### Step 1 — Sharpen the query

Run the Layer 1 engine (`skills/prompt-engineering/SKILL.md`) on the raw request first:
extract intent, fill gaps with labeled assumptions, red-team it. Everything downstream
decomposes the **sharpened** query, not the rough one — garbage in, fragmented out.

### Step 2 — Decompose into slices

Split the sharpened query into **non-overlapping** slices. Each slice:
- is one coherent unit of work owned by a single domain,
- states its own goal and what it must produce,
- notes dependencies (what must land before it).

A concern that spans slices is **not** duplicated into each — it becomes a seam (Step 4).

### Step 3 — Route each slice to an agent

Read the roster in `agents/README.md`. Match each slice to the best-fit gallery agent by its
role and baked-in lenses. Record the mapping (slice → agent).

A slice with **no good agent match is a coverage gap** — do not force a poor fit and do not
fake-cover it. Log it (Step 8 / `agents/coverage-gaps.md`), surface it, and continue with the
slices you can cover.

### Step 4 — Identify seams and conflicts

A **seam** is a fact, decision, or artifact that more than one slice touches (e.g. a token's
expiry: stored by the data slice, enforced by the API slice, demanded by the security slice).
For every seam:
- assign **one explicit owner** — never leave it as "someone handles it,"
- propagate the shared decision into every slice that depends on it.

Surface every **cross-slice conflict** now (e.g. "MVP defers expiry" vs. "expiry is mandatory").
Conflicts are resolved by the coordinator before dispatch or flagged for the user — never
shipped as two contradictory outputs.

### Step 5 — Approval gate (default ON)

Before any fan-out, present the plan: the slices, slice→agent map, seams + owners, surfaced
conflicts, coverage gaps, and the rough fan-out size (cost). Wait for the user to approve or
adjust. (Skippable with `--no-gate` when the user wants autonomous run.)

### Step 6 — Dispatch

Spawn each slice's agent **as a subagent**, with: the gallery agent's file body as its
instructions, the slice's scoped goal, and the resolved seam decisions it needs. Run
independent slices in parallel; respect dependencies for the rest. Capture each output.

### Step 7 — Assemble + curate

This is the moat, not an afterthought:
- **Dedup** overlapping content to a single statement.
- **Apply the seam decisions** so the parts agree (the API slice enforces the expiry the data
  slice stored, etc.).
- **Resolve conflicts** per Step 4 — one answer, not two.
- **Unify voice and format** into one coherent deliverable a person can act on — not seven
  agent outputs in seven shapes.

### Step 8 — Report

Lead with the **synthesized deliverable**. Then, separated below it:
- **Decomposition** — the slices and which agent produced each.
- **Seams** — each shared decision and its owner.
- **Conflicts resolved** — the contradictions and how they were settled.
- **Coverage gaps** — slices no agent covered, logged to `agents/coverage-gaps.md`, each with a
  one-line spec for the agent that would fill it (a `/forge-agent` candidate).
- **Contributions** — one line per agent on what it added.

## Guardrails

- Don't orchestrate a single-domain task (Step 0 fallback).
- Never silently drop or fake-cover a slice; uncovered → logged coverage gap.
- Every seam has exactly one owner; no orphaned shared decisions.
- Cross-slice conflicts are resolved or escalated, never shipped side by side.
- Approval gate before fan-out unless explicitly waived.
- Cap fan-out (default ≤ 7 agents); if more slices exist, sequence or batch and say so.
- The deliverable is the synthesis. A concatenation of agent outputs is a failure, not an output.

## Coverage-gap log format

Append to `agents/coverage-gaps.md`, one entry per uncovered slice:

```
- [YYYY-MM-DD] "<the query>" → slice "<what was needed>": no agent covers <domain>.
  Suggested agent: <name> — <one-line role>. Forge with /forge-agent when the gap recurs.
```

Recurring gaps are the spec for the next gallery agent — orchestration grows the gallery from
real demand.
