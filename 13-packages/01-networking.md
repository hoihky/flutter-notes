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

## Summary

Keep HTTP clients in repositories; inject them for tests.
