---
title: MediaQuery and Accessibility
order: 4
---

# MediaQuery and Accessibility

`MediaQuery` exposes screen size, padding, orientation, and text scale factor.

```dart
final width = MediaQuery.sizeOf(context).width;
final padding = MediaQuery.paddingOf(context);
```

Respect user text scaling—avoid locking font sizes unless design requires it. Test with large accessibility fonts.


<!-- core:v2 -->
## Core concepts

`MediaQuery` exposes view insets (keyboard, notches), size, orientation, and **text scaler**. Layouts that hard-code heights clip when users enable larger accessibility text. Prefer flexible constraints and `mainAxisSize: MainAxisSize.min` for content-sized columns.

## Responsive storefront hero

```dart
class StoreHero extends StatelessWidget {
  const StoreHero({super.key});

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.sizeOf(context);
    final textScale = MediaQuery.textScalerOf(context).scale(1);
    final heroHeight = size.width > 900 ? 320.0 : 220.0;
    final titleStyle = Theme.of(context).textTheme.headlineMedium!.copyWith(
          fontSize: (28 * textScale).clamp(24, 36),
        );

    return SizedBox(
      height: heroHeight,
      width: double.infinity,
      child: Stack(
        fit: StackFit.expand,
        children: [
          DecoratedBox(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [const Color(0xFF0F766E), const Color(0xFF134E4A)],
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(
              left: 24,
              right: 24,
              bottom: 24 + MediaQuery.paddingOf(context).bottom,
            ),
            child: Align(
              alignment: Alignment.bottomLeft,
              child: Text('HarborCart Spring Drop', style: titleStyle),
            ),
          ),
        ],
      ),
    );
  }
}
```

## Test matrix

Validate at **360×640**, **820×1180**, and **1400×900** with text scale **1.0** and **1.3**.


<!-- enriched:v3 -->

## Scenario

HarborCart checkout broke when users enabled 1.3× text—buttons clipped.

## Deep dive

Respect `MediaQuery` text scaler; prefer flexible layouts over fixed heights.

## Extended example

```dart
final scale = MediaQuery.textScalerOf(context);
final padding = MediaQuery.paddingOf(context);
```

## Refined UI note

Test large accessibility fonts on smallest phone width.

## Try it

- Fix clipped button under large text.
- Use `MediaQuery.sizeOf` for breakpoints.

## Summary

Responsive layouts start with `MediaQuery` and constraints, not hard-coded pixel widths.
