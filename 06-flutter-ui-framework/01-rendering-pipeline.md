---
title: Rendering Pipeline
order: 1
---

# Rendering Pipeline

Each frame follows **build → layout → paint → compositing**. The framework schedules frames when animation ticks, gestures resolve, or `setState` marks elements dirty.

Enable performance overlay with `MaterialApp(showPerformanceOverlay: true)` in debug builds to spot missed frames.

## Summary

Jank usually means too much work per frame—simplify `build`, cache images, or defer layout.
