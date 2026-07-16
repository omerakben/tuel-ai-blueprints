# Daily close

A calm end-of-day money check: Claude compares what today should have brought in with what is actually there, then writes it down so tomorrow starts clean.

## When to run this

- At closing time, after the last client has paid and the drawer is counted.
- Any evening the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your service list and prices, to check what each service should have rung up.
- business/staff.md — who worked today, so the tally can be split by chair if you want that.
- business/policies.md — your rules on deposits, discounts, and what the drawer starts with.
- templates/daily-close.md — the fill-in shape every close follows.

You paste or say: today's sales export from your card reader or till, and the cash count from the drawer. Mention tips if they are kept aside. If today's appointment book helps explain the numbers, paste that too.

## Steps

1. Claude asks for anything still missing, like the export or the drawer count, and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the day using templates/daily-close.md: services rung on one side, and on the other side the money itself — card takings, cash in the drawer, tips kept aside, and anything else like vouchers or deposits.
3. Anything that does not line up becomes a plain question, for example: "the drawer shows [amount] less than the till expects — was there a cash payout today, maybe for supplies?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. Anything that smells like bookkeeping or tax — a fee that looks wrong, a refund you are not sure how to record — goes on the "for the bookkeeper" list at the bottom of the report. Claude does not answer those on the spot.
6. If you want to email the bookkeeper about an item on that list, Claude writes the note as a draft and waits for you to read it and say send. Same for any message to staff or your card company: draft first, and it goes nowhere until you say so.
7. Claude shows you the finished report as a draft. You read it and correct anything, then give the go-ahead. Then it is saved as reports/daily-close-[date].md.
8. If today surfaced a fact worth keeping (say the drawer always starts with [float amount]), Claude shows you the exact line it would add to business/policies.md and waits for your yes before writing it.

## What you get

One tidy page saved as reports/daily-close-[date].md:

- The day at a glance: services rung, card total, cash total, tips.
- Expected next to actual, with any difference shown plainly.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a day-by-day record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never give bookkeeping or tax advice; those questions go on the bookkeeper list and stay there.
- Never invent or round a figure that did not come from your export or drawer count, or from your own words.
- Never record a payment or issue a refund anywhere — this playbook only writes the report.
- Never add a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
