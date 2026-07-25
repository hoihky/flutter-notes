---
title: Player UI and Queue
order: 4
---

# Player UI and Queue

Full-screen **now playing** uses **`Stack`** (art background + gradient), **`Column`** (controls), **`Slider`**, **`IconButton`**, and a **`showModalBottomSheet`** queue. **`DraggableScrollableSheet`** optional for partial-height player on tablets.

## Now playing screen

```dart
import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../data/repositories/audio_repository.dart';

class NowPlayingScreen extends StatelessWidget {
  const NowPlayingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final audio = context.watch<AudioRepository>();
    final track = audio.current;
    if (track == null) {
      return const Scaffold(body: Center(child: Text('Nothing playing')));
    }

    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        leading: IconButton(
          icon: const Icon(Icons.keyboard_arrow_down),
          onPressed: () => Navigator.of(context).pop(),
        ),
        actions: [
          IconButton(icon: const Icon(Icons.more_vert), onPressed: () => _showTrackMenu(context)),
        ],
      ),
      body: Stack(
        fit: StackFit.expand,
        children: [
          CachedNetworkImage(imageUrl: track.artUrl ?? '', fit: BoxFit.cover),
          DecoratedBox(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Colors.black.withValues(alpha: 0.3),
                  Colors.black.withValues(alpha: 0.85),
                  Colors.black,
                ],
              ),
            ),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              child: Column(
                children: [
                  const Spacer(),
                  AspectRatio(
                    aspectRatio: 1,
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(12),
                      child: CachedNetworkImage(imageUrl: track.artUrl ?? '', fit: BoxFit.cover),
                    ),
                  ),
                  const SizedBox(height: 32),
                  Text(
                    track.title,
                    textAlign: TextAlign.center,
                    style: Theme.of(context).textTheme.headlineSmall,
                  ),
                  Text(track.artist, style: Theme.of(context).textTheme.titleMedium),
                  const SizedBox(height: 24),
                  StreamBuilder<Duration>(
                    stream: audio.positionStream,
                    builder: (context, snapshot) {
                      final position = snapshot.data ?? Duration.zero;
                      return StreamBuilder<Duration?>(
                        stream: audio.durationStream,
                        builder: (context, durSnap) {
                          final total = durSnap.data ?? track.duration;
                          final value = total.inMilliseconds == 0
                              ? 0.0
                              : position.inMilliseconds / total.inMilliseconds;
                          return Column(
                            children: [
                              Slider(
                                value: value.clamp(0.0, 1.0),
                                onChanged: (v) {
                                  audio.seek(Duration(milliseconds: (v * total.inMilliseconds).round()));
                                },
                              ),
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Text(_format(position)),
                                  Text(_format(total)),
                                ],
                              ),
                            ],
                          );
                        },
                      );
                    },
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      IconButton(icon: const Icon(Icons.shuffle), onPressed: () {}),
                      IconButton(icon: const Icon(Icons.skip_previous), onPressed: audio.skipPrevious),
                      FilledButton(
                        style: FilledButton.styleFrom(
                          shape: const CircleBorder(),
                          padding: const EdgeInsets.all(20),
                        ),
                        onPressed: audio.togglePlayPause,
                        child: Icon(audio.isPlaying ? Icons.pause : Icons.play_arrow, size: 36),
                      ),
                      IconButton(icon: const Icon(Icons.skip_next), onPressed: audio.skipNext),
                      IconButton(icon: const Icon(Icons.repeat), onPressed: () {}),
                    ],
                  ),
                  const SizedBox(height: 16),
                  OutlinedButton.icon(
                    onPressed: () => _openQueue(context),
                    icon: const Icon(Icons.queue_music),
                    label: const Text('Queue'),
                  ),
                  const Spacer(flex: 1),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  static String _format(Duration d) {
    final m = d.inMinutes.remainder(60).toString().padLeft(2, '0');
    final s = d.inSeconds.remainder(60).toString().padLeft(2, '0');
    return '$m:$s';
  }

  static void _openQueue(BuildContext context) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      isScrollControlled: true,
      builder: (context) => const _QueueSheet(),
    );
  }

  static void _showTrackMenu(BuildContext context) {
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
            leading: const Icon(Icons.share),
            title: const Text('Share'),
            onTap: () => Navigator.pop(context),
          ),
        ],
      ),
    );
  }
}
```

### Layout map

| Region | Widgets |
|--------|---------|
| Background | `Stack` + `Image` + gradient `DecoratedBox` |
| Art | `AspectRatio` + `ClipRRect` |
| Progress | `StreamBuilder` + `Slider` + `Row` of `Text` |
| Transport | `Row` + `FilledButton` + `IconButton` |

## Reorderable queue sheet

Uses **`ReorderableListView.builder`**, **`ListTile`**, **`Dismissible`** optional:

```dart
class _QueueSheet extends StatelessWidget {
  const _QueueSheet();

  @override
  Widget build(BuildContext context) {
    final audio = context.watch<AudioRepository>();
    final queue = audio.queue;
    return DraggableScrollableSheet(
      expand: false,
      initialChildSize: 0.6,
      minChildSize: 0.35,
      maxChildSize: 0.95,
      builder: (context, scrollController) {
        return Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(16),
              child: Text('Queue', style: Theme.of(context).textTheme.titleLarge),
            ),
            Expanded(
              child: ReorderableListView.builder(
                scrollController: scrollController,
                itemCount: queue.length,
                onReorder: audio.reorderQueue,
                itemBuilder: (context, index) {
                  final t = queue[index];
                  return ListTile(
                    key: ValueKey(t.id),
                    leading: const Icon(Icons.drag_handle),
                    title: Text(t.title),
                    subtitle: Text(t.artist),
                    trailing: Text(t.durationLabel),
                    onTap: () => audio.playTracks(queue, startIndex: index),
                  );
                },
              ),
            ),
          ],
        );
      },
    );
  }
}
```

## Hero transition (optional polish)

Wrap album art on album detail and mini player with matching **`Hero`** tags:

```dart
Hero(
  tag: 'art-${track.id}',
  child: ClipRRect(borderRadius: BorderRadius.circular(8), child: image),
)
```

## Summary

**Now playing** layers **`Stack`** visuals with a **`Column`** of controls. **`Slider`** + streams handle progress; **`showModalBottomSheet`** + **`DraggableScrollableSheet`** present the **queue** with **`ReorderableListView`**. Wire the same `AudioRepository` used in the shell mini bar.
