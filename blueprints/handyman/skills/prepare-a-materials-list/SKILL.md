# Prepare a materials list

Turn the week's jobs into one shopping list, sorted by store — so you make one run, not four.

## When to run this

- Right after the week plan is set, while the jobs are fresh.
- The night before a supply run.
- A big job just landed and you want its list kept separate from the weekly one.

## What Claude reads first

- The newest week plan in reports/, or the job list you paste in.
- business/suppliers.md — which store you use for what, so the list sorts itself the way you shop.
- assets/ — photos or notes you've dropped in that show what a job needs.

## Steps

1. Walk the jobs one at a time. For each, Claude lists the materials from what you describe — it prompts with plain questions ("paint and patch, or just patch?") but the list is built from your answers, not its assumptions.
2. Mark the safety-critical picks as yours. Where the wrong product is a safety matter — anything for electrical, gas, or structural work, fasteners that hold weight, ladders and fall gear — the line names the need ("the right anchors for a wall-hung cabinet") and leaves the pick to you and the counter pro. Claude never chooses those products.
3. Sort by store using suppliers.md. Anything without a home goes under "you pick the store".
4. Add quantities only where you gave them. A blank beats a guess — [how many?] is an honest line on a shopping list.
5. Show you the list and adjust until it matches how you actually shop.
6. Save it to reports/ — print it, or read it off your phone in the aisle.

## What you get

One page in reports/, a fresh one each run, named like reports/materials-list-YYYY-MM-DD.md. Inside:

- The list, sorted by store, each line tied to the job it's for.
- The "your pick" lines — safety-critical items named but never chosen.
- Open questions — quantities and choices still waiting on you.

## Never

- Never pick a safety-critical product — nothing for electrical, gas, or structural work, no load-bearing fasteners, no ladders or fall gear. Claude names the need; you or the counter pro choose the item.
- Never order, reserve, or buy anything, anywhere. The list is paper; the shopping is yours.
- Never invent a price, a stock level, or a store hour. If you want prices on the list, you supply them.
- Never turn a see-it-first job (electrical, gas, structural, roofing, asbestos, lead, mold) into a materials list — that job gets a look in person before it gets a list.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
