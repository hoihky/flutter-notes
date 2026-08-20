---
title: Control Flow
order: 2
---

# Control Flow

Control flow structures in Dart mirror C-style languages with a few ergonomic additions.

## Conditionals and loops

```dart
if (score >= 90) {
  print('A');
} else if (score >= 80) {
  print('B');
}

for (var i = 0; i < 3; i++) {
  print(i);
}

for (final item in items) {
  print(item);
}

while (condition) {
  // ...
}
```

## Switch expressions

Dart 3 supports expressive `switch` on patterns:

```dart
String label(Status s) => switch (s) {
  Status.playing => 'Now playing',
  Status.paused => 'Paused',
  Status.stopped => 'Stopped',
};
```

## Collections in conditions

Use `is` and `as` for type checks and casts. Prefer pattern matching over unchecked casts when possible.


<!-- enriched:v3 -->

## Scenario

StudioBoard assigns review states with combinatorial rules. Nested `if` statements duplicated logic between services and UI badges.

## Deep dive

Pattern matching with `switch` on enums keeps labels, colors, and analytics events in one expression. Loops should prefer `for-in` when traversing collections owned by models.

## Extended example

```dart
enum ReviewState { draft, inReview, blocked, shipped }

Color badgeColor(ReviewState state) => switch (state) {
      ReviewState.draft => const Color(0xFF64748B),
      ReviewState.inReview => const Color(0xFF2563EB),
      ReviewState.blocked => const Color(0xFFDC2626),
      ReviewState.shipped => const Color(0xFF059669),
    };
```

## Refined UI note

Centralize enum-to-color mapping so light and dark themes swap palettes without touching widgets.

## Try it

- Translate a nested `if/else` chain into a `switch` expression.
- Iterate a map with `for-in` and collect keys matching a predicate.

## Summary

Master `for-in` loops and modern `switch` expressions—they appear frequently in UI code that maps enums to labels and icons.
