---
title: Material and Cupertino
order: 2
---

# Material and Cupertino

**Material** widgets follow Google's design system; **Cupertino** mimics iOS. You can mix them, but consistency matters for UX.

```dart
MaterialApp(
  theme: ThemeData(colorSchemeSeed: Colors.deepPurple),
  home: ...,
);
```

```dart
CupertinoApp(
  theme: const CupertinoThemeData(brightness: Brightness.light),
  home: ...,
);
```

## Summary

Choose a primary design language per platform or use adaptive constructors (`Switch.adaptive`).
