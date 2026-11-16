# Module 05 — Wireframe Generator

Goal: convert flows into usable screen structures with explicit behavior and states.

## Honesty rule

A wireframe in Markdown/ASCII/SVG/HTML is a **textual representation**. Name it exactly that.
Never claim a Figma file, image, or interactive prototype exists unless a tool actually created it
and returned a reference.

## Representation choice

| Environment / request | Format |
|---|---|
| Default, chat or terminal | ASCII box wireframe in a code block + annotation table |
| User asks for something visual and files can be written | Static HTML (semantic, no external deps) or SVG |
| Figma tool available and authorized | Figma adapter; still keep the textual spec as source of truth |

ASCII conventions: `[ Button ]`, `( ) radio`, `[x] checkbox`, `[____] input`, `[v] select`,
`==== ` header bar, `▸` link, `⚠` error, `…` loading. Width ~60 chars; one wireframe per state
only when the layout changes; otherwise describe the state in the table.

```text
+----------------------------------------------------------+
| ==== Logo                         Help ▸   Sign in ▸ ==== |
| Step 2 of 6 · Vehicle details        [■■□□□□]            |
|                                                          |
| Licence plate *        [__________]                      |
| Year *                 [v 2024     ]                     |
| ⚠ Enter a year between 1980 and 2026                     |
|                                                          |
| [ Back ]                               [ Continue → ]    |
+----------------------------------------------------------+
```

## Mandatory screen documentation

1. Screen ID (`SCR-n`) 2. Screen name 3. User goal 4. Related user story (`US-n`) 5. Layout
structure (regions, order, reading order) 6. Components (`CMP-n` when defined) 7. Interactions
8. States 9. Accessibility considerations 10. Design rationale (`DD-n` references).

Template: `assets/templates/screen-specification-template.md`.

## States (cover each that applies; say "N/A — reason" otherwise)

| State | Specify |
|---|---|
| Default | Initial content, prefilled values, focus position |
| Loading | Skeleton vs spinner; what stays interactive; announced to AT (`aria-busy`/live region) |
| Empty | Explanation + primary action, never a blank area |
| Error | System error: message, cause in plain words, recovery action, data preserved |
| Success | Confirmation, next step, reference number if any |
| Disabled | Why disabled, how to enable (prefer keeping enabled + validating) |
| Validation error | Inline per field + summary on submit; focus moves to summary or first error |
| Partial completion | Saved progress indicator, resume path |
| Timeout | Warning before expiry when possible (WCAG 2.2.1), extend option, data retention |
| Unauthorized / Forbidden | 401 → re-authenticate and return; 403 → explain, offer alternative |

## Layout and hierarchy heuristics

- One primary action per screen region; secondary actions visually subordinate.
- Reading order in DOM = visual order.
- Group related fields (fieldset/legend); ask only what is needed at that step.
- Labels above inputs on forms for scanability and zoom; do not use placeholder as label.
- Primary CTA position consistent across steps.

## Cross-screen consistency check

After drafting all screens, check: same component for same job, same labels for same action, CTA
placement, progress indicator, error pattern, back/cancel behavior. Report inconsistencies.

## Deliverables

Screen inventory, low-fidelity wireframes, screen specifications, state coverage table.
