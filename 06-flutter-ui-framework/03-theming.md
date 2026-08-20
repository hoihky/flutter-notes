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


<!-- core:v2 -->
## Core concepts

`ThemeData` is an inherited bundle of defaults: color scheme, typography, component themes. Child widgets call `Theme.of(context)` instead of hard-coding colors. Dark mode is not a separate app—it is another `ThemeData` paired with `themeMode: ThemeMode.system`.

## Brand-ready theme for StudioBoard

```dart
ThemeData studioBoardTheme(Brightness brightness) {
  const seed = Color(0xFF7C3AED);
  final scheme = ColorScheme.fromSeed(seedColor: seed, brightness: brightness);
  return ThemeData(
    useMaterial3: true,
    colorScheme: scheme,
    cardTheme: CardTheme(
      elevation: 0,
      color: scheme.surfaceContainerHighest,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    ),
  );
}
```

## Sophisticated problem

Designers request **per-feature accent colors** without forking the whole theme. Solve with `ThemeExtension` (see Part 12) rather than inline `Color(0xFF...)` literals scattered across 40 files.


<!-- enriched:v3 -->

## Scenario

StudioBoard branding changed weekly until design tokens moved into `ThemeData`.

## Deep dive

Centralize color, type, and component styles; read via `Theme.of(context)`.

## Extended example

```dart
Theme(
  data: Theme.of(context).copyWith(
    colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF7C3AED)),
  ),
  child: child,
);
```

## Refined UI note

Define `ThemeExtension` for radii/spacing to avoid magic numbers.

## Try it

- Move hard-coded colors to theme.
- Build dark variant with same seed.

## Summary

Centralize brand colors and text styles in theme extensions for large apps.
