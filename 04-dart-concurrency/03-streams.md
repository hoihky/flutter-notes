---
title: Streams
order: 3
---

# Streams

`Stream<T>` emits multiple asynchronous events—ideal for playback position, download progress, or WebSocket feeds.

```dart
Stream<int> countdown(int from) async* {
  for (var i = from; i >= 0; i--) {
    await Future.delayed(const Duration(seconds: 1));
    yield i;
  }
}
```

Use `StreamBuilder` in Flutter to rebuild when new events arrive. Remember to cancel subscriptions in `dispose`.


<!-- enriched:v3 -->

## Scenario

PulseRoutine countdown streams tick once per second for active intervals.

## Deep dive

Streams emit many events; cancel subscriptions in `dispose`.

## Extended example

```dart
Stream<int> ticks(int from) async* {
  for (var i = from; i >= 0; i--) {
    await Future<void>.delayed(const Duration(seconds: 1));
    yield i;
  }
}
```

## Engineering note

Prefer a single subscription owner per stream.

## Try it

- Build UI with StreamBuilder.
- Guard mounted in listeners.

## Summary

Streams model ongoing events; pair them with controllers in state management solutions.
