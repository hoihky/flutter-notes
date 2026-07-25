---
title: Local State with setState
order: 1
---

# Local State with setState

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
