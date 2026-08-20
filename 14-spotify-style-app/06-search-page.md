---
title: Search Page
order: 6
---

# Search Page

Search has two modes:

1. **Browse** — empty query shows genre **`GridView`** and suggested categories.
2. **Results** — typing filters tracks and albums via **`CatalogRepository.search`**.

Uses **`TextField`**, debounced queries, **`ListView`**, **`ListTile`**, and **`TabBar`** or sections for Tracks vs Albums.

## Stateful search screen

```dart
import 'dart:async';

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

import '../../data/models/album.dart';
import '../../data/models/track.dart';
import '../../data/repositories/audio_repository.dart';
import '../../data/repositories/catalog_repository.dart';
import '../../shared/widgets/track_list_tile.dart';

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});

  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final _controller = TextEditingController();
  final _focusNode = FocusNode();
  Timer? _debounce;
  String _query = '';
  List<Track> _tracks = [];
  List<Album> _albums = [];

  static const _categories = [
  ('Pop', Color(0xFF8E44AD)),
  ('Jazz', Color(0xFF2980B9)),
  ('Rock', Color(0xFFC0392B)),
  ('Hip-hop', Color(0xFF27AE60)),
  ('Classical', Color(0xFF7F8C8D)),
  ('Focus', Color(0xFF16A085)),
];

  @override
  void dispose() {
    _debounce?.cancel();
    _controller.dispose();
    _focusNode.dispose();
    super.dispose();
  }

  void _onQueryChanged(String value) {
    _debounce?.cancel();
    _debounce = Timer(const Duration(milliseconds: 300), () {
      final catalog = context.read<CatalogRepository>();
      setState(() {
        _query = value;
        _tracks = catalog.search(value);
        _albums = catalog.searchAlbums(value);
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    final searching = _query.trim().isNotEmpty;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
          child: TextField(
            controller: _controller,
            focusNode: _focusNode,
            decoration: InputDecoration(
              hintText: 'What do you want to listen to?',
              prefixIcon: const Icon(Icons.search),
              suffixIcon: _query.isEmpty
                  ? null
                  : IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        _controller.clear();
                        _onQueryChanged('');
                      },
                    ),
              filled: true,
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(8),
                borderSide: BorderSide.none,
              ),
            ),
            onChanged: _onQueryChanged,
            textInputAction: TextInputAction.search,
          ),
        ),
        Expanded(
          child: searching ? _SearchResults(tracks: _tracks, albums: _albums) : _BrowseGrid(categories: _categories),
        ),
      ],
    );
  }
}
```

### Layout: Column + Expanded

The **`TextField`** stays fixed at the top; **`Expanded`** gives the results/browse area bounded height for inner **`ListView`** / **`GridView`**.

## Browse grid (empty query)

```dart
class _BrowseGrid extends StatelessWidget {
  const _BrowseGrid({required this.categories});

  final List<(String, Color)> categories;

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      padding: const EdgeInsets.all(16),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        mainAxisSpacing: 12,
        crossAxisSpacing: 12,
        childAspectRatio: 1.6,
      ),
      itemCount: categories.length,
      itemBuilder: (context, index) {
        final (label, color) = categories[index];
        return Material(
          color: color,
          borderRadius: BorderRadius.circular(8),
          clipBehavior: Clip.antiAlias,
          child: InkWell(
            onTap: () {
              // Pre-fill search with category label
            },
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Align(
                alignment: Alignment.bottomLeft,
                child: Text(
                  label,
                  style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                ),
              ),
            ),
          ),
        );
      },
    );
  }
}
```

Each cell uses **`Material`** + **`InkWell`** + **`Align`** — layout from Parts 7–9.

## Search results — tracks and albums

```dart
class _SearchResults extends StatelessWidget {
  const _SearchResults({required this.tracks, required this.albums});

  final List<Track> tracks;
  final List<Album> albums;

  @override
  Widget build(BuildContext context) {
    if (tracks.isEmpty && albums.isEmpty) {
      return const Center(child: Text('No results'));
    }

    return ListView(
      padding: const EdgeInsets.only(bottom: 96),
      children: [
        if (albums.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 4),
            child: Text('Albums', style: Theme.of(context).textTheme.titleMedium),
          ),
          SizedBox(
            height: 160,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 16),
              itemCount: albums.length,
              separatorBuilder: (_, __) => const SizedBox(width: 12),
              itemBuilder: (context, index) {
                final album = albums[index];
                return SizedBox(
                  width: 120,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Expanded(
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(8),
                          child: Image.network(album.coverUrl, width: 120, fit: BoxFit.cover),
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(album.title, maxLines: 1, overflow: TextOverflow.ellipsis),
                    ],
                  ),
                );
              },
            ),
          ),
        ],
        Padding(
          padding: const EdgeInsets.fromLTRB(16, 16, 16, 4),
          child: Text('Songs', style: Theme.of(context).textTheme.titleMedium),
        ),
        ...tracks.asMap().entries.map((e) {
          final track = e.value;
          return TrackListTile(
            track: track,
            index: e.key,
            onTap: () {
              context.read<AudioRepository>().playTrack(track);
            },
            trailing: IconButton(
              icon: const Icon(Icons.more_vert),
              onPressed: () => _songMenu(context, track),
            ),
          );
        }),
      ],
    );
  }

  static void _songMenu(BuildContext context, Track track) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (context) => Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          ListTile(
            leading: const Icon(Icons.playlist_add),
            title: const Text('Add to playlist'),
            onTap: () => Navigator.pop(context),
          ),
          ListTile(
            leading: const Icon(Icons.album),
            title: const Text('Go to album'),
            onTap: () {
              Navigator.pop(context);
              context.push('/album/${track.albumId}');
            },
          ),
        ],
      ),
    );
  }
}
```

| UI control | Usage |
|------------|--------|
| `TextField` | Query input, clear suffix |
| `GridView` | Genre browse |
| Horizontal `ListView` | Album hits |
| `TrackListTile` | Song rows |
| `showModalBottomSheet` | Track overflow menu |

## Desktop: persistent search in rail body

On wide layouts the same `SearchScreen` fills the **`Expanded`** region beside **`NavigationRail`** — no code change; **`LayoutBuilder`** optional for two-column results (albums left, tracks right) when `maxWidth > 900`.


<!-- enriched:v3 -->

## Scenario

Search blended genre grid and live results—Column + Expanded bounded inner lists.

## Deep dive

Debounce query; show browse grid when empty; split album vs track results.

## Extended example

```dart
Timer(const Duration(milliseconds: 280), () => runSearch(text));
```

## Refined UI note

Filled rounded search field matches home chrome.

## Try it

- Clear button resets state.
- Empty results illustration.

## Summary

Search uses **`Column` + `Expanded`**, a filled **`TextField`** with debounce, **`GridView`** for categories, and **`ListView`** sections for album carousel + song **`ListTile`** results. Hook **`AudioRepository.playTrack`** on row tap and **`go_router`** for album navigation.
