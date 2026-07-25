---
title: What Is Flutter?
order: 1
---

# What Is Flutter?

Flutter is Google's UI toolkit for building natively compiled applications for mobile, web, desktop, and embedded devices from a single codebase. Unlike frameworks that wrap native widgets, Flutter draws every pixel using its own rendering engine (**Impeller** on iOS and **Skia** elsewhere), which gives you consistent visuals and fine-grained control across platforms.

## Why teams choose Flutter

- **Single codebase** — One Dart project targets Android, iOS, web, Windows, macOS, and Linux.
- **Fast iteration** — Hot reload updates UI in seconds without losing application state.
- **Expressive UI** — Composable widgets, rich animations, and Material/Cupertino design languages.
- **Strong tooling** — `flutter` CLI, DevTools, and IDE plugins for VS Code and Android Studio.

## How Flutter compares to alternatives

| Approach | UI rendering | Typical language |
|----------|--------------|------------------|
| Flutter | Custom engine + widgets | Dart |
| React Native | Native components via bridge | JavaScript/TypeScript |
| Native (Swift/Kotlin) | Platform widgets | Swift / Kotlin |

Flutter trades some platform-native look-and-feel defaults for consistency and speed of development. You can still integrate platform code through **platform channels** when you need sensors, billing, or OS-specific APIs.

## The Dart connection

Flutter applications are written in **Dart**. Dart is optimized for client development: sound null safety, async/await, JIT compilation during development, and AOT compilation for release builds. You do not need to master every Dart feature before writing your first screen, but solid Dart fundamentals make Flutter code easier to reason about.

## Your first mental model

Think of a Flutter app as a tree of **widgets**. Widgets describe configuration; the framework reconciles changes efficiently. State changes trigger rebuilds of affected subtrees. Later parts of this book unpack widgets, layout, and state management in depth.

```dart
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Hello Flutter')),
        body: const Center(child: Text('Welcome')),
      ),
    );
  }
}
```

## Summary

Flutter is a cross-platform UI framework powered by Dart and a high-performance renderer. Understanding that apps are widget trees sets the stage for everything that follows in this book.
