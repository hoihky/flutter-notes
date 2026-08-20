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


<!-- enriched:v3 -->

## Scenario

HarborCart checkout pipeline needed explicit event→state traces for audits.

## Deep dive

BLoC/Riverpod shine when flows are complex; simpler apps may use Provider.

## Extended example

```dart
sealed class CheckoutEvent {}
class SubmitCheckout extends CheckoutEvent {}
sealed class CheckoutState {}
class CheckoutIdle extends CheckoutState {}
```

## Engineering note

Pick architecture to match team testing habits, not hype.

## Try it

- Diagram event/state flow.
- Compare Provider vs Riverpod compile safety.

## Summary

State management is about boundaries: UI reacts to immutable view models; services own async work.
