# TEST-004 — Design system generation

## Case A — New system

**Input**

> Create a design system foundation for a B2B analytics web app: tokens and specs for Button,
> Input, Select, Table, Tabs, Modal and Notification.

**Verifiable criteria**

- [must] Mode C stated.
- [must] Tokens in JSON using `$value` / `$type`, with a primitive and a semantic layer; semantic
  tokens reference primitives.
- [must] Saved tokens pass `validate_skill.py`-style checks (valid JSON, references resolve).
- [must] Each component spec includes variants, sizes, states, tokens used, keyboard model and
  accessibility notes.
- [must] Component states matrix present.
- [must] Contrast claims are either computed and shown, or marked NOT VERIFIED.
- [should] Usage guidelines with when to use / when not to use.
- [should] Dense-data considerations for tables (sorting, row actions, responsive strategy).

## Case B — Existing system must be respected

**Input:** a project with `src/styles/tokens.css` defining `--color-primary: #0052CC;` and a
`Button` component, plus the prompt:

> Add a destructive button variant and an alert component.

**Verifiable criteria**

- [must] Inventories and reuses existing tokens/components first.
- [must] Proposes new tokens/variants as additions; does not rename or replace `--color-primary`
  or the existing `Button`.
- [must] Does not edit the files without explicit authorization (see TEST-006).

**Execution log**

| Case | Date | Agent / model | Result | Notes |
|---|---|---|---|---|
| A | — | — | Not executed | |
| B | — | — | Not executed | |
