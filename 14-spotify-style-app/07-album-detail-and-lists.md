---
title: Album Detail and Album Lists
order: 7
---

# Album Detail and Album Lists

**Album detail** is the template for media pages: collapsing **`SliverAppBar`**, hero artwork, metadata **`Row`**, play/shuffle **`FilledButton`**, and a **`SliverList`** of tracks. **Album lists** appear on home (grid), search (horizontal), and library (vertical **`ListView`**).

## Album list screen (library tab section)

A dedicated “All albums” route or library section:

```dart
class AlbumListScreen extends StatelessWidget {
  const AlbumListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final albums = context.watch<CatalogRepository>().albums;

    return LayoutBuilder(
      builder: (context, constraints) {
        final cross = constraints.maxWidth > 700 ? 3 : 2;
        return GridView.builder(
          padding: const EdgeInsets.all(16),
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: cross,
            crossAxisSpacing: 12,
            mainAxisSpacing: 12,
            childAspectRatio: 0.75,
          ),
          itemCount: albums.length,
          itemBuilder: (context, index) {
            final album = albums[index];
            return AlbumCard(
              album: album,
              showTitleBelow: true,
              onTap: () => context.push('/album/${album.id}'),
            );
          },
        );
      },
    );
  }
}
```

**`LayoutBuilder`** adjusts column count from **constraints**, not screen type alone (Part 8).

## Album detail — CustomScrollView + SliverAppBar

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:go_router/go_router.dart';

import '../../data/repositories/audio_repository.dart';
import '../../data/repositories/catalog_repository.dart';
import '../../shared/widgets/track_list_tile.dart';

class AlbumDetailScreen extends StatelessWidget {
  const AlbumDetailScreen({super.key, required this.albumId});

  final String albumId;

  @override
  Widget build(BuildContext context) {
    final catalog = context.read<CatalogRepository>();
    final album = catalog.albumById(albumId);
    if (album == null) {
      return const Scaffold(body: Center(child: Text('Album not found')));
    }
    final tracks = catalog.tracksForAlbum(albumId);
    final theme = Theme.of(context);

    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            expandedHeight: 280,
            pinned: true,
            flexibleSpace: FlexibleSpaceBar(
              title: Text(album.title),
              background: Stack(
                fit: StackFit.expand,
                children: [
                  Image.network(album.coverUrl, fit: BoxFit.cover),
                  DecoratedBox(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [Colors.transparent, theme.scaffoldBackgroundColor],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(album.artist, style: theme.textTheme.titleMedium),
                  Text('${album.year} · ${tracks.length} songs', style: theme.textTheme.bodySmall),
                  const SizedBox(height: 16),
                  Row(
                    children: [
                      FilledButton.icon(
                        onPressed: () {
                          context.read<AudioRepository>().playTracks(tracks, startIndex: 0);
                        },
                        icon: const Icon(Icons.play_arrow),
                        label: const Text('Play'),
                      ),
                      const SizedBox(width: 12),
                      OutlinedButton.icon(
                        onPressed: () {
                          final shuffled = List.of(tracks)..shuffle();
                          context.read<AudioRepository>().playTracks(shuffled);
                        },
                        icon: const Icon(Icons.shuffle),
                        label: const Text('Shuffle'),
                      ),
                      const Spacer(),
                      IconButton(
                        icon: const Icon(Icons.favorite_border),
                        onPressed: () {},
                      ),
                      IconButton(
                        icon: const Icon(Icons.more_horiz),
                        onPressed: () => _albumMenu(context, album.title),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
          SliverList.builder(
            itemCount: tracks.length,
            itemBuilder: (context, index) {
              final track = tracks[index];
              return TrackListTile(
                track: track,
                index: index,
                onTap: () {
                  context.read<AudioRepository>().playTracks(tracks, startIndex: index);
                },
                trailing: IconButton(
                  icon: const Icon(Icons.more_vert),
                  onPressed: () => _trackMenu(context, track),
                ),
              );
            },
          ),
          const SliverPadding(padding: EdgeInsets.only(bottom: 120)),
        ],
      ),
    );
  }

  static void _albumMenu(BuildContext context, String title) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (context) => Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          ListTile(
            leading: const Icon(Icons.playlist_add),
            title: Text('Add $title to playlist'),
            onTap: () => Navigator.pop(context),
          ),
          ListTile(
            leading: const Icon(Icons.download_outlined),
            title: const Text('Download'),
            onTap: () => Navigator.pop(context),
          ),
        ],
      ),
    );
  }

  static void _trackMenu(BuildContext context, track) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (context) => Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          ListTile(
            leading: const Icon(Icons.queue_music),
            title: const Text('Add to queue'),
            onTap: () => Navigator.pop(context),
          ),
          ListTile(
            leading: const Icon(Icons.person),
            title: Text('Go to ${track.artist}'),
            onTap: () => Navigator.pop(context),
          ),
        ],
      ),
    );
  }
}
```

### Widget breakdown

| Section | Layout / controls |
|---------|-------------------|
| Header | `SliverAppBar` + `FlexibleSpaceBar` + `Stack` image/gradient |
| Meta | `Column` + `Text` |
| Actions | `Row` + `FilledButton` + `OutlinedButton` + `Spacer` + `IconButton` |
| Tracks | `SliverList.builder` + `TrackListTile` |

## List-style album catalog (alternative)

For “Albums” sorted A–Z, use **`ListView.separated`** with leading art:

```dart
ListView.separated(
  itemCount: albums.length,
  separatorBuilder: (_, __) => const Divider(height: 1, indent: 72),
  itemBuilder: (context, index) {
    final album = albums[index];
    return ListTile(
      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      leading: ClipRRect(
        borderRadius: BorderRadius.circular(4),
        child: Image.network(album.coverUrl, width: 56, height: 56, fit: BoxFit.cover),
      ),
      title: Text(album.title),
      subtitle: Text('${album.artist} · ${album.year}'),
      trailing: const Icon(Icons.chevron_right),
      onTap: () => context.push('/album/${album.id}'),
    );
  },
)
```

## Wide layout: master–detail (desktop)

```dart
LayoutBuilder(
  builder: (context, constraints) {
    if (constraints.maxWidth < 900) {
      return AlbumDetailScreen(albumId: albumId);
    }
    return Row(
      children: [
        SizedBox(width: 320, child: AlbumListScreen(selectedId: albumId)),
        const VerticalDivider(width: 1),
        Expanded(child: AlbumDetailScreen(albumId: albumId)),
      ],
    );
  },
)
```

**`Row` + `SizedBox` + `Expanded`** implements a Spotify-like split view on desktop.

## Summary

Album **lists** use **`GridView`** or **`ListView`** + **`ListTile`**. **Detail** pages combine **`SliverAppBar`**, action **`Row`**, and **`SliverList`** of tracks wired to **`playTracks`**. Use **`Stack`** in the flexible space bar for art + gradient legibility.
