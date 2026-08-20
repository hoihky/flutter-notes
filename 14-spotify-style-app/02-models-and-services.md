---
title: Models and Services
order: 2
---

# Models and Services

Screens stay thin when **models** describe data and **repositories** own loading, search, and playback. Widgets only call methods like `catalog.search(query)` or `context.read<AudioRepository>().playTrack(track)`.

## Track model

```dart
class Track {
  const Track({
    required this.id,
    required this.title,
    required this.artist,
    required this.albumId,
    required this.durationMs,
    this.artUrl,
  });

  final String id;
  final String title;
  final String artist;
  final String albumId;
  final int durationMs;
  final String? artUrl;

  Duration get duration => Duration(milliseconds: durationMs);

  String get durationLabel {
    final m = duration.inMinutes.remainder(60).toString().padLeft(2, '0');
    final s = duration.inSeconds.remainder(60).toString().padLeft(2, '0');
    return '$m:$s';
  }

  factory Track.fromJson(Map<String, dynamic> json) => Track(
        id: json['id'] as String,
        title: json['title'] as String,
        artist: json['artist'] as String,
        albumId: json['albumId'] as String,
        durationMs: json['durationMs'] as int,
        artUrl: json['artUrl'] as String?,
      );
}
```

## Album model

```dart
class Album {
  const Album({
    required this.id,
    required this.title,
    required this.artist,
    required this.year,
    required this.coverUrl,
    required this.trackIds,
  });

  final String id;
  final String title;
  final String artist;
  final int year;
  final String coverUrl;
  final List<String> trackIds;

  factory Album.fromJson(Map<String, dynamic> json) => Album(
        id: json['id'] as String,
        title: json['title'] as String,
        artist: json['artist'] as String,
        year: json['year'] as int,
        coverUrl: json['coverUrl'] as String,
        trackIds: (json['trackIds'] as List).cast<String>(),
      );
}
```

## Playlist model

```dart
class Playlist {
  const Playlist({
    required this.id,
    required this.title,
    required this.description,
    required this.coverUrl,
    required this.trackIds,
  });

  final String id;
  final String title;
  final String description;
  final String coverUrl;
  final List<String> trackIds;

  factory Playlist.fromJson(Map<String, dynamic> json) => Playlist(
        id: json['id'] as String,
        title: json['title'] as String,
        description: json['description'] as String,
        coverUrl: json['coverUrl'] as String,
        trackIds: (json['trackIds'] as List).cast<String>(),
      );
}
```

## CatalogRepository — home, search, lists

```dart
import 'dart:convert';
import 'package:flutter/services.dart';

class CatalogRepository {
  final List<Album> _albums = [];
  final List<Track> _tracks = [];
  final List<Playlist> _playlists = [];
  final Map<String, Track> _trackById = {};
  final Map<String, Album> _albumById = {};

  Future<void> load() async {
    final raw = await rootBundle.loadString('assets/mock/catalog.json');
    final map = jsonDecode(raw) as Map<String, dynamic>;
    _tracks
      ..clear()
      ..addAll((map['tracks'] as List).map((e) => Track.fromJson(e as Map<String, dynamic>)));
    _albums
      ..clear()
      ..addAll((map['albums'] as List).map((e) => Album.fromJson(e as Map<String, dynamic>)));
    _playlists
      ..clear()
      ..addAll((map['playlists'] as List).map((e) => Playlist.fromJson(e as Map<String, dynamic>)));
    for (final t in _tracks) {
      _trackById[t.id] = t;
    }
    for (final a in _albums) {
      _albumById[a.id] = a;
    }
  }

  List<Album> get albums => List.unmodifiable(_albums);
  List<Playlist> get playlists => List.unmodifiable(_playlists);
  List<Track> get tracks => List.unmodifiable(_tracks);

  Album? albumById(String id) => _albumById[id];
  Playlist? playlistById(String id) {
    for (final p in _playlists) {
      if (p.id == id) return p;
    }
    return null;
  }
  Track? trackById(String id) => _trackById[id];

  List<Track> tracksForAlbum(String albumId) {
    final album = _albumById[albumId];
    if (album == null) return [];
    return album.trackIds.map((id) => _trackById[id]!).toList();
  }

  List<Track> tracksForPlaylist(String playlistId) {
    final playlist = _playlists.firstWhere((p) => p.id == playlistId);
    return playlist.trackIds.map((id) => _trackById[id]!).toList();
  }

  /// Case-insensitive search across track title, artist, album title.
  List<Track> search(String query) {
    final q = query.trim().toLowerCase();
    if (q.isEmpty) return [];
    return _tracks.where((t) {
      final albumTitle = _albumById[t.albumId]?.title.toLowerCase() ?? '';
      return t.title.toLowerCase().contains(q) ||
          t.artist.toLowerCase().contains(q) ||
          albumTitle.contains(q);
    }).toList();
  }

  List<Album> searchAlbums(String query) {
    final q = query.trim().toLowerCase();
    if (q.isEmpty) return [];
    return _albums
        .where((a) => a.title.toLowerCase().contains(q) || a.artist.toLowerCase().contains(q))
        .toList();
  }
}
```

Home screen uses `albums.take(6)`, search uses `search()`, library uses `playlists`.

## AudioRepository — playback + queue

`ChangeNotifier` drives **mini player** and **now playing** rebuilds via `context.watch<AudioRepository>()`.

```dart
import 'package:flutter/foundation.dart';
import 'package:just_audio/just_audio.dart';

import '../models/track.dart';

class AudioRepository extends ChangeNotifier {
  final AudioPlayer _player = AudioPlayer();
  Track? _current;
  List<Track> _queue = [];
  int _queueIndex = 0;

  Track? get current => _current;
  List<Track> get queue => List.unmodifiable(_queue);
  bool get isPlaying => _player.playing;
  Stream<Duration> get positionStream => _player.positionStream;
  Stream<Duration?> get durationStream => _player.durationStream;
  Stream<bool> get playingStream => _player.playingStream;

  Future<void> init() async {
    _player.playerStateStream.listen((state) {
      if (state.processingState == ProcessingState.completed) {
        skipNext();
      }
      notifyListeners();
    });
  }

  Future<void> playTracks(List<Track> tracks, {int startIndex = 0}) async {
    if (tracks.isEmpty) return;
    _queue = List.of(tracks);
    _queueIndex = startIndex.clamp(0, _queue.length - 1);
    await _loadAndPlay(_queue[_queueIndex]);
  }

  Future<void> playTrack(Track track) => playTracks([track]);

  Future<void> _loadAndPlay(Track track) async {
    _current = track;
    notifyListeners();
  }

  Future<void> togglePlayPause() async {
    if (_player.playing) {
      await _player.pause();
    } else {
      await _player.play();
    }
    notifyListeners();
  }

  Future<void> skipNext() async {
    if (_queue.isEmpty) return;
    _queueIndex = (_queueIndex + 1) % _queue.length;
    await _loadAndPlay(_queue[_queueIndex]);
  }

  Future<void> skipPrevious() async {
    if (_queue.isEmpty) return;
    _queueIndex = (_queueIndex - 1) < 0 ? _queue.length - 1 : _queueIndex - 1;
    await _loadAndPlay(_queue[_queueIndex]);
  }

  Future<void> seek(Duration position) => _player.seek(position);

  void reorderQueue(int oldIndex, int newIndex) {
    if (newIndex > oldIndex) newIndex -= 1;
    final item = _queue.removeAt(oldIndex);
    _queue.insert(newIndex, item);
    _queueIndex = _queue.indexOf(_current!);
    notifyListeners();
  }

  @override
  void dispose() {
    _player.dispose();
    super.dispose();
  }
}
```

In a real app, set `_player.setUrl` or `setAudioSource` with your CDN. The UI code in later chapters stays the same.

## Shared UI: TrackListTile

Reused on album, playlist, and search results — **`ListTile`** + **`Row`**-friendly layout:

```dart
class TrackListTile extends StatelessWidget {
  const TrackListTile({
    super.key,
    required this.track,
    required this.index,
    this.onTap,
    this.trailing,
  });

  final Track track;
  final int index;
  final VoidCallback? onTap;
  final Widget? trailing;

  @override
  Widget build(BuildContext context) {
    return ListTile(
      contentPadding: const EdgeInsets.symmetric(horizontal: 16),
      leading: SizedBox(
        width: 32,
        child: Text('${index + 1}', textAlign: TextAlign.center),
      ),
      title: Text(track.title, maxLines: 1, overflow: TextOverflow.ellipsis),
      subtitle: Text(track.artist, maxLines: 1, overflow: TextOverflow.ellipsis),
      trailing: trailing ?? Text(track.durationLabel),
      onTap: onTap,
    );
  }
}
```


<!-- enriched:v3 -->

## Scenario

Player UI rebuilt every 200ms until audio position used streams not setState loops.

## Deep dive

Repositories isolate IO; ChangeNotifier exposes playback snapshot.

## Extended example

```dart
class AudioRepository extends ChangeNotifier {
  Duration position = Duration.zero;
  void tick(Duration next) { position = next; notifyListeners(); }
}
```

## Engineering note

Parse JSON once; pass immutable models to widgets.

## Try it

- Fake catalog in tests.
- Map album→tracks lookup.

## Summary

**CatalogRepository** powers home rows, album lists, library playlists, and search. **AudioRepository** holds **current track** and **queue** for the player bar and reorderable queue sheet. Shared tiles keep **ListTile** styling consistent across screens.
