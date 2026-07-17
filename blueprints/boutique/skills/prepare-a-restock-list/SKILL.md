# Prepare a restock list

Turns your rack and shelf counts into a per-vendor reorder sheet with a ready-to-send message for each vendor — ordering costs money, so placing every order stays your move.

## When to run this

Run this when the racks look thin, when you do your regular count, or a few days before a vendor's usual order day.

A steady rhythm helps. Many shops do a quick count on a quiet weekday morning. If you tell Claude your rhythm, it can fold a stock reminder into your morning brief.

## What Claude reads first

- business/suppliers.md — who supplies each line, the reorder point for each item, usual order amounts, lead times, and how each vendor takes orders.
- business/services.md — your line names, so the sheet matches how you talk about your stock.
- business/profile.md — your shop's name for the order messages.

From you: today's counts. Read them out or paste them in any shape you like — "black tees: [count], the linen dresses: two left, gift boxes: almost out" is plenty. Claude asks about anything unclear rather than guess.

## Steps

1. Claude opens business/suppliers.md and shows you the lines it knows about, grouped by vendor, so you can count against a list instead of from memory.
2. You give today's counts. Words like "almost out" get repeated back, and Claude asks you to pin them to a number.
3. If an item has no reorder point on file, Claude asks two questions: at what count should we reorder, and how much do you usually buy? It then shows you the exact lines it wants to add to business/suppliers.md and waits for your yes before writing anything.
4. Claude compares your counts to the reorder points and builds one sheet showing which items dipped below their point and how much to order from which vendor. Anything uncertain is marked "check this" instead of being guessed.
5. Claude shows you the sheet. Drop items, change amounts, add something it missed, or ask why an item made the list.
6. When the sheet looks right to you, Claude saves it to reports/ and drafts one order message per vendor, written the way that vendor likes to be reached (it's noted in business/suppliers.md).
7. Claude shows you each draft, one vendor at a time, and stops there. You send each message yourself — or tell Claude to copy it out for you to paste. Nothing reaches a vendor without your go-ahead on that exact draft, every time.

## What you get

One reorder sheet, saved as reports/restock-list-YYYY-MM-DD.md.

The sheet has a section per vendor. Each section lists the item, how many to order, the pack or case size, and the count that put it there. A line reads like this:

    [item] — order [quantity] ([pack size]). Count [count], reorder point [point].

Items Claude wasn't sure about sit in a short "check this" list at the top so nothing slips through quietly.

Below the sheet: the drafted order message for each vendor, ready to copy once you've approved it.

If you added new reorder points along the way, those now live in business/suppliers.md too — but only the lines you approved.

## Never

- Never place an order or hand over payment details. You send every order yourself, fresh, each time.
- Never invent a number — counts, prices, pack sizes, minimums. If it isn't in the business/ files or something you just said, Claude asks.
- Never write reorder points into business/suppliers.md without showing you the exact lines and getting your yes first.
- Never put promises in a draft that cost money later, such as payment terms or delivery dates. Those are yours to settle with the vendor.
- Never reuse last time's approval. A new sheet means a new go-ahead.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
