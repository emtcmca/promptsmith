# promptsmith evals

A light, host-judged harness to test and refine promptsmith. Lives here, **not** loaded as a
plugin component (`evals/` isn't a scanned dir), so the plugin surface stays clean.

## Why it's shaped this way

promptsmith is zero-call and model-agnostic — the host model does the reasoning, so two runs
of `/sharpen` are never byte-identical. You can't assert `expected == actual`. So the harness
judges in two passes:

1. **Structural invariants** — deterministic checks (sections present, assumptions labeled,
   ✅/⚠️/❌ used). Catch format regressions. No judgment needed.
2. **Quality rubric** — the host scores each output against a skeptic-framed rubric, per
   dimension, ✅/⚠️/❌ + a one-line reason. The judge is told to *break* the output, not bless it.

Fittingly, promptsmith judges itself: the `skeptic` lens and `prompt-engineer` agent are the
judges.

## Layout

```
evals/
  README.md     this file
  rubric.md     structural invariants + quality dimensions per route, and the scoring scale
  runner.md     the protocol the host follows: run case → check → judge → write scorecard
  cases/        23 input fixtures (one per file): the input + case-specific must / must-not
                (01-08 engine/lens/agent core; 09-16 + 20-21 gallery-agent stress, incl. 15-16
                hard-gate security, 20 backend-builder, 21 mcp-integrator; 17-19 + 22-23
                orchestration & security — 17 live dispatch, 18 fallback, 19 coverage-gap, 22
                intent-gate refusal, 23 lens injection-resistance)
  runs/         dated scorecards — the regression trail, committed
  known-bad/    negative fixtures the harness MUST FAIL — the test of the test (calibration)
```

**Judge independence.** The harness is host-judged, which risks a producer grading its own work
(the first 9 runs were all-PASS). For high-stakes routes (cases 15, 16, 17, 20) the judge must be a
**separate invocation** from the producer (see `runner.md`), and the `known-bad/` fixtures must
periodically FAIL — a judge that can't say no isn't judging.

## How to run

Tell Claude Code: **"run the promptsmith evals"** (all cases) or **"run eval case 02"**.
It follows `runner.md`: executes each case the way a user would, checks invariants, judges the
rubric adversarially, and writes a scorecard to `runs/`.

## The refinement loop

1. Baseline run → commit the scorecard in `runs/`.
2. Change a lens / the engine / an agent.
3. Re-run the same cases.
4. Diff against the last run: keep the change only if the target dimension rose **and** nothing
   else regressed. Revert if it didn't.

Tuning by measured before/after, not vibes.
