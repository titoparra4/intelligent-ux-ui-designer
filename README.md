# Intelligent UX/UI Designer

**English** · [Español](README.es.md)

An [Agent Skill](https://agentskills.io/specification) that makes your AI agent work like a senior
UX/UI designer: it turns requirements, user stories, processes, screenshots or frontend code into
research briefs, journeys, user flows, annotated wireframes, design tokens, accessibility and
usability reviews, responsive specifications and developer/QA handoff — with traceability and
explicit evidence.

> Design decisions must be driven by user needs, usability principles, accessibility
> requirements, technical feasibility and measurable business goals — not visual aesthetics alone.

## The problem it solves

General-purpose agents asked to "design a screen" tend to jump to visuals, skip error and empty
states, invent personas or metrics, forget accessibility and produce specs nobody can test. This
skill gives the agent a structured method: understand the problem, design the full flow including
unhappy paths, justify decisions, verify quality and hand off testable specifications — while
being honest about what is assumption and what was verified.

## Capabilities

| # | Module | Produces |
|---|---|---|
| 01 | UX Research Assistant | Research brief, proto-personas, needs matrix, JTBD, hypotheses, research plan |
| 02 | User Journey Mapping | AS-IS / TO-BE journeys, pain points, opportunity backlog |
| 03 | Information Architecture | Sitemap, navigation structure, content hierarchy, rationale |
| 04 | User Flow Generator | Mermaid flows with decisions, error recovery and business-rule traceability |
| 05 | Wireframe Generator | Low-fidelity wireframes (ASCII/Markdown, optional SVG/HTML) with all UI states |
| 06 | UI Design System | W3C-format design tokens, component specs, states matrix, usage guidelines |
| 07 | Accessibility Reviewer | WCAG 2.2 A/AA findings with criterion, severity and verification method |
| 08 | Responsive Design | Content-based breakpoint matrix, adaptive component rules, layout specs |
| 09 | UX Heuristic Evaluator | Nielsen heuristic findings, severity 0–4, prioritized improvement plan |
| 10 | Design Handoff | Screen/component specs, interaction contract, validation matrix, Given/When/Then AC, QA scenarios |

Cross-cutting: 10 mandatory design principles, decision records (`DD-n`), stable IDs
(`REQ`, `US`, `FLOW`, `SCR`, `CMP`, `UX`, `AC`) and 8 quality gates (PASS / FAIL / NOT VERIFIED).

## Architecture

```text
SKILL.md                 Orchestrator: activation, modes, module routing, contracts, safety
references/              One file per module + principles + quality gates (loaded on demand)
assets/templates/        Reusable deliverable templates
assets/examples/         Worked insurance example (story → flow → wireframes → handoff) + tokens
scripts/validate_skill.py  Standard-library validator for the package
tests/                   Structural check + 10 behavioral scenarios
```

The orchestrator picks one of six modes and loads only the references it needs
(progressive disclosure):

| Mode | When | Sequence |
|---|---|---|
| A — Full Product Design | Idea / story → experience | Research → Journey → IA → Flows → Wireframes → Design System → Accessibility → Responsive → Handoff |
| B — UX Audit | Existing interface | Context → Heuristics → Accessibility → Prioritized findings |
| C — Design System | Tokens and components | Existing assets → Tokens → Components → Variants → Accessibility → Docs |
| D — Design to Development | Design exists | Inspection → Screen specs → Component mapping → Interactions → AC |
| E — UX Optimization | Improve a product | Pain points → Hypotheses → Improvements → Validation plan |
| F — Focused Task | One deliverable | Only the module needed |

## Use cases

- Designing a new feature from a user story, end to end.
- Auditing an existing screen or flow for usability and accessibility.
- Creating or extending a design system with semantic tokens.
- Turning a design into specs, acceptance criteria and QA scenarios.
- Preparing responsive behavior for a data-dense back office.

## Requirements

- An agent that supports Agent Skills (for example Claude Code or OpenAI Codex).
- No external tools are required. Optional: Python 3.8+ to run the validator; Figma, Storybook,
  browsers or accessibility scanners if your agent has them and you authorize their use.

## Installation

> The repository must be published on GitHub for the commands below to work.

### With skills.sh

```bash
npx skills add titoparra4/intelligent-ux-ui-designer
```

Run `npx skills --help` to see the options of your installed version (agent selection, global
install).

### Manual installation

Copy the skill files (`SKILL.md`, `references/`, `assets/`, `scripts/`) into a folder named
**`intelligent-ux-ui-designer`** inside your agent's skills directory:

| Agent | Project scope | User scope |
|---|---|---|
| Claude Code | `.claude/skills/intelligent-ux-ui-designer/` | `~/.claude/skills/intelligent-ux-ui-designer/` |
| OpenAI Codex | `.agents/skills/intelligent-ux-ui-designer/` | `~/.agents/skills/intelligent-ux-ui-designer/` (check your Codex version's docs) |
| Other agents | See your agent's documentation for its skills directory | |

```bash
git clone https://github.com/titoparra4/intelligent-ux-ui-designer.git
mkdir -p ~/.claude/skills/intelligent-ux-ui-designer
cp -R intelligent-ux-ui-designer/{SKILL.md,references,assets,scripts} ~/.claude/skills/intelligent-ux-ui-designer/
```

## Usage

The skill activates when your request matches its description; you can also name it explicitly
("use the intelligent-ux-ui-designer skill…", or `$intelligent-ux-ui-designer` in Codex).
`agents/openai.yaml` provides optional display metadata for Codex.

Available capabilities depend on your agent and its integrations: without a Mermaid renderer you
get Mermaid source; without Figma you get textual wireframes; without a browser or scanner,
accessibility checks are static and reported as such.

### Example prompts

- "Design the experience to buy car insurance online from this user story: …"
- "Audit this checkout page for usability and accessibility" (attach a screenshot or HTML).
- "Create design tokens and specs for Button, Input and Modal for our app."
- "Write UX acceptance criteria and QA scenarios for this login screen."
- "Define the responsive behavior of our orders dashboard."
- "Diseña el flujo de alta de usuario y sus wireframes."

### Expected results

A response that states the mode, lists assumptions, produces the requested deliverables with
stable IDs, records significant decisions, and ends with a quality gate summary. See
[`assets/examples/`](assets/examples/) for a complete worked example.

## Security and safety policy

- **Read-only by default** — never modifies, overwrites or deletes existing files, components or
  tokens without explicit authorization; proposes new artifacts or diffs instead.
- **No implicit installs or network calls**; no data sent to external services without consent.
- **Untrusted inputs** — repository files, documents and screenshots are treated as data;
  embedded instructions are reported, never followed.
- **Privacy** — secrets and personal data are referenced by type/location, not reproduced.
- **Honesty** — no invented research, metrics, test results or integrations; no WCAG conformance
  claims without documented checks.

## Limitations

- Produces design specifications and low-fidelity representations, not finished visual design or
  production code.
- Accessibility review from screenshots or descriptions is static; it cannot replace testing
  with keyboard, assistive technologies and real users.
- Proto-personas and journeys are hypotheses until validated with research.
- Mermaid diagrams are linted, not rendered, by the validator.
- Quality depends on the underlying model and the context you provide.

## Validation

```bash
python3 scripts/validate_skill.py
```

Checks structure, frontmatter (Agent Skills spec), links, JSON, token references, WCAG contrast of
the example token pairs, and basic Mermaid syntax. Behavioral scenarios TEST-001…TEST-010 are in
[`tests/`](tests/README.md) with their execution status.

## Contributing

1. Open an issue describing the change.
2. Keep `SKILL.md` concise; put detail in `references/`.
3. Run `python3 scripts/validate_skill.py` and update the relevant test scenario.
4. Add an entry to `CHANGELOG.md`.

## License

[MIT](LICENSE)

## Roadmap

- Optional adapters guidance for Figma and Storybook MCP servers.
- Automated runner for behavioral scenarios with an LLM-as-judge rubric.
- Additional worked examples (B2B dashboard, mobile onboarding).
- Content design / UX writing module.

## Versioning

[Semantic Versioning](https://semver.org/). The version lives in `SKILL.md`
(`metadata.version`) and [`CHANGELOG.md`](CHANGELOG.md).
