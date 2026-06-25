---
description: "Review an existing prompt, page, component, or draft through one or more expert lenses. Returns findings, not a rewrite."
usage: "/promptsmith:lens <target or pasted artifact> [--lens name,name] — e.g. /promptsmith:lens (paste a React component) --lens ux-designer,accessibility"
category: "dev"
---

Review an existing artifact through professional lenses and report findings. This command
critiques; it does not rewrite. To rewrite, feed the findings into `/sharpen`.

## Step 1 — Load the engine

Read `skills/prompt-engineering/SKILL.md` in full. This command runs the **LENS** path
(engine Step 5 is the core; Steps 2–4 inform what to look for).

## Step 2 — Parse arguments

Parse `$ARGUMENTS`:
- `--lens <a,b>` — explicit lenses. If absent, auto-pick 1–3 by topic (engine Step 5).
- Everything else = the target: a pasted artifact, a description, or a file reference.

If a file path is given, read it. If the target is empty, ask what to review and stop.

## Step 3 — Load lenses

Resolve each lens name against, in priority order (later overrides earlier):
1. This plugin's `lenses/` directory.
2. `~/.claude/promptsmith-lenses/` (user global).
3. `./.promptsmith-lenses/` (project local).

If a named lens isn't found, say so and continue with the others. List which lenses ran.

## Step 4 — Apply and report

Run the target against each lens's checklist. For each lens, output:

```
## <lens name>
- ✅ <item that passes — brief>
- ⚠️  <item that's weak — what and why>
- ❌ <item that fails — what's missing and the fix>
```

Order findings worst-first within each lens. Be specific and concrete — quote the part of
the artifact you're reacting to. No praise padding; ✅ lines exist only to show what was
checked, not to flatter.

## Step 5 — Close

End with the **top 3 fixes** across all lenses, ranked by impact, and a one-line offer:
"Run `/promptsmith:sharpen` with these findings to get a corrected version" (or bare
`/sharpen` if installed standalone).
