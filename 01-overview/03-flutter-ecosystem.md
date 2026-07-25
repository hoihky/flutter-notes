---
title: The Flutter Ecosystem
order: 3
---

# The Flutter Ecosystem

Building production apps requires more than widgets. The Flutter ecosystem includes package management, CI/CD, design resources, and community libraries on [pub.dev](https://pub.dev).

## pub.dev and Pub

**Pub** is Dart's package manager. Dependencies are declared in `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.2.0
```

Run `flutter pub get` after editing the file. Version constraints use semantic versioning; caret syntax (`^1.2.0`) allows compatible updates.

## Flutter SDK channels

The `flutter` tool supports **stable**, **beta**, and **master** channels. Most teams ship on **stable**. Use `flutter upgrade` cautiously in CI; pin SDK versions for reproducible builds.

## DevTools

**Flutter DevTools** provides performance overlays, widget inspectors, memory views, and network logging. Launch from your IDE or with `dart devtools` while an app is running in debug mode.

## Federated plugins

Plugins split implementation across platforms (Android, iOS, web, desktop). When you add a package, check which platforms it supports and whether it is **FFI**- or **method-channel**-based.

## Learning resources

- Official docs: [docs.flutter.dev](https://docs.flutter.dev)
- API reference: [api.flutter.dev](https://api.flutter.dev)
- Sample apps in the Flutter GitHub repository

## Summary

The ecosystem centers on Pub for packages, the Flutter CLI for builds, and DevTools for debugging. Choosing well-maintained packages saves weeks of platform-specific work.
