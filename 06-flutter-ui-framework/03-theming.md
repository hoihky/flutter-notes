---
title: Theming
order: 3
---

# Theming

`ThemeData` propagates colors, typography, and component defaults through `Theme.of(context)`.

```dart
final theme = Theme.of(context);
Text('Headline', style: theme.textTheme.headlineSmall);
```

Dark mode uses `ThemeMode.system` and separate `darkTheme` on `MaterialApp`.

## Summary

Centralize brand colors and text styles in theme extensions for large apps.
