---
title: Generics
order: 1
---

# Generics

Generics let you write type-safe code that works across multiple types.

```dart
class Box<T> {
  Box(this.value);
  final T value;
}

T? first<T>(List<T> items) => items.isEmpty ? null : items.first;
```

Flutter APIs use generics extensively: `ListView.builder`, `FutureBuilder<T>`, `StreamBuilder<T>`, and `ValueNotifier<T>`.

## Constraints

```dart
class Repository<T extends Identifiable> { ... }
```

Constraints document expectations and enable safer APIs.

## Summary

When you see angle brackets in Flutter docs, you are looking at generic types—specify the type argument for clearer analyzer support.
