#!/usr/bin/env python3
"""Validate the intelligent-ux-ui-designer skill package.

Self-contained: Python 3.8+ standard library only. Read-only: it never modifies files and makes
no network calls.

Checks
  1. Required files and directories exist.
  2. SKILL.md frontmatter follows the Agent Skills specification (name, description, optional
     fields, length limits) and the body stays under 500 lines.
  3. Relative Markdown links in every .md file resolve to existing files.
  4. Every JSON file parses.
  5. Design token files: every {reference} resolves and every declared contrast pair meets its
     WCAG minimum ratio (computed with the WCAG 2.x relative luminance formula).
  6. Mermaid code blocks declare a known diagram type and have no unquoted ';' inside node labels.

Usage
  python3 scripts/validate_skill.py [SKILL_ROOT] [--json]

Exit code 0 when no check fails, 1 otherwise. Warnings do not fail the run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_ID = "intelligent-ux-ui-designer"

REQUIRED_FILES = [
    "SKILL.md", "README.md", "README.es.md", "LICENSE", "CHANGELOG.md", ".gitignore",
    "references/ux-research.md", "references/user-journey.md",
    "references/information-architecture.md", "references/user-flows.md",
    "references/wireframes.md", "references/design-system.md", "references/accessibility.md",
    "references/responsive-design.md", "references/ux-heuristics.md",
    "references/design-handoff.md", "references/design-principles.md",
    "references/quality-gates.md",
    "assets/templates/ux-research-template.md", "assets/templates/user-journey-template.md",
    "assets/templates/screen-specification-template.md",
    "assets/templates/design-handoff-template.md",
    "assets/templates/accessibility-audit-template.md",
    "assets/templates/design-decision-template.md",
    "assets/examples/insurance-user-story.md", "assets/examples/insurance-user-flow.md",
    "assets/examples/insurance-wireframes.md", "assets/examples/insurance-handoff.md",
    "assets/examples/design-tokens-example.json",
    "scripts/validate_skill.py",
    "tests/test-skill-structure.md", "tests/test-user-story.md",
    "tests/test-accessibility-review.md", "tests/test-design-system.md",
    "tests/test-existing-interface.md", "tests/test-file-safety.md",
]

REQUIRED_SKILL_SECTIONS = [
    "Scope", "Language rule", "Input handling", "Operational modes", "Module routing",
    "Workflow orchestration", "Output contracts", "Quality gates", "Safety rules", "Examples",
]

ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "metadata",
                       "allowed-tools"}
MERMAID_TYPES = ("flowchart", "graph", "journey", "sequenceDiagram", "stateDiagram",
                 "stateDiagram-v2", "classDiagram", "erDiagram", "gantt", "mindmap", "pie",
                 "timeline", "quadrantChart")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^```(\w[\w-]*)?\s*$")
REF_RE = re.compile(r"^\{([^{}]+)\}$")


class Report:
    def __init__(self) -> None:
        self.results: list[dict] = []

    def add(self, check: str, status: str, detail: str) -> None:
        self.results.append({"check": check, "status": status, "detail": detail})

    def ok(self, check: str, detail: str) -> None:
        self.add(check, "PASS", detail)

    def fail(self, check: str, detail: str) -> None:
        self.add(check, "FAIL", detail)

    def warn(self, check: str, detail: str) -> None:
        self.add(check, "WARN", detail)

    @property
    def failed(self) -> bool:
        return any(r["status"] == "FAIL" for r in self.results)


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text: str) -> tuple[dict, str] | None:
    """Minimal YAML subset parser: top-level `key: value` plus one level of nested mapping."""
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block, body = text[4:end], text[end + 4:].lstrip("\n")
    data: dict = {}
    current: str | None = None
    for raw in block.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")):
            if current is None or not isinstance(data.get(current), dict):
                return None
            key, _, value = raw.strip().partition(":")
            data[current][key.strip()] = value.strip().strip('"').strip("'")
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            return None
        key, value = key.strip(), value.strip()
        if value == "":
            data[key] = {}
            current = key
        else:
            data[key] = value.strip('"').strip("'")
            current = None
    return data, body


def check_skill_md(root: Path, rep: Report) -> None:
    path = root / "SKILL.md"
    if not path.is_file():
        rep.fail("skill.frontmatter", "SKILL.md missing")
        return
    text = path.read_text(encoding="utf-8")
    parsed = parse_frontmatter(text)
    if parsed is None:
        rep.fail("skill.frontmatter", "SKILL.md must start with a valid '---' YAML frontmatter block")
        return
    fm, body = parsed

    unknown = set(fm) - ALLOWED_FRONTMATTER
    if unknown:
        rep.warn("skill.frontmatter", f"Fields outside the spec: {sorted(unknown)}")

    name = fm.get("name", "")
    if not name:
        rep.fail("skill.name", "'name' is required")
    elif not NAME_RE.match(name) or len(name) > 64:
        rep.fail("skill.name", f"'{name}' must be 1-64 chars, lowercase letters, digits, single hyphens")
    elif name != SKILL_ID:
        rep.fail("skill.name", f"'{name}' differs from expected id '{SKILL_ID}'")
    else:
        rep.ok("skill.name", name)
        if root.resolve().name != name:
            rep.warn("skill.name", f"Directory '{root.resolve().name}' differs from name '{name}'. "
                     "Install the skill into a directory named after it.")

    desc = fm.get("description", "")
    if not desc:
        rep.fail("skill.description", "'description' is required")
    elif len(desc) > 1024:
        rep.fail("skill.description", f"{len(desc)} chars (max 1024)")
    else:
        lowered = desc.lower()
        hints = [w for w in ("use when", "not for") if w not in lowered]
        if hints:
            rep.warn("skill.description", f"Missing activation hints: {hints}")
        rep.ok("skill.description", f"{len(desc)}/1024 chars")

    comp = fm.get("compatibility")
    if comp is not None and len(comp) > 500:
        rep.fail("skill.compatibility", f"{len(comp)} chars (max 500)")
    if "metadata" in fm and not isinstance(fm["metadata"], dict):
        rep.fail("skill.metadata", "'metadata' must be a mapping")

    lines = len(text.splitlines())
    (rep.ok if lines < 500 else rep.warn)("skill.length", f"{lines} lines (recommended < 500)")

    headings = {h.strip() for h in re.findall(r"^#{2,3}\s+(.+)$", body, re.M)}
    missing = [s for s in REQUIRED_SKILL_SECTIONS if not any(h.startswith(s) for h in headings)]
    if missing:
        rep.fail("skill.sections", f"Missing sections: {missing}")
    else:
        rep.ok("skill.sections", f"{len(REQUIRED_SKILL_SECTIONS)} required sections present")

    for i in range(1, 11):
        if not re.search(rf"\|\s*{i:02d}\s*\|", body):
            rep.fail("skill.routing", f"Module {i:02d} missing from the routing table")
            break
    else:
        rep.ok("skill.routing", "Modules 01-10 routed")


# ---------------------------------------------------------------- structure & links

def check_structure(root: Path, rep: Report) -> None:
    missing = [f for f in REQUIRED_FILES if not (root / f).is_file()]
    if missing:
        rep.fail("structure", f"Missing: {missing}")
    else:
        rep.ok("structure", f"{len(REQUIRED_FILES)} required files present")


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def strip_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def check_links(root: Path, rep: Report) -> None:
    broken = []
    count = 0
    for md in markdown_files(root):
        for target in LINK_RE.findall(strip_code(md.read_text(encoding="utf-8"))):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                continue
            count += 1
            rel = target.split("#", 1)[0]
            if rel.startswith("/"):
                broken.append(f"{md.relative_to(root)} -> {target} (absolute path)")
            elif not (md.parent / rel).exists():
                broken.append(f"{md.relative_to(root)} -> {target}")
    if broken:
        rep.fail("links", "; ".join(broken))
    else:
        rep.ok("links", f"{count} relative links resolve")


# ---------------------------------------------------------------- JSON & tokens

def flatten_tokens(node: dict, prefix: str = "") -> dict:
    out = {}
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if "$value" in value:
            out[path] = value
        else:
            out.update(flatten_tokens(value, path))
    return out


def resolve(tokens: dict, path: str, seen: tuple = ()):
    if path in seen:
        raise ValueError(f"circular reference at {path}")
    if path not in tokens:
        raise KeyError(path)
    value = tokens[path]["$value"]
    if isinstance(value, str):
        m = REF_RE.match(value)
        if m:
            return resolve(tokens, m.group(1), seen + (path,))
    return value


def luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    channels = []
    for i in (0, 2, 4):
        c = int(h[i:i + 2], 16) / 255
        channels.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a: str, b: str) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def check_json(root: Path, rep: Report) -> None:
    for jf in sorted(p for p in root.rglob("*.json") if ".git" not in p.parts):
        rel = jf.relative_to(root)
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            rep.fail(f"json:{rel}", f"Invalid JSON: {exc}")
            continue
        rep.ok(f"json:{rel}", "parses")
        if "token" in jf.name:
            check_tokens(rel, data, rep)


def check_tokens(rel: Path, data: dict, rep: Report) -> None:
    tokens = flatten_tokens(data)
    bad = []
    for path in tokens:
        try:
            resolve(tokens, path)
        except (KeyError, ValueError) as exc:
            bad.append(f"{path}: {exc}")
    if bad:
        rep.fail(f"tokens:{rel}", f"Unresolved references: {bad}")
    else:
        rep.ok(f"tokens:{rel}", f"{len(tokens)} tokens, all references resolve")

    pairs = (data.get("$extensions", {}).get(SKILL_ID, {}).get("contrastPairs", []))
    if not pairs:
        rep.warn(f"contrast:{rel}", "No contrastPairs declared; contrast not verified")
        return
    failures, lines = [], []
    for p in pairs:
        try:
            fg, bg = resolve(tokens, p["fg"]), resolve(tokens, p["bg"])
            ratio = contrast(fg, bg)
        except (KeyError, ValueError, TypeError) as exc:
            failures.append(f"{p}: {exc}")
            continue
        line = f"{p['fg']} on {p['bg']} = {ratio:.2f}:1 (min {p['min']})"
        lines.append(line)
        if ratio + 1e-9 < float(p["min"]):
            failures.append(line)
    if failures:
        rep.fail(f"contrast:{rel}", "; ".join(failures))
    else:
        rep.ok(f"contrast:{rel}", f"{len(lines)} pairs meet minimum: " + "; ".join(lines))


# ---------------------------------------------------------------- Mermaid

def mermaid_blocks(text: str):
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = FENCE_RE.match(lines[i].strip())
        if m and m.group(1) == "mermaid":
            start, block = i + 1, []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            yield start, block
        i += 1


LABEL_RE = re.compile(r"(\[\[.*?\]\]|\(\[.*?\]\)|\[.*?\]|\{.*?\}|>.*?\])")


def check_mermaid(root: Path, rep: Report) -> None:
    issues, count = [], 0
    for md in markdown_files(root):
        for start, block in mermaid_blocks(md.read_text(encoding="utf-8")):
            count += 1
            where = f"{md.relative_to(root)}:{start}"
            body = [l for l in block if l.strip() and not l.strip().startswith("%%")]
            if not body or not body[0].strip().startswith(MERMAID_TYPES):
                issues.append(f"{where} unknown diagram type")
                continue
            for offset, line in enumerate(block):
                for label in LABEL_RE.findall(line):
                    if ";" in label and '"' not in label:
                        issues.append(f"{where}+{offset} unquoted ';' in {label}")
    if issues:
        rep.fail("mermaid", "; ".join(issues))
    else:
        rep.ok("mermaid", f"{count} diagrams pass basic lint (not a full render)")


# ---------------------------------------------------------------- main

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("root", nargs="?", default=str(Path(__file__).resolve().parent.parent),
                        help="Skill root directory (default: parent of scripts/)")
    parser.add_argument("--json", action="store_true", help="Print results as JSON")
    args = parser.parse_args(argv)
    root = Path(args.root)

    rep = Report()
    if not root.is_dir():
        rep.fail("root", f"{root} is not a directory")
    else:
        check_structure(root, rep)
        check_skill_md(root, rep)
        check_links(root, rep)
        check_json(root, rep)
        check_mermaid(root, rep)

    if args.json:
        print(json.dumps({"root": str(root), "passed": not rep.failed, "results": rep.results},
                         indent=2, ensure_ascii=False))
    else:
        for r in rep.results:
            print(f"[{r['status']:4}] {r['check']}: {r['detail']}")
        totals = {s: sum(r["status"] == s for r in rep.results) for s in ("PASS", "WARN", "FAIL")}
        print(f"\n{totals['PASS']} passed, {totals['WARN']} warnings, {totals['FAIL']} failed")
    return 1 if rep.failed else 0


if __name__ == "__main__":
    sys.exit(main())
