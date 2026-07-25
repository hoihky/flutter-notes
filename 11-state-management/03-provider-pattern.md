---
title: Provider Pattern
order: 3
---

# Provider Pattern

The **provider** package wraps `InheritedWidget` for ergonomics:

```dart
ChangeNotifierProvider(
  create: (_) => PlayerController()..init(),
  child: const AppShell(),
);
```

```dart
context.watch<PlayerController>().toggle();
```

Separate `read` (no rebuild) from `watch` (rebuild on notify).

## Summary

Provider scales to medium apps before you need heavier architectures.
