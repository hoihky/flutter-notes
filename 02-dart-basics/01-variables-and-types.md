---
title: Variables and Types
order: 1
---

# Variables and Types

Dart variables hold references to objects. Type annotations help the analyzer catch mistakes before you run the app.

## Declaring variables

```dart
int count = 0;
final String title = 'Playlist';
const double pi = 3.14159;
var dynamicLater = 'inferred as String';
```

- **`final`** — Set once at runtime.
- **`const`** — Compile-time constant; deeply immutable.
- **`var`** — Type inferred from the initializer.

## Built-in types

| Type | Example |
|------|---------|
| `int` | `42` |
| `double` | `3.14` |
| `String` | `'hello'` |
| `bool` | `true` |
| `List<T>` | `[1, 2, 3]` |
| `Map<K, V>` | `{'a': 1}` |

## Null safety

Non-nullable types cannot hold `null` unless you opt in with `?`:

```dart
String? nickname;
String display = nickname ?? 'Guest';
```

The null-aware operators `?.`, `??`, and `??=` reduce boilerplate when handling optional values—common in JSON APIs and UI forms.

## Summary

Prefer `final` for locals that are assigned once. Use explicit types on public APIs; `var` is fine when the initializer makes the type obvious.
