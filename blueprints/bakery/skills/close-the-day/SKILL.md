# Close the day

A calm end-of-day check: Claude tallies the till, the card reader, and what sold out — all from your numbers — then writes it down so tomorrow starts clean.

## When to run this

- At closing time, once the case is cleared and the drawer is counted.
- Any evening the numbers feel off and you want a second pair of eyes.
- Before a day off, so nothing sits unchecked over the break.

## What Claude reads first

- business/services.md — your lineup and prices, to make sense of what sold.
- business/policies.md — your rules on deposits and discounts, and what the drawer starts with.
- templates/daily-close.md — the fill-in shape every close follows.
- reports/ — today's bake list, if there is one, so sold-out notes line up with what was baked.

You paste or say: today's sales from your card reader or till, the cash count from the drawer, and what sold out or came home. Mention any custom order deposits taken today so they're noted on the right day.

## Steps

1. Claude asks for anything still missing — the card total, the drawer count — and works only from what you give it. No guessing, no filling gaps.
2. Claude tallies the day using templates/daily-close.md: what sold and what sold out on one side, and on the other the money itself — card takings, cash in the drawer, and anything else like deposits or vouchers.
3. Anything that does not line up becomes a plain question, for example: "the drawer shows [amount] less than the till expects — was there a cash payout today, maybe for a supply run?" Never a conclusion, and never a name attached as a cause.
4. You answer what you can. Claude writes each answer next to its question. Whatever stays open is marked "to check tomorrow", not resolved by guesswork.
5. What sold out and what came home gets written down plainly — it feeds tomorrow's bake list, so honest beats tidy.
6. Anything that smells like bookkeeping or tax — a fee that looks wrong, a deposit you're not sure how to record — goes on the "for the bookkeeper" list at the bottom of the report. Claude does not answer those on the spot.
7. If you want to message the bookkeeper about an item on that list, Claude writes the note as a draft and waits for you to read it and say send.
8. Claude shows you the finished report as a draft. You read it and correct anything, then give the go-ahead. Then it is saved as reports/daily-close-YYYY-MM-DD.md.
9. If today surfaced a fact worth keeping (say the drawer always starts with [float amount]), Claude shows you the exact line it would add to business/policies.md and waits for your yes before writing it.

## What you get

One tidy page saved as reports/daily-close-YYYY-MM-DD.md:

- The day at a glance: what sold, card total, cash total, deposits taken.
- What sold out (and roughly when) and what came home — tomorrow's bake list will use both.
- Expected next to actual, with any difference shown plainly.
- Open questions with your answers, and whatever is left to check tomorrow.
- A short "for the bookkeeper" list of month-end items.

Over time these pages become a day-by-day record your bookkeeper will thank you for.

## Never

- Never state or imply that anyone took money or made a mistake — a mismatch is a question to ask, not a finding to announce.
- Never change a figure you gave, and never smooth one over to make the page balance. Your numbers go in as you said them; anything odd becomes a question.
- Never give bookkeeping or tax advice, and never present this report as checked by an accountant. It organizes your numbers; the bookkeeper list carries the real questions.
- Never record a payment, move money, or issue a refund anywhere — this playbook only writes the report.
- Never add a fact to business/ without showing you the exact line and getting your yes first.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
