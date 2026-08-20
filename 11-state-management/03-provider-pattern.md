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


<!-- enriched:v3 -->

## Scenario

Melody Hub player state spanned mini bar and full screen.

## Deep dive

Provider exposes services and notifiers; `watch` rebuilds, `read` invokes without rebuild.

## Extended example

```dart
class PlayerModel extends ChangeNotifier {
  bool playing = false;
  void toggle() { playing = !playing; notifyListeners(); }
}
```

## Engineering note

Separate read vs watch to avoid rebuild storms in callbacks.

## Try it

- Wire ChangeNotifierProvider.
- Move audio out of widgets.

## Summary

Provider scales to medium apps before you need heavier architectures.
