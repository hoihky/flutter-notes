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

## Summary

Pick a routing strategy early in multi-screen apps; sidebars and tabs compose with nested navigators.
