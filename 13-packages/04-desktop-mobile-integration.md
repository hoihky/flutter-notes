---
title: Desktop and Mobile Integration
order: 4
---

# Desktop and Mobile Integration

Packages like **window_manager** (desktop window chrome), **url_launcher**, and **package_info_plus** fill platform gaps.

Use **flutter_acrylic** or native title bars thoughtfully on desktop; respect mobile safe areas with `SafeArea`.


<!-- enriched:v3 -->

## Scenario

HarborCart desktop window needed minimum size and title bar tweaks.

## Deep dive

Use platform plugins judiciously; guard with `Platform.isWindows` etc.

## Extended example

```dart
import 'dart:io' show Platform;
bool get isDesktop => Platform.isWindows || Platform.isMacOS || Platform.isLinux;
```

## Refined UI note

SafeArea + NavigationRail spacing differs on desktop—retest after window resize.

## Try it

- Document supported platforms per plugin.
- Add menu bar shortcut stub.

## Summary

Read pub.dev platform tabs before committing to a dependency in a multi-platform roadmap.
