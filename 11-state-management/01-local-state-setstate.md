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


<!-- core:v2 -->
## When setState is enough

Local ephemeral UI—expanded/collapsed panels, tab indexes inside one screen, form field focus—can stay inside `StatefulWidget`. Problems begin when distant cousins need the same data; that is the signal to lift state or inject a notifier.

## Collapsible promo banner (HarborCart)

```dart
class PromoBanner extends StatefulWidget {
  const PromoBanner({super.key});
  @override
  State<PromoBanner> createState() => _PromoBannerState();
}

class _PromoBannerState extends State<PromoBanner> {
  var expanded = true;

  @override
  Widget build(BuildContext context) {
    return AnimatedCrossFade(
      firstChild: MaterialBanner(
        content: const Text('Free shipping this weekend'),
        actions: [TextButton(onPressed: () => setState(() => expanded = false), child: const Text('Dismiss'))],
      ),
      secondChild: const SizedBox.shrink(),
      crossFadeState: expanded ? CrossFadeState.showFirst : CrossFadeState.showSecond,
      duration: const Duration(milliseconds: 250),
    );
  }
}
```

`AnimatedCrossFade` sells the dismiss with motion—cheap polish tied to local state.


<!-- enriched:v3 -->

## Scenario

HarborCart quantity stepper lived entirely inside one widget—setState was enough.

## Deep dive

Lift state when siblings need the same data; keep ephemeral UI local.

## Extended example

```dart
class QtyStepper extends StatefulWidget {
  const QtyStepper({super.key});
  @override
  State<QtyStepper> createState() => _QtyStepperState();
}
class _QtyStepperState extends State<QtyStepper> {
  int qty = 1;
  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        IconButton(onPressed: () => setState(() => qty = (qty - 1).clamp(1, 99)), icon: const Icon(Icons.remove)),
        Text('$qty'),
        IconButton(onPressed: () => setState(() => qty = (qty + 1).clamp(1, 99)), icon: const Icon(Icons.add)),
      ],
    );
  }
}
```

## Engineering note

setState marks element dirty; keep build pure.

## Try it

- Identify state to lift.
- Add disabled at min/max.

## Summary

`setState` is perfect for ephemeral UI state isolated to one widget.
