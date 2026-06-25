# promptsmith roadmap

## Architecture: two layers

Decided 2026-06-24. promptsmith is built in two deliberately separate layers so the founding
identity survives the ambition.

**Layer 1 — promptsmith-core (current, shipping).**
The portable prompt & context engineering method: `/sharpen`, `/forge-agent`, `/lens`, the
shared engine, the lens library, and the pre-forged agent gallery. **No model calls, no API
keys, model-agnostic, paste-anywhere.** This is the defensible identity and it stays intact.

**Layer 2 — orchestration (planned, deferred).**
promptsmith as a *coordinator*: sharpen the prompt to perfection, decompose it into
non-overlapping slices, dispatch each to the right specialist as a live subagent, then receive,
assemble, and curate their work into one coherent result before returning it. This layer is
**Claude-Code-native** — it requires a runtime that can spawn subagents (Task / Workflow), so
it has runtime dependencies the core does not. It is built **last**, only after core + gallery
are tuned, per "build from the ground up; staff the coordinator last."

The gallery is the bridge: today its files are paste-ready system prompts; under Layer 2 they
become the **specialist roster** the coordinator dispatches to. Nothing built now is wasted.

---

## Now — Layer 1 build & tune

- [x] Engine, three commands, templates, eight base lenses (initial scaffold).
- [x] Real-run test pass — validated engine on a live request (`docs/test-runs/`).
- [x] Fix plugin command references to the namespaced form; fix standalone install's lens copy.
- [x] Add `seo`, `api-design`, `data-integrity` lenses (cover the common out-of-scope items).
- [x] Start the pre-forged agent gallery: `feature-spec`, `copy-rewrite`, `api-reviewer`.
- [x] Wire `/forge-agent` to seed from the gallery before building cold.
- [x] Add a named `voice` to the agent template + gallery so each speaks in character.
- [x] Build out the v1 roster (Tier 1–3) — 14 specialists across spec/build/test/review/docs/content:
      `test-author`, `refactor-planner`, `data-modeler`, `docs-writer`, `debugger`,
      `research-synthesizer`, `frontend-builder`, `security-review`, `governance-letter`,
      `sop-writer`, `prompt-engineer` (+ the original three).
  - Deliberately **not** built as agents: `perf-audit`, `seo-auditor` — they would clone the
    `performance` / `seo` lenses, already reachable via `/lens`. Gallery stays makers + lens-fusers.
- [ ] Tune from real use: run each command/agent on real tasks, log friction in `docs/test-runs/`,
      fix the engine/templates/lenses. Core is "tuned" when real runs stop surfacing defects.
- [ ] Merge `test/real-run-pass` to main once the gallery + tuning land.
- [ ] Push to GitHub (`emtcmca/promptsmith`); flip marketplace source from local path to repo.

## Later — Layer 2 orchestration (runtime deps; build after core+gallery tuned)

The hard, failure-prone parts — design these hardest:

- **Decomposition.** Split the sharpened prompt into specialist slices with no overlap and no
  gaps. Decide who owns each seam.
- **Dispatch.** Route each slice to the right gallery specialist as a live subagent; run
  independent slices in parallel.
- **Assembly + curation.** Merge conflicting outputs into one voice — dedup, resolve
  contradictions, enforce consistent tone/format. This synthesis step is the real moat (cf.
  Auris coordinator synthesis). A pile of subagent outputs is not a deliverable.
- **Guardrails.** Detect when orchestration is overkill (a single agent does it better) and
  fall back to plain `/sharpen`. Cap fan-out. Surface what each specialist did.
- **Agent tool / source access.** Some specialists are only fully useful with live tools —
  `research-synthesizer` needs web/retrieval; others may need a database, a file reader, or a
  code runner. The orchestration runtime is where agents get scoped tool access. Until then,
  affected agents must **degrade honestly** (D5: declare no-source, label training knowledge,
  never fabricate citations). Phase-2 task: a way to grant an agent the tools it needs.

### Worked example: shareable dashboard links

A manual stand-in-coordinator run of *"Add public, read-only shareable links to user
dashboards"* (eval case 17) decomposed to feature-spec, data-modeler, security-review, and
frontend-builder. Run in isolation, the agents exposed exactly the failure modes Layer 2 must
own:

- **Unowned seam.** `expires_at`: data-modeler *stores* it, security-review *demands enforcement*,
  the API slice would *check* it — and in isolation each assumes another owns it. Nobody enforces.
  → The coordinator must assign every seam an explicit owner.
- **Overlap / duplication.** feature-spec and security-review both raise "public = data exposure";
  data-modeler and security-review both opine on token randomness. → Dedup the concern to one voice.
- **Direct conflict.** feature-spec's "no expiry in the MVP cut line" contradicts security-review's
  "expiry is mandatory." → The coordinator resolves it before output; it doesn't paste both.
- **Pile, not deliverable.** Four output contracts, four personas. → Synthesis to one voice is the moat.

This is the acceptance bar encoded in case 17: decompose-without-overlap, seam-ownership,
conflict-resolution, single-voice synthesis, domain completeness.

Open questions to resolve before Layer 2:
- Host mechanism: Task tool vs. Workflow harness for dispatch + assembly?
- How does the coordinator pick specialists — lens/topic match, or an explicit routing pass?
- Where does the user approve the decomposition before fan-out (cost + correctness gate)?
- How is a cross-agent conflict surfaced and resolved — coordinator decides, or escalate to the user?
