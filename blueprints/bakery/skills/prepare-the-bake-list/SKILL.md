# Prepare the bake list

Builds tomorrow's bake list from the orders that are due and your usual counter lineup — proposed to you, adjusted by you, and only final when you say so.

## When to run this

At the end of the day, once tomorrow's orders are known — many bakers run it right after the daily close. It also pairs with the end-of-day schedule: the proposed list is waiting before you flour the bench in the morning.

## What Claude reads first

- business/services.md — your usual counter lineup and how many of each you tend to bake.
- reports/ — today's close, if there is one: what sold out and what came home.
- business/clients.md — standing orders from regulars, if you've saved any.
- From you or assets/: tomorrow's orders — preorders, custom bakes due, anything promised. Paste them, read them out, or drop the list in assets/. If Claude can't find tomorrow's orders, it asks; it never assumes there are none.

## Steps

1. Claude gathers tomorrow's commitments: custom orders due, preorders, and standing orders. Each one is listed with the name and what was agreed, exactly as written or said — nothing added.
2. Claude starts the counter list from the usual lineup in services.md.
3. If today's close says something sold out early or came home unsold, Claude suggests a change — "the rye sold out by noon; bake a few more?" — always as a question with the reason, never as a decision.
4. Claude puts it together: one page, orders at the top with names, the counter lineup below with proposed counts.
5. Anything that looks tight — a big order and a full counter on the same morning — gets flagged as a question. Whether it all fits the ovens is your call; Claude never trims an order to make the page look tidy.
6. Claude shows you the list. Change counts, drop a bake, add one it doesn't know about. Changed lines come back for another look.
7. On your yes, the list is saved to reports/ — ready for the morning.

## What you get

One file in reports/, named reports/bake-list-YYYY-MM-DD.md, dated for the day it gets baked:

- Orders due, each with the customer's name and what was agreed.
- The counter lineup with proposed counts, and the reason next to any count that differs from usual.
- Open questions — anything that needs your call before the ovens go on.

## Never

- Never invent an order. If it isn't written down or you didn't just say it, it doesn't go on the list.
- Never drop or shrink a customer's order to make the day fit. Anything that doesn't fit is flagged as a question for you.
- Never treat the proposed list as final, and never confirm capacity. The ovens are yours; the list is a proposal until your yes.
- Never confirm anything to a customer from this list — pickup dates, times, and promises still go through you, every time.
- Never guess counts from a hunch. Suggested changes come from your closes or your words, with the reason shown.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
