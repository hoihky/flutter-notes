---
title: The Dart Event Loop
order: 1
---

# The Dart Event Loop

Dart runs code on a single thread per isolate, scheduling asynchronous work on an event loop.

## Microtasks vs events

- **Microtask queue** — Runs before the next event; used by `Future` completions and `scheduleMicrotask`.
- **Event queue** — I/O, timers, and user input.

Long synchronous work blocks UI frames. Keep `build` methods fast; offload heavy CPU work to isolates.

## Summary

Understanding the event loop explains why `await` yields control and why blocking the isolate janks animations.
