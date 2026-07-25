---
title: async, await, and Futures
order: 2
---

# async, await, and Futures

`Future<T>` represents a value available later. `async`/`await` flatten nested callbacks.

```dart
Future<List<Track>> loadTracks() async {
  final response = await http.get(uri);
  return parseTracks(response.body);
}
```

## Combining futures

```dart
final results = await Future.wait([loadUser(), loadPlaylists()]);
```

## Error handling

Unhandled async errors may reach `FlutterError.onError` or `runZonedGuarded`. Always handle errors in UI-facing loaders.

## Summary

Repositories return `Future` or `Stream` objects; widgets listen and rebuild when data arrives.
