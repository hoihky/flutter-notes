---
title: Application Lifecycle
order: 3
---

# Application Lifecycle

Mobile apps move through states: resumed, inactive, paused, detached. Listen with `WidgetsBindingObserver`:

```dart
class _HomeState extends State<Home> with WidgetsBindingObserver {
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused) {
      // pause audio
    }
  }
}
```

Desktop and web have related visibility APIs; pause expensive work when the window is hidden.

## Summary

Lifecycle hooks coordinate audio playback, sync, and resource release—critical for the music app in Part 14.
