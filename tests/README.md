# Test Scenarios

Two kinds of tests:

- **Automated structural checks** — `python3 scripts/validate_skill.py`. Deterministic; run in CI
  or locally.
- **Behavioral scenarios** (TEST-001 … TEST-010) — prompts given to an agent with the skill
  installed; the output is scored against the verifiable criteria in each file. They require a
  human or LLM evaluator and are **not** executed by the validation script.

## Index and execution status

| ID | Scenario | File | Status |
|---|---|---|---|
| STRUCT | Package structure, frontmatter, links, JSON, tokens contrast, Mermaid lint | [test-skill-structure.md](test-skill-structure.md) | Automated — see `CHANGELOG.md` for last run |
| TEST-001 | User story to design | [test-user-story.md](test-user-story.md) | Pending evaluation |
| TEST-002 | Existing interface review | [test-existing-interface.md](test-existing-interface.md) | Pending evaluation |
| TEST-003 | Accessibility audit | [test-accessibility-review.md](test-accessibility-review.md) | Pending evaluation |
| TEST-004 | Design system generation | [test-design-system.md](test-design-system.md) | Pending evaluation |
| TEST-005 | Responsive specification | [test-responsive.md](test-responsive.md) | Pending evaluation |
| TEST-006 | No destructive changes | [test-file-safety.md](test-file-safety.md) | Pending evaluation |
| TEST-007 | Incomplete requirements | [test-user-story.md](test-user-story.md) | Pending evaluation |
| TEST-008 | Limited tool environment | [test-skill-structure.md](test-skill-structure.md) | Pending evaluation |
| TEST-009 | Cross-module traceability | [test-traceability-regression.md](test-traceability-regression.md) | Pending evaluation |
| TEST-010 | Regression | [test-traceability-regression.md](test-traceability-regression.md) | Pending evaluation |

## How to run a behavioral scenario

1. Install the skill in an agent (see the README).
2. Start a fresh session; paste the **Input** exactly.
3. Score each **Verifiable criterion** as Met / Not met, quoting the output as evidence.
4. A scenario passes when every criterion marked **[must]** is met.
5. Record agent, model, date and result in the scenario's **Execution log**. Do not mark a
   scenario as passed without a recorded run.
