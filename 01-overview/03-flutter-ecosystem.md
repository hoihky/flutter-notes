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


<!-- enriched:v3 -->

## Scenario

StudioBoard links design previews, issue trackers, and build badges. Teams wasted days on unmaintained plugins before adopting a short list of pub.dev packages with desktop support and recent commits.

## Deep dive

The ecosystem spans CLI tooling, analyzer lints, DevTools profilers, and federated plugins. Evaluate packages by platform matrix, changelog cadence, and whether they pull native SDK requirements you cannot satisfy in CI.

## Extended example

```dart
// lib/di/package_gate.dart
class PackageGate {
  const PackageGate({required this.name, required this.supportsDesktop});
  final String name;
  final bool supportsDesktop;
}

const studioBoardDeps = [
  PackageGate(name: 'file_selector', supportsDesktop: true),
  PackageGate(name: 'mobile_only_scanner', supportsDesktop: false),
];

bool blockedOnDesktop(Iterable<PackageGate> gates) =>
    gates.any((g) => !g.supportsDesktop);
```

## Engineering note

Document allowed package categories in CONTRIBUTING before UI work lands.

## Try it

- Run DevTools CPU profiler while scrolling a heavy list.
- Pick one dependency and justify it using pub.dev platform tabs.

## Summary

The ecosystem centers on Pub for packages, the Flutter CLI for builds, and DevTools for debugging. Choosing well-maintained packages saves weeks of platform-specific work.
