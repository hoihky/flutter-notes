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


<!-- enriched:v3 -->

## Scenario

Melody Hub merges local favorites with server playlists without duplicating track ids.

## Deep dive

Lists preserve order; sets enforce uniqueness; maps give O(1) lookup. Use collection literals with `if` and spread to build immutable view models for `setState`.

## Extended example

```dart
List<String> mergePlaylistIds(List<String> local, List<String> remote) {
  final seen = <String>{};
  final merged = <String>[];
  for (final id in [...local, ...remote]) {
    if (seen.add(id)) merged.add(id);
  }
  return merged;
}
```

## Engineering note

Return new lists from repositories; avoid mutating lists held inside `State`.

## Try it

- Group emails by sender using a `Map<String, List<Email>>`.
- Remove items in-place vs copy-on-write: explain trade-offs.

## Summary

Collection literals and spread operators are everyday tools in Flutter build methods.
