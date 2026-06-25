# promptsmith eval rubric

Two passes per case: **structural** (deterministic) then **quality** (host-judged). A case
also carries its own case-specific must / must-not (in its `cases/` file) — check those too.

## Scoring scale

Per criterion, one mark + a one-line reason:

- ✅ **pass** — clearly meets it.
- ⚠️ **weak** — partially; name what's missing.
- ❌ **fail** — doesn't meet it; name the gap.

Quote the part of the output you're reacting to. No praise padding — ✅ shows what was
checked, not flattery.

## Judge stance (quality pass)

Adversarial. Your job is to **break** the output, not bless it. Default to ⚠️ or ❌ when
uncertain — make the output earn ✅. Judge through the `skeptic` lens; for prompt/system-prompt
outputs, also the `prompt-engineer` agent's eye.

## Verdict per case

- **Hard gates** (any ❌ here = case FAILS regardless of the rest): the route's structural
  invariants, and the **faithfulness / guardrail** dimension (no invented facts; guardrails
  honored).
- Otherwise: **PASS** if no ❌ on any dimension, **WEAK** if ⚠️s but no ❌, **FAIL** if any ❌.

---

## Structural invariants (deterministic)

### SHARPEN
- All 8 blocks present and filled: ROLE, OBJECTIVE, CONTEXT, REQUIREMENTS, GUARDRAILS,
  SUCCESS CRITERIA, OUTPUT FORMAT, OUT OF SCOPE.
- No unfilled `<...>` placeholders remain.
- Prompt is in one copy-pasteable block; assumptions + push-back + open questions come *after* it.
- Each assumption has an explicit "Override with:".

### FORGE
- System-prompt block present, copy-pasteable.
- Has: persona opening, **Voice** line, Objective, Operating principles, Inputs, Method,
  Constraints/guardrails, Output contract, When-unsure.
- Method includes an explicit self-challenge step before finalizing.
- Followed by assumptions + push-back + open questions + install note.

### LENS
- Per-lens block, findings prefixed ✅/⚠️/❌.
- Findings ordered worst-first.
- Ends with a top-3-fixes list and the `/promptsmith:sharpen` offer.
- Names which lenses ran (and flags any requested-but-missing).

### GALLERY AGENT
- Output matches that agent's own **Output contract** section, section for section.
- A **Voice** is detectable in the prose.

### ORCHESTRATION *(forward target — Layer 2; not runnable until a coordinator exists)*
- Output is **one coherent deliverable**, not concatenated agent outputs.
- Every domain the request implies is represented or explicitly deferred with a reason.
- Every seam (a fact/step >1 agent touches) has a named owner.
- Until Layer 2 ships, a case on this route scores **N/A — blocked**, not PASS/FAIL.

---

## Quality dimensions (host-judged)

### SHARPEN
- **Push-back is real** — surfaced a genuine weakness in the request, not flattery or a non-issue.
- **Named concreteness** — tone/feel adjectives named explicitly; no "some reasonable tone".
- **Faithfulness** *(hard gate)* — assumed only preferences/defaults; invented no domain facts.
- **Lens fit** — auto-picked lenses match the topic; their checklists show up in REQUIREMENTS.
- **Would steer** — a competent agent following this prompt would do the right thing.

### FORGE
- **Durable** — written for every run, not the one example task.
- **In-character voice** — the Voice line is specific and the body actually sounds like it.
- **Self-correcting** — the baked-in self-challenge is substantive, not a token line.
- **Concrete contract** — output contract is exact enough to be checkable.
- **Seeded** *(process)* — if a close gallery match existed, it was adapted, not built cold.

### LENS
- **Maps to checklist** — findings trace to the lens's actual items, not generic advice.
- **Specific** — quotes/points at the artifact; not vague.
- **Impact-ordered** — worst-first, and the top-3 fixes are the highest-leverage ones.
- **No padding** — ✅ lines show coverage, don't flatter.

### GALLERY AGENT
- **Contract honored** *(structural above)* + **guardrails honored** *(hard gate)* — e.g.
  copy-rewrite invents no facts; api-reviewer flags unseen-protections as confirm-items;
  feature-spec states a cut line and the sharpest objection.
- **In voice** — reads as the persona, not generic assistant.
- **Self-challenge done** — the agent's own pre-finalize check actually happened.

### ORCHESTRATION *(Layer 2 — score only once a coordinator exists)*
- **Decompose without overlap** — no concern stated 2–3× across slices.
- **Seam ownership** — each shared fact/step (e.g. expiry enforcement) is assigned to exactly
  one slice, not left implicit.
- **Conflict resolved** — cross-agent contradictions are reconciled before output, not pasted side by side.
- **Single-voice synthesis** — one coherent deliverable, not a pile of agent outputs.
- **Completeness** — every implied domain represented or deferred with a reason.
- **Coverage-gap honesty** — slices with no matching agent are logged as unmet gaps and
  surfaced (candidates for a new forged agent), never silently dropped or faked.
