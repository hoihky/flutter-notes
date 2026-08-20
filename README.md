# Developing Flutter Applications

Markdown ebook and generated documentation site for learning Flutter and Dart, from language fundamentals through a Spotify-style multi-platform music player capstone.

## Content

| Part | Folder | Topics |
|------|--------|--------|
| 1 | `01-overview/` | Flutter, Dart, ecosystem, tooling |
| 2 | `02-dart-basics/` | Variables, control flow, functions, collections, classes |
| 3 | `03-dart-advanced/` | Generics, null safety, mixins, libraries |
| 4 | `04-dart-concurrency/` | Event loop, futures, streams, isolates |
| 5 | `05-flutter-app-lifecycle/` | Architecture, widget tree, lifecycle, navigation |
| 6 | `06-flutter-ui-framework/` | Rendering, Material/Cupertino, theming |
| 7 | `07-layout-basics/` | Row, Column, Stack, constraints |
| 8 | `08-layout-advanced/` | Expanded, LayoutBuilder, slivers |
| 9 | `09-ui-controls-basics/` | Text, buttons, fields, lists |
| 10 | `10-ui-controls-advanced/` | Scrollables, sheets, gestures, adaptive nav |
| 11 | `11-state-management/` | setState, Provider, Riverpod/BLoC |
| 12 | `12-custom-ui/` | Decorations, CustomPaint, custom widgets |
| 13 | `13-packages/` | HTTP, persistence, audio, desktop |
| 14 | `14-spotify-style-app/` | End-to-end music app project |

## Build the site (MDWeb)

Custom theme and footer live in this repo:

```bash
/Users/rainechen/Desktop/Kwan/Source/Projects/MDWeb/src/MDWeb.Cli/bin/Debug/net10.0/mdweb \
  --source . \
  --output ./site \
  --theme ./theme \
  --title "Developing Flutter Applications" \
  --description "Flutter and Dart ebook with layout, UI, and capstone projects" \
  --footer-file ./site-footer.html
```

Open `site/index.html` in a browser, or run `npx serve site` for local preview.