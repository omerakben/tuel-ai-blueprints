# TUEL AI blueprints

**Download your business. Open it. Let Claude run it.**

A blueprint is a ready-to-operate folder for one kind of small business. Open it in Claude Desktop and Claude becomes a capable operator for that business — drafting the marketing, closing out the day, reminding clients to rebook, watching the stock — and checking with you before anything real happens.

## How it works

1. **Download** the folder for your kind of business from the catalog below.
2. **Open it** in Claude Desktop and say hello. Claude asks a few plain questions — one at a time, about twenty minutes — and ends with your first win: your business profile saved and a ready-to-post promo.
3. **Let it run.** Turn on the morning brief and the end-of-day close. From then on Claude drafts, tallies, reminds, and watches the stock. You decide.

Everything is draft-first: nothing is sent, posted, paid, or promised without your fresh okay on that exact item.

## Catalog

| Blueprint | For | Status |
|---|---|---|
| [`salon`](blueprints/salon/) | Barber and beauty salons | ✅ available |
| `cafe` | Cafés and coffee shops | 🛠️ planned |
| `food-truck` | Food trucks and market stalls | 🛠️ planned |
| `boutique` | Independent retail shops | 🛠️ planned |
| `gym` | Gyms and fitness studios | 🛠️ planned |
| `cleaning-service` | Home and office cleaning crews | 🛠️ planned |
| `plumber` | Plumbing and skilled trades | 🛠️ planned |
| `photographer` | Photographers and solo creatives | 🛠️ planned |
| `dental-front-desk` | Dental practice front desks (admin only, no patient health records) | 🛠️ planned |

## Get one folder

You only need your business, not this whole repository. Download the repository ZIP, keep just the folder for your business, and open that folder in Claude Desktop — that's the whole install.

Builders can grab a single folder from the command line once this repository is published on GitHub:

```bash
npx degit omerakben/tuel-ai-blueprints/blueprints/salon salon
```

## What a blueprint is (and is not)

A blueprint is an ordinary working folder: instructions, playbooks, templates, and empty business-memory files that Claude reads as context. It is not a Claude plugin and not a packaged Skill; nothing inside auto-installs or registers anything. File names like `START-HERE.md` and `blueprint.yaml` are this project's conventions, not Anthropic-defined behavior. Your business files stay on your computer, belong to you, and are never shipped back to anyone.

A blueprint is operational help, not professional advice. Month-end summaries go to your bookkeeper; contracts go to your lawyer; nothing here processes health records.

## For builders

- `standard/SPEC.md` — the blueprint standard; `standard/blueprint.schema.json` — the manifest contract.
- `templates/_blank/` — the scaffold; start a new vertical with `python tools/create_blueprint.py <slug> --name "..." --business-type "..."`.
- `python tools/lint.py` — checks every blueprint; CI runs it on each pull request.
- `docs/` — vision, brand voice, roadmap. `CONTRIBUTING.md` — how to add a vertical.
