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


<!-- enriched:v3 -->

## Scenario

StudioBoard attachments include images, PDFs, and link cards. Untyped maps caused runtime casts in UI code.

## Deep dive

Generics encode expectations at compile time. Constrain parameters when operations only apply to shared supertypes.

## Extended example

```dart
abstract class BoardItem { String get id; }
class LinkItem implements BoardItem { LinkItem(this.id, this.url); @override final String id; final String url; }
class ItemCache<T extends BoardItem> {
  final _map = <String, T>{};
  void store(T item) => _map[item.id] = item;
  T? read(String id) => _map[id];
}
```

## Engineering note

Specify generic types on Flutter builders like `FutureBuilder<List<Album>>`.

## Try it

- Implement `firstWhereOrNull` as a generic function.
- Add `T extends Comparable` constraint.

## Summary

When you see angle brackets in Flutter docs, you are looking at generic types—specify the type argument for clearer analyzer support.
