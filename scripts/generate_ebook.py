#!/usr/bin/env python3
"""Generate Flutter ebook markdown under the repo root."""
from __future__ import annotations

import os
from textwrap import dedent

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write_rel(path: str, content: str) -> None:
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(dedent(content).lstrip("\n"))


PARTS: list[tuple[str, str, int, list[tuple[str, str, int, str]]]] = [
    (
        "01-overview",
        "Part 1 — Flutter, Dart & Ecosystem",
        1,
        [
            (
                "01-what-is-flutter.md",
                "What Is Flutter?",
                1,
                """
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
                """,
            ),
            (
                "02-dart-language-overview.md",
                "Dart Language Overview",
                2,
                """
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

                ## Summary

                Dart is Flutter's programming language: strongly typed, null-safe, and async-friendly. Flutter projects organize Dart code under `lib/` and manage packages through `pubspec.yaml`.
                """,
            ),
            (
                "03-flutter-ecosystem.md",
                "The Flutter Ecosystem",
                3,
                """
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
                """,
            ),
            (
                "04-development-environment.md",
                "Setting Up Your Environment",
                4,
                """
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
                """,
            ),
        ],
    ),
    (
        "02-dart-basics",
        "Part 2 — Dart Basics",
        2,
        [
            (
                "01-variables-and-types.md",
                "Variables and Types",
                1,
                """
                Dart variables hold references to objects. Type annotations help the analyzer catch mistakes before you run the app.

                ## Declaring variables

                ```dart
                int count = 0;
                final String title = 'Playlist';
                const double pi = 3.14159;
                var dynamicLater = 'inferred as String';
                ```

                - **`final`** — Set once at runtime.
                - **`const`** — Compile-time constant; deeply immutable.
                - **`var`** — Type inferred from the initializer.

                ## Built-in types

                | Type | Example |
                |------|---------|
                | `int` | `42` |
                | `double` | `3.14` |
                | `String` | `'hello'` |
                | `bool` | `true` |
                | `List<T>` | `[1, 2, 3]` |
                | `Map<K, V>` | `{'a': 1}` |

                ## Null safety

                Non-nullable types cannot hold `null` unless you opt in with `?`:

                ```dart
                String? nickname;
                String display = nickname ?? 'Guest';
                ```

                The null-aware operators `?.`, `??`, and `??=` reduce boilerplate when handling optional values—common in JSON APIs and UI forms.

                ## Summary

                Prefer `final` for locals that are assigned once. Use explicit types on public APIs; `var` is fine when the initializer makes the type obvious.
                """,
            ),
            (
                "02-control-flow.md",
                "Control Flow",
                2,
                """
                Control flow structures in Dart mirror C-style languages with a few ergonomic additions.

                ## Conditionals and loops

                ```dart
                if (score >= 90) {
                  print('A');
                } else if (score >= 80) {
                  print('B');
                }

                for (var i = 0; i < 3; i++) {
                  print(i);
                }

                for (final item in items) {
                  print(item);
                }

                while (condition) {
                  // ...
                }
                ```

                ## Switch expressions

                Dart 3 supports expressive `switch` on patterns:

                ```dart
                String label(Status s) => switch (s) {
                  Status.playing => 'Now playing',
                  Status.paused => 'Paused',
                  Status.stopped => 'Stopped',
                };
                ```

                ## Collections in conditions

                Use `is` and `as` for type checks and casts. Prefer pattern matching over unchecked casts when possible.

                ## Summary

                Master `for-in` loops and modern `switch` expressions—they appear frequently in UI code that maps enums to labels and icons.
                """,
            ),
            (
                "03-functions.md",
                "Functions",
                3,
                """
                Functions are first-class values in Dart. Flutter code uses them for callbacks, builders, and event handlers.

                ## Syntax

                ```dart
                int add(int a, int b) => a + b;

                void greet(String name, {String greeting = 'Hello'}) {
                  print('$greeting, $name');
                }
                ```

                ## Named and optional parameters

                Flutter widgets rely heavily on **named parameters** in constructors:

                ```dart
                Text('Title', style: TextStyle(fontSize: 18));
                ```

                Use `{}` for named parameters and `[]` for optional positional parameters. Mark named parameters `required` when they must be supplied.

                ## Closures

                ```dart
                final numbers = [1, 2, 3];
                final doubled = numbers.map((n) => n * 2).toList();
                ```

                Closures capture variables from enclosing scopes—useful for listeners, but watch for memory leaks if you forget to cancel subscriptions.

                ## Summary

                Read widget constructors as function calls with many named parameters. Arrow syntax keeps simple functions concise.
                """,
            ),
            (
                "04-collections.md",
                "Collections",
                4,
                """
                Lists, sets, and maps model in-memory data before you persist or send it over the network.

                ## Lists

                ```dart
                final tracks = <String>['Intro', 'Verse', 'Chorus'];
                tracks.add('Outro');
                final first = tracks.first;
                ```

                ## Maps

                ```dart
                final durations = <String, int>{
                  'Intro': 30,
                  'Verse': 45,
                };
                durations['Chorus'] = 60;
                ```

                ## Spread and collection-if

                ```dart
                final adminMenu = [
                  'Home',
                  if (isAdmin) 'Settings',
                  ...extraItems,
                ];
                ```

                These literals simplify building dynamic widget child lists.

                ## Immutability

                Prefer unmodifiable views or copy-on-write patterns when exposing data from state classes so widgets do not mutate shared lists accidentally.

                ## Summary

                Collection literals and spread operators are everyday tools in Flutter build methods.
                """,
            ),
            (
                "05-classes-and-objects.md",
                "Classes and Objects",
                5,
                """
                Dart classes encapsulate state and behavior. Flutter widgets are classes; so are your domain models.

                ## Defining a class

                ```dart
                class Track {
                  Track({required this.id, required this.title, this.duration});

                  final String id;
                  final String title;
                  final Duration? duration;
                }
                ```

                ## Constructors

                Use initializing formals (`this.field`) and named constructors for clarity:

                ```dart
                class Track {
                  Track.playlistEntry(this.title) : id = 'generated';
                  final String id;
                  final String title;
                }
                ```

                ## Equality

                For value objects, override `==` and `hashCode` or use packages like `equatable` (covered later). Identical widget configuration depends on stable equality for keys and lists.

                ## Summary

                Model your app domain with small immutable classes. Widgets wrap these models and reflect their data in the UI.
                """,
            ),
        ],
    ),
    (
        "03-dart-advanced",
        "Part 3 — Advanced Dart",
        3,
        [
            (
                "01-generics.md",
                "Generics",
                1,
                """
                Generics let you write type-safe code that works across multiple types.

                ```dart
                class Box<T> {
                  Box(this.value);
                  final T value;
                }

                T? first<T>(List<T> items) => items.isEmpty ? null : items.first;
                ```

                Flutter APIs use generics extensively: `ListView.builder`, `FutureBuilder<T>`, `StreamBuilder<T>`, and `ValueNotifier<T>`.

                ## Constraints

                ```dart
                class Repository<T extends Identifiable> { ... }
                ```

                Constraints document expectations and enable safer APIs.

                ## Summary

                When you see angle brackets in Flutter docs, you are looking at generic types—specify the type argument for clearer analyzer support.
                """,
            ),
            (
                "02-null-safety-deep-dive.md",
                "Null Safety Deep Dive",
                2,
                """
                Sound null safety eliminates a large class of runtime crashes by tracking nullability in the type system.

                ## Promotion

                The analyzer promotes types after null checks:

                ```dart
                void printLength(String? text) {
                  if (text == null) return;
                  print(text.length); // text is String here
                }
                ```

                ## Late variables

                `late` defers initialization when you know a field will be set before use—common in `State` objects:

                ```dart
                late final AnimationController _controller;

                @override
                void initState() {
                  super.initState();
                  _controller = AnimationController(vsync: this);
                }
                ```

                Misusing `late` causes runtime errors; prefer constructor initialization when possible.

                ## Summary

                Treat `?` as documentation of optional data. Combine `??`, `?.`, and promotion to keep UI code readable.
                """,
            ),
            (
                "03-mixins-and-extensions.md",
                "Mixins and Extensions",
                3,
                """
                Mixins share behavior across classes without full inheritance. Extensions add methods to existing types.

                ## Mixins

                ```dart
                mixin PlaybackLogging {
                  void logPlay(String track) => print('Playing $track');
                }

                class Player with PlaybackLogging {}
                ```

                Flutter's `State` class uses mixins like `TickerProviderStateMixin` for animations.

                ## Extensions

                ```dart
                extension DurationFormat on Duration {
                  String get mmss {
                    final m = inMinutes.remainder(60).toString().padLeft(2, '0');
                    final s = inSeconds.remainder(60).toString().padLeft(2, '0');
                    return '$m:$s';
                  }
                }
                ```

                Extensions keep UI formatting out of domain models.

                ## Summary

                Reach for extensions for small conveniences; use mixins when multiple classes need shared implementation.
                """,
            ),
            (
                "04-exceptions-and-errors.md",
                "Exceptions and Errors",
                4,
                """
                Dart distinguishes **Exceptions** (intended to be caught) from **Errors** (programming mistakes).

                ```dart
                Future<void> loadCatalog() async {
                  try {
                    await api.fetchTracks();
                  } on SocketException catch (e) {
                    // network unavailable
                  } catch (e, st) {
                    // log st stack trace
                    rethrow;
                  } finally {
                    // cleanup
                  }
                }
                ```

                In Flutter UI, surface failures with `SnackBar`, error widgets, or dedicated error screens—never silently swallow exceptions in `build`.

                ## Summary

                Catch exceptions at boundaries (repositories, isolates). Let the analyzer and tests guard against logic errors.
                """,
            ),
            (
                "05-libraries-and-exports.md",
                "Libraries and Exports",
                5,
                """
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
                """,
            ),
        ],
    ),
    (
        "04-dart-concurrency",
        "Part 4 — Dart Concurrency",
        4,
        [
            (
                "01-event-loop.md",
                "The Dart Event Loop",
                1,
                """
                Dart runs code on a single thread per isolate, scheduling asynchronous work on an event loop.

                ## Microtasks vs events

                - **Microtask queue** — Runs before the next event; used by `Future` completions and `scheduleMicrotask`.
                - **Event queue** — I/O, timers, and user input.

                Long synchronous work blocks UI frames. Keep `build` methods fast; offload heavy CPU work to isolates.

                ## Summary

                Understanding the event loop explains why `await` yields control and why blocking the isolate janks animations.
                """,
            ),
            (
                "02-async-await-futures.md",
                "async, await, and Futures",
                2,
                """
                `Future<T>` represents a value available later. `async`/`await` flatten nested callbacks.

                ```dart
                Future<List<Track>> loadTracks() async {
                  final response = await http.get(uri);
                  return parseTracks(response.body);
                }
                ```

                ## Combining futures

                ```dart
                final results = await Future.wait([loadUser(), loadPlaylists()]);
                ```

                ## Error handling

                Unhandled async errors may reach `FlutterError.onError` or `runZonedGuarded`. Always handle errors in UI-facing loaders.

                ## Summary

                Repositories return `Future` or `Stream` objects; widgets listen and rebuild when data arrives.
                """,
            ),
            (
                "03-streams.md",
                "Streams",
                3,
                """
                `Stream<T>` emits multiple asynchronous events—ideal for playback position, download progress, or WebSocket feeds.

                ```dart
                Stream<int> countdown(int from) async* {
                  for (var i = from; i >= 0; i--) {
                    await Future.delayed(const Duration(seconds: 1));
                    yield i;
                  }
                }
                ```

                Use `StreamBuilder` in Flutter to rebuild when new events arrive. Remember to cancel subscriptions in `dispose`.

                ## Summary

                Streams model ongoing events; pair them with controllers in state management solutions.
                """,
            ),
            (
                "04-isolates.md",
                "Isolates",
                4,
                """
                Isolates are independent workers with separate memory. Communicate via message passing—no shared mutable state.

                ```dart
                final result = await compute(parseLargeJson, rawBytes);
                ```

                `compute` spawns a short-lived isolate for CPU-heavy work like JSON parsing or image decoding.

                For long-running workers, use `Isolate.spawn` and ports. Flutter 3+ also documents isolate groups for advanced scenarios.

                ## Summary

                Use isolates when profiling shows CPU work blocking the UI thread—not for every network call.
                """,
            ),
        ],
    ),
    (
        "05-flutter-app-lifecycle",
        "Part 5 — Flutter App & Lifecycle",
        5,
        [
            (
                "01-flutter-architecture.md",
                "Flutter Architecture",
                1,
                """
                Flutter layers stack from embedded platform views up to your widgets:

                1. **Embedder** — OS window, input, surfaces.
                2. **Engine** — Skia/Impeller, Dart runtime, compositing.
                3. **Framework** — Widgets, rendering, gestures, painting.

                Your code interacts primarily with the **framework** layer. Understanding separation helps when debugging performance or platform integration.

                ## Summary

                Widgets are Dart configuration; the engine turns them into pixels. Platform channels cross from framework to embedder.
                """,
            ),
            (
                "02-widget-tree-element-render.md",
                "Widget, Element, and Render Trees",
                2,
                """
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

                ## Summary

                Cheap widget rebuilds are normal; expensive work belongs outside `build`.
                """,
            ),
            (
                "03-app-lifecycle.md",
                "Application Lifecycle",
                3,
                """
                Mobile apps move through states: resumed, inactive, paused, detached. Listen with `WidgetsBindingObserver`:

                ```dart
                class _HomeState extends State<Home> with WidgetsBindingObserver {
                  @override
                  void initState() {
                    super.initState();
                    WidgetsBinding.instance.addObserver(this);
                  }

                  @override
                  void didChangeAppLifecycleState(AppLifecycleState state) {
                    if (state == AppLifecycleState.paused) {
                      // pause audio
                    }
                  }
                }
                ```

                Desktop and web have related visibility APIs; pause expensive work when the window is hidden.

                ## Summary

                Lifecycle hooks coordinate audio playback, sync, and resource release—critical for the music app in Part 14.
                """,
            ),
            (
                "04-navigation-overview.md",
                "Navigation Overview",
                4,
                """
                Flutter 3 recommends **Navigator 2.0** patterns or higher-level routers like `go_router` for declarative routes.

                Imperative push/pop remains common:

                ```dart
                Navigator.of(context).push(
                  MaterialPageRoute(builder: (_) => const AlbumPage()),
                );
                ```

                Named routes centralize paths for deep linking:

                ```dart
                MaterialApp(
                  routes: {
                    '/': (_) => const HomePage(),
                    '/album': (_) => const AlbumPage(),
                  },
                );
                ```

                ## Summary

                Pick a routing strategy early in multi-screen apps; sidebars and tabs compose with nested navigators.
                """,
            ),
        ],
    ),
    (
        "06-flutter-ui-framework",
        "Part 6 — Flutter UI Framework",
        6,
        [
            (
                "01-rendering-pipeline.md",
                "Rendering Pipeline",
                1,
                """
                Each frame follows **build → layout → paint → compositing**. The framework schedules frames when animation ticks, gestures resolve, or `setState` marks elements dirty.

                Enable performance overlay with `MaterialApp(showPerformanceOverlay: true)` in debug builds to spot missed frames.

                ## Summary

                Jank usually means too much work per frame—simplify `build`, cache images, or defer layout.
                """,
            ),
            (
                "02-material-cupertino.md",
                "Material and Cupertino",
                2,
                """
                **Material** widgets follow Google's design system; **Cupertino** mimics iOS. You can mix them, but consistency matters for UX.

                ```dart
                MaterialApp(
                  theme: ThemeData(colorSchemeSeed: Colors.deepPurple),
                  home: ...,
                );
                ```

                ```dart
                CupertinoApp(
                  theme: const CupertinoThemeData(brightness: Brightness.light),
                  home: ...,
                );
                ```

                ## Summary

                Choose a primary design language per platform or use adaptive constructors (`Switch.adaptive`).
                """,
            ),
            (
                "03-theming.md",
                "Theming",
                3,
                """
                `ThemeData` propagates colors, typography, and component defaults through `Theme.of(context)`.

                ```dart
                final theme = Theme.of(context);
                Text('Headline', style: theme.textTheme.headlineSmall);
                ```

                Dark mode uses `ThemeMode.system` and separate `darkTheme` on `MaterialApp`.

                ## Summary

                Centralize brand colors and text styles in theme extensions for large apps.
                """,
            ),
            (
                "04-mediaquery-and-text-scale.md",
                "MediaQuery and Accessibility",
                4,
                """
                `MediaQuery` exposes screen size, padding, orientation, and text scale factor.

                ```dart
                final width = MediaQuery.sizeOf(context).width;
                final padding = MediaQuery.paddingOf(context);
                ```

                Respect user text scaling—avoid locking font sizes unless design requires it. Test with large accessibility fonts.

                ## Summary

                Responsive layouts start with `MediaQuery` and constraints, not hard-coded pixel widths.
                """,
            ),
        ],
    ),
    (
        "07-layout-basics",
        "Part 7 — Basic Layout",
        7,
        [
            (
                "01-row-column-flex.md",
                "Row, Column, and Flex",
                1,
                """
                `Row` and `Column` extend `Flex`, arranging children along horizontal or vertical axes.

                ```dart
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Icon(Icons.play_arrow),
                    Expanded(child: Text(track.title)),
                    Text(track.durationLabel),
                  ],
                )
                ```

                - **mainAxis** — Direction of arrangement.
                - **crossAxis** — Perpendicular alignment via `crossAxisAlignment`.

                ## Summary

                Most list rows are `Row` + `Expanded` patterns; columns stack sections vertically.
                """,
            ),
            (
                "02-container-padding-margin.md",
                "Container, Padding, and Margin",
                2,
                """
                `Padding` applies inset around a child. `Container` combines padding, margins, constraints, decoration, and alignment.

                ```dart
                Container(
                  margin: const EdgeInsets.symmetric(horizontal: 16),
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.grey.shade900,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: const Text('Album art placeholder'),
                )
                ```

                Prefer `Padding` when you only need inset without decoration.

                ## Summary

                Margin is outside the box; padding is inside—mirror CSS mental models carefully.
                """,
            ),
            (
                "03-stack-positioned.md",
                "Stack and Positioned",
                3,
                """
                `Stack` overlays children. `Positioned` anchors children with explicit edges.

                ```dart
                Stack(
                  children: [
                    Image.network(coverUrl, fit: BoxFit.cover),
                    const Positioned(
                      bottom: 8,
                      right: 8,
                      child: Icon(Icons.explicit, color: Colors.white),
                    ),
                  ],
                )
                ```

                Use `Align` or `FractionallySizedBox` when relative positioning suffices.

                ## Summary

                Stacks build layered UIs—album art with gradients and playback controls.
                """,
            ),
            (
                "04-align-centered-constraints.md",
                "Align, Center, and Constraints",
                4,
                """
                Parents pass **constraints** downward; children choose sizes and report sizes upward.

                `Center` is `Align` with alignment `center`. `SizedBox` fixes dimensions; `ConstrainedBox` sets min/max bounds.

                ```dart
                ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 480),
                  child: child,
                )
                ```

                ## Summary

                When layout fails, read the yellow/black striped error—it usually states unbounded constraints.
                """,
            ),
        ],
    ),
    (
        "08-layout-advanced",
        "Part 8 — Advanced Layout",
        8,
        [
            (
                "01-expanded-flexible.md",
                "Expanded and Flexible",
                1,
                """
                Inside `Flex`, `Expanded` forces a child to share remaining space. `Flexible` allows a child to shrink but not necessarily grow.

                ```dart
                Row(
                  children: [
                    Flexible(flex: 2, child: Text(title, overflow: TextOverflow.ellipsis)),
                    Flexible(child: Text(artist)),
                  ],
                )
                ```

                ## Summary

                Without `Expanded`, `Row` children with unbounded width (like `Text`) may overflow.
                """,
            ),
            (
                "02-wrap-flow.md",
                "Wrap and Flow Layout",
                2,
                """
                `Wrap` flows children to the next line when space runs out—useful for chips and genre tags.

                ```dart
                Wrap(
                  spacing: 8,
                  children: genres.map((g) => Chip(label: Text(g))).toList(),
                )
                ```

                ## Summary

                When horizontal `Row` overflows, consider `Wrap` or horizontal `ListView`.
                """,
            ),
            (
                "03-layoutbuilder.md",
                "LayoutBuilder",
                3,
                """
                `LayoutBuilder` exposes parent constraints to choose different layouts:

                ```dart
                LayoutBuilder(
                  builder: (context, constraints) {
                    if (constraints.maxWidth > 800) {
                      return const DesktopShell();
                    }
                    return const MobileShell();
                  },
                )
                ```

                This pattern powers responsive music apps with sidebar navigation on wide screens.

                ## Summary

                Branch on `constraints`, not only `MediaQuery`, when the parent limits width (e.g., dialogs).
                """,
            ),
            (
                "04-intrinsic-sliver.md",
                "Intrinsic Dimensions and Slivers",
                4,
                """
                **Slivers** are scrollable layout segments. `CustomScrollView` combines `SliverAppBar`, `SliverList`, and `SliverGrid`.

                ```dart
                CustomScrollView(
                  slivers: [
                    const SliverAppBar(title: Text('Browse'), floating: true),
                    SliverList.builder(
                      itemCount: items.length,
                      itemBuilder: (context, index) => ListTile(title: Text(items[index])),
                    ),
                  ],
                )
                ```

                `IntrinsicHeight` and `IntrinsicWidth` are expensive—use sparingly.

                ## Summary

                Master slivers for collapsing headers and coordinated scrolling in media apps.
                """,
            ),
        ],
    ),
    (
        "09-ui-controls-basics",
        "Part 9 — Basic UI Controls",
        9,
        [
            (
                "01-text-and-images.md",
                "Text and Images",
                1,
                """
                `Text` uses `TextStyle` or theme text styles. `Image` loads assets, network URLs, or memory bytes.

                ```dart
                Image.asset('assets/album.png', width: 64, height: 64)
                Image.network(url, errorBuilder: (_, __, ___) => const Icon(Icons.broken_image))
                ```

                Declare assets in `pubspec.yaml`. Cache network images with `cached_network_image` in production apps.

                ## Summary

                Always provide error and loading builders for network media.
                """,
            ),
            (
                "02-buttons.md",
                "Buttons",
                2,
                """
                Material 3 offers `FilledButton`, `OutlinedButton`, and `TextButton`. Icon buttons handle toolbar actions.

                ```dart
                FilledButton.icon(
                  onPressed: isPlaying ? null : _play,
                  icon: const Icon(Icons.play_arrow),
                  label: const Text('Play'),
                )
                ```

                Disable buttons with `onPressed: null` for unavailable actions.

                ## Summary

                Match button prominence to action importance—one primary action per screen region.
                """,
            ),
            (
                "03-text-fields.md",
                "Text Fields",
                3,
                """
                `TextField` and `TextFormField` capture input. Use controllers or `onChanged` callbacks.

                ```dart
                TextField(
                  decoration: const InputDecoration(
                    labelText: 'Search',
                    prefixIcon: Icon(Icons.search),
                  ),
                  onSubmitted: _search,
                )
                ```

                For forms with validation, wrap fields in `Form` with a `GlobalKey<FormState>`.

                ## Summary

                Search bars in music apps debounce input before hitting APIs—implement debounce in the presenter or state layer.
                """,
            ),
            (
                "04-lists-and-grids.md",
                "Lists and Grids",
                4,
                """
                `ListView.builder` lazily builds children—essential for long catalogs.

                ```dart
                ListView.separated(
                  itemCount: tracks.length,
                  separatorBuilder: (_, __) => const Divider(height: 1),
                  itemBuilder: (context, index) => TrackTile(track: tracks[index]),
                )
                ```

                `GridView` variants mirror list constructors for album grids.

                ## Summary

                Prefer builders over `children: [...]` for large collections.
                """,
            ),
        ],
    ),
    (
        "10-ui-controls-advanced",
        "Part 10 — Advanced UI Controls",
        10,
        [
            (
                "01-scrollables-and-physics.md",
                "Scrollables and Physics",
                1,
                """
                Customize scrolling with `ScrollPhysics`:

                ```dart
                ListView(
                  physics: const BouncingScrollPhysics(),
                  children: ...,
                )
                ```

                `ScrollController` listens to offset for parallax or showing scroll-to-top buttons.

                ## Summary

                Nested scrollables require careful `PrimaryScrollController` assignment.
                """,
            ),
            (
                "02-dialogs-bottom-sheets.md",
                "Dialogs and Bottom Sheets",
                2,
                """
                ```dart
                showModalBottomSheet(
                  context: context,
                  builder: (context) => const QueueSheet(),
                );
                ```

                `AlertDialog` confirms destructive actions like removing downloads.

                ## Summary

                Sheets suit queue management and track options; dialogs suit short decisions.
                """,
            ),
            (
                "03-gestures.md",
                "Gestures",
                3,
                """
                `GestureDetector` and `InkWell` handle taps, drags, and long presses.

                ```dart
                GestureDetector(
                  onHorizontalDragEnd: (details) {
                    if (details.primaryVelocity! > 0) _skipPrevious();
                  },
                  child: artwork,
                )
                ```

                For complex arenas, study `Listener` and `RawGestureDetector`.

                ## Summary

                Use `InkWell` inside Material for splash effects; match platform gesture expectations.
                """,
            ),
            (
                "04-navigation-rail-tabs.md",
                "Tabs and NavigationRail",
                4,
                """
                `NavigationBar` suits mobile bottom navigation; `NavigationRail` suits desktop and tablet sidebars.

                ```dart
                Scaffold(
                  body: Row(
                    children: [
                      NavigationRail(
                        selectedIndex: _index,
                        onDestinationSelected: (i) => setState(() => _index = i),
                        destinations: const [
                          NavigationRailDestination(icon: Icon(Icons.home), label: Text('Home')),
                          NavigationRailDestination(icon: Icon(Icons.library_music), label: Text('Library')),
                        ],
                      ),
                      const VerticalDivider(width: 1),
                      Expanded(child: _pages[_index]),
                    ],
                  ),
                )
                ```

                ## Summary

                Adaptive navigation is a hallmark of polished multi-platform Flutter apps.
                """,
            ),
        ],
    ),
    (
        "11-state-management",
        "Part 11 — State Management",
        11,
        [
            (
                "01-local-state-setstate.md",
                "Local State with setState",
                1,
                """
                `StatefulWidget` pairs immutable configuration with mutable `State`:

                ```dart
                class PlayPause extends StatefulWidget {
                  const PlayPause({super.key});
                  @override
                  State<PlayPause> createState() => _PlayPauseState();
                }

                class _PlayPauseState extends State<PlayPause> {
                  bool playing = false;
                  void _toggle() => setState(() => playing = !playing);

                  @override
                  Widget build(BuildContext context) {
                    return IconButton(
                      icon: Icon(playing ? Icons.pause : Icons.play_arrow),
                      onPressed: _toggle,
                    );
                  }
                }
                ```

                ## Summary

                `setState` is perfect for ephemeral UI state isolated to one widget.
                """,
            ),
            (
                "02-inherited-notifier.md",
                "InheritedWidget and Notifiers",
                2,
                """
                `InheritedWidget` efficiently notifies dependents when shared data changes. `ValueNotifier` + `ValueListenableBuilder` offer a lighter pattern:

                ```dart
                ValueListenableBuilder(
                  valueListenable: positionNotifier,
                  builder: (context, position, _) => Slider(value: position, onChanged: _seek),
                )
                ```

                ## Summary

                Lift state up when multiple widgets need the same data.
                """,
            ),
            (
                "03-provider-pattern.md",
                "Provider Pattern",
                3,
                """
                The **provider** package wraps `InheritedWidget` for ergonomics:

                ```dart
                ChangeNotifierProvider(
                  create: (_) => PlayerController()..init(),
                  child: const AppShell(),
                );
                ```

                ```dart
                context.watch<PlayerController>().toggle();
                ```

                Separate `read` (no rebuild) from `watch` (rebuild on notify).

                ## Summary

                Provider scales to medium apps before you need heavier architectures.
                """,
            ),
            (
                "04-riverpod-and-bloc.md",
                "Riverpod and BLoC Overview",
                4,
                """
                **Riverpod** improves testability with compile-safe providers. **BLoC** separates events and states for predictable flows.

                ```dart
                // Simplified BLoC idea
                // on<Event> => emit<State>
                ```

                Choose based on team familiarity. Large apps often combine repository layers with any of these libraries.

                ## Summary

                State management is about boundaries: UI reacts to immutable view models; services own async work.
                """,
            ),
        ],
    ),
    (
        "12-custom-ui",
        "Part 12 — Custom Look & Feel",
        12,
        [
            (
                "01-decorations-and-themes.md",
                "Decorations and Theme Extensions",
                1,
                """
                `BoxDecoration`, gradients, and shadows shape cards and tiles.

                ```dart
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [Colors.purple.shade800, Colors.black],
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                  ),
                )
                ```

                `ThemeExtension` adds custom tokens accessible via `Theme.of(context).extension<MyColors>()`.

                ## Summary

                Encode brand tokens once; avoid scattering hex colors across widgets.
                """,
            ),
            (
                "02-custom-paint.md",
                "CustomPaint and Canvas",
                2,
                """
                `CustomPainter` draws waveforms, progress rings, and visualizers.

                ```dart
                class WavePainter extends CustomPainter {
                  @override
                  void paint(Canvas canvas, Size size) {
                    final paint = Paint()..color = Colors.greenAccent;
                    canvas.drawLine(Offset.zero, Offset(size.width, size.height), paint);
                  }

                  @override
                  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
                }
                ```

                ## Summary

                Repaint only when data changes—implement `shouldRepaint` precisely.
                """,
            ),
            (
                "03-composing-custom-widgets.md",
                "Composing Custom Widgets",
                3,
                """
                Extract widgets when build methods grow:

                ```dart
                class TrackProgressBar extends StatelessWidget {
                  const TrackProgressBar({super.key, required this.position, required this.duration});
                  final Duration position;
                  final Duration duration;

                  @override
                  Widget build(BuildContext context) {
                    final value = duration.inMilliseconds == 0
                        ? 0.0
                        : position.inMilliseconds / duration.inMilliseconds;
                    return Slider(value: value.clamp(0, 1), onChanged: null);
                  }
                }
                ```

                Custom widgets can be `StatelessWidget` facades over render objects only when necessary.

                ## Summary

                Composition beats monolithic build methods—your Spotify-style UI will be a tree of small widgets.
                """,
            ),
        ],
    ),
    (
        "13-packages",
        "Part 13 — Packages for Real Apps",
        13,
        [
            (
                "01-networking.md",
                "Networking",
                1,
                """
                Use `http` for simple calls or **dio** for interceptors, timeouts, and download progress.

                ```dart
                final response = await dio.get('/v1/tracks', queryParameters: {'q': query});
                ```

                Model JSON with `json_serializable` or manual `fromJson` factories. Never block `build` with network I/O.

                ## Summary

                Keep HTTP clients in repositories; inject them for tests.
                """,
            ),
            (
                "02-persistence.md",
                "Local Persistence",
                2,
                """
                **shared_preferences** stores small flags. **hive** or **isar** handle structured offline caches. **sqflite** fits relational data on mobile.

                Desktop apps may use `path_provider` for file locations and SQLite similarly.

                ## Summary

                Cache album art and playlists for offline listening scenarios.
                """,
            ),
            (
                "03-audio-playback.md",
                "Audio and Video Packages",
                3,
                """
                **just_audio** plays streams and files with gapless support on many platforms. **audio_service** integrates background playback and media notifications.

                Verify desktop support matrices—some plugins are mobile-first.

                ## Summary

                Abstract playback behind an interface so UI code stays platform-agnostic.
                """,
            ),
            (
                "04-desktop-mobile-integration.md",
                "Desktop and Mobile Integration",
                4,
                """
                Packages like **window_manager** (desktop window chrome), **url_launcher**, and **package_info_plus** fill platform gaps.

                Use **flutter_acrylic** or native title bars thoughtfully on desktop; respect mobile safe areas with `SafeArea`.

                ## Summary

                Read pub.dev platform tabs before committing to a dependency in a multi-platform roadmap.
                """,
            ),
        ],
    ),
    (
        "14-spotify-style-app",
        "Part 14 — Spotify-Style Music App",
        14,
        [
            (
                "01-project-setup.md",
                "Project Setup",
                1,
                """
                Create the capstone app:

                ```bash
                flutter create melody_hub --platforms=android,ios,windows,macos,linux,web
                cd melody_hub
                ```

                Organize by feature:

                ```
                lib/
                ├── main.dart
                ├── app.dart
                ├── features/
                │   ├── home/
                │   ├── search/
                │   ├── library/
                │   └── player/
                └── shared/
                    ├── models/
                    └── widgets/
                ```

                Add dependencies: `provider`, `go_router`, `just_audio`, `cached_network_image`.

                ## Summary

                Structure mirrors Spotify areas: browse, search, library, and persistent player chrome.
                """,
            ),
            (
                "02-models-and-services.md",
                "Models and Services",
                2,
                """
                Define immutable models:

                ```dart
                class Track {
                  const Track({required this.id, required this.title, required this.artist, this.artUrl});
                  final String id;
                  final String title;
                  final String artist;
                  final String? artUrl;
                }
                ```

                `AudioRepository` wraps `just_audio` and exposes `Stream<Duration>` for position updates. `CatalogService` fetches mock JSON or a real API.

                ## Summary

                Keep widgets ignorant of audio plugin details—test services with fakes.
                """,
            ),
            (
                "03-shell-layout.md",
                "Responsive App Shell",
                3,
                """
                Combine `NavigationRail` + content + bottom player bar:

                ```dart
                class AppShell extends StatelessWidget {
                  const AppShell({super.key, required this.child});
                  final Widget child;

                  @override
                  Widget build(BuildContext context) {
                    final wide = MediaQuery.sizeOf(context).width >= 900;
                    return Scaffold(
                      body: Column(
                        children: [
                          Expanded(
                            child: Row(
                              children: [
                                if (wide) const SideNavRail(),
                                Expanded(child: child),
                              ],
                            ),
                          ),
                          const MiniPlayerBar(),
                        ],
                      ),
                      bottomNavigationBar: wide ? null : const MobileNavBar(),
                    );
                  }
                }
                ```

                ## Summary

                The shell stays mounted while inner routes swap—player state persists across tabs.
                """,
            ),
            (
                "04-player-ui-and-polish.md",
                "Player UI and Polish",
                4,
                """
                Build a full-screen player with draggable sheet, album art hero, shuffle/repeat toggles, and queue sheet. Animate transitions with `Hero` and `AnimatedSwitcher`.

                Persist last played track with `shared_preferences`. Handle lifecycle pause/resume from Part 5.

                ## Testing checklist

                - [ ] Resize window across mobile/desktop breakpoints
                - [ ] Keyboard shortcuts on desktop (space to play/pause)
                - [ ] Semantic labels for screen readers

                ## Summary

                You now have an end-to-end Flutter application applying Dart fundamentals, layout, state, packages, and custom UI—a foundation you can extend with real APIs and authentication.
                """,
            ),
        ],
    ),
]


def main() -> None:
    write_rel(
        "index.md",
        """
        ---
        title: Developing Flutter Applications
        order: 0
        ---

        # Developing Flutter Applications

        Welcome to this hands-on guide for building Flutter apps from first principles through a full multi-platform music player UI.

        ## How to use this book

        Parts are ordered for progressive learning:

        1. **Overview** — Flutter, Dart, and the ecosystem
        2. **Dart basics** — Language fundamentals
        3. **Advanced Dart** — Generics, null safety, libraries
        4. **Concurrency** — Async programming and isolates
        5. **App lifecycle** — Architecture and navigation
        6. **UI framework** — Material, Cupertino, theming
        7. **Basic layout** — Rows, columns, stacks
        8. **Advanced layout** — Slivers and responsive builders
        9. **Basic controls** — Text, buttons, lists
        10. **Advanced controls** — Gestures, sheets, adaptive nav
        11. **State management** — From `setState` to Provider and beyond
        12. **Custom UI** — Themes, painters, composition
        13. **Packages** — Networking, storage, audio, desktop
        14. **Capstone** — Spotify-style music app

        Code samples use Dart 3 and current Flutter Material APIs. Type along in your editor and run examples with `flutter run`.

        ## Prerequisites

        - Basic programming experience
        - Flutter SDK installed (`flutter doctor` clean)
        - A device or emulator for at least one target platform

        Start with [Part 1 — Flutter, Dart & Ecosystem](01-overview/01-what-is-flutter.md) when you are ready.
        """,
    )

    for folder, _part_title, part_order, chapters in PARTS:
        for filename, title, order, body in chapters:
            write_rel(
                f"{folder}/{filename}",
                f"""
                ---
                title: {title}
                order: {order}
                ---

                # {title}

                {body.strip()}
                """,
            )

    print(f"Wrote ebook under {ROOT}")


if __name__ == "__main__":
    main()
