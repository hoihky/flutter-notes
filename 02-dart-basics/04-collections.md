---
title: Collections
order: 4
---

# Collections

Lists, sets, and maps model in-memory data before you persist or send it over the network.

## Lists

```dart
final tracks = <String>['Intro', 'Verse', 'Chorus'];
tracks.add('Outro');
final first = tracks.first;
```

## Maps

```dart
final durations = <String, int>{
  'Intro': 30,
  'Verse': 45,
};
durations['Chorus'] = 60;
```

## Spread and collection-if

```dart
final adminMenu = [
  'Home',
  if (isAdmin) 'Settings',
  ...extraItems,
];
```

These literals simplify building dynamic widget child lists.

## Immutability

Prefer unmodifiable views or copy-on-write patterns when exposing data from state classes so widgets do not mutate shared lists accidentally.

## Summary

Collection literals and spread operators are everyday tools in Flutter build methods.
