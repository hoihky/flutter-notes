---
title: Local Persistence
order: 2
---

# Local Persistence

**shared_preferences** stores small flags. **hive** or **isar** handle structured offline caches. **sqflite** fits relational data on mobile.

Desktop apps may use `path_provider` for file locations and SQLite similarly.


<!-- enriched:v3 -->

## Scenario

Melody Hub cached last queue offline between launches.

## Deep dive

Match storage to data shape: preferences for flags, files/SQLite for structured caches.

## Extended example

```dart
// conceptual: SharedPreferences for last track id
Future<void> saveLastTrack(String id) async {
  final p = await SharedPreferences.getInstance();
  await p.setString('last_track', id);
}
```

## Engineering note

Never block build waiting on disk IO.

## Try it

- Design offline schema.
- Encrypt sensitive prefs on desktop.

## Summary

Cache album art and playlists for offline listening scenarios.
