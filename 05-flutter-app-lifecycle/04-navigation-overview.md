---
title: Navigation Overview
order: 4
---

# Navigation Overview

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


<!-- enriched:v3 -->

## Scenario

StudioBoard deep links opened wrong tabs when routes were stringly typed.

## Deep dive

Prefer declarative routers for deep links; keep imperative push for modal tasks.

## Extended example

```dart
Navigator.of(context).push(
  MaterialPageRoute(builder: (_) => const IssueDetailScreen(id: 'SB-12')),
);
```

## Refined UI note

Animate route transitions consistently—200–300ms curves feel calm.

## Try it

- Add named route map.
- Sketch nested navigator for tabs.

## Summary

Pick a routing strategy early in multi-screen apps; sidebars and tabs compose with nested navigators.
