# promptsmith

**Prompt & context engineering for agents — as a Claude Code plugin.**

You already know the move: a rough request gets *far* better results once you've spelled out
the tone you wanted, the constraints you forgot to state, the edge cases you didn't think of,
and asked the agent to push back on you and review the work like a seasoned professional.

`promptsmith` makes that scaffolding a command instead of something you retype every time.

- **No dependencies. No API keys. No model calls.** It's pure method + structure. Your agent
  (Claude Code, or anything you paste the output into) does the reasoning. Model-agnostic by
  construction.
- **Four commands** (three core + a coordinator), one shared engine, a library of expert lenses
  you can extend, and a 20-agent specialist gallery.

---

## What it does

| Command | You give it | You get back |
|---|---|---|
| `/sharpen` | a rough task request | a complete, gap-filled, reviewed **prompt** to paste into any agent |
| `/forge-agent` | a short description of an assistant | a complete, reusable **system prompt** |
| `/lens` | an existing prompt / page / draft | **findings** from one or more professional lenses |
| `/orchestrate` | a multi-domain request | **one synthesized deliverable** — the gallery, coordinated *(Layer 2)* |

The first three are **Layer 1**: zero model calls, paste-anywhere. `/orchestrate` is **Layer 2**
— it dispatches live subagents, so it needs a host that can spawn them (Claude Code). See
[ROADMAP](ROADMAP.md).

Every run is **hybrid**: it returns a finished draft immediately, lists the assumptions it
had to make, and offers a `--deep` interview to resolve them one question at a time.

---

## Why it matters

The value a skilled person adds to a prompt is invisible scaffolding — the tone they wanted, the
constraints they forgot to state, the edge cases they didn't think of, the professional eye they
wish they had, the push-back they need to hear. promptsmith makes that scaffolding explicit,
repeatable, and auditable.

The two-layer split is the bet. **Layer 1** stays portable and honest — no API keys, no model
calls, works pasted into anything — a defensible identity. **Layer 2** turns a roster of
single-purpose specialists into something that handles real multi-domain work *coherently*,
catching the cross-slice conflicts no single agent can see. That's not theoretical: a live
8-agent run (7 specialists + an independent verifier) on *"add public shareable dashboard links"*
caught a **three-way conflict** on link expiry (spec said "no expiry in the MVP," the schema made it
optional, security called it mandatory) and assigned the **unowned seam** everyone assumed someone
else held (who *enforces* `expires_at` at read time). Then the independent verifier caught a **HIGH
data-exposure defect the builder's own "allow-list DTO" missed** — it allow-listed columns but
shipped the entire `widgets` blob to anonymous viewers — so the pipeline **halted and escalated
instead of shipping it.** Honesty guardrails run through everything — never fabricate a fact, a
citation, or an MCP server you can't verify.

So it can: sharpen any vague ask into an executable prompt; author reusable agent system prompts;
review code, prompts, or UI through professional lenses; and — the headline — take a request like
*"add public shareable links to dashboards"* and produce a complete, coherent build (spec → schema
→ API → UI → tests → docs) by coordinating specialists, resolving their conflicts, escalating the
genuine product decisions to you instead of guessing, and flagging where it's missing an agent or
a tool — then growing itself to fill the gap. It shows its work and proves it with evals.

---

## Example — a real run

**Layer 1 — sharpen a vague ask:**
```
/promptsmith:sharpen make the settings page feel calmer and more trustworthy
```
→ a copy-pasteable prompt with the tone adjectives *named* (calm, ordered, trustworthy), the
accessibility/UX/visual lenses folded into the requirements, guardrails from a red-team pass, and
— because it never invents facts — the stack flagged as `[stack?]` rather than assumed. Below it:
the assumptions it made, the push-back worth hearing, and the open questions.

**Layer 2 — coordinate a multi-domain build:**
```
/promptsmith:orchestrate add public read-only shareable links to user dashboards
```
What happens (the proven flow — from a live 8-agent run, logged in `evals/runs/`):
1. **Sharpens** the request, then **decomposes** it into slices: spec · schema · security · API · UI · tests · docs.
2. **Routes** each slice to a gallery agent; **gates** for approval (7 agents > the smart threshold).
3. **Dispatches** them as live subagents in parallel.
4. **Owns the seams** — data-modeler *stores* `expires_at`; the coordinator assigns its *enforcement*
   (the read-time check everyone assumed someone else owned) to the API slice; data-modeler and
   security independently converge on hashing the token, so it stores `sha256(token)`.
5. **Resolves conflicts** — caught a **three-way disagreement on link expiry** (spec "no expiry in
   MVP" vs. schema "optional" vs. security "mandatory") and settled it (mandatory default TTL);
   **escalated** the TTL value and the live-vs-snapshot product call to you instead of guessing.
6. **Verifies, then refuses to ship a hole** — an independent `verifier` re-attacks the built API and
   catches a **HIGH data-exposure defect** the builder's own "allow-list DTO" missed (it allow-listed
   columns but shipped the whole `widgets` blob to anonymous viewers). The pipeline **halts and
   escalates** rather than synthesizing a vouched-for-but-unverified build.
7. **Synthesizes one build plan** — spec, schema, the API handler, the React modal, the test suite,
   and the docs — not seven pasted outputs, with the blocking fix surfaced as an open decision.

---

## Install

### Option A — as a plugin (recommended)

```
/plugin marketplace add emtcmca/promptsmith
/plugin install promptsmith
```

(For local development against a clone, add the working copy instead:
`/plugin marketplace add C:\Dev\promptsmith`.)

Verify: type `/promptsmith` and confirm `/promptsmith:sharpen`, `/promptsmith:forge-agent`,
and `/promptsmith:lens` autocomplete.

### Option B — manual (standalone, bare command names)

Copy `commands/` and `skills/` into your `~/.claude/` directory
(Windows: `C:\Users\<you>\.claude\`), **and** copy `lenses/` into
`~/.claude/promptsmith-lenses/` so the lens pass can find them. Installed this way the
commands are bare — `/sharpen`, `/forge-agent`, `/lens` — because standalone commands
aren't namespaced. (Skip the lenses copy and the engine's lens step has nothing to load.)

---

## Usage

> **Command names are namespaced.** Installed as a plugin (Option A), the commands are
> `/promptsmith:sharpen`, `/promptsmith:forge-agent`, and `/promptsmith:lens` — type
> `/promptsmith` to autocomplete them. Claude Code namespaces every plugin command to avoid
> collisions; bare `/sharpen` exists only with the manual/standalone install (Option B).
> The examples below use the namespaced form.

### Sharpen a request

```
/promptsmith:sharpen update the dashboard to feel calmer and more authoritative
```

You get a copy-pasteable prompt block (role, objective, requirements with the *named* tone
adjectives, guardrails from a red-team pass, success criteria, output format, out-of-scope),
then the assumptions it made, the push-back worth hearing, and open questions.

Force specific lenses:

```
/promptsmith:sharpen redesign the signup form --lens ux-designer,accessibility
```

Go deep (interview instead of assume):

```
/promptsmith:sharpen draft a violation notice for an unresolved fence dispute --deep
```

### Forge a reusable agent

```
/promptsmith:forge-agent a reviewer that critiques HOA letters for tone and compliance
```

Returns a full system prompt — role, objective, standing operating principles (with the
relevant lens baked in), method including a self-challenge step, guardrails, and an output
contract — ready to drop into a subagent, a skill, or any system-prompt field.

### Review through a lens

```
/promptsmith:lens (paste a component, prompt, or draft) --lens visual-design,accessibility
```

Returns findings (✅ checked / ⚠️ weak / ❌ failing) per lens, worst-first, plus the top 3
fixes by impact. To get a corrected version, feed those findings into `/promptsmith:sharpen`.

---

## Expert lenses

A lens is a professional's checklist in a markdown file. Built-in lenses:

| Lens | Applies to |
|---|---|
| `ux-designer` | UI, flows, components, forms, navigation |
| `visual-design` | theme, look & feel, typography, color, spacing |
| `accessibility` | a11y, WCAG, keyboard, contrast, screen readers |
| `security-reviewer` | code, auth, data, input, integrations |
| `performance` | speed, scale, queries, rendering, payloads |
| `api-design` | endpoints, contracts, backend routes, integrations, webhooks |
| `data-integrity` | billing, payments, transactions, schemas, migrations, money |
| `seo` | search, metadata, crawlability, structured data, marketing pages |
| `product-strategist` | scope, value, MVP, prioritization |
| `editorial` | copy, email, docs, tone of voice |
| `skeptic` | the "push back on me" red-team lens (applied by default) |

### Add your own lens (no fork needed)

Drop a markdown file into either of these — they're loaded automatically and override
built-ins of the same name:

- `~/.claude/promptsmith-lenses/` — available everywhere
- `./.promptsmith-lenses/` — specific to one project

Format:

```markdown
---
name: my-lens
applies-to: comma, separated, topics, that, auto-select, this, lens
---

# My Lens
- A specific check the agent runs the draft against.
- Another check. Keep them concrete and answerable.
```

Then: `/promptsmith:sharpen ... --lens my-lens` (or let auto-select pick it up by topic).

---

## Pre-forged agent gallery

The common `/sharpen` *out-of-scope* items (new features, copywriting, performance,
backend/API, SEO) are exactly the jobs a single task agent should refuse but a user often
needs next. The `agents/` gallery holds ready-to-paste **specialist system prompts** for
them — the kind `/promptsmith:forge-agent` produces, saved so you don't rebuild them cold.

A roster of 20 specialists across spec → plan → build → test → review → document:

- **Build:** `feature-spec`, `planner`, `data-modeler`, `backend-builder`, `frontend-builder`, `test-author`, `refactor-planner`
- **Review:** `api-reviewer`, `security-review`, `verifier`, `evaluator`, `compliance-reviewer`, `debugger`
- **Write:** `copy-rewrite`, `docs-writer`, `sop-writer`, `governance-letter`
- **Meta:** `research-synthesizer`, `prompt-engineer`, `mcp-integrator`

Each carries a named **voice** so it speaks in character at injection. `/promptsmith:forge-agent`
checks this gallery first and **adapts** a close match instead of starting cold. Forge your
own, then drop it in `agents/` to grow the roster. Full list + format in
[`agents/README.md`](agents/README.md).

> **Roadmap:** the gallery is also the foundation for a planned **orchestration layer** —
> promptsmith as a coordinator that sharpens a prompt, dispatches the right specialists, and
> assembles their work. That layer is Claude-Code-native; the core plugin stays zero-call and
> paste-anywhere. See [`ROADMAP.md`](ROADMAP.md).

## How it works (the engine)

All three commands run one method, defined in
[`skills/prompt-engineering/SKILL.md`](skills/prompt-engineering/SKILL.md):

1. **Route** — sharpen / forge / lens.
2. **Extract** — goal, audience, tone/feel/theme, constraints, success criteria, format, scope.
3. **Gap-fill** — make explicit, labeled, reversible assumptions (so the draft is usable now).
4. **Push-back** — red-team the request; turn weaknesses into guardrails.
5. **Lens pass** — run the draft against the selected professional checklists.
6. **Synthesize** — emit via the matching template.
7. **Surface + offer depth** — list assumptions and open questions; offer the `--deep` interview.

There is no LLM call inside the plugin. The host agent reads the skill and performs the
reasoning. That's what makes it model-agnostic and zero-cost.

---

## Repo layout

```
promptsmith/
  .claude-plugin/      plugin.json + marketplace.json (install metadata)
  commands/            /sharpen, /forge-agent, /lens
  skills/
    prompt-engineering/SKILL.md   the shared engine
  lenses/              built-in expert lenses
  agents/              pre-forged specialist system prompts (the gallery / dispatch roster)
                       + coverage-gaps.md (slices no agent covers yet)
  skills/
    prompt-engineering/SKILL.md   Layer 1 engine (sharpen/forge/lens)
    orchestration/SKILL.md        Layer 2 coordinator (orchestrate)
  templates/           output skeletons for sharpen + forge
  evals/               host-judged eval harness (rubric, runner, cases, runs)
  docs/                test-run records
```

---

## Docs

- [USING-PROMPTSMITH.md](docs/USING-PROMPTSMITH.md) — the full how-to (human or agent): install,
  command chooser, every command, lenses, the gallery, orchestration, the eval harness.
- [COMMAND-SHEET.md](docs/COMMAND-SHEET.md) — one-page reference: commands, flags, lenses, gallery,
  recipes.
- [SECURITY.md](docs/SECURITY.md) — threat model + the guardrails (untrusted-input boundary, intent
  gate, supplied-fact verification, independent verification).
- [ROADMAP.md](ROADMAP.md) — the two-layer architecture and what's next.

---

## License

Apache-2.0 © 2026 Eric Tetzlaff
