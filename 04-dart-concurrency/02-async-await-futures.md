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


<!-- enriched:v3 -->

## Scenario

HarborCart fetched tax and shipping rules sequentially though APIs are independent.

## Deep dive

`Future.wait` parallelizes independent work; handle partial failures explicitly.

## Extended example

```dart
Future<(TaxRules, ShipRules)> loadRules() async {
  final pair = await Future.wait([fetchTax(), fetchShipping()]);
  return (pair[0] as TaxRules, pair[1] as ShipRules);
}
```

## Engineering note

Repositories return futures; widgets await via listeners or state notifiers.

## Try it

- Chain dependent futures.
- Add `.timeout` with fallback UI.

## Summary

Repositories return `Future` or `Stream` objects; widgets listen and rebuild when data arrives.
