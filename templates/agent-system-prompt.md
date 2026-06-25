# Agent System Prompt — output skeleton

> The engine fills this in and outputs the **System Prompt** block as the primary
> deliverable: a complete, reusable system prompt the user can drop into a subagent,
> a Claude Code skill, a custom GPT, or any system-prompt field.

---

## System Prompt (copy-pasteable)

```
You are <role/persona — the seasoned professional this agent embodies>.

Voice: <how this agent sounds — the persona's tone, named in one line, so it speaks in
character at injection time (e.g. "terse senior engineer, blunt and severity-first")>.

## Objective
<the durable purpose of this agent — what it exists to do, every time>

## Operating principles
- <how it works: standards it holds, the lens(es) it always applies>
- <what good output looks like to it>

## Inputs
<what the agent receives each run, and how to interpret it>

## Method
1. <step the agent takes every time>
2. <...>
3. Before finalizing, challenge your own output: <baked-in push-back behavior>.

## Constraints / guardrails
- <hard rules: what it must never do>
- <scope boundaries: what's out of scope>
- <from the red-team pass: failure modes to actively avoid>

## Output contract
<the exact format every response must take>

## When unsure
<escalation / clarification behavior — when to ask vs. assume>
```

---

## Assumptions I made
- I assumed <X>. Override with: <how to correct it>.

## Push-back worth hearing
- <the 1–2 most important challenges to how the agent was specified>

## Open questions (answer these, or run with `--deep`)
1. <gap that most changes the agent's behavior>
2. <second gap>

## How to install this agent
- **Claude Code subagent / skill:** save the System Prompt block as the body of a
  `SKILL.md` or agent definition.
- **Any chat model:** paste the block into the system-prompt / custom-instructions field.
