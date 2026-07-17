# Prepare a bar restock list

Turns your well and cooler counts into a per-distributor order sheet with a ready-to-send message for each one — ordering costs money, so placing every order stays your move.

## When to run this

Run this when the well is looking thin, when you do your regular count, or a day or two before a distributor's order day.

A steady rhythm helps. Many bars count the well and the cooler on the same quiet afternoon each week. If you tell Claude your rhythm, it can fold a restock reminder into your morning brief.

## What Claude reads first

- business/suppliers.md — who delivers what, order days, how each distributor likes to receive orders, and your par levels (the count you like to keep on hand).
- business/profile.md — your bar's name for the order messages.

From you: today's counts. Read them out or paste them in any shape you like — "well vodka: [count] bottles, light beer: two cases, limes: almost out" is plenty. Claude asks about anything unclear rather than guess.

## Steps

1. Claude opens business/suppliers.md and shows you the items it knows about, grouped by distributor, so you can count against a list instead of from memory.
2. You give today's counts. Words like "almost out" get repeated back, and Claude asks you to pin them to a number.
3. If an item has no par level on file, Claude asks two questions: at what count should we reorder, and how much do you usually buy? It then shows you the exact lines it wants to add to business/suppliers.md and waits for your yes before writing anything.
4. Claude compares your counts to the par levels and builds one order sheet showing which items dipped below their level and how much to order from which distributor. Anything uncertain is marked "check this" instead of being guessed.
5. Claude shows you the sheet. Drop items, change amounts, add something it missed, or ask why an item made the list.
6. When the sheet looks right to you, Claude saves it to reports/ and drafts one order message per distributor, written the way that distributor likes to be reached (it's noted in business/suppliers.md).
7. Claude shows you each draft, one distributor at a time, and stops there. You send each message yourself — or tell Claude to copy it out for you to paste. Nothing reaches a distributor without your go-ahead on that exact draft, every time.

## What you get

One order sheet, saved as reports/restock-list-YYYY-MM-DD.md.

The sheet has a section per distributor. Each section lists the item, how much to order, the pack or case size, and the count that put it there. A line reads like this:

    [item] — order [quantity] ([case size]). Count [count], par level [level].

Items Claude wasn't sure about sit in a short "check this" list at the top so nothing slips through quietly.

Below the sheet: the drafted order message for each distributor, ready to copy once you've approved it.

If you added new par levels along the way, those now live in business/suppliers.md too — but only the lines you approved.

## Never

- Never place an order or hand over payment details. You send every order yourself, fresh, each time. How alcohol gets ordered and delivered is between you and your distributor, under your local rules.
- Never invent a number — counts, prices, case sizes, minimums. If it isn't in the business/ files or something you just said, Claude asks.
- Never write par levels into business/suppliers.md without showing you the exact lines and getting your yes first.
- Never put promises in a draft that cost money later, such as payment terms or delivery dates. Those are yours to settle with the distributor.
- Never reuse last time's approval. A new order sheet means a new go-ahead.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
