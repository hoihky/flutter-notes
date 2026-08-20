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


<!-- enriched:v3 -->

## Scenario

HarborCart optional delivery instructions were conflated with empty strings, printing blank labels on packing slips.

## Deep dive

Treat unknown, empty, and meaningful values as distinct states. Centralize normalization immediately after parsing external input.

## Extended example

```dart
class DeliveryNote {
  const DeliveryNote(this.lines);
  final List<String> lines;
}
DeliveryNote? parseNote(String? raw) {
  if (raw == null) return null;
  final lines = raw.split('\n').map((l) => l.trim()).where((l) => l.isNotEmpty).toList();
  if (lines.isEmpty) return null;
  return DeliveryNote(lines);
}
```

## Engineering note

Avoid forcing nullable fields with `!` inside build; refactor with guards.

## Try it

- Promote nullable locals after guard clauses.
- Compare `late` vs nullable for `AnimationController`.

## Summary

Treat `?` as documentation of optional data. Combine `??`, `?.`, and promotion to keep UI code readable.
