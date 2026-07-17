# Close the day

A calm end-of-night money check: Claude tallies your numbers — till, card, tips — against what the night should have brought in, then writes it down so tomorrow starts clean.

## When to run this

- After last call, once the drawer is counted and the door is locked.
- Any night the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your menu and prices, to check what the night should have rung up.
- business/staff.md — who worked tonight, if you want the tally noted by shift.
- business/policies.md — your rules on tabs, comps, and what the drawer starts with.
- templates/daily-close.md — the fill-in shape every close follows.

You paste or say: tonight's sales export from your card reader or till, and the cash count from the drawer. Mention tips if they're kept aside, and any tabs still open. Claude works only from your numbers — it never pulls figures out of the air.

## Steps

1. Claude asks for anything still missing, like the export or the drawer count, and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the night using templates/daily-close.md: what rang on one side, and on the other the money itself — card takings, cash in the drawer, tips kept aside, and anything open like tabs or deposits.
3. Anything that does not line up becomes a plain question, for example: "the drawer shows [amount] less than the till expects — was there a cash payout tonight, maybe for ice or a delivery?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. Anything that smells like bookkeeping or tax — a fee that looks wrong, a comp you're not sure how to record — goes on the "for the bookkeeper" list at the bottom of the report. Claude does not answer those on the spot.
6. If you want to message the bookkeeper about an item on that list, Claude writes the note as a draft and waits for you to read it and say send. Same for any message to the crew or your card company: draft first, and it goes nowhere until you say so.
7. Claude shows you the finished report as a draft. You read it and correct anything, then give the go-ahead. Then it is saved to reports/.
8. If tonight surfaced a fact worth keeping (say the drawer always starts with [float amount]), Claude shows you the exact line it would add to business/policies.md and waits for your yes before writing it.

## What you get

One tidy page saved as reports/daily-close-YYYY-MM-DD.md:

- The night at a glance: card total, cash total, tips, tabs still open.
- Expected next to actual, with any difference shown plainly.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a night-by-night record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never give bookkeeping or tax advice, and never present a close as accountant-checked; those questions go on the bookkeeper list and stay there.
- Never invent or round a figure that did not come from your export, your drawer count, or your own words.
- Never alter a record, record a payment, or issue a refund anywhere — this playbook only writes the report.
- Never note who was drinking or how much in a close report. The numbers are about the till, not the room.
- Never add a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
