---
title: InheritedWidget and Notifiers
order: 2
---

# InheritedWidget and Notifiers

`InheritedWidget` efficiently notifies dependents when shared data changes. `ValueNotifier` + `ValueListenableBuilder` offer a lighter pattern:

```dart
ValueListenableBuilder(
  valueListenable: positionNotifier,
  builder: (context, position, _) => Slider(value: position, onChanged: _seek),
)
```


<!-- enriched:v3 -->

## Scenario

StudioBoard theme preview propagated accent color without prop drilling.

## Deep dive

InheritedWidget and notifiers broadcast changes to dependents efficiently.

## Extended example

```dart
ValueListenableBuilder(
  valueListenable: accent,
  builder: (context, color, _) => ColoredBox(color: color, child: preview),
);
```

## Engineering note

Prefer small notifiers over one giant app state object.

## Try it

- Build InheritedTheme wrapper.
- Compare rebuild scope vs setState on root.

## Summary

Lift state up when multiple widgets need the same data.
