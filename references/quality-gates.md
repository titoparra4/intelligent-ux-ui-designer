# Quality Gates

Run before closing modes A–E (and the relevant subset in mode F). Each gate ends as:

- **PASS** — criteria met, with evidence.
- **FAIL** — a criterion is not met; list the gap and action.
- **NOT VERIFIED** — cannot be determined with available inputs/tools; list what is needed.

Never mark PASS by default. When in doubt, NOT VERIFIED.

| Gate | Checks | PASS requires |
|---|---|---|
| G1 Requirements Coverage | Every provided `REQ`/`US`/AC maps to at least one flow/screen | Traceability matrix with no unmapped input; deferred items explicitly listed |
| G2 UX Coherence | Flows ↔ screens ↔ navigation consistent; labels, CTAs, patterns consistent; every flow exit defined | Cross-screen consistency check done, no unresolved conflicts |
| G3 Accessibility | Applicable WCAG 2.2 A/AA criteria considered for the deliverable | Each relevant criterion classified as addressed / issue / not verified, with method. Can only be PASS for the scope and method stated |
| G4 Design System Consistency | Components and tokens reused; no ad-hoc values; existing system respected | Every UI element maps to a `CMP`/token or a justified new one |
| G5 Responsive Feasibility | Behavior specified for compact/medium/expanded and touch/keyboard | Layout rules per range for every screen in scope |
| G6 Development Readiness | States, validations, interactions, dependencies, error handling specified | No critical ambiguity; open questions listed as `DEC-n` with owner |
| G7 QA Readiness | AC are testable; positive and negative paths covered | Every US has ≥1 positive and ≥1 negative AC; every AC has a QA scenario |
| G8 Evidence & Honesty | No assumption presented as fact; no unexecuted check presented as result; no invented metrics/research/integrations | All claims labelled; NOT VERIFIED items listed |

## Gate summary format

```markdown
| Gate | Status | Evidence | Pending actions |
|---|---|---|---|
| G1 Requirements Coverage | PASS | Traceability matrix §7: 6/6 US mapped | — |
| G3 Accessibility | NOT VERIFIED | Static review only; contrast not computed | Run axe; keyboard + NVDA test on SCR-003..006 |
| G8 Evidence & Honesty | PASS | All personas labelled proto-persona; no metrics used | — |
```

Gates not applicable to a focused task: list as `N/A — <reason>`.
