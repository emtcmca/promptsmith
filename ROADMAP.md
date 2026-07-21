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
- [x] Push to GitHub (`emtcmca/promptsmith`) — repo is public; marketplace installs via `emtcmca/promptsmith`.

### Release prep (2026-06-25)

Pre-public-promotion hardening pass:
- [x] **Honesty-floor fix** — 8 gallery agents (api-reviewer, backend-builder, data-modeler,
      debugger, frontend-builder, refactor-planner, security-review, test-author) were missing the
      no-fabrication floor that the template + `forge-agent` + `SECURITY.md §4` require in 100% of
      agents. Added a domain-scoped floor to each; the gallery now matches its own invariant.
- [x] **Filled roster gaps** — forged `planner` (ordered task plan), `evaluator` (rubric grading
      for iteration), `compliance-reviewer` (regulatory flag list). Eval cases 25–27 added.
- [x] **Split the marketing roster** to a private/local pack (`C:\Dev\marketing-pack`, not for
      public release) — it diluted the prompt-engineering narrative. Public gallery: **20 agents**.
- [x] **Reconciled all doc counts** that had drifted (16/17/22/15 → 20 agents; 21/24 → 27 cases);
      bumped `plugin.json` to 0.2.0 with a fuller description.
- [x] **Full-suite eval run (all 27 cases)** with independent judging on the high-stakes routes —
      the release gate before tagging `v0.2.0`. Logged:
      `evals/runs/2026-06-25-2039-full-suite-v0.2.0-release-gate.md` (26 PASS / 1 WEAK / 0 FAIL).
      **That scorecard is now stale** — six features merged after it (see below).

### Pre-launch adversarial pass (2026-07-21)

Three parallel audits — eval coverage, adversarial security, feature/doc drift — run before any
public promotion. The launch pitch is verifiable rigor, so the claim has to survive an audit by
someone hostile. It mostly did; three defects were the same shape and that shape is the lesson.

**The pattern worth remembering: three separate documents asserted a defense the files did not
implement.** Not sloppiness — drift. A roster that grows fast outruns its own invariants.

- [x] **Slice outputs declared untrusted** in the coordinator (`skills/orchestration/SKILL.md`
      Step 7 + Guardrails). `SECURITY.md:16` named subagent output as a threat source; only the
      *request* had a boundary. A slice may now never self-certify Step 6.5 or 7.5.
- [x] **Instruction/data boundary added to all 20 gallery agents.** The engine had the clause;
      agents never inherited it, and orchestration Step 6 dispatches the agent body *without* the
      engine. `agents/README.md:6` also invites pasting bodies into external hosts where the
      engine never loads. `verifier.md:42` was instructed to catch this failure in others while
      unprotected against it itself.
- [x] **Lens shadowing closed in `commands/lens.md`.** `SECURITY.md:26-28` claimed project-local
      lenses could not shadow `security-reviewer`; the engine implemented it, the command that
      actually resolves lenses did not, and the two disagreed in the same run.
- [x] **Intent gate extended to `--fix`.** `--fix` turned `/lens` from critic into producer
      without inheriting the gate — it would have improved a credential-harvesting page.
- [x] **Second-order injection broadened** beyond text that addressed the reviewer, to payloads
      aimed at the *next* model to consume the artifact.
- [x] **Approval-gate risk test made non-inferential** — content-derived thresholds let content
      lower the bar.
- [x] **`research-synthesizer` supplied-citation clause added.** `SECURITY.md:37-39` listed it as
      a supplied-facts defender; the clause was absent.
- [x] **Independent-judge list replaced with a rule** (`rubric.md`, `runner.md`) — the enumeration
      predated cases 22–27, so the intent-refusal, injection, and compliance-reviewer cases were
      self-grading, which `runner.md` itself calls "not a valid result."
- [x] **`ai-tells` voice counterweight + carve-outs.** Commit `208e2f8` claimed to resolve the
      ai-tells ↔ voice-preservation tension; it never touched `lenses/ai-tells.md`. `--lens
      ai-tells` alone ran the stripping lens with no counterweight, and had no carve-out for
      quotations, statutory terms of art, or domain terminology.

Held for their own slices:
- [ ] **Delivery shell** — `${CLAUDE_PLUGIN_ROOT}` appears zero times; `lenses/`, `templates/`,
      and `agents/` have no resolvable address at runtime. Untracked hero GIF. Two non-agents
      (`README.md`, `coverage-gaps.md`) loaded as invokable agents. Option B omits `templates/`
      and `agents/`. Doc drift (lens count, `/lens-review`, "planned" orchestration).
- [ ] **Clean-install smoke test** — nothing verifies the plugin works as installed from an empty
      directory. Gates the delivery-shell work: if paths don't resolve, that fix is not doc edits.
- [ ] **User-facing eval loop** — expose the grade/iterate discipline to the user's own prompts
      (approved 2026-07-21). Today `evals/` tests promptsmith only.
- [ ] **New eval cases 28–34 + KB4–6** — six features shipped with zero dedicated cases.

## Now in progress — Layer 2 orchestration (Claude-Code-native)

**Status (2026-06-25):** coordinator v0 built on branch `feat/layer2-orchestration` —
`skills/orchestration/SKILL.md` (the pipeline) + `commands/orchestrate.md` (the `/orchestrate`
command) + `agents/coverage-gaps.md` (the gap log). The pipeline encodes gate → sharpen →
decompose → route → seams/conflicts → approval gate → dispatch (subagents) → assemble/curate →
report. **Not yet merged** (awaits review). Open mechanism decisions remain (below). Acceptance
target is eval case 17.

- [x] Coordinator pipeline (decompose / route / seams / synthesize) specified as runnable protocol.
- [x] Coverage-gap detection + log (`agents/coverage-gaps.md`) feeding `/forge-agent`.
- [x] Approval gate before fan-out (default ON; `--no-gate` to waive); `--dry` to inspect routing.
- [x] First live multi-agent run: case 17 PASS via real 4-agent dispatch; guardrail cases 18
  (overkill-fallback) + 19 (coverage-gap) PASS; D6 applied (catch agent-emergent conflicts).
- [x] Full live re-run (2026-06-25): case 17 as a real **7-agent build + independent verifier**
  (runs/2026-06-25-2101-orchestration-case17-live-7agent.md). Caught a 3-way expiry conflict,
  assigned the unowned `expires_at`-enforcement seam, and Step 6.5's verifier caught a HIGH
  `widgets` over-serialization defect → synthesis halted + escalated. The regression anchor now
  has a non-simulated PASS.
- [ ] Continue tuning from real runs (more domains, larger fan-out, the deferred slices).
- [x] Forge `backend-builder` to fill the API-maker gap (gallery now 15 agents).
- [x] Mechanism decisions resolved (2026-06-25): dispatch = **subagents** (Workflow later only
  if fan-out demands); agent form = **inline-prompt** (single source of truth, portable);
  approval gate = **smart threshold** (auto ≤3 agents/low-risk, gate larger; `--gate`/`--no-gate`
  override); command name = `/orchestrate`; specialist selection = roster/lens match.

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
- **Coverage-gap detection → gallery growth.** When part of a request falls outside every
  existing agent's purview, the coordinator must not silently drop it or fake-cover it. It
  **logs the unmet slice** (what was asked, why no agent fits), surfaces it to the user, and
  feeds it back to the gallery: a recurring gap becomes the spec for a new agent forged via
  `/forge-agent` and dropped into `agents/`. This is the feedback loop that makes the roster
  grow from real demand instead of guesswork — orchestration and the gallery improving each other.
- **Agent tool / source access.** Some specialists are only fully useful with live tools —
  `research-synthesizer` needs web/retrieval; others may need a database, a file reader, or a
  code runner. The orchestration runtime is where agents get scoped tool access. Until then,
  affected agents must **degrade honestly** (D5: declare no-source, label training knowledge,
  never fabricate citations). Phase-2 task: a way to grant an agent the tools it needs.
  - **`mcp-integrator` is the front half of this.** When the coordinator hits a slice that needs
    a tool/data source, it routes to `mcp-integrator` to recommend an existing MCP server or spec a
    new one (adopt-before-build, least-privilege) **and emit the wiring recipe** (`claude mcp add` /
    config). It advises and hands off the runnable steps; it does not auto-connect. The remaining
    Phase-2 piece is the **runtime that actually applies the wiring** (approval-gated) and attaches
    the MCP to the agent's session.

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

Resolved (2026-06-25):
- Host mechanism → **subagents** (Agent/Task); Workflow revisited only if fan-out outgrows it.
- Specialist selection → **roster/lens match** against `agents/README.md`.
- Approval point → **smart-threshold gate** before fan-out (Step 5).
- Conflict handling → coordinator **resolves within authority, escalates product/risk calls** (D6).

Still open (deferred, not blocking):
- Promote gallery agents to first-class Claude Code subagent definitions (agentType)? — kept
  inline-prompt for now (single source of truth, portable).
- Workflow harness for very large / pipelined fan-outs.
