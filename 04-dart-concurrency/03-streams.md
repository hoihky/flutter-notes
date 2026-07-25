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

## Summary

Streams model ongoing events; pair them with controllers in state management solutions.
