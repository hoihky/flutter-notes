---
title: MediaQuery and Accessibility
order: 4
---

# MediaQuery and Accessibility

`MediaQuery` exposes screen size, padding, orientation, and text scale factor.

```dart
final width = MediaQuery.sizeOf(context).width;
final padding = MediaQuery.paddingOf(context);
```

Respect user text scaling—avoid locking font sizes unless design requires it. Test with large accessibility fonts.

## Summary

Responsive layouts start with `MediaQuery` and constraints, not hard-coded pixel widths.
