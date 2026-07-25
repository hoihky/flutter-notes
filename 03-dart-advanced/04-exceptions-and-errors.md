---
title: Exceptions and Errors
order: 4
---

# Exceptions and Errors

Dart distinguishes **Exceptions** (intended to be caught) from **Errors** (programming mistakes).

```dart
Future<void> loadCatalog() async {
  try {
    await api.fetchTracks();
  } on SocketException catch (e) {
    // network unavailable
  } catch (e, st) {
    // log st stack trace
    rethrow;
  } finally {
    // cleanup
  }
}
```

In Flutter UI, surface failures with `SnackBar`, error widgets, or dedicated error screens—never silently swallow exceptions in `build`.

## Summary

Catch exceptions at boundaries (repositories, isolates). Let the analyzer and tests guard against logic errors.
