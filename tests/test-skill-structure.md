# STRUCT — Skill structure (automated) · TEST-008 — Limited tool environment

## STRUCT — Automated structural validation

**Command**

```bash
python3 scripts/validate_skill.py            # human-readable
python3 scripts/validate_skill.py --json     # machine-readable
```

**Expected result:** exit code `0`, no `FAIL` lines. A `WARN` about the directory name is expected
when the repository is cloned under a different folder name.

**Covers**

| Check | Criterion |
|---|---|
| Structure | All files listed in `REQUIRED_FILES` exist |
| Frontmatter | `name` = `intelligent-ux-ui-designer`, valid format; `description` ≤ 1024 chars with "Use when" and "Not for"; `compatibility` ≤ 500 chars |
| Body | `SKILL.md` < 500 lines; required sections present; modules 01–10 in the routing table |
| Links | Every relative Markdown link resolves; no absolute paths |
| JSON | All JSON files parse |
| Tokens | All `{references}` resolve; declared contrast pairs meet WCAG minimums |
| Mermaid | Known diagram type; no unquoted `;` inside node labels (basic lint, not a render) |

**Negative checks (manual):** temporarily break a link, rename `name`, or set a contrast pair to
`#999999` on white in a copy of the repo → the script must exit `1` and name the failure.

## TEST-008 — Limited tool environment

**Input** (agent with file read/write only; no browser, Figma, Mermaid renderer or scanners):

> Diseña el flujo y los wireframes de un formulario de alta de usuario para una app de gimnasio.
> Revisa también su accesibilidad.

**Verifiable criteria**

- [must] Produces a Mermaid flow (or text outline) and ASCII/Markdown wireframes.
- [must] Labels wireframes as textual representations; does not claim Figma files, images or
  prototypes.
- [must] Accessibility review states method = static review; marks keyboard, screen reader and
  contrast checks as `NOT VERIFIED` (unless contrast was computed from given hex values, shown).
- [must] Does not try to install tools or call external services.
- [should] Lists which optional tools would enable further verification.

**Execution log**

| Date | Agent / model | Result | Notes |
|---|---|---|---|
| — | — | Not executed | |
