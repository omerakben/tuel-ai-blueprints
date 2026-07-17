# Close the day

A calm end-of-night money check: Claude tallies covers, till, card, and tips from your numbers, turns anything that doesn't line up into a question, and writes it down so tomorrow starts clean.

## When to run this

- At closing, after the last table has paid and the till is counted.
- Any night the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your menu and prices, to sense-check what the night should have rung up.
- business/staff.md — who worked tonight, if you want the tally split by shift.
- business/policies.md — your rules on comps, discounts, and what the till starts with.
- templates/daily-close.md — the fill-in shape every close follows.

You paste or say: tonight's sales export from your card reader or till, the cash count, the cover count, and tips if they're kept aside. If tonight's book helps explain the numbers, paste that too.

## Steps

1. Claude asks for anything still missing, like the export or the till count, and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the night using templates/daily-close.md: covers served on one side, and on the other side the money itself — card takings, cash in the till, tips kept aside, and anything else like gift cards or deposits.
3. Anything that does not line up becomes a plain question, for example: "the till shows [amount] less than the card reader expects — was there a cash payout tonight, maybe for a delivery?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. Anything that smells like bookkeeping or tax — a fee that looks wrong, a refund you're not sure how to record — goes on the "for the bookkeeper" list at the bottom of the report. Claude does not answer those on the spot.
6. If you want to message the bookkeeper about an item on that list, Claude writes the note as a draft and waits for you to read it and say send. Same for any note to the crew or your card company: draft first, and it goes nowhere until you say so.
7. Claude shows you the finished report as a draft. You read it, correct anything, and give the go-ahead. Then it is saved as reports/daily-close-YYYY-MM-DD.md.
8. If tonight surfaced a fact worth keeping (say the till always starts with [float amount]), Claude shows you the exact line it would add to business/policies.md and waits for your yes before writing it.

## What you get

One tidy page saved as reports/daily-close-YYYY-MM-DD.md:

- The night at a glance: covers served, card total, cash total, tips.
- Expected next to actual, with any difference shown plainly.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a night-by-night record your bookkeeper will thank you for.

## Never

- Never states or implies that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never gives bookkeeping or tax advice, and never presents a tally as accountant-checked. It is your numbers, organized; the judgment calls go on the bookkeeper list.
- Never invents or rounds a figure that did not come from your export, your till count, or your own words.
- Never records a payment or issues a refund anywhere — this playbook only writes the report.
- Never adds a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
