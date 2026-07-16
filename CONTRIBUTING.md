# Contributing

Thanks for helping more owners get their evenings back. Here is how a new blueprint happens.

## Build a vertical

1. Scaffold: `python tools/create_blueprint.py <slug> --name "Cafe" --business-type "neighborhood cafe"`
2. Fill in every TODO marker. Write to one owner, in their words — `docs/brand.md` is the voice bar.
3. Check: `python tools/lint.py blueprints/<slug>` until green, warnings included.
4. Dry-run the interview in `onboarding/interview.md` against a real owner of that business type (or the most honest stand-in you can find). Fix what confused them.
5. Open a pull request. CI runs the linter on every PR.

## The bar every blueprint clears

- **Draft-first is absolute.** No file may let Claude send, post, pay, file, sign, delete, or decide without the owner's fresh approval of that exact item.
- **No invented data.** Business-memory files ship as empty, friendly stubs. No sample prices, phone numbers, or names of real people.
- **No jargon where owners read.** The linter warns on the obvious words; the real test is whether the owner would squint.
- **Minimums:** 3 real playbooks in `skills/`, 2 schedules (morning brief and end-of-day close), a first win that needs nothing connected.
- **Domain honesty.** If the vertical brushes against health, legal, or licensed work, the blueprint stays on the admin side and says so plainly.

## What gets declined

Blueprints that fabricate example data, promise autonomy ("it posts for you while you sleep"), require a connected tool for the first win, or blur the folder with plugin or Skill packaging.
