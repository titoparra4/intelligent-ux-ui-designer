# TEST-009 — Cross-module traceability · TEST-010 — Regression

## TEST-009 — Cross-module traceability

**Input**

> Using these stories, produce flows, screens, components, acceptance criteria and QA scenarios:
> US-001 As a member I want to book a class so I can secure my spot.
> US-002 As a member I want to cancel a booking so the spot is freed.
> US-003 As a member I want to join a waitlist when a class is full.

**Verifiable criteria**

- [must] Stable IDs used consistently (`US`, `FLOW`, `SCR`, `CMP`, `AC`, `QA`).
- [must] Traceability matrix where every US maps to ≥1 FLOW, SCR, AC and QA.
- [must] Every AC is referenced by ≥1 QA scenario; every QA references an existing AC.
- [must] Every SCR referenced in flows exists in the screen inventory (no dangling IDs).
- [must] Each US has ≥1 positive and ≥1 negative AC (G7).
- [should] Shared components reused across screens (same CMP ID for the same job).

## TEST-010 — Regression

**Input** (continuing the TEST-009 session):

> Change: cancellations are only allowed up to 2 hours before the class. Update only the
> acceptance criteria; I will update the wireframes myself.

**Verifiable criteria**

- [must] Lists all artifacts affected by the change (flow decision, cancel screen states, AC, QA).
- [must] Updates only acceptance criteria (and QA only if asked / or clearly marks QA as needing
  update without changing it).
- [must] Keeps existing IDs; new criteria get new IDs; replaced ones are marked deprecated, not
  renumbered.
- [must] Flags wireframes and flow as "affected — not updated (user will update)".
- [must] Edge case covered: exactly 2 hours before, timezone of the class (assumption or question).

**Execution log**

| Test | Date | Agent / model | Result | Notes |
|---|---|---|---|---|
| TEST-009 | — | — | Not executed | |
| TEST-010 | — | — | Not executed | |
