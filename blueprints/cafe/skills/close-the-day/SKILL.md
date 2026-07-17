# Close the day

A calm end-of-day money check: Claude tallies the till, card, and tips from what you paste or read out, asks about anything that doesn't line up, and writes it down so tomorrow starts clean.

## When to run this

- At closing time, after the last customer and the drawer count.
- Any evening the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your menu and prices, for sense-checking what the day rang up.
- business/policies.md — your rules on refunds, remakes, and what the drawer starts with.
- templates/daily-close.md — the fill-in shape every close follows.

You paste or say: today's sales summary from your till or card reader, the cash count from the drawer, and tips if they're kept aside.

## Steps

1. Claude asks for anything still missing — the summary, the drawer count — and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the day using templates/daily-close.md: card takings, cash in the drawer, and tips, each written exactly as you gave it.
3. Anything that doesn't line up becomes a plain question, for example: "the drawer shows [amount] less than the till expects — was there a cash payout today, maybe for a delivery?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. Anything that smells like bookkeeping or tax — a fee that looks wrong, a refund you're not sure how to record — goes on the "for the bookkeeper" list at the bottom. Claude doesn't answer those on the spot.
6. Claude shows you the finished report as a draft. You correct anything, then give the go-ahead, and it's saved as reports/day-close-YYYY-MM-DD.md.
7. If today surfaced a fact worth keeping — say, what the drawer always starts with — Claude shows you the exact line it would add to business/policies.md and waits for your yes.

## What you get

One tidy page saved as reports/day-close-YYYY-MM-DD.md:

- The day at a glance: card total, cash total, tips.
- Expected next to actual, with any difference shown plainly.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a day-by-day record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never give bookkeeping or tax advice; those questions go on the bookkeeper list and stay there.
- Never invent or round a figure that didn't come from your till, your drawer count, or your own words.
- Never change a number once you've confirmed it — a correction gets its own note, never a quiet rewrite.
- Never present the report as checked by an accountant. It's a tidy record of your own numbers, nothing more.
- Never record a payment or issue a refund anywhere. This playbook only writes the report.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
