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


<!-- enriched:v3 -->

## Scenario

LedgerAir imported 40k rows synchronously, freezing splash transition.

## Deep dive

`compute` runs CPU-heavy parsing off the UI isolate.

## Extended example

```dart
Future<List<Row>> loadRows(String csv) => compute(parseCsv, csv);
List<Row> parseCsv(String csv) => csv.split('\n').map(Row.parse).toList();
```

## Engineering note

Only send sendable data to isolates.

## Try it

- Pick one CPU task for compute.
- Contrast isolate vs thread.

## Summary

Use isolates when profiling shows CPU work blocking the UI thread—not for every network call.
