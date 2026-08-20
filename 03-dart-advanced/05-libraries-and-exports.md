---
title: Libraries and Exports
order: 5
---

# Libraries and Exports

Dart organizes code into libraries—typically one per file, with `part`/`part of` used sparingly.

## Imports

```dart
import 'package:my_app/models/track.dart';
import 'package:flutter/material.dart' show StatelessWidget, Widget;
```

## Barrel files

Export related libraries from a single entry:

```dart
// models.dart
export 'track.dart';
export 'album.dart';
```

This keeps import lines short in large apps like the Spotify-style project in Part 14.


<!-- enriched:v3 -->

## Scenario

Melody Hub imports grew noisy when every screen imported five model files.

## Deep dive

Barrel files expose module surfaces; use `show`/`hide` to resolve symbol collisions.

## Extended example

```dart
export 'models/track.dart';
export 'models/album.dart';
```

## Engineering note

Dependency direction flows inward: UI → domain → utils.

## Try it

- Split god file into feature modules.
- Fix a circular import.

## Summary

Structure `lib/` by feature or layer and use barrel exports for public module surfaces.
