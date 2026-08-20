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


<!-- enriched:v3 -->

## Scenario

HarborCart list reordering reused wrong state because keys were omitted.

## Deep dive

Widgets configure; elements mount; render objects layout/paint. Keys preserve state when child order changes.

## Extended example

```dart
ListView.builder(
  itemBuilder: (context, i) => CartLineTile(key: ValueKey(lines[i].sku), line: lines[i]),
);
```

## Engineering note

Stable keys for dynamic lists; avoid `UniqueKey` unless intentional reset.

## Try it

- Explain three trees in your words.
- Fix reorder bug with ValueKey.

## Summary

Cheap widget rebuilds are normal; expensive work belongs outside `build`.
