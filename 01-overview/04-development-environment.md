---
title: Setting Up Your Environment
order: 4
---

# Setting Up Your Environment

A reliable development environment reduces friction when you learn layout, state, and platform integration.

## Install the Flutter SDK

1. Download the SDK for your OS from flutter.dev or use a version manager.
2. Add `flutter/bin` to your `PATH`.
3. Run `flutter doctor` and resolve reported issues (Xcode, Android SDK, licenses).

```bash
flutter doctor -v
```

## Editors

**VS Code** with the Flutter and Dart extensions is lightweight. **Android Studio** bundles the Android SDK and device emulators. Both support breakpoints, hot reload, and refactoring.

## Devices and emulators

- **Android Emulator** — Create AVDs in Android Studio Device Manager.
- **iOS Simulator** — Requires macOS and Xcode.
- **Desktop** — Enable with `flutter config --enable-windows-desktop` (or macOS/Linux equivalents).
- **Chrome** — `flutter run -d chrome` for web.

## Creating a project

```bash
flutter create hello_flutter
cd hello_flutter
flutter run
```

Use `flutter create --platforms=android,ios,windows,macos,linux,web` to limit generated platforms.

## Summary

Run `flutter doctor` until all critical checks pass, pick an editor, and verify hot reload on at least one mobile and one desktop target if you plan multi-platform apps later in this book.
