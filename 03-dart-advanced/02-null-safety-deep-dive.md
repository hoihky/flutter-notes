---
title: Null Safety Deep Dive
order: 2
---

# Null Safety Deep Dive

Sound null safety eliminates a large class of runtime crashes by tracking nullability in the type system.

## Promotion

The analyzer promotes types after null checks:

```dart
void printLength(String? text) {
  if (text == null) return;
  print(text.length); // text is String here
}
```

## Late variables

`late` defers initialization when you know a field will be set before use—common in `State` objects:

```dart
late final AnimationController _controller;

@override
void initState() {
  super.initState();
  _controller = AnimationController(vsync: this);
}
```

Misusing `late` causes runtime errors; prefer constructor initialization when possible.

## Summary

Treat `?` as documentation of optional data. Combine `??`, `?.`, and promotion to keep UI code readable.
