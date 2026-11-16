# Module 08 — Responsive Design

Goal: experiences that adapt to device, viewport, input mode and user settings.

## Principles

- **Content-first breakpoints.** Add a breakpoint where the layout breaks for *this* content, not
  because a device exists. Starting values are allowed but must be justified.
- **Mobile-first** when the primary context is mobile or the content benefits from prioritization;
  say so explicitly if desktop-first is more appropriate (e.g., dense data back-office).
- **Fluid by default.** Relative units (`rem`, `%`, `fr`), `clamp()` for type/spacing, intrinsic
  layouts (flex-wrap, grid `auto-fit/minmax`), container queries for reusable components.
- **Input modes.** Touch targets ≥ 24×24 CSS px (WCAG 2.5.8), 44×44 recommended; no hover-only
  features; support keyboard on every size.
- **User settings.** 200% text zoom (1.4.4), 400% zoom / 320 CSS px reflow without 2-D scrolling
  (1.4.10), orientation not locked (1.3.4), `prefers-reduced-motion`, `prefers-color-scheme` if
  theming.

## Breakpoint Matrix (starting point — adjust to content)

| Range | Name | Columns | Gutter / margin | Typical changes |
|---|---|---|---|---|
| < 600px | Compact | 4 | 16 / 16px | Single column, stacked actions, bottom-anchored primary CTA if long forms |
| 600–1023px | Medium | 8 | 24 / 24px | Two-column where content allows, nav may collapse |
| ≥ 1024px | Expanded | 12 | 24 / 32px+ | Side summary panels, persistent nav, max content width ~ 1200–1440px |

Justify each change in the matrix with the content reason (`DD-n`).

## Adaptive component rules

| Component | Compact | Medium | Expanded |
|---|---|---|---|
| Navigation | Menu button + drawer or bottom nav (≤5 items) | Collapsible | Persistent top/side |
| Tables | Cards or priority columns + row expansion; never squeeze | Horizontal scroll inside a labelled region as last resort | Full table |
| Forms | 1 column, full-width inputs | 1–2 columns by logical pairs | Max line length ~ 60–75 ch |
| Modals | Full-screen sheet | Centered | Centered |
| Summary panel | Collapsible above CTA | Below content | Sticky side panel |

## Layout Behavior Specification

Per screen: region order per range, what hides vs collapses (never hide essential content or
functions on small screens), sticky elements (must not obscure focus — 2.4.11), overflow rules,
image behavior (`srcset`, aspect ratio), text truncation policy (avoid truncating critical data).

## Review checks

Overflow at 320px, legibility (min 16px body), orientation, zoom 200/400%, sticky elements vs
focus and on-screen keyboard, touch target spacing. Mark as `[NOT VERIFIED]` unless tested in a
real or emulated viewport.

## Deliverables

Responsive Strategy, Breakpoint Matrix, Adaptive Component Rules, Responsive Wireframes (compact
and expanded at minimum), Layout Behavior Specification.
