#!/usr/bin/env python3
"""Build the GitHub Pages site into _site/.

Reads every blueprints/*/blueprint.yaml, injects the catalog into
web/index.html, and produces one deterministic ZIP per blueprint under
_site/downloads/. Standard library + PyYAML only.

Usage: python tools/build_site.py
"""

from __future__ import annotations

import json
import hashlib
import shutil
import stat
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("build_site.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
SITE = REPO_ROOT / "_site"
ZIP_DATE = (2026, 1, 1, 0, 0, 0)  # fixed timestamp keeps archives deterministic
WEB_ASSETS = REPO_ROOT / "web" / "assets"
TUEL_PUBLIC = REPO_ROOT.parent / "tuel-ai" / "public"
TUEL_BRAND_ASSETS = ("tuel-icon.svg", "tuel-logo-nav-dark.svg")

# Presentation facts the manifests do not carry. Every blueprint must
# appear here — the build fails loudly on a missing or extra entry.
META: dict[str, dict[str, str]] = {
    "salon":            {"cat": "care",   "emoji": "\U0001F488", "win": "This week's promo post, drafted for your review", "kw": "barber beauty hair stylist"},
    "cafe":             {"cat": "food",   "emoji": "☕",     "win": "Today's special, drafted for your review", "kw": "coffee espresso shop"},
    "bakery":           {"cat": "food",   "emoji": "\U0001F950", "win": "A custom-order reply, drafted for your review", "kw": "patisserie pastry bread cake"},
    "restaurant":       {"cat": "food",   "emoji": "\U0001F35D", "win": "A reservation reply, drafted for your review", "kw": "diner bistro kitchen"},
    "bar":              {"cat": "food",   "emoji": "\U0001F378", "win": "Tonight's promo, drafted for your review", "kw": "pub tavern cocktails"},
    "food-truck":       {"cat": "food",   "emoji": "\U0001F69A", "win": "Today's location post, drafted for your review", "kw": "street food stall market"},
    "boutique":         {"cat": "shops",  "emoji": "\U0001F457", "win": "A new-arrivals post, drafted for your review", "kw": "retail clothing store shop"},
    "florist":          {"cat": "shops",  "emoji": "\U0001F490", "win": "A custom-order reply, drafted for your review", "kw": "flowers blooms wedding"},
    "tattoo-studio":    {"cat": "shops",  "emoji": "\U0001F58B", "win": "An inquiry reply, drafted for your review", "kw": "ink artist"},
    "photographer":     {"cat": "shops",  "emoji": "\U0001F4F8", "win": "An inquiry reply, drafted for your review", "kw": "photo camera portraits weddings"},
    "event-planner":    {"cat": "shops",  "emoji": "\U0001F3AA", "win": "An inquiry reply, drafted for your review", "kw": "weddings parties events"},
    "gym":              {"cat": "care",   "emoji": "\U0001F3CB", "win": "A class-fill post, drafted for your review", "kw": "fitness studio training"},
    "pet-groomer":      {"cat": "care",   "emoji": "\U0001F429", "win": "Your due-back list and text drafts, prepared for review", "kw": "dog cat grooming pets"},
    "tutoring-studio":  {"cat": "care",   "emoji": "\U0001F4DA", "win": "A parent inquiry reply, drafted for your review", "kw": "tutor lessons students teaching"},
    "cleaning-service": {"cat": "trades", "emoji": "\U0001F9FD", "win": "A job estimate, drafted for your review", "kw": "maid janitorial house office"},
    "lawn-care":        {"cat": "trades", "emoji": "\U0001F331", "win": "A yard estimate, drafted for your review", "kw": "landscaping mowing garden"},
    "plumber":          {"cat": "trades", "emoji": "\U0001F527", "win": "A job estimate, drafted for your review", "kw": "pipes leak drain trades"},
    "handyman":         {"cat": "trades", "emoji": "\U0001F528", "win": "A job estimate, drafted for your review", "kw": "repairs odd jobs fix"},
    "auto-repair":      {"cat": "trades", "emoji": "\U0001F697", "win": "A customer status update, drafted for your review", "kw": "mechanic garage car shop"},
}

CATEGORY_ORDER = {"food": 0, "shops": 1, "care": 2, "trades": 3}


def load_catalog() -> list[dict[str, str]]:
    found = {p.parent.name: p for p in sorted(REPO_ROOT.glob("blueprints/*/blueprint.yaml"))}
    missing = sorted(set(found) - set(META))
    extra = sorted(set(META) - set(found))
    if missing or extra:
        sys.exit(f"build_site.py META map out of date — on disk but unmapped: {missing}; mapped but not on disk: {extra}")

    catalog = []
    for slug, manifest_path in found.items():
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        meta = META[slug]
        catalog.append({
            "slug": slug,
            "name": manifest["name"],
            "version": manifest["version"],
            "business_type": manifest["business_type"],
            "summary": manifest["summary"],
            "category": meta["cat"],
            "emoji": meta["emoji"],
            "first_win": meta["win"],
            "keywords": meta["kw"],
        })
    catalog.sort(key=lambda b: (CATEGORY_ORDER[b["category"]], b["name"]))
    return catalog


def blueprint_files(slug: str) -> list[Path]:
    src = REPO_ROOT / "blueprints" / slug
    return [
        path
        for path in sorted(src.rglob("*"))
        if path.is_file() and path.name != ".DS_Store"
    ]


def build_zip(slug: str, dest: Path) -> int:
    src = REPO_ROOT / "blueprints" / slug
    files = blueprint_files(slug)
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in files:
            arcname = f"{slug}/{path.relative_to(src)}"
            info = zipfile.ZipInfo(arcname, date_time=ZIP_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            zf.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return len(files)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def format_bytes(size: int) -> str:
    if size < 1024:
        return f"{size} B"
    if size < 1024 * 1024:
        return f"{size / 1024:.1f} KB"
    return f"{size / (1024 * 1024):.1f} MB"


def copy_site_assets() -> None:
    if not WEB_ASSETS.is_dir():
        sys.exit("web/assets is missing")
    shutil.copytree(WEB_ASSETS, SITE / "assets")

    # The checked-in copies keep remote builds self-contained. When the main
    # TUEL checkout is beside this repository, use its canonical brand files
    # and fail if the copies have drifted.
    if not TUEL_PUBLIC.is_dir():
        return
    for asset_name in TUEL_BRAND_ASSETS:
        canonical = TUEL_PUBLIC / asset_name
        vendored = WEB_ASSETS / asset_name
        if not canonical.is_file() or not vendored.is_file():
            sys.exit(f"missing TUEL brand asset: {asset_name}")
        if sha256(canonical) != sha256(vendored):
            sys.exit(
                f"web/assets/{asset_name} is out of sync with "
                f"{canonical}; refresh the checked-in copy"
            )
        shutil.copy2(canonical, SITE / "assets" / asset_name)


def main() -> int:
    catalog = load_catalog()

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "downloads").mkdir(parents=True)
    copy_site_assets()
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    checksum_lines = []
    for entry in catalog:
        filename = f"{entry['slug']}.zip"
        archive = SITE / "downloads" / filename
        entry["file_count"] = build_zip(entry["slug"], archive)
        entry["zip_size"] = format_bytes(archive.stat().st_size)
        entry["sha256"] = sha256(archive)
        checksum_line = f"{entry['sha256']}  {filename}\n"
        checksum_lines.append(checksum_line)
        (SITE / "downloads" / f"{filename}.sha256").write_text(
            checksum_line, encoding="ascii", newline="\n"
        )

    (SITE / "downloads" / "SHA256SUMS.txt").write_text(
        "".join(checksum_lines), encoding="ascii", newline="\n"
    )

    template = (REPO_ROOT / "web" / "index.html").read_text(encoding="utf-8")
    placeholder = "/*__CATALOG__*/[]"
    if placeholder not in template:
        sys.exit("web/index.html is missing the /*__CATALOG__*/[] placeholder")
    catalog_json = json.dumps(catalog, ensure_ascii=False, separators=(",", ":")).replace(
        "<", "\\u003c"
    )
    page = template.replace(placeholder, catalog_json)
    (SITE / "index.html").write_text(page, encoding="utf-8", newline="\n")

    print(
        f"built _site/: index.html + {len(catalog)} deterministic zips "
        "+ SHA256 checksums"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
