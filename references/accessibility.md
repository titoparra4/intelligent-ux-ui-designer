# Module 07 — Accessibility Reviewer

Standard: **WCAG 2.2, levels A and AA**. Reference: https://www.w3.org/TR/WCAG22/

## Honesty rule

Classify every check by verification method and never upgrade it:

| Method | Meaning | Can conclude |
|---|---|---|
| Static review | Reading code, specs, screenshots | "Likely issue" / "No issue observed in the provided material" |
| Automated check | A tool actually ran (axe, Lighthouse, Pa11y, computed contrast) | Issues the tool detects (~30–40% of WCAG issues) |
| Manual validation | Keyboard, screen reader, zoom, real-device testing actually performed | Conformance of that criterion for the tested scope |

Never state "WCAG 2.2 AA compliant". At most: "No failures found for the criteria checked, using
<methods>; criteria X, Y not verified."

Screenshots cannot verify: keyboard behavior, focus order, accessible names, ARIA, reflow, screen
reader output. Mark these `[NOT VERIFIED]`.

## Review checklist (most frequent criteria)

| Area | WCAG 2.2 criteria |
|---|---|
| Text alternatives | 1.1.1 Non-text Content (A) |
| Structure & semantics | 1.3.1 Info and Relationships (A), 1.3.2 Meaningful Sequence (A), 2.4.6 Headings and Labels (AA), 4.1.2 Name, Role, Value (A) |
| Input purpose | 1.3.5 Identify Input Purpose (AA) — `autocomplete` on personal data |
| Color & contrast | 1.4.1 Use of Color (A), 1.4.3 Contrast Minimum (AA), 1.4.11 Non-text Contrast (AA) |
| Resize & reflow | 1.4.4 Resize Text (AA), 1.4.10 Reflow (AA, 320 CSS px), 1.4.12 Text Spacing (AA) |
| Hover/focus content | 1.4.13 Content on Hover or Focus (AA) |
| Keyboard | 2.1.1 Keyboard (A), 2.1.2 No Keyboard Trap (A) |
| Timing | 2.2.1 Timing Adjustable (A), 2.2.2 Pause, Stop, Hide (A) |
| Navigation | 2.4.1 Bypass Blocks (A), 2.4.2 Page Titled (A), 2.4.3 Focus Order (A), 2.4.4 Link Purpose (A), 2.4.7 Focus Visible (AA) |
| New in 2.2 | 2.4.11 Focus Not Obscured (Minimum) (AA), 2.5.7 Dragging Movements (AA), 2.5.8 Target Size (Minimum) (AA, 24×24 CSS px), 3.2.6 Consistent Help (A), 3.3.7 Redundant Entry (A), 3.3.8 Accessible Authentication (Minimum) (AA) |
| Pointer | 2.5.1 Pointer Gestures (A), 2.5.2 Pointer Cancellation (A), 2.5.3 Label in Name (A) |
| Language | 3.1.1 Language of Page (A), 3.1.2 Language of Parts (AA) |
| Predictability | 3.2.1 On Focus (A), 3.2.2 On Input (A), 3.2.3 Consistent Navigation (AA), 3.2.4 Consistent Identification (AA) |
| Forms & errors | 3.3.1 Error Identification (A), 3.3.2 Labels or Instructions (A), 3.3.3 Error Suggestion (AA), 3.3.4 Error Prevention (Legal, Financial, Data) (AA) |
| Status | 4.1.3 Status Messages (AA) |

Note: 4.1.1 Parsing is obsolete/removed in WCAG 2.2 — do not cite it.

## Contrast computation

If you compute contrast, show inputs and result: relative luminance
`L = 0.2126 R + 0.7152 G + 0.0722 B` (sRGB linearized: `c ≤ 0.04045 ? c/12.92 : ((c+0.055)/1.055)^2.4`),
ratio `(L1 + 0.05) / (L2 + 0.05)`. Mark as `[VERIFIED — computed]`. Colors sampled from a
compressed screenshot are approximate; say so.

## Cognitive accessibility (beyond A/AA, recommend)

Plain language, one task per step, visible progress, no time pressure, predictable layout,
avoid memory load (3.3.7), meaningful error messages with fix instructions.

## Severity

| Severity | Definition |
|---|---|
| Critical | Blocks task completion for a user group (e.g., keyboard trap, unlabeled required field in checkout) |
| High | Major difficulty or workaround needed |
| Medium | Causes friction or confusion; task still possible |
| Low | Minor; best-practice deviation |

## Finding format

| Field | Content |
|---|---|
| ID | `A11Y-001` |
| Element | Screen / component / selector |
| Problem | What fails, for whom |
| WCAG criterion | Number, name, level |
| Severity | Critical / High / Medium / Low |
| Evidence | Source + method (static / automated / manual) |
| Recommendation | Specific fix (code or design) |
| Verification method | How to confirm the fix (e.g., "Tab through form; focus ring visible ≥3:1") |

Template: `assets/templates/accessibility-audit-template.md`.

## Deliverables

Accessibility report with scope, methods, findings, criteria verified / not verified, and a
pending-validation list (screen reader pairs to test, e.g., NVDA+Firefox, VoiceOver+Safari,
TalkBack+Chrome).
