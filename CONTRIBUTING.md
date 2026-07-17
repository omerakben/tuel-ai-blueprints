# Contributing

Thanks for helping more owners get their evenings back. Here is how a new blueprint happens.

## Build a vertical

1. Scaffold: `python tools/create_blueprint.py <slug> --name "Cafe" --business-type "neighborhood cafe"`
2. Fill in every TODO marker. Write to one owner, in their words. `docs/brand.md` is the voice bar.
3. Do not edit copied Business OS files inside one blueprint. Change `standard/core/`, then run `python3 tools/sync_business_os.py --write` so every target receives the same reviewed version.
4. Check `python3 tools/sync_business_os.py --check`, `python3 tools/lint.py --strict`, and `python3 tools/lint.py --self-test` until all three pass.
5. Dry-run the interview, readiness gate, Assisted pilot, isolated Repeatable work packet, one daily schedule, routine advancement and pause decision, monthly adoption review, weekly review, a duplicate run, a stale source, and an untrusted instruction against a real owner of that business type or the most honest stand-in you can find. Record only the checks that actually happened.
6. Open a pull request. CI verifies the shared core, strict lint rules, self-tests, and the packaged site.

## The bar every blueprint clears

- **Draft-first is absolute.** No file may let Claude send, post, pay, file, sign, delete, or decide without the owner's fresh approval of that exact item.
- **No invented data.** Business-memory files ship as empty, friendly stubs. No sample prices, phone numbers, or names of real people.
- **No jargon where owners read.** The linter rejects the obvious words; the real test is whether the owner would squint.
- **Shared control layer.** Keep the standard safety block, three role guides, review and next-use-case playbooks, four control workflows, weekly operations and monthly adoption reviews, record templates, adoption guide, and upgrade guide byte-for-byte aligned with `standard/`.
- **Routine-level adoption.** Every vertical has a business-specific `adoption/use-case-map.md`. A new or changed routine starts Assisted in Manual mode. Only the owner advances, pauses, moves back, or retires it, and no stage expands action authority.
- **Minimums:** 5 playbooks in `skills/`, 4 schedules, 4 workflows, 10 templates, 3 roles, one adoption map, and a first win that needs nothing connected.
- **Domain honesty.** If the vertical brushes against health, legal, or licensed work, the blueprint stays on the admin side and says so plainly.
- **Platform honesty.** Recheck `docs/platform-capabilities.md` before changing claims about accounts, data processing, permissions, scheduled work, or connected tools.
- **Owner data stays protected.** Repository updates never overwrite `business/`, `assets/`, `reports/`, `operations/`, or `inbox/` in an installed folder.

## What gets declined

Blueprints that fabricate example data, promise unattended outside action, require a connected tool for the first win, weaken the safety floor, claim unverified data residency or permissions, or blur the folder with plugin or Skill packaging.
