---
description: "Author a complete, reusable agent system prompt from a short description — role, objective, method, guardrails, output contract, and baked-in push-back."
usage: "/promptsmith:forge-agent <description of the agent you want> [--lens name,name] [--deep] — e.g. /promptsmith:forge-agent a reviewer that critiques HOA letters for tone and compliance"
category: "dev"
---

Turn a short description into a complete, reusable agent system prompt. Output is plain
text you can drop into a subagent, a skill, a custom GPT, or any system-prompt field.

## Step 1 — Load the engine

Read `skills/prompt-engineering/SKILL.md` in full. This command runs the **FORGE** path.

## Step 2 — Parse arguments

Parse `$ARGUMENTS`:
- `--lens <a,b>` — lenses to bake into the agent's standing behavior. If absent, auto-pick
  the lens(es) that match the agent's domain (e.g. an editor agent → `editorial`).
- `--deep` — interview one question at a time instead of assuming (engine Step 7).
- Everything else = the description of the agent to build.

If the description is empty, ask what agent to build and stop.

## Step 3 — Seed from the gallery (if a match exists)

Before building cold, check this plugin's `agents/` gallery for a specialist whose role is
close to the request (see `agents/README.md` for the roster). If one matches, **read it and
adapt it** — swap domain, tone, and lenses to fit the description — rather than starting from
a blank page. If nothing is close, forge fresh. Either way, the output meets the same bar.

## Step 4 — Run the engine

Execute engine Steps 2–7 with route = FORGE. Key differences from SHARPEN:
- **Durable, not one-off.** Write for *every* future run, not one task. Avoid task-specific detail.
- **Bake in the lens.** The selected lens(es) become standing operating principles, not a
  one-time pass — the agent should always think like that professional.
- **Bake in push-back.** Include an explicit self-challenge step in the agent's Method so it
  red-teams its own output before responding.
- **Define an output contract.** The agent's responses must have a consistent, named shape.

Synthesize using `templates/agent-system-prompt.md`.

## Step 5 — Output

Lead with the **System Prompt** block in a copy-pasteable code fence. Then, below it:
assumptions made, push-back worth hearing, open questions (with the `--deep` offer), and
the short "How to install this agent" note from the template.

No preamble. The system prompt comes first.
