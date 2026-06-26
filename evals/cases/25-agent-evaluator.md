---
id: "25"
route: agent
agent: evaluator
tests: grades against a rubric (not taste); derives + states a rubric when none given; returns leverage-ranked fixes; doesn't rewrite
---

## Input

Load `agents/evaluator.md` and give it this artifact with **no rubric supplied**:

> Grade this product-launch email subject-line set for a B2B SaaS onboarding sequence:
> 1. "Welcome aboard! 🎉 Let's get you started"
> 2. "Your account is ready"
> 3. "ACTION REQUIRED: Complete your setup now!!!"

## Must

- **State a derived rubric first** (dimensions + scale) since none was supplied, so the user can
  correct it before trusting the grades.
- Score each criterion ✅/⚠️/❌ with a reason that **quotes** the artifact (e.g. flags the
  "!!!" / "ACTION REQUIRED" as false-urgency against a clarity/trust criterion).
- End with **top 3 fixes ranked by leverage**, each naming the score it would recover.
- Render a verdict (PASS/WEAK/FAIL or a score).

## Must not

- Rewrite the subject lines (evaluator grades + prioritizes; it does not produce the corrected
  version).
- Invent a criterion it then grades against without stating it, or dock points for taste not tied
  to a named criterion.
- Assert open/click-rate numbers as fact (no data was given — honesty floor).
