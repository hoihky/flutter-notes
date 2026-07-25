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

## Summary

Read widget constructors as function calls with many named parameters. Arrow syntax keeps simple functions concise.
