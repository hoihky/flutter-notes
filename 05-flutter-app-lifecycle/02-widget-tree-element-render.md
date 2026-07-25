---
title: Widget, Element, and Render Trees
order: 2
---

# Widget, Element, and Render Trees

Flutter maintains three parallel trees:

- **Widget tree** — Immutable configuration you write.
- **Element tree** — Long-lived mounts linking widgets to elements.
- **Render tree** — Layout and paint objects.

When `setState` runs, Flutter walks elements to see which widgets changed, reusing elements when `runtimeType` and `key` match.

## Keys

Keys disambiguate widgets when lists reorder:

```dart
ListView.builder(
  itemBuilder: (context, index) => TrackTile(
    key: ValueKey(tracks[index].id),
    track: tracks[index],
  ),
);
```

## Summary

Cheap widget rebuilds are normal; expensive work belongs outside `build`.
