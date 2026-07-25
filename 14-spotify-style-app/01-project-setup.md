---
title: Project Setup
order: 1
---

# Project Setup

This capstone builds **Melody Hub** — a multi-platform music client with a Spotify-like information architecture:

| Area | Features |
|------|----------|
| **Home** | Greeting, recently played, made-for-you playlists, album rows |
| **Search** | Query field, genre browse grid, live results |
| **Library** | Playlists, liked songs, album collection |
| **Album** | Hero art, metadata, track list, play/shuffle |
| **Playlist** | Cover, description, reorderable or static track list |
| **Player** | Mini bar + full-screen now playing + queue |

You will combine **layout** widgets (`Row`, `Column`, `Stack`, `Expanded`, `CustomScrollView`, `LayoutBuilder`) and **UI** widgets (`NavigationBar`, `ListTile`, `TextField`, `SliverAppBar`, dialogs, sheets) from Parts 7–10.

## Create the project

```bash
flutter create melody_hub --platforms=android,ios,windows,macos,linux,web
cd melody_hub
```

## Dependencies (`pubspec.yaml`)

```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.1.2
  go_router: ^14.2.0
  just_audio: ^0.9.40
  cached_network_image: ^3.4.1
  collection: ^1.18.0

flutter:
  uses-material-design: true
  assets:
    - assets/mock/
```

Run `flutter pub get`. For this tutorial, **mock JSON** in `assets/mock/catalog.json` avoids network setup; swap `CatalogRepository` for an API later.

## Folder structure (feature-first)

```
lib/
├── main.dart
├── app.dart
├── router.dart
├── theme/
│   └── app_theme.dart
├── data/
│   ├── models/
│   │   ├── track.dart
│   │   ├── album.dart
│   │   └── playlist.dart
│   └── repositories/
│       ├── catalog_repository.dart
│       └── audio_repository.dart
├── features/
│   ├── shell/
│   │   ├── app_shell.dart
│   │   ├── mini_player_bar.dart
│   │   └── side_nav_rail.dart
│   ├── home/
│   │   └── home_screen.dart
│   ├── search/
│   │   └── search_screen.dart
│   ├── library/
│   │   └── library_screen.dart
│   ├── album/
│   │   └── album_detail_screen.dart
│   ├── playlist/
│   │   └── playlist_detail_screen.dart
│   └── player/
│       └── now_playing_screen.dart
└── shared/
    └── widgets/
        ├── album_card.dart
        ├── playlist_card.dart
        ├── section_header.dart
        └── track_list_tile.dart
```

## Entry point (`main.dart`)

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'app.dart';
import 'data/repositories/audio_repository.dart';
import 'data/repositories/catalog_repository.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final catalog = CatalogRepository();
  await catalog.load();
  final audio = AudioRepository();
  runApp(
    MultiProvider(
      providers: [
        Provider.value(value: catalog),
        ChangeNotifierProvider(create: (_) => audio..init()),
      ],
      child: const MelodyHubApp(),
    ),
  );
}
```

## App widget and theme (`app.dart`)

```dart
import 'package:flutter/material.dart';
import 'router.dart';
import 'theme/app_theme.dart';

class MelodyHubApp extends StatelessWidget {
  const MelodyHubApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Melody Hub',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.dark,
      routerConfig: appRouter,
    );
  }
}
```

Dark theme matches streaming apps and makes album art pop:

```dart
// theme/app_theme.dart
class AppTheme {
  static ThemeData get dark {
    const seed = Color(0xFF1DB954); // accent reminiscent of streaming apps
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      colorScheme: ColorScheme.fromSeed(seedColor: seed, brightness: Brightness.dark),
      navigationBarTheme: const NavigationBarThemeData(
        height: 64,
        labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
      ),
    );
  }
}
```

## Routing (`router.dart`)

Use **`StatefulShellRoute`** so each tab keeps its own navigation stack while the **mini player** stays outside the shell (mounted in `AppShell`).

```dart
import 'package:go_router/go_router.dart';

import 'features/album/album_detail_screen.dart';
import 'features/home/home_screen.dart';
import 'features/library/library_screen.dart';
import 'features/playlist/playlist_detail_screen.dart';
import 'features/player/now_playing_screen.dart';
import 'features/search/search_screen.dart';
import 'features/shell/app_shell.dart';

final _rootNavigatorKey = GlobalKey<NavigatorState>();

final appRouter = GoRouter(
  navigatorKey: _rootNavigatorKey,
  initialLocation: '/home',
  routes: [
    StatefulShellRoute.indexedStack(
      builder: (context, state, navigationShell) {
        return AppShell(navigationShell: navigationShell);
      },
      branches: [
        StatefulShellBranch(
          routes: [
            GoRoute(path: '/home', builder: (_, __) => const HomeScreen()),
          ],
        ),
        StatefulShellBranch(
          routes: [
            GoRoute(path: '/search', builder: (_, __) => const SearchScreen()),
          ],
        ),
        StatefulShellBranch(
          routes: [
            GoRoute(path: '/library', builder: (_, __) => const LibraryScreen()),
          ],
        ),
      ],
    ),
    GoRoute(
      parentNavigatorKey: _rootNavigatorKey,
      path: '/album/:id',
      builder: (context, state) => AlbumDetailScreen(albumId: state.pathParameters['id']!),
    ),
    GoRoute(
      parentNavigatorKey: _rootNavigatorKey,
      path: '/playlist/:id',
      builder: (context, state) => PlaylistDetailScreen(playlistId: state.pathParameters['id']!),
    ),
    GoRoute(
      parentNavigatorKey: _rootNavigatorKey,
      path: '/now-playing',
      builder: (_, __) => const NowPlayingScreen(),
    ),
  ],
);
```

Album and playlist routes use **`parentNavigatorKey: _rootNavigatorKey`** so they cover the full window (including over the tab bar) — same as opening a detail screen in production apps.

## Mock catalog asset (sketch)

`assets/mock/catalog.json`:

```json
{
  "albums": [
    {
      "id": "a1",
      "title": "Midnight Drive",
      "artist": "Nova Lane",
      "year": 2024,
      "coverUrl": "https://picsum.photos/seed/a1/400",
      "trackIds": ["t1", "t2", "t3"]
    }
  ],
  "tracks": [
    {
      "id": "t1",
      "title": "Neon Skyline",
      "artist": "Nova Lane",
      "albumId": "a1",
      "durationMs": 214000,
      "artUrl": "https://picsum.photos/seed/t1/200"
    }
  ],
  "playlists": [
    {
      "id": "p1",
      "title": "Deep Focus",
      "description": "Instrumental beats",
      "coverUrl": "https://picsum.photos/seed/p1/400",
      "trackIds": ["t1", "t2"]
    }
  ]
}
```

## What you will build next

1. **Models and repositories** — parse JSON, expose search and lookup APIs.
2. **Shell** — `NavigationRail` / `NavigationBar`, `Column` + `Expanded` + persistent **mini player**.
3. **Screens** — each chapter wires specific layout and UI controls into a complete flow.

## Summary

Melody Hub uses **feature folders**, **Provider** for audio state, **go_router** for tabs and full-screen details, and a **dark Material 3** theme. Detail routes sit on the root navigator so album and playlist pages feel modal and full-bleed.
