---
id: "09"
route: agent
agent: test-author
tests: case enumeration (happy/edge/failure), error paths asserted, behavior-named tests
---

## Input

Load `agents/test-author.md` as the system prompt and run it on:

```
Write tests for parse_duration(s): parses strings like "1h30m", "45m", "2h" into total
seconds. Invalid input should raise.
```

## Must

- Full output contract: Contract under test, Cases (grouped happy/edge/failure), Tests, Gaps.
- Enumerate edges: `0m`, whitespace, unit-only, large values, and at least one failure
  (`abc`, `1x`, negative, reordered units).
- Tests named for the behavior; error/raise paths asserted explicitly, not just happy path.

## Must not

- Test private internals instead of the public `parse_duration` contract.
- Skip the failure cases (the "should raise" half).
