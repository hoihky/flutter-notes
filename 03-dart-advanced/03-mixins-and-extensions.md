---
title: Mixins and Extensions
order: 3
---

# Mixins and Extensions

Mixins share behavior across classes without full inheritance. Extensions add methods to existing types.

## Mixins

```dart
mixin PlaybackLogging {
  void logPlay(String track) => print('Playing $track');
}

class Player with PlaybackLogging {}
```

Flutter's `State` class uses mixins like `TickerProviderStateMixin` for animations.

## Extensions

```dart
extension DurationFormat on Duration {
  String get mmss {
    final m = inMinutes.remainder(60).toString().padLeft(2, '0');
    final s = inSeconds.remainder(60).toString().padLeft(2, '0');
    return '$m:$s';
  }
}
```

Extensions keep UI formatting out of domain models.

## Summary

Reach for extensions for small conveniences; use mixins when multiple classes need shared implementation.
