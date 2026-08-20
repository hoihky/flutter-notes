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


<!-- enriched:v3 -->

## Scenario

LedgerAir rejected entire imports when one row contained a bad date.

## Deep dive

Model row-level failures as exceptions with context; let programming errors remain assertions in debug.

## Extended example

```dart
class RowParseException implements Exception {
  RowParseException(this.index, this.line);
  final int index; final String line;
}
```

## Engineering note

Translate exceptions to user strings in the presentation layer only.

## Try it

- Map network failures to retry UI.
- Choose caught vs uncaught for programmer bugs.

## Summary

Catch exceptions at boundaries (repositories, isolates). Let the analyzer and tests guard against logic errors.
