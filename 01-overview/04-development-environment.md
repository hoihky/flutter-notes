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


<!-- enriched:v3 -->

## Scenario

HarborCart contributors use mixed hosts; CI builds Linux desktop artifacts while designers preview iOS simulators. Environment drift caused 'works on my machine' layout failures.

## Deep dive

Pin Flutter SDK versions, enable only required platforms, and treat `flutter doctor` as a pre-flight checklist—not a suggestion. Pair editor plugins with command-line `dart format` and `dart analyze` in pre-commit hooks.

## Extended example

```bash
# .tool-versions or CI image pin example
flutter --version
dart analyze lib/
dart format --output=none --set-exit-if-changed lib/
flutter test
```

## Engineering note

Add a `Makefile` or `melos` script so onboarding runs identical commands everywhere.

## Try it

- Fix every `flutter doctor` issue on your machine.
- Run the app on one mobile and one desktop target in the same session.

## Summary

Run `flutter doctor` until all critical checks pass, pick an editor, and verify hot reload on at least one mobile and one desktop target if you plan multi-platform apps later in this book.
