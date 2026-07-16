#!/usr/bin/env python3
"""Lint TUEL blueprint folders against the TUEL Blueprint Standard.

Usage:
    python tools/lint.py [BLUEPRINT_DIR ...] [--json] [--strict] [--self-test]

With no arguments, lints every directory under blueprints/ plus
templates/_blank. Dependency policy: standard library + PyYAML only.
The manifest contract lives in standard/blueprint.schema.json; this
linter loads it at runtime and refuses to run if the schema uses a
keyword it does not implement, so schema evolution can never silently
skip validation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("lint.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "standard" / "blueprint.schema.json"

REQUIRED_FILES = (
    "START-HERE.md",
    "blueprint.yaml",
    "CLAUDE.md",
    "onboarding/interview.md",
    "onboarding/checklist.md",
)

MANIFEST_SECTIONS = {
    # manifest key -> (directory, filename pattern for a slug)
    "skills": ("skills", "{slug}/SKILL.md"),
    "schedules": ("schedules", "{slug}.md"),
    "workflows": ("workflows", "{slug}.md"),
    "templates": ("templates", "{slug}.md"),
    "memory_files": ("business", "{slug}.md"),
}

MIN_SKILLS = 3
MIN_SCHEDULES = 2

HARD_RULES_RE = re.compile(r"^#{1,6}\s*hard rules", re.IGNORECASE | re.MULTILINE)
SOURCE_OF_TRUTH_RE = re.compile(r"source of truth", re.IGNORECASE)

OWNER_FACING_GLOBS = ("START-HERE.md", "onboarding/*.md", "templates/*.md", "business/*.md", "connectors.md")
JARGON_RE = re.compile(r"\b(connectors?|MCP|schema|API|endpoint)\b", re.IGNORECASE)
CURRENCY_RE = re.compile(r"\$\d")
PHONE_RE = re.compile(r"\(?\b\d{3}\)?[-.\s]\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.\w{2,}\b")
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")

TEMPLATE_SLUG = "_blank"


# --------------------------------------------------------------------------
# Minimal JSON Schema validation (exactly the keywords the schema uses)
# --------------------------------------------------------------------------

class UnsupportedSchemaKeyword(Exception):
    """The schema file uses a keyword this validator does not implement."""


_HANDLED = {"type", "required", "properties", "additionalProperties", "pattern",
            "minLength", "maxLength", "minItems", "uniqueItems", "items", "enum", "$ref"}
_IGNORED = {"$schema", "$id", "title", "description", "default", "$defs"}

_TYPE_MAP = {"object": dict, "string": str, "array": list}


def _check_keywords(schema: dict) -> None:
    for keyword in schema:
        if keyword not in _HANDLED and keyword not in _IGNORED:
            raise UnsupportedSchemaKeyword(
                f"standard/blueprint.schema.json uses '{keyword}', which tools/lint.py "
                f"does not implement. Update the validator before using this keyword."
            )


def validate_instance(value: object, schema: dict, defs: dict, path: str, errors: list[str]) -> None:
    _check_keywords(schema)

    if "$ref" in schema:
        ref = schema["$ref"]
        prefix = "#/$defs/"
        if not ref.startswith(prefix) or ref[len(prefix):] not in defs:
            raise UnsupportedSchemaKeyword(f"unsupported $ref target: {ref}")
        validate_instance(value, defs[ref[len(prefix):]], defs, path, errors)
        return

    expected = schema.get("type")
    if expected is not None:
        py_type = _TYPE_MAP.get(expected)
        if py_type is None:
            raise UnsupportedSchemaKeyword(f"unsupported type '{expected}' at {path}")
        if not isinstance(value, py_type) or isinstance(value, bool):
            errors.append(f"{path}: expected {expected}, got {type(value).__name__}")
            return

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: {value!r} is not one of {schema['enum']}")

    if isinstance(value, str):
        if "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match pattern {schema['pattern']!r}")
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: shorter than minLength {schema['minLength']}")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: longer than maxLength {schema['maxLength']}")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: needs at least {schema['minItems']} items, has {len(value)}")
        if schema.get("uniqueItems"):
            seen = [json.dumps(v, sort_keys=True, default=str) for v in value]
            if len(seen) != len(set(seen)):
                errors.append(f"{path}: items must be unique")
        if "items" in schema:
            for i, item in enumerate(value):
                validate_instance(item, schema["items"], defs, f"{path}[{i}]", errors)

    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path}: missing required field '{key}'")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value:
                if key not in props:
                    errors.append(f"{path}: unknown field '{key}'")
        for key, subschema in props.items():
            if key in value:
                validate_instance(value[key], subschema, defs, f"{path}.{key}", errors)


# --------------------------------------------------------------------------
# Blueprint checks
# --------------------------------------------------------------------------

@dataclass
class Finding:
    level: str  # "error" | "warning"
    check: str
    message: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _line_exempt(line: str, template_mode: bool) -> bool:
    return template_mode and bool(PLACEHOLDER_RE.search(line))


def lint_blueprint(bp_dir: Path, schema: dict, template_mode: bool) -> list[Finding]:
    findings: list[Finding] = []
    err = lambda check, msg: findings.append(Finding("error", check, msg))
    warn = lambda check, msg: findings.append(Finding("warning", check, msg))

    # 1. Required files exist and are non-empty.
    for rel in REQUIRED_FILES:
        f = bp_dir / rel
        if not f.is_file():
            err("required-files", f"missing {rel}")
        elif not _read(f).strip():
            err("required-files", f"{rel} is empty")

    # Directories the standard requires.
    if not (bp_dir / "assets" / "README.md").is_file():
        err("layout", "assets/README.md is missing")
    if not (bp_dir / "reports").is_dir():
        err("layout", "reports/ directory is missing")

    # 2. Manifest parses and validates.
    manifest: dict | None = None
    manifest_path = bp_dir / "blueprint.yaml"
    if manifest_path.is_file():
        try:
            loaded = yaml.safe_load(_read(manifest_path))
        except yaml.YAMLError as exc:
            err("manifest", f"blueprint.yaml does not parse: {exc}")
        else:
            if isinstance(loaded, dict):
                manifest = loaded
                schema_errors: list[str] = []
                defs = schema.get("$defs", {})
                validate_instance(manifest, schema, defs, "$", schema_errors)
                if template_mode and manifest.get("slug") == TEMPLATE_SLUG:
                    schema_errors = [e for e in schema_errors if not e.startswith("$.slug:")]
                for msg in schema_errors:
                    err("manifest", msg)
            else:
                err("manifest", "blueprint.yaml must be a YAML mapping")

    # 3. Slug matches directory name.
    if manifest is not None and manifest.get("slug") != bp_dir.name:
        err("slug", f"manifest slug {manifest.get('slug')!r} != directory name {bp_dir.name!r}")

    # 4. CLAUDE.md contract.
    claude_path = bp_dir / "CLAUDE.md"
    if claude_path.is_file():
        text = _read(claude_path)
        if not HARD_RULES_RE.search(text):
            err("operating-agent", "CLAUDE.md has no 'Hard rules' heading")
        if "business/" not in text or not SOURCE_OF_TRUTH_RE.search(text):
            err("operating-agent", "CLAUDE.md must name business/ as the source of truth")

    # 5. Manifest <-> disk, both directions.
    if manifest is not None:
        for key, (dirname, pattern) in MANIFEST_SECTIONS.items():
            listed = manifest.get(key) or []
            if not isinstance(listed, list):
                continue  # schema validation already reported it
            for slug in listed:
                if not isinstance(slug, str):
                    continue
                f = bp_dir / dirname / pattern.format(slug=slug)
                if not f.is_file() or not _read(f).strip():
                    err(key, f"manifest lists '{slug}' but {dirname}/{pattern.format(slug=slug)} is missing or empty")
            section_dir = bp_dir / dirname
            on_disk: set[str] = set()
            if section_dir.is_dir():
                if key == "skills":
                    on_disk = {p.name for p in section_dir.iterdir() if p.is_dir()}
                else:
                    on_disk = {p.stem for p in section_dir.glob("*.md")}
                    if key == "memory_files":
                        pass  # business/*.md all count
            for slug in sorted(on_disk - set(listed)):
                err(key, f"{dirname}/{slug} exists on disk but is not in the manifest")

    # 6. Minimum counts on disk.
    skill_dirs = [p for p in (bp_dir / "skills").iterdir() if p.is_dir()] if (bp_dir / "skills").is_dir() else []
    real_skills = [p for p in skill_dirs if (p / "SKILL.md").is_file() and _read(p / "SKILL.md").strip()]
    if len(real_skills) < MIN_SKILLS:
        err("skills", f"needs at least {MIN_SKILLS} skills with a non-empty SKILL.md, found {len(real_skills)}")
    schedule_files = list((bp_dir / "schedules").glob("*.md")) if (bp_dir / "schedules").is_dir() else []
    if len(schedule_files) < MIN_SCHEDULES:
        err("schedules", f"needs at least {MIN_SCHEDULES} schedules, found {len(schedule_files)}")

    # 7. Warnings: data in business memory stubs.
    for stub in sorted((bp_dir / "business").glob("*.md")) if (bp_dir / "business").is_dir() else []:
        for n, line in enumerate(_read(stub).splitlines(), start=1):
            if _line_exempt(line, template_mode):
                continue
            for regex, label in ((CURRENCY_RE, "currency amount"), (PHONE_RE, "phone number"), (EMAIL_RE, "email address")):
                if regex.search(line):
                    warn("stub-data", f"business/{stub.name}:{n} looks like a {label} — business memory ships as empty stubs")

    # 8. Warnings: platform jargon in owner-facing files.
    owner_files: list[Path] = []
    for pattern in OWNER_FACING_GLOBS:
        owner_files.extend(sorted(bp_dir.glob(pattern)))
    for f in owner_files:
        if not f.is_file():
            continue
        for n, line in enumerate(_read(f).splitlines(), start=1):
            if _line_exempt(line, template_mode):
                continue
            m = JARGON_RE.search(line)
            if m:
                rel = f.relative_to(bp_dir)
                warn("jargon", f"{rel}:{n} uses '{m.group(0)}' — owner-facing text stays jargon-free")

    return findings


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def default_targets() -> list[Path]:
    targets: list[Path] = []
    blueprints = REPO_ROOT / "blueprints"
    if blueprints.is_dir():
        targets.extend(sorted(p for p in blueprints.iterdir() if p.is_dir()))
    blank = REPO_ROOT / "templates" / TEMPLATE_SLUG
    if blank.is_dir() and any(blank.iterdir()):
        targets.append(blank)
    return targets


def is_template(path: Path) -> bool:
    return "templates" in [p.name for p in path.parents] or path.parent.name == "templates"


def run(targets: list[Path], schema: dict, strict: bool, as_json: bool) -> int:
    reports = []
    total_errors = total_warnings = 0
    for bp_dir in targets:
        findings = lint_blueprint(bp_dir, schema, template_mode=is_template(bp_dir))
        errors = [f for f in findings if f.level == "error"]
        warnings = [f for f in findings if f.level == "warning"]
        total_errors += len(errors)
        total_warnings += len(warnings)
        reports.append((bp_dir, errors, warnings))

    if as_json:
        payload = {
            "blueprints": [
                {
                    "path": str(bp),
                    "errors": [f"[{f.check}] {f.message}" for f in errs],
                    "warnings": [f"[{f.check}] {f.message}" for f in warns],
                }
                for bp, errs, warns in reports
            ],
            "summary": {"blueprints": len(reports), "errors": total_errors, "warnings": total_warnings},
        }
        print(json.dumps(payload, indent=2))
    else:
        if not reports:
            print("No blueprints to lint yet (blueprints/ and templates/_blank are empty). ✓")
            return 0
        for bp, errs, warns in reports:
            mark = "✗" if errs else ("⚠" if warns else "✓")
            print(f"{mark} {bp.relative_to(REPO_ROOT) if bp.is_relative_to(REPO_ROOT) else bp}")
            for f in errs:
                print(f"    ✗ [{f.check}] {f.message}")
            for f in warns:
                print(f"    ⚠ [{f.check}] {f.message}")
        print(f"\n{len(reports)} blueprint(s): {total_errors} error(s), {total_warnings} warning(s)")

    failing = total_errors > 0 or (strict and total_warnings > 0)
    return 1 if failing else 0


# --------------------------------------------------------------------------
# Self-test
# --------------------------------------------------------------------------

def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _make_blueprint(bp: Path, slug: str, *, jargon: bool = False, hard_rules: bool = True,
                    skill_names: tuple[str, ...] = ("greet-clients", "plan-week", "close-day"),
                    extra_skill_dir: str | None = None, drop_skill_file: str | None = None,
                    template_tokens: bool = False) -> None:
    start = "Hi! I'm your business's assistant. Open me in Claude Desktop and say hello.\n"
    if jargon:
        start += "We will set up a connector for your email.\n"
    if template_tokens:
        start += "Welcome to {{NAME}}, your {{BUSINESS_TYPE}} assistant.\n"
    _write(bp / "START-HERE.md", start)

    manifest = {
        "name": "Test Business",
        "slug": slug,
        "version": "0.1.0",
        "business_type": "test business",
        "summary": "A test blueprint.",
        "skills": list(skill_names),
        "schedules": ["morning-brief", "end-of-day"],
        "workflows": [],
        "templates": [],
        "memory_files": ["profile", "services"],
    }
    _write(bp / "blueprint.yaml", yaml.safe_dump(manifest, sort_keys=False))

    rules = "## Hard rules\n- Draft first, always.\n" if hard_rules else "## Rules\n- Be nice.\n"
    _write(bp / "CLAUDE.md", f"# Operating agent\n{rules}\nbusiness/ is the source of truth.\n")
    _write(bp / "onboarding/interview.md", "Ask one question at a time.\n")
    _write(bp / "onboarding/checklist.md", "Tier 1: business name.\n")
    _write(bp / "business/profile.md", "Your business profile. [Complete during onboarding]\n")
    _write(bp / "business/services.md", "Your services. [Complete during onboarding]\n")
    _write(bp / "assets/README.md", "Put your logo and price list here.\n")
    (bp / "reports").mkdir(parents=True, exist_ok=True)
    _write(bp / "connectors.md", "Ways to plug in your everyday tools, all optional.\n")
    for skill in skill_names:
        if skill == drop_skill_file:
            continue
        _write(bp / "skills" / skill / "SKILL.md", f"# {skill}\nSteps.\n")
    if extra_skill_dir:
        _write(bp / "skills" / extra_skill_dir / "SKILL.md", "# extra\nSteps.\n")
    _write(bp / "schedules/morning-brief.md", "Mode: local. Prompt: start the day.\n")
    _write(bp / "schedules/end-of-day.md", "Mode: local. Prompt: close the day.\n")


def self_test(schema: dict) -> int:
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        def check(name: str, bp: Path, template_mode: bool, expect_errors: bool, expect_warnings: bool | None = None) -> None:
            findings = lint_blueprint(bp, schema, template_mode)
            errors = [f for f in findings if f.level == "error"]
            warnings = [f for f in findings if f.level == "warning"]
            ok = (bool(errors) == expect_errors)
            if expect_warnings is not None:
                ok = ok and (bool(warnings) == expect_warnings)
            cases.append((name, ok, [f"{f.level}:{f.message}" for f in findings]))

        bp = root / "valid-shop"
        _make_blueprint(bp, "valid-shop")
        check("valid blueprint passes", bp, False, expect_errors=False, expect_warnings=False)

        bp = root / "no-start"
        _make_blueprint(bp, "no-start")
        (bp / "START-HERE.md").unlink()
        check("missing START-HERE.md fails", bp, False, expect_errors=True)

        bp = root / "wrong-name"
        _make_blueprint(bp, "other-slug")
        check("slug mismatch fails", bp, False, expect_errors=True)

        bp = root / "ghost-skill"
        _make_blueprint(bp, "ghost-skill", skill_names=("a-skill", "b-skill", "c-skill", "d-skill"),
                        drop_skill_file="d-skill")
        check("manifest skill without file fails", bp, False, expect_errors=True)

        bp = root / "stray-skill"
        _make_blueprint(bp, "stray-skill", extra_skill_dir="not-in-manifest")
        check("skill dir not in manifest fails", bp, False, expect_errors=True)

        bp = root / "no-hard-rules"
        _make_blueprint(bp, "no-hard-rules", hard_rules=False)
        check("CLAUDE.md without hard rules fails", bp, False, expect_errors=True)

        bp = root / "jargon-shop"
        _make_blueprint(bp, "jargon-shop", jargon=True)
        check("jargon warns but does not fail", bp, False, expect_errors=False, expect_warnings=True)

        bp = root / "templates" / TEMPLATE_SLUG
        _make_blueprint(bp, TEMPLATE_SLUG, template_tokens=True)
        check("_blank template passes in template mode", bp, True, expect_errors=False, expect_warnings=False)

    width = max(len(name) for name, _, _ in cases)
    all_ok = True
    for name, ok, findings in cases:
        print(f"{'PASS' if ok else 'FAIL'}  {name.ljust(width)}")
        if not ok:
            all_ok = False
            for f in findings:
                print(f"        {f}")
    print(f"\nself-test: {'all good ✓' if all_ok else 'FAILURES ✗'}")
    return 0 if all_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="blueprint directories (default: blueprints/* + templates/_blank)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--strict", action="store_true", help="warnings count as errors")
    parser.add_argument("--self-test", action="store_true", help="run the linter's own test fixtures")
    args = parser.parse_args()

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

    if args.self_test:
        return self_test(schema)

    targets = [Path(p).resolve() for p in args.paths] if args.paths else default_targets()
    for t in targets:
        if not t.is_dir():
            print(f"not a directory: {t}", file=sys.stderr)
            return 2
    return run(targets, schema, strict=args.strict, as_json=args.json)


if __name__ == "__main__":
    sys.exit(main())
