---
title: Dart Language Overview
order: 2
---

# Dart Language Overview

Dart is a statically typed language with optional type inference, designed for building user interfaces and server applications. For Flutter developers, Dart is the language of widgets, business logic, and asynchronous I/O.

## Core language pillars

1. **Sound null safety** — Types distinguish nullable (`String?`) from non-nullable (`String`) values at compile time.
2. **Object-oriented model** — Everything is an object; single inheritance with mixins.
3. **Functional features** — First-class functions, closures, collection literals, and higher-order methods like `map` and `where`.
4. **Asynchronous programming** — `Future` and `Stream` with `async`/`await` syntax.

## Running Dart code

The Flutter SDK bundles a Dart SDK. You can also use the standalone `dart` command for scripts and small experiments:

```bash
dart --version
dart run bin/main.dart
```

Inside a Flutter project, `flutter pub get` resolves dependencies declared in `pubspec.yaml`.

## Project anatomy

```
my_app/
├── lib/
│   └── main.dart      # Entry point
├── test/              # Unit and widget tests
├── pubspec.yaml       # Dependencies and assets
└── android/ ios/ ...  # Platform folders
```

Application code lives in `lib/`. Platform folders contain native project files; Flutter tooling keeps them in sync when possible.

## Style and tooling

- **`dart format`** — Applies standard formatting.
- **`dart analyze`** — Static analysis via the analyzer.
- **`flutter test`** — Runs tests in the Flutter test harness.

Adopting these tools early prevents style debates and catches bugs before runtime.


<!-- enriched:v3 -->

## Scenario

LedgerAir ingests CSV exports where optional memo columns are frequently blank. The first prototype used empty strings interchangeably with `null`, breaking filters for 'missing memo'.

## Deep dive

Dart's sound nullability distinguishes unknown (`null`) from empty but present values. Combine `?`, `??`, and early returns to express business rules directly in models before widgets ever render.

## Extended example

```dart
class LedgerRow {
  const LedgerRow({required this postedOn, required this.amountCents, this.memo});
  final DateTime postedOn;
  final int amountCents;
  final String? memo;

  bool get needsReview => memo == null;

  String displayMemo() => memo ?? '— add memo —';
}

List<LedgerRow> rowsNeedingReview(Iterable<LedgerRow> rows) {
  return [for (final row in rows) if row.needsReview) row];
}
```

## Engineering note

Model optional CSV columns as nullable fields, not magic strings.

## Try it

- Write a parser that treats blank cells as `null`.
- Explain why `late` is riskier than constructor initialization for UI fields.

## Summary

Dart is Flutter's programming language: strongly typed, null-safe, and async-friendly. Flutter projects organize Dart code under `lib/` and manage packages through `pubspec.yaml`.
