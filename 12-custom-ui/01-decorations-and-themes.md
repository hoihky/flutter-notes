---
title: Decorations and Theme Extensions
order: 1
---

# Decorations and Theme Extensions

Custom inbox UIs need more than `ThemeData.colorScheme` — swipe action colors, unread highlights, and per-category accents should live in one place. **`ThemeExtension`** (Material 3) lets you attach app-specific tokens to `ThemeData` and swap entire palettes without rewriting widgets.

## Class hierarchy

```mermaid
flowchart TB
  ThemeData --> ThemeExtension
  ThemeExtension --> InboxThemeExtension
  Widget --> InheritedWidget
  InheritedWidget --> Theme
  Theme --> Theme.of context
```

| API | Role |
|-----|------|
| `ThemeData` | Colors, text themes, component themes |
| `ThemeExtension<T>` | Custom immutable tokens; `copyWith` + `lerp` |
| `Theme.of(context).extension<InboxThemeExtension>()` | Read tokens in widgets |
| `MaterialApp.theme` / `themeMode` | Global theme selection |

## BoxDecoration in list tiles

List rows often combine **padding**, **border**, and **background**:

```dart
Container(
  margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
  decoration: BoxDecoration(
    color: background,
    borderRadius: BorderRadius.circular(12),
    border: Border.all(color: borderColor, width: unread ? 2 : 0.5),
    boxShadow: [
      if (elevated)
        BoxShadow(
          color: Colors.black.withValues(alpha: 0.08),
          blurRadius: 8,
          offset: const Offset(0, 2),
        ),
    ],
  ),
  child: child,
)
```

Gradients work for promotional email rows:

```dart
decoration: BoxDecoration(
  borderRadius: BorderRadius.circular(12),
  gradient: LinearGradient(
    colors: [accent.withValues(alpha: 0.15), Colors.transparent],
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
  ),
),
```

## InboxThemeExtension — swappable color themes

Define an extension that holds every color the email list needs:

```dart
import 'package:flutter/material.dart';

@immutable
class InboxThemeExtension extends ThemeExtension<InboxThemeExtension> {
  const InboxThemeExtension({
    required this.name,
    required this.readRowColor,
    required this.unreadRowColor,
    required this.unreadBorder,
    required this.swipeArchive,
    required this.swipeDelete,
    required this.swipeStar,
    required this.personalAccent,
    required this.workAccent,
    required this.newsletterAccent,
    required this.securityAccent,
  });

  final String name;
  final Color readRowColor;
  final Color unreadRowColor;
  final Color unreadBorder;
  final Color swipeArchive;
  final Color swipeDelete;
  final Color swipeStar;
  final Color personalAccent;
  final Color workAccent;
  final Color newsletterAccent;
  final Color securityAccent;

  static const classic = InboxThemeExtension(
    name: 'Classic',
    readRowColor: Color(0xFFF5F5F5),
    unreadRowColor: Color(0xFFFFFFFF),
    unreadBorder: Color(0xFF1A73E8),
    swipeArchive: Color(0xFF5F6368),
    swipeDelete: Color(0xFFD93025),
    swipeStar: Color(0xFFF9AB00),
    personalAccent: Color(0xFF34A853),
    workAccent: Color(0xFF1A73E8),
    newsletterAccent: Color(0xFF9334E6),
    securityAccent: Color(0xFFEA4335),
  );

  static const midnight = InboxThemeExtension(
    name: 'Midnight',
    readRowColor: Color(0xFF1E1E1E),
    unreadRowColor: Color(0xFF2D2D2D),
    unreadBorder: Color(0xFF8AB4F8),
    swipeArchive: Color(0xFF5F6368),
    swipeDelete: Color(0xFFF28B82),
    swipeStar: Color(0xFFFDD663),
    personalAccent: Color(0xFF81C995),
    workAccent: Color(0xFF8AB4F8),
    newsletterAccent: Color(0xFFC58AF9),
    securityAccent: Color(0xFFF28B82),
  );

  static const ocean = InboxThemeExtension(
    name: 'Ocean',
    readRowColor: Color(0xFFE8F4F8),
    unreadRowColor: Color(0xFFFFFFFF),
    unreadBorder: Color(0xFF00796B),
    swipeArchive: Color(0xFF546E7A),
    swipeDelete: Color(0xFFC62828),
    swipeStar: Color(0xFFFF8F00),
    personalAccent: Color(0xFF00897B),
    workAccent: Color(0xFF0277BD),
    newsletterAccent: Color(0xFF6A1B9A),
    securityAccent: Color(0xFFD84315),
  );

  static List<InboxThemeExtension> get presets => [classic, midnight, ocean];

  @override
  InboxThemeExtension copyWith({
    String? name,
    Color? readRowColor,
    Color? unreadRowColor,
    Color? unreadBorder,
    Color? swipeArchive,
    Color? swipeDelete,
    Color? swipeStar,
    Color? personalAccent,
    Color? workAccent,
    Color? newsletterAccent,
    Color? securityAccent,
  }) {
    return InboxThemeExtension(
      name: name ?? this.name,
      readRowColor: readRowColor ?? this.readRowColor,
      unreadRowColor: unreadRowColor ?? this.unreadRowColor,
      unreadBorder: unreadBorder ?? this.unreadBorder,
      swipeArchive: swipeArchive ?? this.swipeArchive,
      swipeDelete: swipeDelete ?? this.swipeDelete,
      swipeStar: swipeStar ?? this.swipeStar,
      personalAccent: personalAccent ?? this.personalAccent,
      workAccent: workAccent ?? this.workAccent,
      newsletterAccent: newsletterAccent ?? this.newsletterAccent,
      securityAccent: securityAccent ?? this.securityAccent,
    );
  }

  @override
  InboxThemeExtension lerp(InboxThemeExtension? other, double t) {
    if (other == null) return this;
    return InboxThemeExtension(
      name: name,
      readRowColor: Color.lerp(readRowColor, other.readRowColor, t)!,
      unreadRowColor: Color.lerp(unreadRowColor, other.unreadRowColor, t)!,
      unreadBorder: Color.lerp(unreadBorder, other.unreadBorder, t)!,
      swipeArchive: Color.lerp(swipeArchive, other.swipeArchive, t)!,
      swipeDelete: Color.lerp(swipeDelete, other.swipeDelete, t)!,
      swipeStar: Color.lerp(swipeStar, other.swipeStar, t)!,
      personalAccent: Color.lerp(personalAccent, other.personalAccent, t)!,
      workAccent: Color.lerp(workAccent, other.workAccent, t)!,
      newsletterAccent: Color.lerp(newsletterAccent, other.newsletterAccent, t)!,
      securityAccent: Color.lerp(securityAccent, other.securityAccent, t)!,
    );
  }
}
```

Attach to `ThemeData`:

```dart
ThemeData buildTheme(InboxThemeExtension inbox, Brightness brightness) {
  final base = ThemeData(
    useMaterial3: true,
    brightness: brightness,
    colorScheme: ColorScheme.fromSeed(
      seedColor: inbox.workAccent,
      brightness: brightness,
    ),
  );
  return base.copyWith(extensions: [inbox]);
}

// In widgets:
InboxThemeExtension inboxTheme(BuildContext context) {
  return Theme.of(context).extension<InboxThemeExtension>() ?? InboxThemeExtension.classic;
}
```

## Switching themes without packages

Hold the selected preset in **`StatefulWidget`** (or `ValueNotifier` from `dart` + `ListenableBuilder`):

```dart
class InboxApp extends StatefulWidget {
  const InboxApp({super.key});
  @override
  State<InboxApp> createState() => _InboxAppState();
}

class _InboxAppState extends State<InboxApp> {
  InboxThemeExtension _inboxTheme = InboxThemeExtension.classic;

  void _setTheme(InboxThemeExtension next) => setState(() => _inboxTheme = next);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: buildTheme(_inboxTheme, Brightness.light),
      darkTheme: buildTheme(InboxThemeExtension.midnight, Brightness.dark),
      home: InboxScreen(
        inboxTheme: _inboxTheme,
        onThemeChanged: _setTheme,
      ),
    );
  }
}
```

Expose a **`PopupMenuButton`** on the inbox app bar listing `InboxThemeExtension.presets`.


<!-- enriched:v3 -->

## Scenario

LedgerAir inbox needed swappable palettes for focus, night, and high-contrast modes.

## Deep dive

ThemeExtension stores custom tokens; DecoratedBox paints row chrome.

## Extended example

```dart
final inbox = Theme.of(context).extension<InboxThemeExtension>()!;
BoxDecoration(rowDecoration(Color bg) => BoxDecoration(color: bg, borderRadius: BorderRadius.circular(12)));
```

## Refined UI note

Limit palette to one accent + neutrals so unread borders remain visible.

## Try it

- Add fourth theme preset.
- Move swipe colors to extension.

## Summary

Use **`BoxDecoration`** for row chrome and **`ThemeExtension`** for inbox-specific colors. Multiple presets (Classic, Midnight, Ocean) plug into **`ThemeData.extensions`** so the email list in Chapter 4 reads one object for swipe colors and category accents.
