---
title: Flutter Architecture
order: 1
---

# Flutter Architecture

Flutter layers stack from embedded platform views up to your widgets:

1. **Embedder** — OS window, input, surfaces.
2. **Engine** — Skia/Impeller, Dart runtime, compositing.
3. **Framework** — Widgets, rendering, gestures, painting.

Your code interacts primarily with the **framework** layer. Understanding separation helps when debugging performance or platform integration.


<!-- core:v2 -->
## Layer responsibilities

| Layer | Owns | Example bug symptom |
|-------|------|---------------------|
| Framework | Widgets, gestures, focus | Wrong layout math |
| Engine | Rasterization, text shaping | Garbled glyphs |
| Embedder | Window, vsync, plugins | Keyboard inset missing |

Melody Hub audio bugs often live at **plugin/embedder** boundaries, while list jank is usually **framework** rebuild scope.

## Minimal layered diagram in code comments

Document boundaries in services:

```dart
/// Framework-facing API. Implementation may call platform channels (embedder).
abstract class AudioBridge {
  Future<void> play(Uri source);
}
```

## Fancy UI consequence

When embedder keyboard insets arrive late, wrap body with `AnimatedPadding` driven by `MediaQuery.viewInsets` so fields glide instead of jumping.


<!-- enriched:v3 -->

## Scenario

Melody Hub audio glitched when engineers confused engine vs framework responsibilities.

## Deep dive

Embedder handles OS surfaces; engine renders; framework builds widget trees. Know which layer owns your bug.

## Extended example

```dart
class LayerLegend extends StatelessWidget {
  const LayerLegend({super.key});
  @override
  Widget build(BuildContext context) {
    return const Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('Framework → widgets you write'),
        Text('Engine → rendering + Dart runtime'),
        Text('Embedder → OS window + input'),
      ],
    );
  }
}
```

## Engineering note

Platform channels bridge framework to embedder for sensors.

## Try it

- Trace one bug to a layer.
- List embedder responsibilities.

## Summary

Widgets are Dart configuration; the engine turns them into pixels. Platform channels cross from framework to embedder.
