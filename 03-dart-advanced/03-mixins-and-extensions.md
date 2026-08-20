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


<!-- enriched:v3 -->

## Scenario

PulseRoutine shares heartbeat telemetry between widgets and background timers.

## Deep dive

Mixins compose behavior across unrelated classes; extensions add convenience without subclassing SDK types.

## Extended example

```dart
mixin Heartbeat { DateTime get pulseAt => DateTime.now(); }
extension ColorFade on Color {
  Color soften([double amount = 0.2]) => withValues(alpha: amount);
}
```

## Engineering note

Keep extensions file scoped; do not hide business rules in extension methods.

## Try it

- Format user initials via extension.
- Apply mixin to two State classes.

## Summary

Reach for extensions for small conveniences; use mixins when multiple classes need shared implementation.
