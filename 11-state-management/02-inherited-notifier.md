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

## Summary

Lift state up when multiple widgets need the same data.
