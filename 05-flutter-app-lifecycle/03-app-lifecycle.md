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


<!-- enriched:v3 -->

## Scenario

PulseRoutine must pause timers when app backgrounds during a session.

## Deep dive

Listen to `AppLifecycleState` to pause audio, sync, or sensors.

## Extended example

```dart
class SessionHost extends StatefulWidget {
  const SessionHost({super.key});
  @override
  State<SessionHost> createState() => _SessionHostState();
}
class _SessionHostState extends State<SessionHost> with WidgetsBindingObserver {
  @override
  void initState() { super.initState(); WidgetsBinding.instance.addObserver(this); }
  @override
  void dispose() { WidgetsBinding.instance.removeObserver(this); super.dispose(); }
  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused) pauseSession();
  }
  @override
  Widget build(BuildContext context) => const SizedBox();
  void pauseSession() {}
}
```

## Engineering note

Remove observers in dispose.

## Try it

- Pause mock audio on inactive.
- Compare desktop visibility APIs.

## Summary

Lifecycle hooks coordinate audio playback, sync, and resource release—critical for the music app in Part 14.
