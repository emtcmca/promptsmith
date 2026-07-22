# promptsmith — launch plan

Status: **draft, 2026-07-21.** Sequenced. Nothing in Phase 1+ ships until Phase 0 is done —
promoting a repo that looks mid-build burns the one first impression each channel gives you.

Baseline at time of writing: public repo, 2 stars, 0 topics, no release notes, `v0.2.0` tag
with 6 unreleased features on `main`.

---

## The positioning problem (read first)

There are hundreds of "prompt improver" repos. Almost none of them can answer *"how do you know
it works?"* promptsmith can, and that is the only durable wedge:

- **27 eval cases, 14 logged runs**, including known-bad calibration fixtures and an independent
  judge on high-stakes routes.
- **A red-team pass** (13 findings) with a threat model in `docs/SECURITY.md`.
- **An honesty floor** enforced across 100% of gallery agents — no fabricated facts, citations,
  or MCP servers.
- **A live 7-agent orchestration run** where the verifier caught a HIGH over-serialization
  defect and *halted synthesis* instead of shipping it (`evals/runs/2026-06-25-2101-*`).

So the pitch is never "I made a prompt tool." It is **"I built an eval harness for prompt
scaffolding, and here is what it caught."** The tool is the artifact; the receipts are the story.

Corollary lesson from `transparent-confidence`: do not make adoption or traction claims. There
is no traction yet. Claim only what is measured.

### Wording rule (decided 2026-07-21)

promptsmith **is not** an eval harness; it is a prompt & context engineering toolkit that **has**
one. Getting this wrong is a self-inflicted wound: a developer who installs expecting to eval
*their* prompts and finds four slash commands has been misled, and a product whose entire pitch is
"we don't make unsubstantiated claims" cannot open with one.

- **Product surfaces** (README top-line, `plugin.json`, repo description, awesome-list entries)
  → **"eval-backed."** Never "is an eval harness."
- **Story surfaces** (article, HN first comment, LinkedIn, social) → lead with the eval harness at
  full strength. *"Most prompt tools can't answer 'how do you know it works?' So I built the eval
  harness first."* True as narrative, and it is the whole thesis.

**Updated 2026-07-21 — grade mode shipped (as `/lens --grade`), so the line moves.** A user can now
run their own prompt through a scored rubric and compare two versions with regressions named. On
product surfaces you may now say promptsmith **grades prompts against a rubric** and is
**eval-backed**, because both are literally true. *(Grading was briefly a standalone `/grade`
command; merged into `/lens --grade` the same day, pre-promotion, after two launch reviews flagged
the lens/grade overlap. Command surface is four.)*

Still do not say it *is* an eval harness, flatly. `evals/` (the 37-case regression suite with
known-bad calibration) tests promptsmith; `/lens --grade` scores the user's prompts. They are
related by method, not identical, and a reader who installs expecting the former gets the latter.
The honest strong claim:

> The same score → change → re-score → keep-only-what-didn't-regress loop promptsmith runs on
> itself, pointed at your prompts.

That sentence is defensible line by line, and it is stronger than the overclaim would have been.

---

## Phase 0 — ship-readiness (blocking)

No promotion until every box is checked. Order revised 2026-07-21 after three adversarial audits;
the audits are folded in as steps 2–3 because fixing files after an eval run invalidates the run.

```
1. clean-install smoke test   ← gates everything                     ✅ done 2026-07-21
2. delivery shell
   2a. functional  (paths, agent descriptions, phantom agents)       ✅ done 2026-07-21
   2b. docs + metadata (GIF, Option B, plugin.json, doc drift)       ✅ done 2026-07-21
3. security findings          (3 HIGH, 5 MED)                        ✅ done 2026-07-21
4. user-facing eval loop      (/lens --grade)                        ✅ done 2026-07-21
5. new eval cases             (27→37 cases, 3→6 fixtures)            ✅ done 2026-07-21
6. full suite re-run          → v0.3.0 → promote          ✅ SUITE GREEN 2026-07-21
7. clean-install re-verify    ✅ PASS 2026-07-21 — plugin.json bumped to 0.3.0
```

**Phase 0 complete.** All seven steps done. Clean-install re-verify confirmed every
`${CLAUDE_PLUGIN_ROOT}` path resolves from a non-repo cwd, all 20 agents load with descriptions,
no phantom agents, four commands advertised, twelve lenses present, manifest bumped to 0.3.0.
Next: merge to main, tag v0.3.0, cut the GitHub Release — *then* Phase 1 promotion (awesome-list
PRs), Phase 2 (article), Phase 3 (Show HN).

**Step 6 done — suite green.** All 37 cases run blind: **36 PASS · 1 WEAK (fixed) · 0 FAIL**,
calibration **6/6 known-bad correctly FAILED**. Full record: `evals/runs/2026-07-21-post-adversarial-pass.md`.
Only step 7 (clean-install re-verify) remains before the tag. Promotion (awesome-list PRs, article,
HN) stays gated behind the tag.

Worth keeping for the article: the harness's first real outing caught a defect in its own fixture
and a defect in its own methodology *before* it caught anything in the product, and two subagents
reported their own contamination unprompted. That is what a working eval loop looks like from the
inside, and it is a better story than a clean green run.

**What step 1 changed about the plan.** The smoke test found a defect neither audit caught: all 20
gallery agents lacked a `description`, the one frontmatter field a host uses to auto-select an
agent by task context. The gallery — the marquee feature in the README and `plugin.json` — could
not be invoked automatically. Worth noting for the launch story: this was invisible to code
review and visible in 30 seconds from a live agent roster. **Install it before you market it.**

Step 1 runs first because items in step 2 are unknowable without it: if `lenses/` and `templates/`
genuinely don't resolve at runtime, that is an architecture fix, not a doc edit. Step 7 repeats it
because every step in between touches files the installer copies.

- [x] **Commit the README restructure + demo GIF.** The GIF is the single highest-leverage asset
      — most visitors decide in 5 seconds, above the fold. It was referenced by the README while
      untracked, so the hero image was broken on GitHub the whole time.
- [x] **Ship the proof asset — done 2026-07-22.** The "why download this?" gap the GTM/cold-user
      audits flagged. Built as the **prompt delta** (`proof-prompt-delta.png/.gif`): one-line
      request → the fleshed prompt promptsmith hands back, each added line tagged in the margin
      with the decision the one-liner left unstated (retryable-only, jitter, the double-charge
      prohibition, the honesty-floor open question). Answer-vs-answer **code delta**
      (`proof-code-delta.png/.gif`) kept for a dev audience in a README `<details>`. README section
      retitled "What you actually get"; both generators committed (`make-prompt-delta.py`,
      `make-code-delta.py`) so the assets are reproducible. Original design was answer-first;
      switched to prompt-first after a target-reader review found the code-only cut didn't show
      the product.
- [x] **Re-run the full eval suite — done 2026-07-21.** 36 PASS · 1 WEAK (fixed) · 0 FAIL;
      6/6 known-bad fixtures correctly FAILED. Scorecard: `evals/runs/2026-07-21-post-adversarial-pass.md`.
- [x] **Cut `v0.3.0` — done 2026-07-21.** `plugin.json` bumped, tag pushed, GitHub Release
      published with real notes (`--latest`, not a draft).
- [x] **GitHub repo metadata — done 2026-07-21.** Topics, description (now names `/orchestrate`),
      and homepage all set:
      - Topics: `claude-code`, `claude-code-plugin`, `prompt-engineering`, `ai-agents`,
        `agent-orchestration`, `llm`, `anthropic`, `context-engineering`, `subagents`
      - Description: add `/orchestrate` (current one predates Layer 2)
      - Homepage URL: point at the README anchor or erictetzlaff.com
- [x] **Reconcile counts** — done 2026-07-21 and verified against `ls`: 20 agents · 12 lenses ·
      27 cases · 4 commands. (Superseded note follows.) Original entry: lens count changed
      (12 now) and drifted counts are exactly what a reviewer catches first.

---

## Phase 1 — evergreen distribution (highest ROI, zero cost)

Awesome-list PRs keep delivering traffic for years. Do these before any post — a post drives one
spike; a list entry compounds. **Stagger them** (2–3 days apart); simultaneous identical PRs
across every list reads as spam to maintainers who watch each other.

Targets, in priority order:

1. `hesreallyhim/awesome-claude-code` — the canonical one. Highest traffic.
2. `ComposioHQ/awesome-claude-skills` — already cited as a source in `planned-features.md`.
3. Claude Code plugin marketplace registries (community-maintained plugin indexes).
4. `e2b-dev/awesome-ai-agents` — orchestration/gallery angle.
5. `promptslab/Awesome-Prompt-Engineering` or equivalent.

**PR hygiene that gets merged:** read `CONTRIBUTING.md` first, match the existing entry format
exactly, one entry per PR, alphabetical placement, one-line description under whatever char limit
they enforce, no marketing adjectives. Verify each list's format before opening — a
malformed entry is a silent close.

Draft entry line (tune per list):

> **[promptsmith](https://github.com/emtcmca/promptsmith)** — Prompt & context engineering
> commands for Claude Code: sharpen rough requests, forge reusable agent system prompts, review
> through expert lenses, and orchestrate a 20-agent gallery. Zero deps, no API keys, eval-backed.

---

## Phase 2 — the article (the real asset)

One well-built technical post that the HN submission and every social post points back to.
Write it once; reuse it everywhere.

**Do not write "I built a prompt tool."** Write the teardown. Candidate angles, best first:

1. **"I ran 7 AI agents on one feature. They contradicted each other — here's the log."**
   The case-17 run is genuinely interesting *independent of promptsmith*: three agents each
   assumed another owned `expires_at` enforcement, so nobody enforced it. Unowned seams are a
   real, general multi-agent failure mode. The tool is the answer at the end, not the premise.
2. **"How do you eval a prompt tool that makes zero model calls?"** — the known-bad fixtures and
   independent-judge design. Narrow, credible, low bullshit surface.
3. **"An honesty floor for agent system prompts"** — the no-fabrication invariant and the
   audit that found 8 of 20 agents violating it. Admitting the bug is the credibility.

Angle 1 has the widest reach; angle 2 earns the most respect from the people who matter.
Recommendation: **write angle 1, and make angle 2 the second half.**

Publish to dev.to (canonical), cross-post to the personal blog with `rel=canonical`.

**Rules:** show real logged output, not paraphrase. Link the actual run files. Include the
failure. No screenshots of prose — code blocks. No "revolutionary/game-changing/leverage."

---

## Phase 3 — Show HN

Submit **after** the article and release are live, so the repo survives the click-through.

- Title: `Show HN: Promptsmith – prompt engineering commands for Claude Code, with an eval harness`
- Tue–Thu, ~8–10am ET.
- First comment (post it yourself, immediately): what it is, what it explicitly does *not* do
  (no model calls, no API keys, static-copy install by design), the honest limitation
  (`/orchestrate` is Claude-Code-only), and a direct link to the evals directory.
- Expect hostility toward "another AI prompt tool." The defense is not argument — it is the
  eval harness and the logged failure. Lead the first comment with it.
- Answer every comment for the first 3 hours. Never argue; concede real points publicly.

---

## Phase 4 — owned channels

- **LinkedIn** — the warmest audience. Same story as the article, compressed. Link the repo.
- **X / Bluesky** — thread of the case-17 conflict, one screenshot per beat.
- **Reddit** — `r/ClaudeAI`, `r/ClaudeCode`. Read each sub's self-promo rule first; several ban
  it outright or require a flair. Contribute before posting.
- **Anthropic Discord / community channels** — plugin-sharing threads if they exist.

---

## What success looks like (set expectations honestly)

A good outcome for a niche dev tool with no existing audience is **tens of stars and a handful
of real users**, not hundreds. The metric that actually matters: **one external issue or PR
filed by someone Eric does not know.** That is the signal `transparent-confidence` never got
(2 stars, 6 self-seeded issues, downloads trending down). Track that, not stars.

Do not cite promptsmith adoption numbers in a resume, profile, or pitch until that signal exists.

---

## Sequence summary

```
Phase 0 (blocking)  →  Phase 1 (staggered, evergreen)  →  Phase 2 (article)  →  Phase 3 (HN)  →  Phase 4
ship-ready             awesome lists                      dev.to                Show HN         LinkedIn/X/Reddit
```
