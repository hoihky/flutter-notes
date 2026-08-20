---
title: Audio and Video Packages
order: 3
---

# Audio and Video Packages

**just_audio** plays streams and files with gapless support on many platforms. **audio_service** integrates background playback and media notifications.

Verify desktop support matrices—some plugins are mobile-first.


<!-- enriched:v3 -->

## Scenario

Melody Hub needed background audio policies on mobile.

## Deep dive

Abstract player behind interface; UI listens to streams from repository.

## Extended example

```dart
abstract class PlaybackEngine {
  Stream<Duration> get position;
  Future<void> load(Uri source);
  Future<void> toggle();
}
```

## Engineering note

Verify desktop support matrix before committing to plugin.

## Try it

- Fake engine for tests.
- Handle lifecycle pause.

## Summary

Abstract playback behind an interface so UI code stays platform-agnostic.
