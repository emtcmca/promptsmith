# Pre-forged agent gallery

Ready-to-paste specialist **system prompts** — the kind `/promptsmith:forge-agent` produces,
saved so you don't rebuild them cold each time.

Each file is a complete agent: paste its body into a Claude Code subagent, a `SKILL.md`, a
custom GPT, or any system-prompt field and it works as-is. They exist because the common
`/sharpen` *out-of-scope* items (new features, copywriting, performance, backend/API, SEO)
are exactly the jobs a single task agent should refuse but a user often needs next.

## The gallery

| Agent | Does | Lenses baked in |
|---|---|---|
| `feature-spec` | turns a rough feature idea into a reviewed spec / mini-PRD | product-strategist, skeptic |
| `copy-rewrite` | rewrites copy to a named tone without inventing facts | editorial, skeptic |
| `api-reviewer` | reviews a backend endpoint / contract for correctness and abuse | api-design, security-reviewer, skeptic |
| `test-author` | writes focused tests for given code, behavior-first | skeptic |
| `refactor-planner` | turns messy code + a goal into a staged, commit-by-commit plan | product-strategist, skeptic |
| `data-modeler` | turns requirements into a schema + safe migration plan | data-integrity, api-design |
| `backend-builder` | builds an endpoint/service to contract — validated, authorized, idempotent | api-design, data-integrity, security-reviewer |
| `docs-writer` | turns code/feature into README, usage, or an ADR | editorial, skeptic |
| `debugger` | turns an error + context into ranked root-cause hypotheses + probes | skeptic |
| `research-synthesizer` | fans out, then synthesizes sources into a cited brief | skeptic, editorial |
| `mcp-integrator` | finds/recommends MCP servers for a task, or specs a new server/client | api-design, security-reviewer, product-strategist |
| `frontend-builder` | builds a UI component to brand, a11y, and UX standards | ux-designer, accessibility, visual-design |
| `security-review` | reviews a change for vulnerabilities across several lenses | security-reviewer, data-integrity, api-design, skeptic |
| `governance-letter` | drafts HOA / board correspondence — firm, compliant, on-tone | editorial, skeptic |
| `sop-writer` | turns a process into a clear, followable SOP | editorial, product-strategist |
| `prompt-engineer` | sharpens a system prompt into a tighter, more concrete one | skeptic, editorial |

## How `/forge-agent` uses this

Before building an agent from scratch, `/promptsmith:forge-agent` checks this gallery for a
close match. If one exists, it **adapts** that agent to your description (swapping domain,
tone, and lenses) instead of starting cold — faster, and consistent in shape. If nothing
matches, it forges fresh and you can drop the result here to grow the gallery.

## Format

Each file is frontmatter + the system prompt as the body:

```markdown
---
name: agent-name
role: one-line description of the specialist
voice: the persona's tone in a few words
lenses: lens-a, lens-b
---

You are <role>.

Voice: <how this agent sounds — named so it speaks in character at injection>.

## Objective ...
## Operating principles ...
## Method ...
## Constraints / guardrails ...
## Output contract ...
## When unsure ...
```

Everything below the frontmatter is the paste-ready system prompt. Keep them durable
(written for every run, not one task) with push-back and an output contract baked in —
the same standard `/forge-agent` holds.

## Add your own

Forge one with `/promptsmith:forge-agent ...`, then save the System Prompt block here as
`agents/<name>.md` with the frontmatter above. It becomes a seed for future forges.
