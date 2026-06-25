# Sharpened Prompt — output skeleton

> The engine fills this in and outputs the **Prompt** block as the primary deliverable.
> Everything below the block is reported separately, after it.

---

## Prompt (copy-pasteable)

```
ROLE: <who the agent should act as for this task — include the expert lens(es) applied>

OBJECTIVE: <the real goal, one or two sentences>

CONTEXT: <the relevant background the agent needs — stack, audience, prior state>

REQUIREMENTS:
- <concrete requirement 1, drawn from extraction + lens checklists>
- <concrete requirement 2>
- <tone / feel / theme requirements, named explicitly>
- <constraints: what must not break, length, format, brand rules>

GUARDRAILS (from red-team pass):
- <guardrail addressing a failure mode the literal request ignored>

SUCCESS CRITERIA:
- <how we'll know the result is good>

OUTPUT FORMAT: <the exact shape of the deliverable>

OUT OF SCOPE: <what to explicitly not do>
```

---

## Assumptions I made
- I assumed <X>. Override with: <how to correct it>.
- I assumed <Y>. Override with: <how to correct it>.

## Push-back worth hearing
- <the 1–2 most important challenges to the original request>

## Open questions (answer these, or run with `--deep`)
1. <gap that most changes the output>
2. <second gap>
