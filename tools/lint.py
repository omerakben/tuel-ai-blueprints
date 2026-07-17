#!/usr/bin/env python3
"""Lint TUEL blueprint folders against TUEL Blueprint Standard 1.0.

Usage:
    python3 tools/lint.py [BLUEPRINT_DIR ...] [--json] [--strict] [--self-test]

With no paths, the command checks every directory under blueprints/ plus
templates/_blank. Runtime dependencies are the Python standard library and
PyYAML. The JSON Schema validator below intentionally implements only the
keywords used by standard/blueprint.schema.json and fails closed when the
schema introduces an unsupported keyword.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("lint.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
STANDARD_ROOT = REPO_ROOT / "standard"
SCHEMA_PATH = STANDARD_ROOT / "blueprint.schema.json"
SAFETY_FLOOR_PATH = STANDARD_ROOT / "safety-floor.md"
SCHEDULE_CONTRACT_PATH = STANDARD_ROOT / "schedule-contract.md"
CORE_ROOT = STANDARD_ROOT / "core"

STANDARD_VERSION = "1.0.0"
TEMPLATE_SLUG = "_blank"

REQUIRED_FILES = (
    "START-HERE.md",
    "blueprint.yaml",
    "CLAUDE.md",
    "UPGRADE.md",
    "onboarding/interview.md",
    "onboarding/checklist.md",
    "connectors.md",
)

CORE_FILES = (
    "roles/operator.md",
    "roles/reality-checker.md",
    "skills/review-the-work/SKILL.md",
    "workflows/verify-a-draft.md",
    "workflows/review-business-memory.md",
    "workflows/handle-an-incident.md",
    "schedules/weekly-operations-review.md",
    "templates/operations-board.md",
    "templates/work-receipt.md",
    "templates/decision-record.md",
    "templates/memory-proposal.md",
    "templates/incident-record.md",
    "templates/weekly-operations-review.md",
    "operations/README.md",
    "inbox/README.md",
    "UPGRADE.md",
)

MANIFEST_SECTIONS = {
    # manifest key -> (directory, filename pattern for one slug)
    "skills": ("skills", "{slug}/SKILL.md"),
    "schedules": ("schedules", "{slug}.md"),
    "workflows": ("workflows", "{slug}.md"),
    "templates": ("templates", "{slug}.md"),
    "memory_files": ("business", "{slug}.md"),
    "roles": ("roles", "{slug}.md"),
}

CORE_MANIFEST_ITEMS = {
    "skills": {"review-the-work"},
    "schedules": {"weekly-operations-review"},
    "workflows": {"verify-a-draft", "review-business-memory", "handle-an-incident"},
    "templates": {
        "operations-board",
        "work-receipt",
        "decision-record",
        "memory-proposal",
        "incident-record",
        "weekly-operations-review",
    },
    "roles": {"operator", "reality-checker"},
}

REQUIRED_MEMORY_FILES = {"profile", "services", "staff", "clients", "suppliers", "policies", "brand"}
PROTECTED_PATHS = {"business/", "assets/", "reports/", "operations/", "inbox/"}

MIN_SKILLS = 4
MIN_SCHEDULES = 3
MIN_WORKFLOWS = 3
MIN_TEMPLATES = 6

HARD_RULES_RE = re.compile(
    r"^[ ]{0,3}#{1,6}[ \t]+hard rules[ \t]*#*[ \t]*$",
    re.IGNORECASE | re.MULTILINE,
)
BUSINESS_SOURCE_RE = re.compile(
    r"^[ ]{0,3}(?:(?:[-*]|\d+\.)\s+)?(?:\*\*)?`?business/`?(?:\*\*)?\s+"
    r"(?:files\s+(?:are|is)|is)\s+the\s+source\s+of\s+truth\b",
    re.IGNORECASE | re.MULTILINE,
)
SHORT_VERSION_HEADING_RE = re.compile(
    r"^(#{1,6})[ \t]+(?:the[ \t]+)?short version[ \t]*#*[ \t]*$",
    re.IGNORECASE | re.MULTILINE,
)
READ_FULL_CLAUDE_RE = re.compile(
    r"read\s+(?:the\s+)?(?:full|entire)\s+`?CLAUDE\.md`?",
    re.IGNORECASE,
)
ACTION_LEVEL_RE = re.compile(
    r"(?:maximum\s+)?action\s+level\s*:\s*([A-F])\b",
    re.IGNORECASE,
)
FENCE_RE = re.compile(r"^[ \t]*```[^\n]*$", re.MULTILINE)

OWNER_FACING_GLOBS = (
    "START-HERE.md",
    "onboarding/*.md",
    "templates/*.md",
    "business/*.md",
    "connectors.md",
)
JARGON_RE = re.compile(r"\b(connectors?|MCP|schemas?|APIs?|endpoints?)\b", re.IGNORECASE)
CURRENCY_RE = re.compile(r"(?:\$\s?\d|\b(?:USD|EUR|GBP)\s+\d)", re.IGNORECASE)
PHONE_RE = re.compile(r"\(?\b\d{3}\)?[-.\s]\d{3}[-.\s]?\d{4}\b")
EMAIL_RE = re.compile(r"\b[\w.+-]+@[\w-]+\.\w{2,}\b")
PLACEHOLDER_RE = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")
UNRESOLVED_WORD_RE = re.compile(r"\b(?:TODO|TBD|FIXME|CHANGEME)\b", re.IGNORECASE)
ANY_TEMPLATE_TOKEN_RE = re.compile(r"\{\{[^}\n]+\}\}")

FALSE_PLATFORM_CLAIMS = (
    (re.compile(r"\b(?:never|does not)\s+(?:get\s+)?upload(?:ed|s)?\b", re.IGNORECASE),
     "do not promise that Claude never uploads folder content"),
    (re.compile(r"\b(?:never|does not)\s+leave(?:s)?\s+(?:your|this|the)\s+(?:computer|device|folder)\b", re.IGNORECASE),
     "do not promise that work never leaves the device"),
    (re.compile(r"\bstays?\s+(?:entirely\s+|only\s+)?(?:local|on\s+(?:your|this)\s+(?:computer|device))\b", re.IGNORECASE),
     "do not promise device-only processing"),
    (re.compile(r"\b(?:no\s+(?:Claude\s+)?account\s+(?:is\s+)?required|works?\s+without\s+(?:a\s+)?Claude\s+account)\b", re.IGNORECASE),
     "do not claim Claude works without the required account"),
    (re.compile(r"\b(?:every|all)\s+connections?\s+(?:starts?|are)\s+read[- ]only\b", re.IGNORECASE),
     "connection capabilities vary; record actual access separately from use policy"),
    (re.compile(r"\b(?:simply|just)\s+skips?\b.*\bnothing\s+breaks\b", re.IGNORECASE),
     "do not promise missed-run behavior that the current platform does not document"),
)

MARKED_CONTROL_REQUIREMENTS = {
    "START-HERE.md": (
        "<!-- TUEL:OWNER-SETUP:START -->",
        "<!-- TUEL:OWNER-SETUP:END -->",
        ("ordinary working folder", "eligible Claude account", "processes the files", "Manual mode"),
    ),
    "onboarding/interview.md": (
        "<!-- TUEL:SETUP-CONTROLS:START -->",
        "<!-- TUEL:SETUP-CONTROLS:END -->",
        ("read the full `CLAUDE.md`", "named decision owner", "local time zone", "operations/setup-status.md"),
    ),
    "onboarding/checklist.md": (
        "<!-- TUEL:CONTROL-CHECKLIST:START -->",
        "<!-- TUEL:CONTROL-CHECKLIST:END -->",
        ("approves decisions", "local time zone", "temporary exports", "never deletes"),
    ),
    "CLAUDE.md": (
        "<!-- TUEL:BUSINESS-OS:START -->",
        "<!-- TUEL:BUSINESS-OS:END -->",
        ("named owner", "roles/reality-checker.md", "work receipt", "review-business-memory.md"),
    ),
}

SCHEDULE_PROMPT_REQUIREMENTS = (
    "Read the full CLAUDE.md before doing anything.",
    "This run is A Observe or B Draft only.",
    "Save output to reports/ only.",
    "Never overwrite a file",
    "End with a work receipt",
    "Do not send, post, pay, file, sign, delete, or change an outside system.",
)

FORBIDDEN_DIR_NAMES = {".git", ".github", ".idea", ".vscode", "__pycache__", "node_modules"}
FORBIDDEN_FILE_NAMES = {
    ".DS_Store",
    "Thumbs.db",
    ".npmrc",
    ".pypirc",
    "credentials.json",
    "credential.json",
    "secrets.json",
    "secret.json",
    "tokens.json",
    "token.json",
    "id_rsa",
    "id_ed25519",
}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".pem", ".key", ".p12", ".pfx"}


class StrictYamlLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys."""

    def construct_mapping(self, node, deep: bool = False):
        seen: list[object] = []
        for key_node, _value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                raise yaml.YAMLError(f"duplicate key {key!r} in mapping")
            seen.append(key)
        return super().construct_mapping(node, deep)


# --------------------------------------------------------------------------
# Minimal JSON Schema validation: exactly the keywords the schema uses
# --------------------------------------------------------------------------


class UnsupportedSchemaKeyword(Exception):
    """The schema file uses a keyword this validator does not implement."""


_HANDLED = {
    "type",
    "required",
    "properties",
    "additionalProperties",
    "pattern",
    "minLength",
    "maxLength",
    "minItems",
    "uniqueItems",
    "items",
    "enum",
    "$ref",
}
_IGNORED = {"$schema", "$id", "title", "description", "default", "$defs"}
_TYPE_MAP = {"object": dict, "string": str, "array": list}


def _check_keywords(schema: dict) -> None:
    for keyword in schema:
        if keyword not in _HANDLED and keyword not in _IGNORED:
            raise UnsupportedSchemaKeyword(
                f"standard/blueprint.schema.json uses '{keyword}', which tools/lint.py "
                f"does not implement. Update the validator before using this keyword."
            )


def check_schema_supported(schema: dict) -> None:
    """Walk the entire schema so an unsupported keyword fails at startup."""
    defs = schema.get("$defs", {})

    def walk(node: object) -> None:
        if not isinstance(node, dict):
            return
        _check_keywords(node)
        if "$ref" in node:
            ref = node["$ref"]
            prefix = "#/$defs/"
            if not (isinstance(ref, str) and ref.startswith(prefix) and ref[len(prefix):] in defs):
                raise UnsupportedSchemaKeyword(f"unsupported $ref target: {ref}")
            siblings = set(node) - {"$ref"} - _IGNORED
            if siblings:
                raise UnsupportedSchemaKeyword(
                    f"validation keywords next to $ref are not evaluated: {sorted(siblings)}"
                )
        declared = node.get("type")
        if declared is not None and declared not in _TYPE_MAP:
            raise UnsupportedSchemaKeyword(f"unsupported type {declared!r}")
        additional = node.get("additionalProperties")
        if additional is not None and not isinstance(additional, bool):
            raise UnsupportedSchemaKeyword("additionalProperties supports only boolean values")
        for sub in node.get("properties", {}).values():
            walk(sub)
        if "items" in node:
            walk(node["items"])

    walk(schema)
    for sub in defs.values():
        walk(sub)


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
            seen = [json.dumps(item, sort_keys=True, default=str) for item in value]
            if len(seen) != len(set(seen)):
                errors.append(f"{path}: items must be unique")
        if "items" in schema:
            for index, item in enumerate(value):
                validate_instance(item, schema["items"], defs, f"{path}[{index}]", errors)

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
    level: str  # error | warning
    check: str
    message: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _normalized_text(path: Path) -> str:
    return _read(path).replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n"


def _line_exempt(line: str, template_mode: bool) -> bool:
    return template_mode and bool(PLACEHOLDER_RE.search(line))


def _section_after_heading(text: str, match: re.Match[str]) -> str:
    level = len(match.group(1))
    remainder = text[match.end():]
    next_heading = re.search(rf"^#{{1,{level}}}[ \t]+", remainder, re.MULTILINE)
    return remainder[:next_heading.start()] if next_heading else remainder


def _valid_iso_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _owner_facing_files(bp_dir: Path) -> list[Path]:
    files: list[Path] = []
    for pattern in OWNER_FACING_GLOBS:
        files.extend(sorted(bp_dir.glob(pattern)))
    return sorted(set(path for path in files if path.is_file()))


def lint_blueprint(bp_dir: Path, schema: dict, template_mode: bool) -> list[Finding]:
    findings: list[Finding] = []
    err = lambda check, message: findings.append(Finding("error", check, message))
    warn = lambda check, message: findings.append(Finding("warning", check, message))

    # 1. Required files and workspace seeds.
    for rel in REQUIRED_FILES:
        path = bp_dir / rel
        if not path.is_file():
            err("required-files", f"missing {rel}")
        elif not _read(path).strip():
            err("required-files", f"{rel} is empty")

    required_seeds = {
        "assets/README.md": True,
        "inbox/README.md": True,
        "operations/README.md": True,
        "reports/.gitkeep": False,
    }
    for rel, must_be_nonempty in required_seeds.items():
        path = bp_dir / rel
        if not path.is_file():
            err("layout", f"{rel} is missing")
        elif must_be_nonempty and not _read(path).strip():
            err("layout", f"{rel} is empty")

    # 2. Manifest parsing and schema validation.
    manifest: dict | None = None
    manifest_path = bp_dir / "blueprint.yaml"
    if manifest_path.is_file():
        try:
            loaded = yaml.load(_read(manifest_path), Loader=StrictYamlLoader)
        except yaml.YAMLError as exc:
            err("manifest", f"blueprint.yaml does not parse: {exc}")
        else:
            if isinstance(loaded, dict):
                manifest = loaded
                schema_errors: list[str] = []
                validate_instance(manifest, schema, schema.get("$defs", {}), "$", schema_errors)
                if template_mode and manifest.get("slug") == TEMPLATE_SLUG:
                    schema_errors = [message for message in schema_errors if not message.startswith("$.slug:")]
                for message in schema_errors:
                    err("manifest", message)
            else:
                err("manifest", "blueprint.yaml must be a YAML mapping")

    # 3. Directory identity and versioned manifest semantics.
    if manifest is not None:
        if manifest.get("slug") != bp_dir.name:
            err("slug", f"manifest slug {manifest.get('slug')!r} != directory name {bp_dir.name!r}")

        version = manifest.get("version")
        if isinstance(version, str) and re.fullmatch(r"\d+\.\d+\.\d+", version):
            if int(version.split(".", 1)[0]) < 1:
                err("version", "Business OS safety and layout changes require blueprint version 1.0.0 or later")

        for key in ("standard_version", "policy_version", "data_layout_version"):
            if manifest.get(key) != STANDARD_VERSION:
                err("version", f"{key} must be {STANDARD_VERSION}")
        if manifest.get("operating_profile") != "draft-only-v1":
            err("version", "operating_profile must be draft-only-v1")

        checked_on = manifest.get("platform_claims_checked_on")
        if not _valid_iso_date(checked_on):
            err("platform-evidence", "platform_claims_checked_on must be a real YYYY-MM-DD date")

        protected = manifest.get("protected_paths")
        if isinstance(protected, list) and set(protected) != PROTECTED_PATHS:
            err("protected-paths", f"protected_paths must be exactly {sorted(PROTECTED_PATHS)}")

        memory_files = manifest.get("memory_files")
        if isinstance(memory_files, list):
            missing_memory = REQUIRED_MEMORY_FILES - set(item for item in memory_files if isinstance(item, str))
            if missing_memory:
                err("memory-files", f"missing required business-memory stubs: {', '.join(sorted(missing_memory))}")

        for key, required in CORE_MANIFEST_ITEMS.items():
            listed = manifest.get(key)
            if isinstance(listed, list):
                missing = required - set(item for item in listed if isinstance(item, str))
                if missing:
                    err("core-manifest", f"{key} is missing standard core item(s): {', '.join(sorted(missing))}")
        roles = manifest.get("roles")
        if isinstance(roles, list) and set(roles) != CORE_MANIFEST_ITEMS["roles"]:
            err("roles", "roles must be exactly operator and reality-checker")

    # 4. Operating-instruction contract and exact safety floor.
    claude_path = bp_dir / "CLAUDE.md"
    if claude_path.is_file():
        claude_text = _read(claude_path).replace("\r\n", "\n").replace("\r", "\n")
        safety_text = _normalized_text(SAFETY_FLOOR_PATH).rstrip("\n")
        if not HARD_RULES_RE.search(claude_text):
            err("operating-agent", "CLAUDE.md has no 'Hard rules' heading")
        if not BUSINESS_SOURCE_RE.search(claude_text):
            err("operating-agent", "CLAUDE.md must state that business/ files are the source of truth")
        if safety_text not in claude_text:
            err("safety-floor", "CLAUDE.md must contain the exact standard/safety-floor.md block")
        if claude_text.count("<!-- TUEL:SAFETY-FLOOR:START -->") != 1 or claude_text.count("<!-- TUEL:SAFETY-FLOOR:END -->") != 1:
            err("safety-floor", "CLAUDE.md must contain exactly one marked safety-floor block")
        for match in SHORT_VERSION_HEADING_RE.finditer(claude_text):
            if not READ_FULL_CLAUDE_RE.search(_section_after_heading(claude_text, match)):
                err("operating-agent", "the Short version section must say to read the full CLAUDE.md first")

    # Setup and operating controls are marked so the synchronizer can update them safely.
    for rel, (start, end, phrases) in MARKED_CONTROL_REQUIREMENTS.items():
        path = bp_dir / rel
        if not path.is_file():
            continue
        text = _read(path)
        if text.count(start) != 1 or text.count(end) != 1 or text.find(start) > text.find(end):
            err("control-block", f"{rel} must contain exactly one complete {start} block")
            continue
        block = text[text.find(start):text.find(end) + len(end)]
        for phrase in phrases:
            if phrase.casefold() not in block.casefold():
                err("control-block", f"{rel} control block is missing required boundary text: {phrase!r}")

    # 5. Exact copies of standard-owned core files.
    for rel in CORE_FILES:
        source = CORE_ROOT / rel
        target = bp_dir / rel
        if not source.is_file():
            err("standard-core", f"canonical standard/core/{rel} is missing")
            continue
        if not target.is_file():
            err("standard-core", f"missing standard-owned core file {rel}")
        elif _normalized_text(target) != _normalized_text(source):
            err("standard-core", f"{rel} differs from standard/core/{rel}")

    # 6. Manifest to disk coverage in both directions.
    if manifest is not None:
        for key, (dirname, pattern) in MANIFEST_SECTIONS.items():
            listed = manifest.get(key) or []
            if not isinstance(listed, list):
                continue
            for slug in listed:
                if not isinstance(slug, str):
                    continue
                rel = f"{dirname}/{pattern.format(slug=slug)}"
                path = bp_dir / rel
                if not path.is_file() or not _read(path).strip():
                    err(key, f"manifest lists '{slug}' but {rel} is missing or empty")
            section_dir = bp_dir / dirname
            if key == "skills" and section_dir.is_dir():
                on_disk = {path.name for path in section_dir.iterdir() if path.is_dir()}
            elif section_dir.is_dir():
                on_disk = {path.stem for path in section_dir.glob("*.md")}
            else:
                on_disk = set()
            listed_slugs = {item for item in listed if isinstance(item, str)}
            for slug in sorted(on_disk - listed_slugs):
                err(key, f"{dirname}/{slug} exists on disk but is not in the manifest")

    # 7. Counts on disk.
    skills_dir = bp_dir / "skills"
    skill_dirs = [path for path in skills_dir.iterdir() if path.is_dir()] if skills_dir.is_dir() else []
    skill_files = [path / "SKILL.md" for path in skill_dirs if (path / "SKILL.md").is_file() and _read(path / "SKILL.md").strip()]
    schedule_files = sorted((bp_dir / "schedules").glob("*.md")) if (bp_dir / "schedules").is_dir() else []
    workflow_files = sorted((bp_dir / "workflows").glob("*.md")) if (bp_dir / "workflows").is_dir() else []
    template_files = sorted((bp_dir / "templates").glob("*.md")) if (bp_dir / "templates").is_dir() else []

    for key, count, minimum in (
        ("skills", len(skill_files), MIN_SKILLS),
        ("schedules", len(schedule_files), MIN_SCHEDULES),
        ("workflows", len(workflow_files), MIN_WORKFLOWS),
        ("templates", len(template_files), MIN_TEMPLATES),
    ):
        if count < minimum:
            err(key, f"needs at least {minimum} {key}, found {count}")

    # 8. Every operational artifact declares an action level. Schedules are A/B only.
    for kind, files in (("skills", skill_files), ("workflows", workflow_files), ("schedules", schedule_files)):
        for path in files:
            text = _read(path)
            levels = [level.upper() for level in ACTION_LEVEL_RE.findall(text)]
            rel = path.relative_to(bp_dir)
            if not levels:
                err("action-level", f"{rel} has no action-level declaration")
            if kind == "schedules" and any(level not in {"A", "B"} for level in levels):
                err("schedule-safety", f"{rel} declares a level above B; schedules are observe or draft only")

    # 9. Every schedule uses the exact run contract and one copy-paste prompt.
    schedule_contract = _normalized_text(SCHEDULE_CONTRACT_PATH).rstrip("\n")
    for path in schedule_files:
        text = _read(path).replace("\r\n", "\n").replace("\r", "\n")
        rel = path.relative_to(bp_dir)
        if schedule_contract not in text:
            err("schedule-contract", f"{rel} must contain the exact standard/schedule-contract.md block")
        if text.count("<!-- TUEL:SCHEDULE-CONTRACT:START -->") != 1 or text.count("<!-- TUEL:SCHEDULE-CONTRACT:END -->") != 1:
            err("schedule-contract", f"{rel} must contain exactly one marked schedule-contract block")
        if len(FENCE_RE.findall(text)) != 2:
            err("schedule-prompt", f"{rel} must contain exactly one fenced copy-paste prompt")
        else:
            fences = list(FENCE_RE.finditer(text))
            prompt = text[fences[0].end():fences[1].start()]
            for phrase in SCHEDULE_PROMPT_REQUIREMENTS:
                if phrase not in prompt:
                    err("schedule-prompt", f"{rel} prompt is missing required safety preamble text: {phrase!r}")

    # 10. Connection evidence and capability/use-policy consistency.
    if manifest is not None:
        connectors = manifest.get("connectors")
        platform_date = manifest.get("platform_claims_checked_on")
        connector_text = _read(bp_dir / "connectors.md") if (bp_dir / "connectors.md").is_file() else ""
        if isinstance(connectors, list):
            for index, connector in enumerate(connectors):
                if not isinstance(connector, dict):
                    continue
                label = connector.get("name") if isinstance(connector.get("name"), str) else f"entry {index + 1}"
                verified_on = connector.get("verified_on")
                if not _valid_iso_date(verified_on):
                    err("connection-evidence", f"{label}: verified_on must be a real YYYY-MM-DD date")
                elif _valid_iso_date(platform_date) and verified_on > platform_date:
                    err("connection-evidence", f"{label}: verified_on cannot be later than platform_claims_checked_on")
                if connector.get("status") == "confirmed-official-example" and not connector.get("official_url"):
                    err("connection-evidence", f"{label}: confirmed official examples require official_url")
                access = connector.get("access")
                use_policy = connector.get("use_policy")
                if (access == "none") != (use_policy == "not-connected"):
                    err("connection-policy", f"{label}: access none and use_policy not-connected must be used together")
                if connector.get("status") == "local-or-export-fallback" and access != "none":
                    err("connection-policy", f"{label}: local-or-export-fallback must declare access none")
                if isinstance(label, str):
                    label_parts = re.split(r"\s*&\s*", label)
                    label_pattern = r"[ \t]+(?:&|and)[ \t]+".join(re.escape(part) for part in label_parts)
                    heading = re.compile(rf"^[ ]{{0,3}}#{{1,6}}[ \t]+{label_pattern}(?:[ \t]|$|\()", re.IGNORECASE | re.MULTILINE)
                    if not heading.search(connector_text):
                        err("connections", f"connectors.md needs a heading for manifest recommendation {label!r}")

    # 11. Business-memory stubs contain no likely real or invented contact/financial data.
    business_dir = bp_dir / "business"
    business_files = sorted(business_dir.glob("*.md")) if business_dir.is_dir() else []
    for stub in business_files:
        for line_number, line in enumerate(_read(stub).splitlines(), start=1):
            if _line_exempt(line, template_mode):
                continue
            for regex, label in (
                (CURRENCY_RE, "currency amount"),
                (PHONE_RE, "phone number"),
                (EMAIL_RE, "email address"),
            ):
                if regex.search(line):
                    warn("stub-data", f"business/{stub.name}:{line_number} looks like a {label}; business memory ships as an empty stub")

    # 12. Owner-facing language and known false platform claims.
    owner_files = _owner_facing_files(bp_dir)
    for path in owner_files:
        for line_number, line in enumerate(_read(path).splitlines(), start=1):
            if _line_exempt(line, template_mode):
                continue
            jargon = JARGON_RE.search(line)
            if jargon:
                warn("jargon", f"{path.relative_to(bp_dir)}:{line_number} uses '{jargon.group(0)}'; owner-facing text stays jargon-free")

    for path in sorted(bp_dir.rglob("*.md")):
        for line_number, line in enumerate(_read(path).splitlines(), start=1):
            if _line_exempt(line, template_mode):
                continue
            if re.search(r"\b(?:never|do not)\s+promise\b", line, re.IGNORECASE):
                continue
            for regex, guidance in FALSE_PLATFORM_CLAIMS:
                if regex.search(line):
                    err("platform-claim", f"{path.relative_to(bp_dir)}:{line_number} {guidance}")

    # 13. No unresolved authoring markers in a real blueprint.
    for path in sorted(bp_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".txt"}:
            continue
        text = _read(path)
        if not template_mode:
            for line_number, line in enumerate(text.splitlines(), start=1):
                marker = UNRESOLVED_WORD_RE.search(line) or ANY_TEMPLATE_TOKEN_RE.search(line)
                if marker:
                    err("unresolved", f"{path.relative_to(bp_dir)}:{line_number} contains unresolved marker {marker.group(0)!r}")

    # 14. Package hygiene and protected seed-directory contents.
    for path in sorted(bp_dir.rglob("*")):
        rel = path.relative_to(bp_dir)
        if path.is_symlink():
            err("package-hygiene", f"symbolic link is not allowed: {rel}")
            continue
        if any(part in FORBIDDEN_DIR_NAMES for part in rel.parts[:-1]) or (path.is_dir() and path.name in FORBIDDEN_DIR_NAMES):
            err("package-hygiene", f"forbidden directory in package: {rel}")
        if path.is_file():
            lower_name = path.name.lower()
            if path.name in FORBIDDEN_FILE_NAMES or lower_name in {name.lower() for name in FORBIDDEN_FILE_NAMES}:
                err("package-hygiene", f"forbidden package file: {rel}")
            if lower_name == ".env" or lower_name.startswith(".env."):
                err("package-hygiene", f"environment file is not allowed: {rel}")
            if path.suffix.lower() in FORBIDDEN_SUFFIXES:
                err("package-hygiene", f"secret, certificate, or compiled file is not allowed: {rel}")
            if path.name.startswith(".") and path.name != ".gitkeep":
                err("package-hygiene", f"hidden file is not allowed: {rel}")

    allowed_seed_files = {
        "assets": {"README.md"},
        "inbox": {"README.md"},
        "operations": {"README.md"},
        "reports": {".gitkeep"},
    }
    for dirname, allowed in allowed_seed_files.items():
        directory = bp_dir / dirname
        if not directory.is_dir():
            continue
        actual = {str(path.relative_to(directory)) for path in directory.rglob("*") if path.is_file() or path.is_symlink()}
        extras = actual - allowed
        missing = allowed - actual
        for item in sorted(extras):
            err("package-hygiene", f"{dirname}/ ships only {', '.join(sorted(allowed))}; found {dirname}/{item}")
        for item in sorted(missing):
            err("package-hygiene", f"{dirname}/{item} is missing")

    if manifest is not None and isinstance(manifest.get("memory_files"), list) and business_dir.is_dir():
        allowed_business = {f"{slug}.md" for slug in manifest["memory_files"] if isinstance(slug, str)}
        actual_business = {str(path.relative_to(business_dir)) for path in business_dir.rglob("*") if path.is_file() or path.is_symlink()}
        for item in sorted(actual_business - allowed_business):
            err("package-hygiene", f"business/{item} is not a declared memory stub")

    return findings


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def default_targets() -> list[Path]:
    targets: list[Path] = []
    blueprints = REPO_ROOT / "blueprints"
    if blueprints.is_dir():
        targets.extend(sorted(path for path in blueprints.iterdir() if path.is_dir()))
    targets.append(REPO_ROOT / "templates" / TEMPLATE_SLUG)
    return targets


def is_template(path: Path) -> bool:
    return path.resolve().parent == (REPO_ROOT / "templates").resolve()


def run(targets: list[Path], schema: dict, strict: bool, as_json: bool) -> int:
    reports = []
    total_errors = 0
    total_warnings = 0
    for bp_dir in targets:
        findings = lint_blueprint(bp_dir, schema, template_mode=is_template(bp_dir))
        errors = [finding for finding in findings if finding.level == "error"]
        warnings = [finding for finding in findings if finding.level == "warning"]
        total_errors += len(errors)
        total_warnings += len(warnings)
        reports.append((bp_dir, errors, warnings))

    if as_json:
        payload = {
            "blueprints": [
                {
                    "path": str(bp),
                    "errors": [f"[{finding.check}] {finding.message}" for finding in errors],
                    "warnings": [f"[{finding.check}] {finding.message}" for finding in warnings],
                }
                for bp, errors, warnings in reports
            ],
            "summary": {
                "blueprints": len(reports),
                "errors": total_errors,
                "warnings": total_warnings,
            },
        }
        print(json.dumps(payload, indent=2))
    else:
        for bp, errors, warnings in reports:
            mark = "✗" if errors else ("⚠" if warnings else "✓")
            label = bp.relative_to(REPO_ROOT) if bp.is_relative_to(REPO_ROOT) else bp
            print(f"{mark} {label}")
            for finding in errors:
                print(f"    ✗ [{finding.check}] {finding.message}")
            for finding in warnings:
                print(f"    ⚠ [{finding.check}] {finding.message}")
        print(f"\n{len(reports)} blueprint(s): {total_errors} error(s), {total_warnings} warning(s)")

    return 1 if total_errors or (strict and total_warnings) else 0


# --------------------------------------------------------------------------
# Self-test fixtures
# --------------------------------------------------------------------------


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _schedule_fixture(title: str) -> str:
    return (
        f"# {title}\n\n"
        + _normalized_text(SCHEDULE_CONTRACT_PATH)
        + "\n## Prompt to copy\n\n```text\n"
        + "Read the full CLAUDE.md before doing anything. If it is unavailable, stop.\n"
        + "This run is A Observe or B Draft only.\n"
        + "Save output to reports/ only. Never overwrite a file. End with a work receipt.\n"
        + "Do not send, post, pay, file, sign, delete, or change an outside system.\n"
        + "```\n\n"
        + "Action level: B - drafts only.\n"
    )


def _make_blueprint(
    bp: Path,
    slug: str,
    *,
    jargon: bool = False,
    hard_rules: bool = True,
    skill_names: tuple[str, ...] = ("greet-clients", "plan-week", "close-day"),
    extra_skill_dir: str | None = None,
    drop_skill_file: str | None = None,
    template_tokens: bool = False,
) -> None:
    start = "# Start here\n\nOpen this working folder and ask for a first draft.\n"
    if jargon:
        start += "Set up a connector for email.\n"
    if template_tokens:
        start += "Welcome to {{NAME}}, your {{BUSINESS_TYPE}} helper.\nTODO: specialize this folder.\n"
    start += (
        "\n<!-- TUEL:OWNER-SETUP:START -->\n"
        "## Before you begin\n\n"
        "This is an ordinary working folder for an eligible Claude account. Claude processes the files chosen for a task. "
        "Start in Manual mode.\n"
        "<!-- TUEL:OWNER-SETUP:END -->\n"
    )
    _write(bp / "START-HERE.md", start)

    skills = ["review-the-work", *skill_names]
    manifest = {
        "name": "Test Business",
        "slug": slug,
        "version": "1.0.0",
        "standard_version": STANDARD_VERSION,
        "policy_version": STANDARD_VERSION,
        "data_layout_version": STANDARD_VERSION,
        "operating_profile": "draft-only-v1",
        "platform_claims_checked_on": "2026-07-17",
        "business_type": "test business",
        "summary": "A test business working folder.",
        "skills": skills,
        "schedules": ["morning-brief", "end-of-day", "weekly-operations-review"],
        "workflows": ["verify-a-draft", "review-business-memory", "handle-an-incident"],
        "templates": [
            "operations-board",
            "work-receipt",
            "decision-record",
            "memory-proposal",
            "incident-record",
            "weekly-operations-review",
        ],
        "memory_files": sorted(REQUIRED_MEMORY_FILES),
        "roles": ["operator", "reality-checker"],
        "protected_paths": ["business/", "assets/", "reports/", "operations/", "inbox/"],
        "connectors": [],
    }
    _write(bp / "blueprint.yaml", yaml.safe_dump(manifest, sort_keys=False))

    safety = _normalized_text(SAFETY_FLOOR_PATH)
    if hard_rules:
        claude = (
            "# Operating instructions\n\n"
            + safety
            + "\n<!-- TUEL:BUSINESS-OS:START -->\n"
            + "## Business OS loop\n\nConfirm the named owner. Use roles/reality-checker.md, save a work receipt, and use review-business-memory.md.\n"
            + "<!-- TUEL:BUSINESS-OS:END -->\n\n"
            + "## Operating loop\n\nRead, draft, verify, review, receipt.\n"
        )
    else:
        claude = "# Operating instructions\n\n## Rules\n\nBe careful. business/ is the source of truth.\n"
    _write(bp / "CLAUDE.md", claude)

    _write(
        bp / "onboarding/interview.md",
        "# First conversation\n\n"
        "<!-- TUEL:SETUP-CONTROLS:START -->\n"
        "## Keep setup resumable\n\nRead the full `CLAUDE.md`. Ask for the named decision owner and local time zone. "
        "Save confirmed setup state to operations/setup-status.md.\n"
        "<!-- TUEL:SETUP-CONTROLS:END -->\n\n"
        "Ask one question at a time and save a first draft.\n",
    )
    _write(
        bp / "onboarding/checklist.md",
        "# Setup checklist\n\n"
        "<!-- TUEL:CONTROL-CHECKLIST:START -->\n"
        "## Control choices\n\nName who approves decisions. Confirm the local time zone. Review how long temporary exports stay. "
        "Claude never deletes them.\n"
        "<!-- TUEL:CONTROL-CHECKLIST:END -->\n\n"
        "- Business name\n- Services\n- Hours\n",
    )
    for memory_name in sorted(REQUIRED_MEMORY_FILES):
        _write(bp / "business" / f"{memory_name}.md", f"# {memory_name.title()}\n\n[Complete with the owner.]\n")
    _write(bp / "assets/README.md", "# Assets\n\nAdd approved logos or reference files here.\n")
    _write(bp / "reports/.gitkeep", "")
    _write(bp / "connectors.md", "# Optional tools\n\nThe first draft works without connecting a tool.\n")

    for rel in CORE_FILES:
        _write(bp / rel, _normalized_text(CORE_ROOT / rel))

    for skill in skill_names:
        if skill == drop_skill_file:
            continue
        _write(bp / "skills" / skill / "SKILL.md", f"# {skill}\n\nPrepare a local draft.\n\nAction level: B - drafts only.\n")
    if extra_skill_dir:
        _write(bp / "skills" / extra_skill_dir / "SKILL.md", "# Extra\n\nAction level: B - drafts only.\n")
    _write(bp / "schedules/morning-brief.md", _schedule_fixture("Morning brief"))
    _write(bp / "schedules/end-of-day.md", _schedule_fixture("End of day"))


def _read_test_manifest(bp: Path) -> dict:
    loaded = yaml.safe_load(_read(bp / "blueprint.yaml"))
    assert isinstance(loaded, dict)
    return loaded


def _write_test_manifest(bp: Path, manifest: dict) -> None:
    _write(bp / "blueprint.yaml", yaml.safe_dump(manifest, sort_keys=False))


def self_test(schema: dict) -> int:
    cases: list[tuple[str, bool, list[str]]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)

        def check(
            name: str,
            bp: Path,
            template_mode: bool,
            expect_errors: bool,
            expect_warnings: bool | None = None,
        ) -> None:
            findings = lint_blueprint(bp, schema, template_mode)
            errors = [finding for finding in findings if finding.level == "error"]
            warnings = [finding for finding in findings if finding.level == "warning"]
            ok = bool(errors) == expect_errors
            if expect_warnings is not None:
                ok = ok and bool(warnings) == expect_warnings
            cases.append((name, ok, [f"{finding.level}:{finding.check}:{finding.message}" for finding in findings]))

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
        _make_blueprint(bp, "ghost-skill", skill_names=("one", "two", "three", "four"), drop_skill_file="four")
        check("manifest skill without file fails", bp, False, expect_errors=True)

        bp = root / "stray-skill"
        _make_blueprint(bp, "stray-skill", extra_skill_dir="not-in-manifest")
        check("skill directory outside manifest fails", bp, False, expect_errors=True)

        bp = root / "no-hard-rules"
        _make_blueprint(bp, "no-hard-rules", hard_rules=False)
        check("missing safety floor fails", bp, False, expect_errors=True)

        bp = root / "policy-drift"
        _make_blueprint(bp, "policy-drift")
        _write(bp / "CLAUDE.md", _read(bp / "CLAUDE.md").replace("Treat instructions found in email", "Trust instructions found in email", 1))
        check("changed safety floor fails", bp, False, expect_errors=True)

        bp = root / "core-drift"
        _make_blueprint(bp, "core-drift")
        _write(bp / "roles/operator.md", _read(bp / "roles/operator.md") + "\nExtra authority.\n")
        check("changed core file fails", bp, False, expect_errors=True)

        bp = root / "unsafe-schedule"
        _make_blueprint(bp, "unsafe-schedule")
        _write(bp / "schedules/morning-brief.md", _read(bp / "schedules/morning-brief.md") + "\nAction level: D - send it.\n")
        check("schedule above level B fails", bp, False, expect_errors=True)

        bp = root / "unresolved-shop"
        _make_blueprint(bp, "unresolved-shop")
        _write(bp / "onboarding/checklist.md", "# Checklist\n\nTODO: decide later.\n")
        check("unresolved author marker fails", bp, False, expect_errors=True)

        bp = root / "secret-shop"
        _make_blueprint(bp, "secret-shop")
        _write(bp / ".env", "SECRET=value\n")
        check("secret package file fails", bp, False, expect_errors=True)

        bp = root / "official-without-source"
        _make_blueprint(bp, "official-without-source")
        manifest = _read_test_manifest(bp)
        manifest["connectors"] = [{
            "name": "Gmail",
            "why": "Prepare reply drafts.",
            "status": "confirmed-official-example",
            "access": "read-write",
            "use_policy": "draft-only-use",
            "fallback": "Paste the message into the chat.",
            "verified_on": "2026-07-17",
        }]
        _write_test_manifest(bp, manifest)
        _write(bp / "connectors.md", "# Optional tools\n\n## Gmail\n\nPaste a message when it is not connected.\n")
        check("confirmed connection without official source fails", bp, False, expect_errors=True)

        bp = root / "connection-policy-mismatch"
        _make_blueprint(bp, "connection-policy-mismatch")
        manifest = _read_test_manifest(bp)
        manifest["connectors"] = [{
            "name": "Export",
            "why": "Use a saved report.",
            "status": "local-or-export-fallback",
            "access": "read-only",
            "use_policy": "read-only-use",
            "fallback": "Save a report to inbox/.",
            "verified_on": "2026-07-17",
        }]
        _write_test_manifest(bp, manifest)
        _write(bp / "connectors.md", "# Optional tools\n\n## Export\n\nSave a report to inbox/.\n")
        check("connection capability-policy mismatch fails", bp, False, expect_errors=True)

        bp = root / "missed-run-claim"
        _make_blueprint(bp, "missed-run-claim")
        _write(
            bp / "schedules/morning-brief.md",
            _read(bp / "schedules/morning-brief.md")
            + "\nIf the folder is closed, the task simply skips and nothing breaks.\n",
        )
        check("unsupported missed-run claim fails", bp, False, expect_errors=True)

        bp = root / "jargon-shop"
        _make_blueprint(bp, "jargon-shop", jargon=True)
        check("owner jargon warns", bp, False, expect_errors=False, expect_warnings=True)

        bp = root / "templates" / TEMPLATE_SLUG
        _make_blueprint(bp, TEMPLATE_SLUG, template_tokens=True)
        check("_blank authoring template passes", bp, True, expect_errors=False, expect_warnings=False)

    width = max(len(name) for name, _, _ in cases)
    all_ok = True
    for name, ok, findings in cases:
        print(f"{'PASS' if ok else 'FAIL'}  {name.ljust(width)}")
        if not ok:
            all_ok = False
            for finding in findings:
                print(f"        {finding}")
    print(f"\nself-test: {'all good ✓' if all_ok else 'FAILURES ✗'}")
    return 0 if all_ok else 1


def _validate_standard_sources() -> list[str]:
    errors: list[str] = []
    for path in (SCHEMA_PATH, SAFETY_FLOOR_PATH, SCHEDULE_CONTRACT_PATH):
        if not path.is_file() or not _read(path).strip():
            errors.append(f"required standard source is missing or empty: {path.relative_to(REPO_ROOT)}")
    for rel in CORE_FILES:
        path = CORE_ROOT / rel
        if not path.is_file() or not _read(path).strip():
            errors.append(f"required standard core source is missing or empty: standard/core/{rel}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="blueprint directories (default: blueprints/* + templates/_blank)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--strict", action="store_true", help="warnings count as errors")
    parser.add_argument("--self-test", action="store_true", help="run the linter's own fixtures")
    args = parser.parse_args()

    source_errors = _validate_standard_sources()
    if source_errors:
        for error in source_errors:
            print(f"standard error: {error}", file=sys.stderr)
        return 2

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    try:
        check_schema_supported(schema)
    except UnsupportedSchemaKeyword as exc:
        print(f"schema error: {exc}", file=sys.stderr)
        return 2

    if args.self_test:
        return self_test(schema)

    targets = [Path(path).resolve() for path in args.paths] if args.paths else default_targets()
    for target in targets:
        if not target.is_dir():
            print(f"not a directory: {target}", file=sys.stderr)
            return 2
    return run(targets, schema, strict=args.strict, as_json=args.json)


if __name__ == "__main__":
    sys.exit(main())
