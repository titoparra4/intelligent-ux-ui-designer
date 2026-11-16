# Module 10 — Design Handoff

Goal: specifications developers can build and QA can verify without critical ambiguity.

## Contents

1. **Screen Specification** per `SCR-n` (template `assets/templates/screen-specification-template.md`).
2. **Component Specification / mapping** — design component → code component (existing library
   component if one exists, else new `CMP-n`), props, variants.
3. **Interaction Contract** — trigger → behavior → feedback → focus result → timing.
4. **Validation Rules Matrix** — field, type, required, format, constraints, when validated
   (blur / submit / real-time), message, source rule.
5. **States** — loading, empty, error, success, disabled, timeout, unauthorized per screen.
6. **Keyboard interactions** — tab order, shortcuts, focus management after actions.
7. **Responsive behavior** — per range (link to module 08 output).
8. **Technical dependencies** — APIs, fields required from each endpoint, error codes to handle.
9. **UX Acceptance Criteria** — Given / When / Then.
10. **QA Test Scenarios** — positive, negative, boundary, accessibility, responsive.
11. **Traceability Matrix**.

Template: `assets/templates/design-handoff-template.md`.

## Interaction Contract format

| ID | Element | Trigger | Behavior | Feedback | Focus after | Notes |
|---|---|---|---|---|---|---|
| INT-01 | Continue button (SCR-003) | Click / Enter | Validate all fields | If errors: summary + inline | Error summary heading | Data preserved |

## Validation Rules Matrix

| Field | Required | Format / constraint | Validate on | Error message | Rule source |
|---|---|---|---|---|---|
| Email | Yes | RFC-like email pattern | Blur + submit | "Enter an email like name@example.com" | REQ-004 |

Messages: state what happened and how to fix it; no codes alone; no blame.

## UX Acceptance Criteria rules

- Format: `AC-n — <title>` then Given / When / Then (And …).
- Each `Then` is observable and testable (UI state, message, focus position, data retained).
- Cover: happy path, each validation rule, each error path, state transitions, keyboard,
  screen-reader announcements, responsive behavior where it changes behavior.
- Avoid subjective terms ("intuitive", "fast", "nice"). Replace with measurable or observable
  conditions, or mark the threshold as `DEC-n — PENDING`.

Example:

```gherkin
AC-001 — Required fields validation
Given the user is completing the vehicle details form (SCR-003)
When they select "Continue" with one or more required fields empty
Then the form is not submitted
And an error summary listing each empty field appears above the form and receives focus
And each empty field shows an inline message linked via aria-describedby
And previously entered values are preserved
```

## QA Test Scenarios

| QA ID | AC | Type | Preconditions | Steps | Expected result | Priority |
|---|---|---|---|---|---|---|
| QA-001 | AC-001 | Negative | On SCR-003 | Leave plate empty → Continue | Summary + inline error, focus on summary | High |

Types: Positive, Negative, Boundary, Accessibility, Responsive, Resilience (API failure/timeout).

## Traceability Matrix

| REQ | US | FLOW | SCR | CMP | AC | QA | DD |
|---|---|---|---|---|---|---|---|

Every `US` must reach at least one `AC` and one `QA`. Flag gaps as Gate 1 / Gate 7 issues.

## Regression / change impact

When a requirement changes: find the row(s) in the traceability matrix, list every downstream
artifact affected, propose updates only to those, and update only artifacts the user authorizes.
Keep existing IDs; deprecate instead of renumbering (`AC-007 — DEPRECATED by AC-015`).
