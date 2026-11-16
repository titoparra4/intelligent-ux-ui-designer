# Module 06 — UI Design System

Goal: create or extend a coherent, reusable, framework-agnostic design system.

## Existing system first

If a design system, theme or tokens exist (CSS custom properties, `tailwind.config.*`, theme
files, token JSON, component library), **inventory and extend it**. Map new needs onto existing
tokens; propose additions as a separate diff/proposal. Replacing or renaming existing tokens
requires explicit authorization.

## Token architecture

Three layers; components consume only semantic or component tokens.

1. **Primitive** — raw values: `color.blue.600`, `space.4`, `font.size.300`.
2. **Semantic** — intent: `color.action.primary.bg`, `color.text.default`, `color.feedback.error.text`,
   `space.inset.md`.
3. **Component** (optional) — `button.primary.bg` → references a semantic token.

Format: W3C Design Tokens Community Group (`$value`, `$type`, references `{color.blue.600}`). See
`assets/examples/design-tokens-example.json`.

### Categories

| Category | Guidance |
|---|---|
| Color | Semantic roles: text, surface, border, action, feedback (info/success/warning/error), focus. Provide light and dark values when theming is in scope. Never encode meaning by color alone. |
| Typography | Modular scale (e.g., 1.2 or 1.25 ratio) from a 16px base; tokens for family, size, weight, line-height (≥1.5 for body). Use `rem`. |
| Spacing | 4px or 8px base scale (`space.1 = 4px` …). |
| Grid | Columns, gutters, margins per breakpoint (see responsive module). |
| Radius | 3–5 steps; `radius.full` for pills. |
| Elevation | Shadow + z-index scale tied to layers (dropdown, sticky, modal, toast). |
| Motion | Durations and easings; respect `prefers-reduced-motion`. |
| Focus | Dedicated focus ring token meeting contrast (see accessibility). |

### Contrast requirements for color tokens

- Text vs background: ≥ 4.5:1 (normal), ≥ 3:1 (large: ≥ 24px or ≥ 18.66px bold).
- UI component boundaries and focus indicators vs adjacent colors: ≥ 3:1.
- Report computed ratios only if actually computed (WCAG relative luminance formula); otherwise
  `[NOT VERIFIED]`.

## Component specification

For each component (`CMP-n`):

| Field | Content |
|---|---|
| Purpose / when to use / when not to use | |
| Anatomy | Named parts |
| Variants | e.g., primary, secondary, tertiary, destructive |
| Sizes | sm / md / lg with min target size ≥ 24×24 CSS px (44×44 recommended for touch) |
| States | default, hover, focus-visible, active, disabled, loading, error, selected (as applicable) |
| Tokens used | |
| Behavior | Interaction rules, keyboard |
| Accessibility | Role, name, ARIA (prefer native HTML), keyboard model |
| Content guidelines | Label length, tone, casing |
| Responsive behavior | |

Reference components: Button, Input, Select, Checkbox, Radio, Card, Modal, Dialog, Navigation Bar,
Table, Tabs, Notification/Toast, Tooltip, Accordion, Breadcrumbs, Progress Indicator.

### Keyboard models (summary)

| Component | Keys |
|---|---|
| Button | Enter, Space |
| Checkbox | Space |
| Radio group | Arrow keys move and select; Tab enters/leaves group |
| Tabs | Arrow keys between tabs; Tab into panel; Home/End |
| Modal/Dialog | Focus moves in, trapped, Esc closes, focus returns to trigger |
| Accordion | Enter/Space toggles header |
| Menu / listbox | Arrows, Home/End, typeahead, Esc |
| Tooltip | Shows on focus and hover, dismissible with Esc, hoverable (WCAG 1.4.13) |

## Component States Matrix

| CMP | Default | Hover | Focus | Active | Disabled | Loading | Error | Selected |
|---|---|---|---|---|---|---|---|---|

## Naming

`<category>.<role>.<variant>.<state>` for tokens; components in PascalCase; variants as props
(`variant="secondary"`). Consistent across design and code.

## Deliverables

Design System Specification, Design Tokens JSON, Component Inventory, Component States Matrix,
Usage Guidelines, Component Accessibility Notes.
