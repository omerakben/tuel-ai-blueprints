#!/usr/bin/env python3
"""Build the GitHub Pages site into _site/.

Reads every blueprints/*/blueprint.yaml, injects the catalog into
web/index.html, and produces one deterministic ZIP per blueprint under
_site/downloads/. Standard library + PyYAML only.

Usage: python tools/build_site.py
"""

from __future__ import annotations

import json
import shutil
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

# Presentation facts the manifests do not carry. Every blueprint must
# appear here — the build fails loudly on a missing or extra entry.
META: dict[str, dict[str, str]] = {
    "salon":            {"cat": "care",   "emoji": "\U0001F488", "win": "This week's promo post, ready to go", "kw": "barber beauty hair stylist"},
    "cafe":             {"cat": "food",   "emoji": "☕",     "win": "Today's special, drafted and ready to post", "kw": "coffee espresso shop"},
    "bakery":           {"cat": "food",   "emoji": "\U0001F950", "win": "A custom-order reply, ready to send", "kw": "patisserie pastry bread cake"},
    "restaurant":       {"cat": "food",   "emoji": "\U0001F35D", "win": "A reservation reply, ready to send", "kw": "diner bistro kitchen"},
    "bar":              {"cat": "food",   "emoji": "\U0001F378", "win": "Tonight's promo, drafted", "kw": "pub tavern cocktails"},
    "food-truck":       {"cat": "food",   "emoji": "\U0001F69A", "win": "Today's location post, ready", "kw": "street food stall market"},
    "boutique":         {"cat": "shops",  "emoji": "\U0001F457", "win": "A new-arrivals post, ready", "kw": "retail clothing store shop"},
    "florist":          {"cat": "shops",  "emoji": "\U0001F490", "win": "A custom-order reply, ready to send", "kw": "flowers blooms wedding"},
    "tattoo-studio":    {"cat": "shops",  "emoji": "\U0001F58B", "win": "An inquiry reply, ready to send", "kw": "ink artist"},
    "photographer":     {"cat": "shops",  "emoji": "\U0001F4F8", "win": "An inquiry reply, ready to send", "kw": "photo camera portraits weddings"},
    "event-planner":    {"cat": "shops",  "emoji": "\U0001F3AA", "win": "An inquiry reply, ready to send", "kw": "weddings parties events"},
    "gym":              {"cat": "care",   "emoji": "\U0001F3CB", "win": "A class-fill post, ready", "kw": "fitness studio training"},
    "pet-groomer":      {"cat": "care",   "emoji": "\U0001F429", "win": "Your due-back list, texts drafted", "kw": "dog cat grooming pets"},
    "tutoring-studio":  {"cat": "care",   "emoji": "\U0001F4DA", "win": "A parent inquiry reply, ready", "kw": "tutor lessons students teaching"},
    "cleaning-service": {"cat": "trades", "emoji": "\U0001F9FD", "win": "A job estimate, drafted", "kw": "maid janitorial house office"},
    "lawn-care":        {"cat": "trades", "emoji": "\U0001F331", "win": "A yard estimate, drafted", "kw": "landscaping mowing garden"},
    "plumber":          {"cat": "trades", "emoji": "\U0001F527", "win": "A job estimate, drafted", "kw": "pipes leak drain trades"},
    "handyman":         {"cat": "trades", "emoji": "\U0001F528", "win": "A job estimate, drafted", "kw": "repairs odd jobs fix"},
    "auto-repair":      {"cat": "trades", "emoji": "\U0001F697", "win": "A customer status update, drafted", "kw": "mechanic garage car shop"},
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
            "business_type": manifest["business_type"],
            "summary": manifest["summary"],
            "category": meta["cat"],
            "emoji": meta["emoji"],
            "first_win": meta["win"],
            "keywords": meta["kw"],
        })
    catalog.sort(key=lambda b: (CATEGORY_ORDER[b["category"]], b["name"]))
    return catalog


def build_zip(slug: str, dest: Path) -> None:
    src = REPO_ROOT / "blueprints" / slug
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(src.rglob("*")):
            if path.is_file() and ".DS_Store" not in path.name:
                arcname = f"{slug}/{path.relative_to(src)}"
                info = zipfile.ZipInfo(arcname, date_time=ZIP_DATE)
                info.external_attr = 0o644 << 16
                zf.writestr(info, path.read_bytes())


def main() -> int:
    catalog = load_catalog()

    template = (REPO_ROOT / "web" / "index.html").read_text(encoding="utf-8")
    placeholder = "/*__CATALOG__*/[]"
    if placeholder not in template:
        sys.exit("web/index.html is missing the /*__CATALOG__*/[] placeholder")
    page = template.replace(placeholder, json.dumps(catalog, ensure_ascii=False))

    if SITE.exists():
        shutil.rmtree(SITE)
    (SITE / "downloads").mkdir(parents=True)
    (SITE / "index.html").write_text(page, encoding="utf-8")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")

    for entry in catalog:
        build_zip(entry["slug"], SITE / "downloads" / f"{entry['slug']}.zip")

    print(f"built _site/: index.html + {len(catalog)} zips")
    return 0


if __name__ == "__main__":
    sys.exit(main())
