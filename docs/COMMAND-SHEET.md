# promptsmith — command sheet

A one-page reference. For the narrative walkthrough see [USING-PROMPTSMITH.md](USING-PROMPTSMITH.md).

## Install

```
/plugin marketplace add emtcmca/promptsmith
/plugin install promptsmith
```
Verify: type `/promptsmith` → the four commands autocomplete. Plugin commands are **namespaced**
(`/promptsmith:sharpen`); bare names only exist with the manual/standalone install (see README).

## Commands

| Command | Use it for | Returns |
|---|---|---|
| `/promptsmith:sharpen <request>` | a rough one-off task | a complete, reviewed **prompt** |
| `/promptsmith:forge-agent <description>` | a reusable assistant | a durable **system prompt** |
| `/promptsmith:lens <artifact>` | critiquing something | **findings** (✅/⚠️/❌), worst-first |
| `/promptsmith:orchestrate <request>` | a multi-domain build | **one synthesized deliverable** |

**Pick fast:** one domain → `sharpen` (or one gallery agent). Reusable → `forge-agent`.
Critique only → `lens`. Several domains, one coherent result → `orchestrate`.

## Flags

| Flag | Works on | Effect |
|---|---|---|
| `--lens a,b` | sharpen, forge-agent, lens | force specific lenses (else auto-picked by topic) |
| `--deep` | sharpen, forge-agent | interview one question at a time instead of assuming |
| `--dry` | orchestrate | show decomposition + routing, don't dispatch |
| `--gate` | orchestrate | always pause for approval before fan-out |
| `--no-gate` | orchestrate | run autonomously through synthesis |
| *(default)* | orchestrate | smart gate: auto-run ≤3 agents/low-risk, pause for larger |

## Lenses (auto-selected by topic, or force with `--lens`)

`visual-design` · `ux-designer` · `accessibility` · `security-reviewer` · `performance` ·
`api-design` · `data-integrity` · `seo` · `product-strategist` · `editorial` · `skeptic` (default)

**Add your own:** a markdown file with `name:` + `applies-to:` frontmatter in
`~/.claude/promptsmith-lenses/` (global) or `./.promptsmith-lenses/` (project). Auto-loaded.

## Gallery (16 specialists — paste directly, or let `/orchestrate` dispatch them)

- **Build:** feature-spec · data-modeler · backend-builder · frontend-builder · test-author · refactor-planner
- **Review:** api-reviewer · security-review · debugger
- **Write:** copy-rewrite · docs-writer · sop-writer · governance-letter
- **Meta:** research-synthesizer · prompt-engineer · mcp-integrator

Files live in `agents/`. Forge a new one with `/forge-agent` and drop it in to grow the roster.

## Common recipes

```
# Sharpen, forcing lenses and going deep
/promptsmith:sharpen redesign the signup form --lens ux-designer,accessibility --deep

# Forge a specialist (seeds from the gallery if a match exists)
/promptsmith:forge-agent a reviewer that critiques API endpoints for security holes

# Review a component, then get the fix
/promptsmith:lens (paste code) --lens accessibility,visual-design
# → then feed the findings into /promptsmith:sharpen

# Inspect an orchestration plan without spending fan-out
/promptsmith:orchestrate build a password reset flow --dry

# Run the full coordinated build
/promptsmith:orchestrate add public read-only shareable links to dashboards
```

## Eval harness (test & refine)

- Run: say **"run the promptsmith evals"** (all 21 cases) or **"run eval case 17"** (one).
- Output: a dated scorecard in `evals/runs/`.
- Refine: change a lens/engine/agent → re-run the same cases → diff scorecards → keep only
  non-regressing improvements.

## Honesty guardrails (always on)

Never fabricated, always flagged: facts (provisions, numbers, dates, tech stack), sources/citations
(no retrieval → say so), MCP servers (no registry → recommend by capability + "verify exists").
