---
title: Rendering Pipeline
order: 1
---

# Rendering Pipeline

Each frame follows **build → layout → paint → compositing**. The framework schedules frames when animation ticks, gestures resolve, or `setState` marks elements dirty.

Enable performance overlay with `MaterialApp(showPerformanceOverlay: true)` in debug builds to spot missed frames.


<!-- core:v2 -->
## Core concepts

Rendering is not one step—it is a pipeline:

1. **Build** — widgets produce an updated description.
2. **Layout** — render objects negotiate constraints and choose sizes.
3. **Paint** — layers record drawing commands.
4. **Compositing** — engine assembles layers into the final surface.

When Melody Hub's album grid stutters, ask which stage ran too often. Unnecessary **build** work is the most common culprit; unnecessary **repaint** is second (fix with `RepaintBoundary`).

## Fancy grid without extra rebuilds

Split static decoration from changing text so only the label rebuilds:

```dart
class AlbumTile extends StatelessWidget {
  const AlbumTile({super.key, required this.title, required this.imageUrl});
  final String title;
  final String imageUrl;

  @override
  Widget build(BuildContext context) {
    return RepaintBoundary(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: DecoratedBox(
                decoration: BoxDecoration(
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withValues(alpha: 0.18),
                      blurRadius: 12,
                      offset: const Offset(0, 6),
                    ),
                  ],
                ),
                child: Image.network(imageUrl, fit: BoxFit.cover, width: double.infinity),
              ),
            ),
          ),
          const SizedBox(height: 8),
          Text(title, maxLines: 1, overflow: TextOverflow.ellipsis),
        ],
      ),
    );
  }
}
```

## Debugging checklist

- Toggle **performance overlay** in debug.
- Count `setState` calls during scroll.
- Wrap static art in `RepaintBoundary` and profile again.


<!-- enriched:v3 -->

## Scenario

Melody Hub dropped frames when album grids rebuilt entire slivers each tick.

## Deep dive

Frames pipeline build → layout → paint → compositing. Minimize rebuild scope.

## Extended example

```dart
class FrameBudgetBanner extends StatelessWidget {
  const FrameBudgetBanner({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      showPerformanceOverlay: true,
      home: const Scaffold(body: Center(child: Text('Profile me'))),
    );
  }
}
```

## Refined UI note

Use `RepaintBoundary` on expensive static artwork layers.

## Try it

- Enable performance overlay.
- List reasons layout pass reruns.

## Summary

Jank usually means too much work per frame—simplify `build`, cache images, or defer layout.
