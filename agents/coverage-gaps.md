# Coverage gaps — slices no gallery agent covers

Append-only. The Layer 2 coordinator (`/promptsmith:orchestrate`) writes here whenever a request
slice falls outside every existing agent's purview. A **recurring** gap is the spec for the next
gallery agent — forge it with `/promptsmith:forge-agent` and drop it in `agents/`.

Format:

```
- [YYYY-MM-DD] "<the query>" → slice "<what was needed>": no agent covers <domain>.
  Suggested agent: <name> — <one-line role>. Forge when the gap recurs.
```

---

<!-- entries below, newest last -->
