# TUEL AI blueprints

**Download your business. Open it. Let Claude run it.**

**→ Find your business at [omerakben.github.io/tuel-ai-blueprints](https://omerakben.github.io/tuel-ai-blueprints/).** Every folder has a download button and a ready-to-paste hello prompt.

A blueprint is a ready-to-operate folder for one kind of small business. Open it in Claude Desktop and Claude becomes a capable operator for that business: drafting the marketing, closing out the day, reminding clients to rebook, watching the stock, and checking with you before anything real happens.

## How it works

1. **Download** the folder for your kind of business from the catalog below.
2. **Open it** in Claude Desktop and say hello. Claude asks a few plain questions, one at a time, and aims to end the first session with a useful business profile and a ready-to-review draft.
3. **Let it run.** Turn on the morning brief and the end-of-day close. From then on Claude drafts, tallies, reminds, and watches the stock. You decide.

Everything is draft-first: nothing is sent, posted, paid, or promised without your fresh okay on that exact item.

## What every folder can do

TUEL Business OS v1 gives every business the same dependable control layer:

- an operator guide that turns approved facts and current input into useful local drafts
- a separate reality-check guide that reopens sources, recomputes important numbers, and returns ready, revise, or blocked; it is a consistency check, not an independent audit
- an operations board for open work and an inbox for dated temporary exports
- work receipts that show what was read, produced, left uncertain, and sent to the owner for a decision
- decision, incident, weekly review, and business-memory proposal templates
- morning, end-of-day, and weekly schedule recipes that stop at observing or drafting

These are ordinary files Claude reads. They do not install agents, turn on schedules, or grant access. Claude can handle reviewed reading, organizing, calculation, reconciliation, drafting, and local reporting. The owner still performs every send, post, payment, filing, commitment, access change, and deletion.

## Catalog

| Blueprint | For | Status |
|---|---|---|
| [`salon`](blueprints/salon/) | Barber and beauty salons | ✅ available |
| [`cafe`](blueprints/cafe/) | Neighborhood cafés | ✅ available |
| [`bakery`](blueprints/bakery/) | Bakeries and pastry shops | ✅ available |
| [`restaurant`](blueprints/restaurant/) | Small family restaurants | ✅ available |
| [`bar`](blueprints/bar/) | Neighborhood bars | ✅ available |
| [`food-truck`](blueprints/food-truck/) | Food trucks and market stalls | ✅ available |
| [`boutique`](blueprints/boutique/) | Independent retail shops | ✅ available |
| [`florist`](blueprints/florist/) | Flower shops | ✅ available |
| [`gym`](blueprints/gym/) | Small gyms and fitness studios | ✅ available |
| [`pet-groomer`](blueprints/pet-groomer/) | Pet grooming businesses | ✅ available |
| [`tattoo-studio`](blueprints/tattoo-studio/) | Tattoo studios | ✅ available |
| [`photographer`](blueprints/photographer/) | Photographers and solo creatives | ✅ available |
| [`event-planner`](blueprints/event-planner/) | Event planners | ✅ available |
| [`tutoring-studio`](blueprints/tutoring-studio/) | Tutoring studios | ✅ available |
| [`cleaning-service`](blueprints/cleaning-service/) | Home and office cleaning crews | ✅ available |
| [`lawn-care`](blueprints/lawn-care/) | Lawn care and landscaping crews | ✅ available |
| [`plumber`](blueprints/plumber/) | Plumbing businesses | ✅ available |
| [`handyman`](blueprints/handyman/) | Handyman businesses | ✅ available |
| [`auto-repair`](blueprints/auto-repair/) | Independent auto repair shops | ✅ available |
| `dental-front-desk` | Dental practice front desks (admin only, no patient health records) | 🛠️ planned |

## Get one folder

The easy way: the [catalog site](https://omerakben.github.io/tuel-ai-blueprints/) has a download button per business. You get just your folder as a ZIP, nothing else.

Builders can grab a single folder from the command line:

```bash
npx degit omerakben/tuel-ai-blueprints/blueprints/salon salon
```

## What a blueprint is (and is not)

A blueprint is an ordinary working folder: instructions, playbooks, templates, and empty business-memory files that Claude reads as context. It is not a Claude plugin and not a packaged Skill; nothing inside auto-installs or registers anything. File names like `START-HERE.md` and `blueprint.yaml` are this project's conventions, not Anthropic-defined behavior.

The original folder stays under your control. When you use Claude Cowork, Claude processes the files and instructions you choose to share, and Cowork sessions and files are saved to your Claude account under your plan and settings. Keep credentials, payment-card details, government IDs, health records, and other restricted material out of the folder. See [current platform capabilities](docs/platform-capabilities.md) for the dated source record.

A blueprint is operational help, not professional advice. Month-end summaries go to your bookkeeper; contracts go to your lawyer; nothing here processes health records.

## For builders

- `standard/SPEC.md` is the blueprint standard; `standard/blueprint.schema.json` is the manifest contract.
- `templates/_blank/` is the scaffold. Start a new vertical with `python tools/create_blueprint.py <slug> --name "..." --business-type "..."`.
- `python tools/lint.py --strict` checks every blueprint; CI runs it on each pull request.
- `docs/` contains the vision, brand voice, platform fact record, and upgrade guide. `CONTRIBUTING.md` explains how to add a vertical.
