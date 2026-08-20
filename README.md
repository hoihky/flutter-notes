# flutter-notes

Personal study notes on Flutter, Dart, and cross-platform app development — written for my own learning, organized as markdown tutorials and a static site. If they are useful for your study too, you are welcome to read and use them.

See [LICENSE](LICENSE) for terms (CC BY-NC 4.0 — attribution, non-commercial use; no warranty).

## Topics

| Topic | Description | Start reading | Site |
|-------|-------------|---------------|------|
| [Developing Flutter Applications](index.md) | Flutter & Dart fundamentals, layout, UI controls, state management, packages, custom UI, and a Spotify-style music app capstone | [Introduction](index.md) | [site](site/index.html) |

The ebook is organized into fourteen parts under numbered folders (`01-overview/` … `14-spotify-style-app/`). Each part contains multiple chapters with YAML front matter (`title`, `order`). See [index.md](index.md) for the full reading order.

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
| 12 | `12-custom-ui/` | Decorations, CustomPaint, custom email inbox list |
| 13 | `13-packages/` | HTTP, persistence, audio, desktop |
| 14 | `14-spotify-style-app/` | End-to-end Melody Hub music app project |

HTML is generated with [MDWeb](https://github.com/hoihky/MDWeb) and is best previewed with a local static server (e.g. `npx serve site`) so diagrams, syntax highlighting, and assets load correctly.

## Repository layout

```text
flutter-notes/
├── index.md                 # Ebook home / reading order
├── 01-overview/ … 14-spotify-style-app/
├── theme/                   # MDWeb theme (CSS, JS, templates)
├── site-footer.html         # Custom page footer HTML
├── site/                    # Generated HTML site (MDWeb output)
└── LICENSE
```

## Build the site (MDWeb)

Custom theme and footer live in this repo:

```bash
mdweb \
  --source . \
  --output ./site \
  --theme ./theme \
  --title "Developing Flutter Applications" \
  --description "Flutter and Dart ebook with layout, UI, and capstone projects" \
  --footer-file ./site-footer.html
```

Open `site/index.html` in a browser, or run `npx serve site` for local preview.

## License

This repository is licensed under **[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)** (Creative Commons Attribution-NonCommercial 4.0 International). You may share and adapt the notes for **non-commercial** purposes with **attribution**. The content was created and edited with **AI assistance** and is intended for **educational use** only. The material is provided **without warranty**. Full text and disclaimers: [LICENSE](LICENSE).
