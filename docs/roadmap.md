# Roadmap

`salon` shipped first and set the bar; the first wave of 18 more main-street verticals followed (cafe, bakery, restaurant, bar, food-truck, boutique, florist, gym, pet-groomer, tattoo-studio, photographer, event-planner, tutoring-studio, cleaning-service, lawn-care, plumber, handyman, auto-repair) — every one lint-clean against the standard and carrying its own "know your lane" boundary pack. Verticals are added as a copy-fill-lint loop on top of `templates/_blank/`.

## Selection criteria for the next vertical

1. Appointment- or order-driven local business (booking, rebooking, and no-shows are the money problems).
2. Thin software stack — the owner runs on a till, a phone, and maybe one booking tool, so a folder plus exports beats another subscription.
3. A first win Claude can deliver from conversation alone, with nothing connected.
4. No regulated-data core: nothing that needs health records, legal privilege, or licensed judgment to be useful.

## Planned

| Order | Blueprint | Notes |
|---|---|---|
| 1 | `dental-front-desk` | Admin only — recall lists and supply orders without patient health records |
| 2 | `nail-studio` | Close cousin of salon; rebooking and fill-the-chair rhythms |
| 3 | `auto-detailing` | Estimates, before/after posts, route days |
| 4 | `barbershop-single-chair` | Solo-chair variant of salon with a lighter interview |

Further candidates are picked by the selection criteria above, not by list order.

## Later, separately

- Multi-folder packs sharing one set of business files (`bundles/`).
- Packaged Skills and plugins graduated from proven playbooks — each a separate product with its own security and distribution review, never a silent upgrade of a folder.
