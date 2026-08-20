---
title: Networking
order: 1
---

# Networking

Use `http` for simple calls or **dio** for interceptors, timeouts, and download progress.

```dart
final response = await dio.get('/v1/tracks', queryParameters: {'q': query});
```

Model JSON with `json_serializable` or manual `fromJson` factories. Never block `build` with network I/O.


<!-- core:v2 -->
## Repository boundary

Widgets should call `catalog.fetchFeatured()` not `http.get`. Parsing, retry, and error translation belong in one module.

```dart
class CatalogRepository {
  CatalogRepository(this.client);
  final HttpClient client;

  Future<List<Sku>> featured() async {
    final uri = Uri.parse('https://example.test/v1/featured');
    final response = await client.getUrl(uri).then((r) => r.close());
    if (response.statusCode != 200) throw CatalogException(response.statusCode);
    final body = await response.transform(utf8.decoder).join();
    return (jsonDecode(body) as List).map((e) => Sku.fromJson(e as Map<String, dynamic>)).toList();
  }
}
```

## UI pairing

Show **`RefreshIndicator`** on lists fed by repositories so users can retry without a dedicated error screen for transient failures.


<!-- enriched:v3 -->

## Scenario

HarborCart switched from ad-hoc http calls to a repository with timeouts.

## Deep dive

Keep HTTP in services; parse JSON to models before widgets see data.

## Extended example

```dart
class CatalogClient {
  CatalogClient(this.baseUrl);
  final String baseUrl;
  Future<List<Sku>> fetchSkus() async {
    final client = HttpClient();
    try {
      final req = await client.getUrl(Uri.parse('$baseUrl/skus'));
      final res = await req.close();
      final body = await res.transform(utf8.decoder).join();
      return parseSkus(jsonDecode(body) as List);
    } finally {
      client.close();
    }
  }
}
```

## Engineering note

Use dart:io HttpClient or package:http—not both patterns mixed silently.

## Try it

- Add error mapping.
- Mock client in tests.

## Summary

Keep HTTP clients in repositories; inject them for tests.
