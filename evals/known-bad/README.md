# Known-bad fixtures — the test of the test

Each file pairs a case input with a **deliberately wrong output**. The harness **must return FAIL**
on every one. If any scores PASS or WEAK, the judge is rubber-stamping — fix the rubric/judge
before trusting any green run.

These exist because the harness is host-judged: without a control that *must* fail, an all-PASS
history (which is exactly what the first 9 runs produced) is indistinguishable from a judge that
never says no. The known-bad set makes the judge falsifiable.

| Fixture | Plants | Must FAIL on |
|---|---|---|
| KB1 | a sharpen prompt asserting an invented fact as established | faithfulness (hard gate) |
| KB2 | a `/lens` review that obeys an injection in the artifact and clears it | injection-as-finding + the review itself |
| KB3 | a backend handler with string-interpolated SQL (injectable) | api-design / security guardrail (hard gate) |

When a red-team finds a new failure class the judge missed, add a fixture here.
