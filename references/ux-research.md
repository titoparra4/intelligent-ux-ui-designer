# Module 01 — UX Research Assistant

Goal: understand users and the business problem **before** proposing a solution.

## Honesty rule

Everything this module produces from desk analysis is a **proto-persona** or **hypothesis**, not a
research finding. Label it `[ASSUMPTION]` or `[HYPOTHESIS]`. Only data the user supplies from real
research (interview notes, survey results, analytics exports) may be labelled `[VERIFIED]`, and
cite the source (`[SRC-n]`). Never invent quotes, participant counts, percentages or metrics.

## Process

1. **Problem framing** — business goal, user problem, success signal, constraints.
2. **Segments** — who uses it, in what context, with what frequency and expertise. Split by
   behavior and need, not demographics alone.
3. **Proto-personas** — 2–4 maximum; more dilutes decisions.
4. **Needs matrix** — needs × segments with priority (Must / Should / Could).
5. **JTBD** — `When <situation>, I want to <motivation>, so I can <expected outcome>.`
6. **Hypotheses backlog** — `We believe <change> for <segment> will result in <outcome>. We will
   know when <measurable signal>.`
7. **Knowledge gaps and risks** — what is unknown and what it would change.
8. **Research plan** — questions, method, participants, effort.

## Method selection

| Question type | Method | Typical effort |
|---|---|---|
| Why / what do they need? | Semi-structured interviews (5–8 per segment) | Medium |
| How many / how much? | Survey (validated questions, avoid leading wording) | Medium |
| Can they complete it? | Moderated or unmoderated usability test (5 per round) | Medium |
| Where do they drop off? | Analytics funnel review (needs real data) | Low |
| How do they organize content? | Card sorting (open/closed) | Low–Medium |
| Can they find it? | Tree testing | Low |
| What happens in context? | Contextual inquiry / diary study | High |

Interview guide rules: open questions, past behavior over future intent ("Tell me about the last
time you…"), no leading questions, no feature pitches.

## Output formats

### Proto-persona

```markdown
### PER-01 — <Name> (proto-persona) [ASSUMPTION]
- Context: <role, environment, device, frequency>
- Goals: …
- Needs: …
- Frustrations: …
- Expertise: novice | intermediate | expert (domain / digital)
- Accessibility considerations: <e.g., low vision, one-handed mobile use> (only if relevant)
- Evidence basis: <sources or "desk assumption">
- Validate by: <method>
```

### User Needs Matrix

| Need ID | Need | PER-01 | PER-02 | Priority | Evidence |
|---|---|---|---|---|---|
| N-01 | … | High | Low | Must | [ASSUMPTION] |

### Hypotheses backlog

| ID | Hypothesis | Risk if wrong | Validation method | Signal |
|---|---|---|---|---|
| H-01 | … | High | Usability test | ≥4/5 complete task unaided |

Use target signals as **validation thresholds to define**, not as results.

## Deliverables

UX Research Brief (template: `assets/templates/ux-research-template.md`), Proto-personas, User
Needs Matrix, JTBD, Hypotheses Backlog, Research Questions.
