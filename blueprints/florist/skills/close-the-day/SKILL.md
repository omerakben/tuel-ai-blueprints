# Close the day

A calm end-of-day check: Claude tallies what today brought in and what sold out, then writes it down so tomorrow starts clean.

## When to run this

- At closing time, after the last customer has paid and the drawer is counted.
- Any evening the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your offer list, to make sense of what was rung up.
- business/policies.md — your rules on deposits and what the drawer starts with, if you've written them down.
- templates/daily-close.md — the fill-in shape every close follows.

You paste or say: today's sales export from your till or card reader, and the cash count from the drawer. Mention what sold out or ran low — that's tomorrow's buying list talking. If today's order list helps explain the numbers, paste that too.

## Steps

1. Claude asks for anything still missing, like the export or the drawer count, and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the day using templates/daily-close.md: orders filled on one side — walk-ins, pickups, deliveries — and on the other side the money itself: card takings, cash in the drawer, and anything else like deposits taken for events.
3. You tell Claude what sold out or ran low, and anything headed past its best. It goes in the close exactly as you said it, so the next stem order starts from real information.
4. Anything that does not line up becomes a plain question, for example: "the drawer shows [amount] less than the till expects — was there a cash payout today, maybe at the market?" Never a conclusion, and never a name attached as a cause.
5. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
6. Anything that smells like bookkeeping or tax — a fee that looks wrong, an event deposit you're not sure how to record — goes on the "for the bookkeeper" list at the bottom. Claude does not answer those on the spot.
7. If you want to email the bookkeeper about an item on that list, Claude writes the note as a draft and waits for you to read it and say send. Same for any message to a helper or your card company: draft first, and it goes nowhere until you say so.
8. Claude shows you the finished report as a draft. You read it and correct anything, then give the go-ahead. Then it is saved to reports/.

## What you get

One tidy page saved as reports/daily-close-YYYY-MM-DD.md:

- The day at a glance: orders filled, card total, cash total, deposits if any.
- What sold out or ran low, in your words — ready to feed the next stem order.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a day-by-day record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never give bookkeeping or tax advice; those questions go on the bookkeeper list and stay there.
- Never invent or round a figure that did not come from your export, your drawer count, or your own words.
- Never alter a number after it's saved, and never present a close as checked by an accountant — it's your tally, tidied.
- Never record a payment or issue a refund anywhere — this playbook only writes the report.
- Never add a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
