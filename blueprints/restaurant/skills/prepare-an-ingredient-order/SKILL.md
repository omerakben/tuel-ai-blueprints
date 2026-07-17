# Prepare an ingredient order

Walk the cooler, read out the counts, and get a per-supplier order sheet with a ready-to-send message for each — placing every order stays your move.

## When to run this

- The cooler or pantry is looking thin.
- A day or two before a supplier's usual order day.
- On your regular count rhythm. Many kitchens do a quick walk-through on the same morning each week; tell Claude your rhythm and it can fold a reminder into your morning brief.

## What Claude reads first

- business/suppliers.md — who supplies what, reorder points, usual order amounts, and how each supplier likes to receive orders.
- business/profile.md — your restaurant's name for the order messages.

From you: today's counts. Read them out or paste them in any shape — "tomatoes: [count], chicken: two trays left, flour: almost out" is plenty. Claude asks about anything unclear rather than guess.

## Steps

1. Claude opens business/suppliers.md and shows you what it knows about, grouped by supplier, so you can count against a list instead of from memory.
2. You give today's counts as you walk the cooler and the pantry. Words like "almost out" get repeated back, and Claude asks you to pin them to a number.
3. If an item has no reorder point on file, Claude asks two questions: at what count should we reorder, and how much do you usually buy? It then shows you the exact lines it wants to add to business/suppliers.md and waits for your yes before writing anything.
4. Claude compares your counts to the reorder points and builds one order sheet: which items dipped below their point, how much to order, from which supplier. Anything uncertain is marked "check this" instead of being guessed.
5. Claude shows you the sheet. Drop items, change amounts, add what it missed, or ask why an item made the list.
6. When the sheet looks right, Claude saves it to reports/ and drafts one order message per supplier, written the way that supplier likes to be reached (noted in business/suppliers.md).
7. Claude shows you each draft, one supplier at a time, and stops there. You send each message yourself. Nothing reaches a supplier without your go-ahead on that exact draft, every time.

## What you get

One order sheet, saved as reports/ingredient-order-YYYY-MM-DD.md.

The sheet has a section per supplier. Each section lists the item, how much to order, the pack size, and the count that put it there. A line reads like this:

    [item] — order [quantity] ([pack size]). Count [count], reorder point [point].

Items Claude wasn't sure about sit in a short "check this" list at the top so nothing slips through quietly.

Below the sheet: the drafted order message for each supplier, ready to copy once you've approved it.

If you added new reorder points along the way, those now live in business/suppliers.md too — but only the lines you approved.

## Never

- Never places an order or hands over payment details. You send every order yourself, fresh, each time.
- Never invents a number — counts, prices, pack sizes, minimums. If it isn't in the business/ files or something you just said, Claude asks.
- Never writes reorder points into business/suppliers.md without showing you the exact lines and getting your yes first.
- Never puts promises in a draft that cost money later, like payment terms or delivery dates. Those are yours to settle with the supplier.
- Never reuses last time's approval. A new order sheet means a new go-ahead.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
