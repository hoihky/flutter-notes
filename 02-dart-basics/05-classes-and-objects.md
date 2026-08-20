---
title: Classes and Objects
order: 5
---

# Classes and Objects

Dart classes encapsulate state and behavior. Flutter widgets are classes; so are your domain models.

## Defining a class

```dart
class Track {
  Track({required this.id, required this.title, this.duration});

  final String id;
  final String title;
  final Duration? duration;
}
```

## Constructors

Use initializing formals (`this.field`) and named constructors for clarity:

```dart
class Track {
  Track.playlistEntry(this.title) : id = 'generated';
  final String id;
  final String title;
}
```

## Equality

For value objects, override `==` and `hashCode` or use packages like `equatable` (covered later). Identical widget configuration depends on stable equality for keys and lists.


<!-- enriched:v3 -->

## Scenario

LedgerAir attaches receipts to entries. Two entries with identical amounts but different ids incorrectly compared equal when `==` was not overridden.

## Deep dive

Value objects should define equality on business keys. Immutable classes with `copyWith` make undo/redo and filtering predictable.

## Extended example

```dart
class ReceiptRef {
  const ReceiptRef({required this.entryId, required this.storageKey});
  final String entryId;
  final String storageKey;

  @override
  bool operator ==(Object other) =>
      other is ReceiptRef && other.entryId == entryId && other.storageKey == storageKey;

  @override
  int get hashCode => Object.hash(entryId, storageKey);
}
```

## Engineering note

Use `const` constructors wherever fields allow compile-time constants.

## Try it

- Implement `copyWith` on a three-field model.
- Explain when to prefer records vs small classes.

## Summary

Model your app domain with small immutable classes. Widgets wrap these models and reflect their data in the UI.
