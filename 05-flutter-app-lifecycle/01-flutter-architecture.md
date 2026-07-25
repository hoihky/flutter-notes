---
title: Flutter Architecture
order: 1
---

# Flutter Architecture

Flutter layers stack from embedded platform views up to your widgets:

1. **Embedder** — OS window, input, surfaces.
2. **Engine** — Skia/Impeller, Dart runtime, compositing.
3. **Framework** — Widgets, rendering, gestures, painting.

Your code interacts primarily with the **framework** layer. Understanding separation helps when debugging performance or platform integration.

## Summary

Widgets are Dart configuration; the engine turns them into pixels. Platform channels cross from framework to embedder.
