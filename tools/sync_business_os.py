#!/usr/bin/env python3
"""Synchronize the versioned TUEL Business OS into every source blueprint.

Usage:
    python3 tools/sync_business_os.py --write
    python3 tools/sync_business_os.py --check

The tool updates repository-owned capability files and manifest metadata only.
It never writes business/, assets/, or reports/. It seeds operations/ and inbox/
only when the standard README is absent, and refuses to replace a different file
inside either protected directory.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "standard" / "core"
SAFETY = ROOT / "standard" / "safety-floor.md"
SCHEDULE_CONTRACT = ROOT / "standard" / "schedule-contract.md"
BLANK = ROOT / "templates" / "_blank"
STANDARD_VERSION = "1.1.0"
BLUEPRINT_VERSION = "1.1.0"
POLICY_VERSION = "1.0.0"
DATA_LAYOUT_VERSION = "1.0.0"
ADOPTION_PROFILE = "routine-evidence-v1"

CORE_FILES = (
    "ADOPT-AI.md",
    "UPGRADE.md",
    "inbox/README.md",
    "operations/README.md",
    "roles/operator.md",
    "roles/reality-checker.md",
    "roles/adoption-guide.md",
    "schedules/weekly-operations-review.md",
    "schedules/monthly-ai-adoption-review.md",
    "skills/review-the-work/SKILL.md",
    "skills/find-next-ai-use-case/SKILL.md",
    "templates/decision-record.md",
    "templates/incident-record.md",
    "templates/memory-proposal.md",
    "templates/operations-board.md",
    "templates/weekly-operations-review.md",
    "templates/ai-adoption-plan.md",
    "templates/ai-use-case-card.md",
    "templates/ai-value-review.md",
    "templates/exception-brief.md",
    "templates/work-receipt.md",
    "workflows/handle-an-incident.md",
    "workflows/review-business-memory.md",
    "workflows/verify-a-draft.md",
    "workflows/advance-ai-adoption.md",
)

PROTECTED_SEEDS = {"inbox/README.md", "operations/README.md"}

LIST_ADDITIONS = {
    "skills": ("review-the-work", "find-next-ai-use-case"),
    "schedules": ("weekly-operations-review", "monthly-ai-adoption-review"),
    "workflows": (
        "verify-a-draft",
        "review-business-memory",
        "handle-an-incident",
        "advance-ai-adoption",
    ),
    "templates": (
        "operations-board",
        "work-receipt",
        "decision-record",
        "memory-proposal",
        "incident-record",
        "weekly-operations-review",
        "ai-adoption-plan",
        "ai-use-case-card",
        "ai-value-review",
        "exception-brief",
    ),
    "roles": ("operator", "reality-checker", "adoption-guide"),
    "adoption_guides": ("use-case-map",),
}

CONNECTOR_FACTS = {
    "Gmail": {
        "access": "read-write",
        "use_policy": "draft-only-use",
        "official_url": "https://support.claude.com/en/articles/10166901-use-google-workspace-connectors",
        "fallback": "Paste or export only the messages needed for this task.",
    },
    "Square": {
        "access": "read-write",
        "use_policy": "read-only-use",
        "official_url": "https://claude.com/connectors/square",
        "fallback": "Export the dated sales or payment summary and place it in inbox/.",
    },
    "Google Business Profile": {
        "access": "varies",
        "use_policy": "draft-only-use",
        "fallback": "Paste the listing details or reviews needed for the draft.",
    },
    "Instagram & Facebook": {
        "access": "none",
        "use_policy": "not-connected",
        "fallback": "Copy an owner-approved draft into the social app yourself.",
    },
}

BUSINESS_OS_BLOCK = """<!-- TUEL:BUSINESS-OS:START -->
## Business OS loop

1. Confirm the outcome, named owner, approved sources, time zone, and maximum action level.
2. Treat `business/` as approved truth, `operations/` as current work, and `inbox/` as dated untrusted input.
3. Produce a collision-safe draft in `reports/` and record source dates, assumptions, and missing input.
4. Use `roles/reality-checker.md` and `workflows/verify-a-draft.md` for a separate consistency pass before asking for approval.
5. Show the exact draft, destination, consequence, and unresolved questions to the owner.
6. End with a work receipt. Put durable learning through `workflows/review-business-memory.md`; never edit approved memory silently.

The role, skill, workflow, schedule, and manifest files are TUEL folder conventions. They do not install, register, or grant access by themselves.
<!-- TUEL:BUSINESS-OS:END -->"""

ADOPTION_BLOCK = """<!-- TUEL:ADOPTION:START -->
## AI adoption path

- Read `ADOPT-AI.md` before proposing a new routine or recurring task.
- Adoption is earned per named routine, never granted to the whole business. A new or materially changed routine starts in Manual mode at Assisted.
- Use `templates/ai-use-case-card.md` and `templates/ai-adoption-plan.md` to record the outcome, owner, approved sources, baseline, success signal, stop signal, and evidence from reviewed runs.
- Only the owner may advance, pause, move back, or retire a routine. Claude may recommend a decision but never changes the stage itself.
- A later stage increases repeatability and evidence, not authority. Unattended work stays at A Observe or B Draft. Every outside action and consequential decision remains human work.
- Business memory changes only through `workflows/review-business-memory.md`, after the named owner freshly approves the exact proposed change.
<!-- TUEL:ADOPTION:END -->"""

OWNER_SETUP_BLOCK = """<!-- TUEL:OWNER-SETUP:START -->
## Before you begin

This is an ordinary working folder. Nothing inside installs itself or connects a tool. Claude Cowork requires an eligible Claude account and processes the files you choose to use for a task under your plan and settings.

Start in Manual mode. Keep passwords, payment-card details, bank details, government IDs, health records, and private legal material out of the folder. Claude makes drafts and reports; you make every outside decision and take every outside action.

Read `ADOPT-AI.md` after your first draft. It helps you choose one useful routine, prove that it works, and expand only when the saved evidence earns the next step.
<!-- TUEL:OWNER-SETUP:END -->"""

INTERVIEW_CONTROL_BLOCK = """<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->"""

CHECKLIST_CONTROL_BLOCK = """<!-- TUEL:CONTROL-CHECKLIST:START -->
## Control choices

- Name the person who approves decisions and outside actions.
- Confirm the local time zone and usual working days.
- List which files and connected tools Claude may read for routine work.
- Choose how long temporary exports in `inbox/` should be kept. Claude may flag old files but never deletes them.
- Name the accountant, lawyer, technician, or other qualified person who reviews work outside Claude's lane, when relevant.
- Choose one repeated job for the first Assisted routine. Record how it works today, its approved sources, a useful result, and a stop signal.
- Review saved evidence before advancing a routine. A stage change never authorizes sending, posting, paying, filing, signing, deciding, or deleting.
<!-- TUEL:CONTROL-CHECKLIST:END -->"""

SCHEDULE_PROMPT_PREAMBLE = """Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
"""


def targets() -> list[Path]:
    return [BLANK, *sorted(path for path in (ROOT / "blueprints").iterdir() if path.is_dir())]


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").rstrip() + "\n"


def marked_replace(text: str, canonical: str, start: str, end: str) -> str | None:
    if start not in text:
        return None
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    return pattern.sub(canonical.rstrip(), text, count=1)


def transform_claude(text: str, safety: str) -> str:
    text = re.sub(
        r"(?m)^- `business/` is the source of truth\..*$",
        "- `business/` is approved business truth. `operations/` holds current work, `inbox/` holds dated temporary input, and `assets/` holds stable reference files. Working evidence never becomes approved memory without owner review.",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^- Finished work goes to `reports/`\..*$",
        "- Finished drafts, checks, and receipts go to `reports/`. Never edit `assets/` or overwrite an owner file.",
        text,
        count=1,
    )
    replaced = marked_replace(
        text,
        safety,
        "<!-- TUEL:SAFETY-FLOOR:START -->",
        "<!-- TUEL:SAFETY-FLOOR:END -->",
    )
    if replaced is not None:
        text = replaced
    else:
        heading = re.search(r"(?mi)^## Hard rules\s*$", text)
        if not heading:
            raise ValueError("CLAUDE.md has no Hard rules heading")
        old_heading_end = heading.end()
        text = (
            text[: heading.start()]
            + safety.rstrip()
            + "\n\n## Business-specific rules"
            + text[old_heading_end:]
        )

    replaced = marked_replace(
        text,
        BUSINESS_OS_BLOCK,
        "<!-- TUEL:BUSINESS-OS:START -->",
        "<!-- TUEL:BUSINESS-OS:END -->",
    )
    if replaced is not None:
        text = replaced
    else:
        anchor = re.search(r"(?mi)^## Operating loop\s*$", text)
        if not anchor:
            raise ValueError("CLAUDE.md has no Operating loop heading")
        text = text[: anchor.start()] + BUSINESS_OS_BLOCK + "\n\n" + text[anchor.start() :]

    replaced = marked_replace(
        text,
        ADOPTION_BLOCK,
        "<!-- TUEL:ADOPTION:START -->",
        "<!-- TUEL:ADOPTION:END -->",
    )
    if replaced is not None:
        text = replaced
    else:
        business_os_end = "<!-- TUEL:BUSINESS-OS:END -->"
        anchor = text.find(business_os_end)
        if anchor < 0:
            raise ValueError("CLAUDE.md has no complete Business OS block")
        insert_at = anchor + len(business_os_end)
        text = text[:insert_at] + "\n\n" + ADOPTION_BLOCK + text[insert_at:]

    short_heading = re.search(r"(?mi)^## The short version\s*$", text)
    required = "Read the full CLAUDE.md before any work. If it is unavailable, stop and ask me."
    if short_heading:
        tail = text[short_heading.end() :]
        quote = re.search(r"(?m)^> (.+)$", tail)
        if quote and required not in quote.group(1):
            replacement = "> " + required + " " + quote.group(1)
            start = short_heading.end() + quote.start()
            end = short_heading.end() + quote.end()
            text = text[:start] + replacement + text[end:]
    else:
        text = text.rstrip() + (
            "\n\n## The short version\n\n"
            "Offer to save this only after showing the owner the exact text and receiving a fresh yes.\n\n"
            "> " + required
            + " Use business/ as approved truth, make drafts only, never guess or overwrite, and lead with what needs my decision.\n"
        )

    return normalize(text)


def insert_marked_section(text: str, block: str, start: str, end: str) -> str:
    replaced = marked_replace(text, block, start, end)
    if replaced is not None:
        return normalize(replaced)
    title = re.search(r"(?m)^# .+$", text)
    if not title:
        raise ValueError("Markdown file has no title")
    return normalize(text[: title.end()] + "\n\n" + block + text[title.end() :])


def transform_interview(text: str) -> str:
    text = insert_marked_section(
        text,
        INTERVIEW_CONTROL_BLOCK,
        "<!-- TUEL:SETUP-CONTROLS:START -->",
        "<!-- TUEL:SETUP-CONTROLS:END -->",
    )
    text = re.sub(
        r"(?m)^## Part 3[^\n]*$",
        "## Part 3: prove one routine before repeating it",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^Offer the two daily helpers one at a time, and wait for an answer between them\.$",
        "Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief\.md`\. Then:$",
        "If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:",
        text,
        count=1,
    )
    text = re.sub(
        r"(?m)^If yes, same walk-through with `schedules/end-of-day\.md`\. If either is a no, no pressure[^\n]*$",
        "If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.",
        text,
        count=1,
    )
    text = re.sub(
        r"(?ms)^## Set up the daily rhythm\n\nLast step: offer to help turn on two small routines.*?(?=\n## |\Z)",
        "## Prove one routine before repeating it\n\nAfter the first draft, create an adoption plan using `templates/ai-adoption-plan.md`. Run the chosen routine manually and review the evidence. Offer a repeating task only after reviewed runs meet the owner's success and stop signals and the owner chooses to advance that exact routine. A routine may stay Assisted for as long as the owner wants.\n",
        text,
        count=1,
    )
    return normalize(text)


def move_marked_section_to_end(text: str, block: str, start: str, end: str) -> str:
    pattern = re.compile(r"\n*" + re.escape(start) + r".*?" + re.escape(end) + r"\n*", re.DOTALL)
    text = pattern.sub("\n", text, count=1)
    return normalize(text.rstrip() + "\n\n" + block)


def transform_schedule(text: str, contract: str) -> str:
    replaced = marked_replace(
        text,
        contract,
        "<!-- TUEL:SCHEDULE-CONTRACT:START -->",
        "<!-- TUEL:SCHEDULE-CONTRACT:END -->",
    )
    if replaced is not None:
        text = replaced
    else:
        anchor = re.search(r"(?mi)^## How to turn it on\s*$", text)
        if not anchor:
            raise ValueError("schedule has no How to turn it on heading")
        text = text[: anchor.start()] + contract.rstrip() + "\n\n" + text[anchor.start() :]

    first_fence = re.search(r"(?m)^```(?:text)?\s*$", text)
    if not first_fence:
        raise ValueError("schedule has no fenced prompt")
    prompt_tail = text[first_fence.end() :]
    if "Read the full CLAUDE.md before doing anything." not in prompt_tail.split("```", 1)[0]:
        text = text[: first_fence.end()] + "\n" + SCHEDULE_PROMPT_PREAMBLE + text[first_fence.end() :].lstrip("\n")

    text = re.sub(
        r"\[(today|tomorrow)(?:'s)? date\]\.md",
        r"[\1's local date]-[local time or sequence].md",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\[date\]\.md", "[local date]-[local time or sequence].md", text)
    return normalize(text)


def ensure_list_values(text: str, key: str, additions: tuple[str, ...]) -> str:
    pattern = re.compile(rf"(?m)^{re.escape(key)}:\n((?:  - [^\n]+\n)*)")
    match = pattern.search(text)
    if not match:
        raise ValueError(f"manifest has no {key} list")
    existing = [line[4:] for line in match.group(1).splitlines() if line.startswith("  - ")]
    merged = [*existing, *(value for value in additions if value not in existing)]
    replacement = key + ":\n" + "".join(f"  - {value}\n" for value in merged)
    return text[: match.start()] + replacement + text[match.end() :]


def connector_block(name: str, block: str) -> str:
    facts = CONNECTOR_FACTS.get(name)
    if not facts:
        raise ValueError(f"no verified connector metadata for {name!r}")
    lines = block.rstrip().splitlines()
    lines = [
        line
        for line in lines
        if not re.match(r"^    (access|use_policy|official_url|fallback|verified_on):", line)
    ]
    fields = [
        f"    access: {facts['access']}",
        f"    use_policy: {facts['use_policy']}",
    ]
    if facts.get("official_url"):
        fields.append(f'    official_url: "{facts["official_url"]}"')
    fields.extend(
        (
            f'    fallback: "{facts["fallback"]}"',
            '    verified_on: "2026-07-17"',
        )
    )
    return "\n".join([*lines, *fields]) + "\n"


def transform_connectors(text: str) -> str:
    if re.search(r"(?m)^connectors:\s*\[\]\s*$", text):
        return text
    head = text.find("connectors:\n")
    if head < 0:
        return normalize(text.rstrip() + "\nconnectors: []\n")
    prefix = text[: head + len("connectors:\n")]
    body = text[head + len("connectors:\n") :]
    blocks = re.findall(r"(?ms)^  - name: (.+?)\n(.*?)(?=^  - name: |\Z)", body)
    if not blocks:
        return normalize(text)
    rendered = ""
    for name, rest in blocks:
        rendered += connector_block(name.strip(), f"  - name: {name}\n{rest}")
    return normalize(prefix + rendered)


def transform_manifest(text: str) -> str:
    def raise_blueprint_version(match: re.Match[str]) -> str:
        current = tuple(int(part) for part in match.group(1).split("."))
        minimum = tuple(int(part) for part in BLUEPRINT_VERSION.split("."))
        chosen = match.group(1) if current >= minimum else BLUEPRINT_VERSION
        return f'version: "{chosen}"'

    text = re.sub(
        r'(?m)^version:\s*["\']?([0-9]+\.[0-9]+\.[0-9]+)["\']?\s*$',
        raise_blueprint_version,
        text,
        count=1,
    )
    metadata_keys = (
        "standard_version",
        "policy_version",
        "data_layout_version",
        "operating_profile",
        "adoption_profile",
        "platform_claims_checked_on",
    )
    for key in metadata_keys:
        text = re.sub(rf"(?m)^{re.escape(key)}:.*\n?", "", text, count=1)
    metadata = (
        f'standard_version: "{STANDARD_VERSION}"\n'
        f'policy_version: "{POLICY_VERSION}"\n'
        f'data_layout_version: "{DATA_LAYOUT_VERSION}"\n'
        'operating_profile: draft-only-v1\n'
        f'adoption_profile: {ADOPTION_PROFILE}\n'
        'platform_claims_checked_on: "2026-07-17"\n'
    )
    version = re.search(r"(?m)^version:.*$", text)
    if not version:
        raise ValueError("manifest has no version")
    text = text[: version.end()] + "\n" + metadata.rstrip() + text[version.end() :]

    if not re.search(r"(?m)^roles:", text):
        anchor = re.search(r"(?m)^connectors:", text)
        insertion = (
            "roles:\n"
            "  - operator\n"
            "  - reality-checker\n"
            "  - adoption-guide\n"
            "protected_paths:\n"
            "  - business/\n"
            "  - assets/\n"
            "  - reports/\n"
            "  - operations/\n"
            "  - inbox/\n"
        )
        if anchor:
            text = text[: anchor.start()] + insertion + text[anchor.start() :]
        else:
            text = text.rstrip() + "\n" + insertion + "connectors: []\n"

    if not re.search(r"(?m)^adoption_guides:", text):
        anchor = re.search(r"(?m)^connectors:", text)
        insertion = "adoption_guides:\n  - use-case-map\n"
        if anchor:
            text = text[: anchor.start()] + insertion + text[anchor.start() :]
        else:
            text = text.rstrip() + "\n" + insertion + "connectors: []\n"

    for key, additions in LIST_ADDITIONS.items():
        text = ensure_list_values(text, key, additions)

    return transform_connectors(normalize(text))


def desired_files(target: Path, safety: str, contract: str) -> dict[Path, str]:
    desired: dict[Path, str] = {}
    for relative in CORE_FILES:
        desired[target / relative] = normalize((CORE / relative).read_text(encoding="utf-8"))

    desired[target / "CLAUDE.md"] = transform_claude(
        (target / "CLAUDE.md").read_text(encoding="utf-8"), safety
    )
    desired[target / "blueprint.yaml"] = transform_manifest(
        (target / "blueprint.yaml").read_text(encoding="utf-8")
    )
    desired[target / "START-HERE.md"] = move_marked_section_to_end(
        (target / "START-HERE.md").read_text(encoding="utf-8"),
        OWNER_SETUP_BLOCK,
        "<!-- TUEL:OWNER-SETUP:START -->",
        "<!-- TUEL:OWNER-SETUP:END -->",
    )
    desired[target / "onboarding" / "interview.md"] = transform_interview(
        (target / "onboarding" / "interview.md").read_text(encoding="utf-8")
    )
    desired[target / "onboarding" / "checklist.md"] = insert_marked_section(
        (target / "onboarding" / "checklist.md").read_text(encoding="utf-8"),
        CHECKLIST_CONTROL_BLOCK,
        "<!-- TUEL:CONTROL-CHECKLIST:START -->",
        "<!-- TUEL:CONTROL-CHECKLIST:END -->",
    )

    core_schedules = {
        target / relative
        for relative in CORE_FILES
        if relative.startswith("schedules/")
    }
    for schedule in sorted((target / "schedules").glob("*.md")):
        if schedule in core_schedules:
            continue
        desired[schedule] = transform_schedule(schedule.read_text(encoding="utf-8"), contract)
    return desired


def run(write: bool) -> int:
    safety = normalize(SAFETY.read_text(encoding="utf-8"))
    contract = normalize(SCHEDULE_CONTRACT.read_text(encoding="utf-8"))
    drift: list[str] = []

    for target in targets():
        try:
            desired = desired_files(target, safety, contract)
        except (OSError, ValueError) as exc:
            print(f"{target.relative_to(ROOT)}: {exc}", file=sys.stderr)
            return 2

        for path, content in desired.items():
            current = normalize(path.read_text(encoding="utf-8")) if path.exists() else None
            if current == content:
                continue
            relative = path.relative_to(ROOT)
            if not write:
                drift.append(str(relative))
                continue
            target_relative = str(path.relative_to(target))
            if target_relative in PROTECTED_SEEDS and path.exists():
                print(f"refusing to overwrite protected seed {relative}", file=sys.stderr)
                return 2
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"updated {relative}")

    if drift:
        print("Business OS drift found:")
        for item in drift:
            print(f"  {item}")
        print("Run: python3 tools/sync_business_os.py --write")
        return 1
    if not write:
        print(f"Business OS core is synchronized across {len(targets())} targets.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="apply repository-owned Business OS files")
    mode.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    return run(write=args.write)


if __name__ == "__main__":
    sys.exit(main())
