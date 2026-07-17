# The restock list

Read out what's on the shelf and in the fridge; Claude checks it against your reorder points and writes one order sheet per supplier, ready for you to send.

## When to run this

- The evening before your usual ordering day.
- After a busy weekend that emptied the pastry case.
- Any time the shelf looks thin and you want a clear picture before you call anyone.

## What Claude reads first

- business/suppliers.md — who supplies what, your reorder points, and how you place each order.
- business/policies.md — any limits you've set around ordering.
- The last restock list in reports/, if there is one, so nothing gets ordered twice by accident.

You read your counts out loud or paste them — beans, milk, cups, whatever you track. Rough is fine; Claude works with what you say.

## Steps

1. Take the counts one item at a time and reflect each back, so a misheard "two" never becomes a wrong order.
2. Compare each count against the reorder point in business/suppliers.md. At or below the point, the item goes on the list. Above it, it stays off.
3. Anything without a reorder point goes on a "needs your call" list with a question — never a guess. Same for any item Claude can't match to a supplier.
4. Build one order sheet per supplier: the items to reorder, your count, and the reorder point next to each. Order amounts come from your notes in suppliers.md or from you on the spot — Claude never picks an amount for you.
5. Show you the whole thing and wait. Cross off anything, change any amount. Nothing is final until you say so.
6. If you'd like, Claude drafts the order message for each supplier — the email or the text — in your words. You send every one yourself.
7. Save it all as reports/restock-list-YYYY-MM-DD.md.
8. If a reorder point turned out wrong, Claude proposes the exact new line for business/suppliers.md and waits for your yes before writing it.

## What you get

One file in reports/, a fresh one each run, named like reports/restock-list-YYYY-MM-DD.md. Inside:

- One order sheet per supplier, with items, counts, and reorder points side by side.
- Drafted order messages, if you asked for them — ready to copy and send.
- The "needs your call" list: items with no reorder point or no supplier on file.

## Never

- Never place an order or send anything to a supplier. You send; Claude drafts.
- Never guess a count, a reorder point, or an order amount. Missing means ask.
- Never promise a supplier a payment or a date. Money and commitments are yours alone.
- Never invent an item that wasn't in your count or your files.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
