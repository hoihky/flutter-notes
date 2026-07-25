---
title: Riverpod and BLoC Overview
order: 4
---

# Riverpod and BLoC Overview

**Riverpod** improves testability with compile-safe providers. **BLoC** separates events and states for predictable flows.

```dart
// Simplified BLoC idea
// on<Event> => emit<State>
```

Choose based on team familiarity. Large apps often combine repository layers with any of these libraries.

## Summary

State management is about boundaries: UI reacts to immutable view models; services own async work.
