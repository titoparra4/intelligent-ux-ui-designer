# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses
[Semantic Versioning](https://semver.org/).

## [1.0.0] - 2026-11-16

### Added

- `SKILL.md` orchestrator: activation / non-activation conditions, language rule, input
  handling with evidence labels, six operational modes (A–F), module routing, workflow, output
  contracts with stable IDs, quality gates, safety rules and optional integrations.
- Ten module references: UX research, user journey, information architecture, user flows,
  wireframes, design system, accessibility (WCAG 2.2 A/AA), responsive design, UX heuristics,
  design handoff; plus design principles and quality gates.
- Six deliverable templates and a worked insurance example (story, flow, wireframes, handoff,
  design tokens).
- `scripts/validate_skill.py` (standard library only): structure, frontmatter, links, JSON,
  token references, WCAG contrast of declared token pairs, Mermaid lint.
- Structural test and behavioral scenarios TEST-001 … TEST-010.
- English and Spanish READMEs, MIT license, CI workflow, optional Codex metadata.

### Validation

- Structural validation: executed locally on 2026-11-16 with Python 3 — 11 passed, 0 failed
  (1 expected warning: local clone folder name differs from the skill name). Negative run on a
  deliberately broken copy (invalid name, broken link, low-contrast token, unquoted Mermaid `;`)
  failed as expected with exit code 1.
- Behavioral scenarios TEST-001 … TEST-010: defined, **not yet executed**.
