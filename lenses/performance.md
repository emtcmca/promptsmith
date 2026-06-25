---
name: performance
applies-to: code, frontend, backend, database, queries, load time, speed, scale, rendering, data fetching
---

# Performance Lens

A performance engineer's checklist. Turn risks into requirements before the prompt ships.

- **Hot path.** What runs most often or blocks the user? Optimize that, not the rare path.
- **N+1 and over-fetching.** Loops issuing queries/requests? Fetching more data than rendered?
- **Caching.** What's recomputed that could be cached? Is cache invalidation defined?
- **Payload size.** Bundle, image, and response sizes. Lazy-load / paginate where large.
- **Rendering.** Unnecessary re-renders, layout thrash, blocking main thread?
- **Async / parallel.** Independent work done sequentially that could run concurrently?
- **Indexes.** Are DB queries supported by indexes on the filtered/sorted columns?
- **Perceived performance.** Optimistic UI, skeletons, streaming — does it *feel* fast?
- **Measure first.** Is there a metric/benchmark, or are we guessing at the bottleneck?
- **Scale.** Does this hold at 10x the data/users, or only at demo size?
