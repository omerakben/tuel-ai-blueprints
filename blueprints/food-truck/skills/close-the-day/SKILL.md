# Close the day

A calm end-of-day money check: Claude tallies the day from your card reader numbers and your cash count, asks about anything that doesn't line up, and writes it down so tomorrow starts clean.

## When to run this

- At the end of service, once the window is shut and the cash box is counted.
- Any evening the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — the menu and prices, to make sense of what sold.
- business/staff.md — who worked today, if you want the day noted that way.
- business/policies.md — your rules on the cash box float and refunds at the window.
- templates/daily-close.md — the fill-in shape every close follows.

From you: today's totals from your card reader, the cash count from the box, and tips if they're kept aside. What sold out and what came home helps too — it feeds tomorrow's prep list.

## Steps

1. Claude asks for anything still missing, like the reader total or the cash count, and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the day using templates/daily-close.md: card takings, cash in the box, tips kept aside, and anything else like an event deposit you were handed.
3. Anything that does not line up becomes a plain question, for example: "the box shows [amount] less than the float plus cash sales — did you pay for anything out of the box today, maybe ice or a parking fee?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. Anything that smells like bookkeeping or tax — a reader fee that looks wrong, an event deposit you're not sure how to record — goes on the "for the bookkeeper" list at the bottom of the report. Claude does not answer those on the spot.
6. If you want to message the bookkeeper about an item on that list, Claude writes it as a draft and waits for you to read it and say send. Same for any message to the crew or your card company: draft first, and it goes nowhere until you say so.
7. Claude shows you the finished report as a draft. You read it and correct anything, then give the go-ahead. Then it is saved to reports/.
8. If today surfaced a fact worth keeping (say the box always starts with [float amount]), Claude shows you the exact line it would add to business/policies.md and waits for your yes before writing it.

## What you get

One tidy page saved as reports/daily-close-YYYY-MM-DD.md:

- The day at a glance: where you set up, card total, cash total, tips.
- Expected next to actual, with any difference shown plainly.
- What sold out and what came home, ready to feed tomorrow's prep list.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a day-by-day record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never give bookkeeping or tax advice, and never present a tally as checked by an accountant; those questions go on the bookkeeper list and stay there.
- Never alter a figure, and never invent or round one that did not come from your reader, your count, or your own words.
- Never record a payment or issue a refund anywhere — this playbook only writes the report.
- Never add a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
