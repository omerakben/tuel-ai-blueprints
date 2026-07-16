#!/usr/bin/env python3
"""Scaffold a new blueprint from templates/_blank.

Usage:
    python tools/create_blueprint.py <slug> --name "Salon" --business-type "barber & beauty salon"

Copies templates/_blank to blueprints/<slug>, fills in the {{NAME}} and
{{BUSINESS_TYPE}} placeholders (plus {{SLUG}} where present), sets the
manifest slug so the fresh copy lints clean, and renames any path that
contains {{SLUG}}. Standard library only.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import re
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BLANK = REPO_ROOT / "templates" / "_blank"
SLUG_RE = re.compile(r"^[a-z][a-z0-9-]*$")
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".txt", ".csv"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="lowercase-hyphen blueprint slug, e.g. salon")
    parser.add_argument("--name", required=True, help='human name, e.g. "Salon"')
    parser.add_argument("--business-type", required=True, help='e.g. "barber & beauty salon"')
    args = parser.parse_args()

    if not SLUG_RE.match(args.slug):
        print(f"slug {args.slug!r} must match {SLUG_RE.pattern}", file=sys.stderr)
        return 2
    for label, value in (("--name", args.name), ("--business-type", args.business_type)):
        if '"' in value or "\\" in value:
            print(f"{label} must not contain double quotes or backslashes", file=sys.stderr)
            return 2
    if not BLANK.is_dir() or not any(BLANK.iterdir()):
        print("templates/_blank is missing or empty — it is authored separately.", file=sys.stderr)
        return 2
    dest = REPO_ROOT / "blueprints" / args.slug
    if dest.exists():
        print(f"{dest} already exists — refusing to overwrite.", file=sys.stderr)
        return 2

    if not (BLANK / "blueprint.yaml").is_file():
        print("templates/_blank has no blueprint.yaml — not a valid scaffold.", file=sys.stderr)
        return 2

    # Stage in a temp dir beside the destination, then rename atomically, so a
    # failure mid-way never strands a half-built blueprints/<slug>.
    staging_parent = Path(tempfile.mkdtemp(dir=dest.parent, prefix=".scaffold-"))
    try:
        staged = staging_parent / args.slug
        shutil.copytree(BLANK, staged)

        replacements = {
            "{{SLUG}}": args.slug,
            "{{NAME}}": args.name,
            "{{BUSINESS_TYPE}}": args.business_type,
        }
        for path in sorted(staged.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                text = path.read_text(encoding="utf-8")
                for token, value in replacements.items():
                    text = text.replace(token, value)
                path.write_text(text, encoding="utf-8")
            if "{{SLUG}}" in path.name:
                path.rename(path.with_name(path.name.replace("{{SLUG}}", args.slug)))

        manifest = staged / "blueprint.yaml"
        text = manifest.read_text(encoding="utf-8")
        text = re.sub(r"(?m)^slug:.*$", f"slug: {args.slug}", text, count=1)
        manifest.write_text(text, encoding="utf-8")

        staged.rename(dest)
    finally:
        shutil.rmtree(staging_parent, ignore_errors=True)

    print(f"Created blueprints/{args.slug} from templates/_blank.")
    print("Next steps:")
    print(f"  1. Fill in the TODO markers in blueprints/{args.slug}/")
    print(f"  2. Run: python tools/lint.py blueprints/{args.slug}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
