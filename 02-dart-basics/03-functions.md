---
title: Functions
order: 3
---

# Functions

Functions are first-class values in Dart. Flutter code uses them for callbacks, builders, and event handlers.

## Syntax

```dart
int add(int a, int b) => a + b;

void greet(String name, {String greeting = 'Hello'}) {
  print('$greeting, $name');
}
```

## Named and optional parameters

Flutter widgets rely heavily on **named parameters** in constructors:

```dart
Text('Title', style: TextStyle(fontSize: 18));
```

Use `{}` for named parameters and `[]` for optional positional parameters. Mark named parameters `required` when they must be supplied.

## Closures

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2).toList();
```

Closures capture variables from enclosing scopes—useful for listeners, but watch for memory leaks if you forget to cancel subscriptions.


<!-- enriched:v3 -->

## Scenario

PulseRoutine coaches configure intervals with optional labels and audible cues. Positional parameters made call sites ambiguous.

## Deep dive

Named parameters mirror Flutter constructors: required fields first, optional tuning later. Functions are first-class—store them in maps to drive strategy-style UI.

## Extended example

```dart
typedef IntervalBuilder = Widget Function(String label, Duration length);

Widget intervalTile({
  required String label,
  required Duration length,
  VoidCallback? onSkip,
}) {
  return ListTile(
    title: Text(label),
    subtitle: Text('${length.inSeconds}s'),
    trailing: onSkip == null ? null : TextButton(onPressed: onSkip, child: const Text('Skip')),
  );
}
```

## Engineering note

Keep `BuildContext` out of pure formatting functions; pass `TextStyle` in from widgets.

## Try it

- Write `formatDuration(Duration d)` returning `mm:ss`.
- Pass a closure into `List.sort` for custom ordering.

## Summary

Read widget constructors as function calls with many named parameters. Arrow syntax keeps simple functions concise.
