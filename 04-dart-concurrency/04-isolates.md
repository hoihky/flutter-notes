---
title: Isolates
order: 4
---

# Isolates

Isolates are independent workers with separate memory. Communicate via message passing—no shared mutable state.

```dart
final result = await compute(parseLargeJson, rawBytes);
```

`compute` spawns a short-lived isolate for CPU-heavy work like JSON parsing or image decoding.

For long-running workers, use `Isolate.spawn` and ports. Flutter 3+ also documents isolate groups for advanced scenarios.

## Summary

Use isolates when profiling shows CPU work blocking the UI thread—not for every network call.
