# Mandatory Design Principles

Evaluate every significant proposal against these ten principles. Not every principle produces
a note; flag the ones that drive or constrain the decision.

| # | Principle | Ask |
|---|---|---|
| P1 | User-centered design | Which user need (`N-n`) or JTBD does this serve? |
| P2 | Simplicity and clarity | Can a step, field, option or word be removed? |
| P3 | Consistency and predictability | Does it reuse existing patterns, labels and components? |
| P4 | Accessibility by design | Does it work with keyboard, screen reader, zoom, low vision, cognitive load? |
| P5 | Error prevention and recovery | What can go wrong, and how does the user recover without losing work? |
| P6 | Responsive and adaptive behavior | How does it behave across sizes and input modes? |
| P7 | Reusability and maintainability | Is it a reusable component/token or a one-off? |
| P8 | Technical feasibility | What does it require from APIs, data and frontend? Any unknowns? |
| P9 | Business alignment | Which business goal does it support? Any conflict with user needs? |
| P10 | Evidence-based decisions | What evidence supports it? What would invalidate it? |

When user needs and business goals conflict (e.g., collecting extra marketing data in a checkout),
make the conflict explicit, recommend the user-respecting option, and present the trade-off; do
not hide it. Dark patterns (forced continuity, confirmshaming, hidden costs, pre-ticked consent,
roach motels) are never recommended; flag them when found.

## Decision Rationale (`DD-n`)

Record each significant decision (template `assets/templates/design-decision-template.md`):

| Field | Content |
|---|---|
| Decision | What is proposed |
| Problem | What it solves |
| Evidence / assumption | `[VERIFIED]` source or `[ASSUMPTION]` |
| Principle(s) | P1–P10 |
| Expected benefit | Qualitative unless data was provided |
| Trade-offs | What is given up |
| Risk | What could go wrong |
| Validation method | How to confirm it |
| Status | Proposed / Accepted / Rejected / Pending |

A decision is "significant" when it affects navigation, flow structure, data collected, a shared
component or token, accessibility, or is costly to reverse.

## Observation vs hypothesis vs recommendation

- Observation: "The 'Continue' button is grey (#B0B0B0) on white [VERIFIED — SRC-2]."
- Hypothesis: "Users may read it as disabled [HYPOTHESIS]."
- Recommendation: "Use `color.action.primary.bg` for the primary CTA [RECOMMENDATION]."

Never merge the three into a single assertion.
