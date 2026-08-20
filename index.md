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
12. **Custom UI** — Themes, painters, composition, custom email inbox list
13. **Packages** — Networking, storage, audio, desktop
14. **Capstone** — Spotify-style music app

Code samples use Dart 3 and current Flutter Material APIs. Type along in your editor and run examples with `flutter run`.

## Prerequisites

- Basic programming experience
- Flutter SDK installed (`flutter doctor` clean)
- A device or emulator for at least one target platform

Start with [Part 1 — Flutter, Dart & Ecosystem](01-overview/01-what-is-flutter.md) when you are ready.
<!-- enriched:v3 -->

## Scenario

Your organization plans **HarborCart**, a storefront that must feel native on a phone, readable on a ultrawide monitor, and accessible with large system fonts. Designers and engineers will not succeed if layout, state, and services are learned in isolation.

## Deep dive

This manuscript stacks skills deliberately: Dart foundations, concurrency, Flutter lifecycle, layout and controls, state, packages, custom UI, then two capstones. Treat each part as a dependency for the next; skipping layout to jump into animations usually creates unmaintainable `Stack` trees.

## Extended example

```dart
class HarborCartRoot extends StatelessWidget {
  const HarborCartRoot({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(colorSchemeSeed: const Color(0xFF0D9488), useMaterial3: true),
      home: LayoutBuilder(
        builder: (context, constraints) {
          final columns = constraints.maxWidth >= 1100 ? 3 : 1;
          return Scaffold(
            body: GridView.count(
              crossAxisCount: columns,
              padding: const EdgeInsets.all(24),
              children: const [
                _StudyCard(title: 'Layout', subtitle: 'Parts 7–8'),
                _StudyCard(title: 'Controls', subtitle: 'Parts 9–10'),
                _StudyCard(title: 'Capstone', subtitle: 'Part 14'),
              ],
            ),
          );
        },
      ),
    );
  }
}

class _StudyCard extends StatelessWidget {
  const _StudyCard({required this.title, required this.subtitle});
  final String title;
  final String subtitle;

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 0,
      color: Theme.of(context).colorScheme.surfaceContainerHighest,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(title, style: Theme.of(context).textTheme.headlineSmall),
            const SizedBox(height: 8),
            Text(subtitle),
          ],
        ),
      ),
    );
  }
}
```

## Engineering note

Pick one target device class (phone or desktop) and complete Parts 1–6 before customizing visuals.

## Try it

- Map HarborCart screens to the fourteen parts.
- Define three non-negotiable UX rules (spacing, type scale, motion).

