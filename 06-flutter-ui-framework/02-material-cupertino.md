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


<!-- core:v2 -->
## Core concepts

**Material** and **Cupertino** are parallel design vocabularies. Material emphasizes elevation, seed-based color schemes, and M3 shape language. Cupertino emphasizes flat bars, muted greys, and iOS motion curves. Flutter lets you mix them, but mixed apps should do so **intentionally**—usually via adaptive widgets.

## Adaptive settings panel

```dart
class AlertToggle extends StatelessWidget {
  const AlertToggle({super.key, required this.value, required this.onChanged});
  final bool value;
  final ValueChanged<bool> onChanged;

  @override
  Widget build(BuildContext context) {
    return SwitchListTile.adaptive(
      title: const Text('Session reminders'),
      subtitle: const Text('PulseRoutine nudges between intervals'),
      value: value,
      onChanged: onChanged,
    );
  }
}
```

## Refined layout pairing

Place adaptive controls inside **`ListTile`** rows with 16dp horizontal inset. On desktop, constrain settings column to 640dp centered—wide toggles look accidental, not adaptive.


<!-- enriched:v3 -->

## Scenario

HarborCart iOS users expected Cupertino switches in settings but got Material toggles.

## Deep dive

Pick a primary design language per platform or use adaptive constructors.

## Extended example

```dart
Switch.adaptive(value: alertsOn, onChanged: (v) => setAlerts(v));
```

## Refined UI note

Mix Material scaffold with Cupertino pickers only deliberately—not accidentally.

## Try it

- Build settings with adaptive controls.
- Compare AppBar vs CupertinoNavigationBar.

## Summary

Choose a primary design language per platform or use adaptive constructors (`Switch.adaptive`).
