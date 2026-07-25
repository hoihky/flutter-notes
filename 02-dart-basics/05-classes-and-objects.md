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

## Summary

Model your app domain with small immutable classes. Widgets wrap these models and reflect their data in the UI.
