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

## Summary

Structure `lib/` by feature or layer and use barrel exports for public module surfaces.
