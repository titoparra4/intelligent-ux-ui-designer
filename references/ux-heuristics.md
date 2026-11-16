# Module 09 — UX Heuristic Evaluator

Framework: Jakob Nielsen's 10 usability heuristics (NN/g).

| # | Heuristic | Look for |
|---|---|---|
| H1 | Visibility of system status | Progress, loading feedback, confirmation, saved state |
| H2 | Match between system and the real world | User vocabulary, natural order, real-world conventions |
| H3 | User control and freedom | Undo, cancel, back without data loss, exit from flows |
| H4 | Consistency and standards | Same words/components for same meaning; platform conventions |
| H5 | Error prevention | Constraints, defaults, confirmation for destructive actions, format hints |
| H6 | Recognition rather than recall | Visible options, recently used, summaries before submit |
| H7 | Flexibility and efficiency of use | Shortcuts, autofill, saved preferences, bulk actions |
| H8 | Aesthetic and minimalist design | Signal-to-noise, hierarchy, no irrelevant content |
| H9 | Help users recognize, diagnose and recover from errors | Plain language, cause, specific fix |
| H10 | Help and documentation | Contextual help, findable, task-oriented |

## Process

1. **Scope** — screens / flows, personas and tasks evaluated, inputs available.
2. **Walk the tasks** — evaluate per step, not per page in isolation.
3. **Record findings** with evidence (screenshot region, element, code line).
4. **Rate severity** with the rubric below.
5. **Deduplicate and cluster** by root cause.
6. **Prioritize** — severity × frequency × reach, then effort.
7. **Recommend** — before / after, with validation method.

A single evaluator finds a subset of issues; recommend 3–5 evaluators for a full study.

## Severity rubric (Nielsen 0–4)

| Level | Label | Definition |
|---|---|---|
| 0 | Not a problem | — |
| 1 | Cosmetic | Fix if time allows |
| 2 | Minor | Low priority; causes small friction |
| 3 | Major | High priority; users struggle or make errors |
| 4 | Catastrophe | Blocks task or causes serious error; fix before release |

Severity considers frequency, impact and persistence. State the rationale in one line.

## Finding format

| Field | Content |
|---|---|
| Finding ID | `UX-001` |
| Screen / Component | `SCR-n` / `CMP-n` / description |
| Violated heuristic | `H1`–`H10` (+ secondary) |
| Evidence | What was observed and where, with source |
| Severity | 0–4 + rationale |
| User impact | Who is affected and how |
| Business impact | Qualitative (e.g., "may increase support contacts") — **never invented numbers** |
| Recommended improvement | Specific change |
| Validation method | Usability test task, A/B test, analytics event, expert re-review |

## No fabricated metrics

Do not state drop-off rates, conversion, time-on-task or satisfaction scores unless the user
provided them (cite `[SRC-n]`). Phrase as hypotheses: "likely increases abandonment at step 3
[HYPOTHESIS]".

## Deliverables

Heuristic Evaluation Report, UX Findings Backlog, Prioritized Improvement Plan (Now / Next /
Later), Before / After Recommendations.
