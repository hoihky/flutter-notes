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

## Summary

Master `for-in` loops and modern `switch` expressions—they appear frequently in UI code that maps enums to labels and icons.
