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


<!-- core:v2 -->
## Core concepts

Dart runs your UI code on a **single isolate** with one event loop. Tasks queue up as **events** (user input, I/O completion, timers) and **microtasks** (immediate follow-ups, often `Future` completions). The loop drains microtasks before the next event, which is why microtask storms can still block frames even without long synchronous work.

Think of the loop as a busy concierge: it can only carry one task at a time. While the concierge parses a giant JSON string synchronously, nobody gets a new frame painted.

## Diagnosing jank in HarborCart

HarborCart's cart summary used to decode server JSON inside `build`. Scrolling stuttered because `build` ran during scroll-driven rebuilds. Moving parsing to `initState` + `Future` removed the stutter without changing visuals.

```dart
class CartSummary extends StatefulWidget {
  const CartSummary({super.key});
  @override
  State<CartSummary> createState() => _CartSummaryState();
}

class _CartSummaryState extends State<CartSummary> {
  CartTotals? totals;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    final raw = await rootBundle.loadString('assets/mock/cart.json');
    final map = jsonDecode(raw) as Map<String, dynamic>;
    if (!mounted) return;
    setState(() => totals = CartTotals.fromJson(map));
  }

  @override
  Widget build(BuildContext context) {
    if (totals == null) return const LinearProgressIndicator();
    return Text('Total: ${totals!.display}');
  }
}
```

## Polished UI tie-in

Show a **skeleton shimmer** (simple `LinearProgressIndicator` or grey boxes) while awaiting I/O so the loop stays responsive and users perceive progress.


<!-- enriched:v3 -->

## Scenario

StudioBoard froze scrolling while computing diff histograms on the UI thread.

## Deep dive

The event loop interleaves frames, gestures, and async completions. Blocking work delays `build`.

## Extended example

```dart
Future<void> loadBoard() async {
  final json = await fetchBoardJson();
  final summary = summarize(json); // must stay fast
  render(summary);
}
```

## Engineering note

Profile before moving code to isolates.

## Try it

- Explain microtasks vs events.
- Reproduce jank with intentional sleep in build (then remove).

## Summary

Understanding the event loop explains why `await` yields control and why blocking the isolate janks animations.
