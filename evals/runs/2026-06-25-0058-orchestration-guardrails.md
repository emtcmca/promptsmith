# Eval run — 2026-06-25 0058  (orchestration guardrails, host-judged)

- commit: c8a48bd
- cases: 18 (Step 0 fallback), 19 (coverage-gap detection)
- mode: host-judged, **no dispatch** — these test the coordinator's gate + routing + gap logic,
  which is decided before any fan-out, so no subagents are needed (and none were spent).

---

## 18 — orchestration fallback — VERDICT: PASS

Coordinator Step 0 on *"rewrite this paragraph to sound warmer"*:
- ✅ Recognizes a single domain (copy editing). Declines to orchestrate.
- ✅ Falls back with a one-line reason → routes to `copy-rewrite` (or `/promptsmith:sharpen`).
- ✅ Zero fan-out: no decomposition, no subagents.

The Step 0 guard correctly prevents orchestration overkill. PASS.

## 19 — coverage-gap detection — VERDICT: PASS

Coordinator on *"localize the app UI into Spanish and draft the Terms of Service"*:
- ✅ Decomposes to two slices: (a) UI localization → Spanish; (b) draft a ToS.
- ✅ Routes against the roster (`agents/README.md`) and finds **no agent covers translation or
  legal drafting**.
- ✅ Logs both as coverage gaps with suggested new agents (`localizer`, `legal-drafter`) as
  `/forge-agent` candidates — does not force `copy-rewrite` to "translate" or "write legal."
- ✅ States plainly what it cannot deliver rather than faking completeness.

The coverage-gap mechanism fires correctly on uncovered domains. PASS.

*(These eval-detected gaps are intentionally NOT appended to the production
`agents/coverage-gaps.md` — that log is for real coordinator runs, not test fixtures.)*

---

## Run summary

- **18–19: 2 PASS / 0 WEAK / 0 FAIL.** Both orchestration guardrails (overkill-fallback,
  gap-honesty) hold.
- Orchestration suite standing: case 17 PASS (live), 18 PASS, 19 PASS.
- Cost: zero subagents — guardrail logic is pre-dispatch.
