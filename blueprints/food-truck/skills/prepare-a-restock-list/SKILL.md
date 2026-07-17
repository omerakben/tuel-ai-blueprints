# Prepare a restock list

Turns your counts into a per-supplier restock list with a ready-to-send message for each supplier — ordering costs money, so placing every order stays your move.

## When to run this

Run this when the shelves in the truck or at your base are looking thin, when you do your regular count, or a day or two before a supplier's usual order day.

A steady rhythm helps. Many trucks count after the last service of the week. If you tell Claude your rhythm, it can fold a restock reminder into your morning brief.

## What Claude reads first

- business/suppliers.md — who supplies what, the restock point for each item, usual order amounts, pack sizes, and how each supplier likes to receive orders.
- business/profile.md — the truck's name for the order messages.

From you: today's counts. Read them out or paste them in any shape you like — "buns: one case, sauce: [count] bottles, propane: one tank left" is plenty. Claude asks about anything unclear rather than guess.

## Steps

1. Claude opens business/suppliers.md and shows you the items it knows about, grouped by supplier, so you can count against a list instead of from memory.
2. You give today's counts. Words like "almost out" get repeated back, and Claude asks you to pin them to a number.
3. If an item has no restock point on file, Claude asks two questions: at what count should we restock, and how much do you usually buy? It then shows you the exact lines it wants to add to business/suppliers.md and waits for your yes before writing anything.
4. Claude compares your counts to the restock points and builds one list showing which items dipped below their point and how much to order from which supplier. Anything uncertain is marked "check this" instead of being guessed.
5. Claude shows you the list. Drop items, change amounts, add something it missed, or ask why an item made the list.
6. When the list looks right to you, Claude saves it to reports/ and drafts one order message per supplier, written the way that supplier likes to be reached (it's noted in business/suppliers.md).
7. Claude shows you each draft, one supplier at a time, and stops there. You place each order yourself — by phone, by text, on their site — or tell Claude to copy the message out for you to paste. Nothing reaches a supplier without your go-ahead on that exact draft, every time.

## What you get

One restock list, saved as reports/restock-list-YYYY-MM-DD.md.

The list has a section per supplier. Each section lists the item, how many to order, the pack size, and the count that put it there. A line reads like this:

    [item] — order [quantity] ([pack size]). Count [count], restock point [point].

Items Claude wasn't sure about sit in a short "check this" list at the top so nothing slips through quietly.

Below the list: the drafted order message for each supplier, ready to copy once you've approved it.

If you added new restock points along the way, those now live in business/suppliers.md too — but only the lines you approved.

## Never

- Never place an order or hand over payment details. You place every order yourself, fresh, each time.
- Never invent a number — counts, prices, pack sizes, minimums. If it isn't in the business/ files or something you just said, Claude asks.
- Never write restock points into business/suppliers.md without showing you the exact lines and getting your yes first.
- Never put promises in a draft that cost money later, such as payment terms or delivery dates. Those are yours to settle with the supplier.
- Never claim anything about an ingredient's freshness or sourcing in an order note beyond what you or the supplier already put in writing.
- Never reuse last time's approval. A new list means a new go-ahead.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
