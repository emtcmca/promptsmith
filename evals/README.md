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
  cases/        input fixtures (one per file): the input + case-specific must / must-not
  runs/         dated scorecards — the regression trail, committed
```

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
