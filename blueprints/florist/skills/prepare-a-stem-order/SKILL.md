# Prepare a stem order

Lines up the week's orders against what's in the cooler and drafts the list you take to the market or read to your wholesaler.

## When to run this

- The evening before a buying day, so the list is ready when you leave.
- When a big order lands and you need to know what it adds to the buy.
- Any time the cooler runs thin and you want the gap written down before you shop.

## What Claude reads first

- business/suppliers.md — who you buy from, their buying days and cutoffs, and how you order.
- business/clients.md — standing orders that repeat every week.
- reports/ — recent daily closes for what sold out, and any confirmed event proposals with dates coming up.
- What you paste or say: this week's orders and your cooler count, in your own words.

## Steps

1. Claude gathers what the week needs: the orders you paste or read out, standing orders from clients.md, and any booked event whose date falls in the window. If it can't see the week's orders, it asks — it never builds a list from guesswork.
2. You tell Claude what's in the cooler, your own words and your own counts. Claude writes it down as you said it and reads it back.
3. Claude lines up what the week needs against what's on hand and lists the gap, stem by stem. Every line traces to an order or to your count — Claude can point at where each number came from.
4. Claude splits the list by supplier using suppliers.md: market stems on one sheet, plants on another, hard goods on a third if they're low. Anything with no supplier listed becomes a question for you.
5. Claude shows you the sheets and stops. You cross off, add, or change lines — the market always has surprises, and the sheet should leave room for them.
6. Claude saves the sheets to reports/. You place every order yourself: at the market, on the phone, however you always buy.

## What you get

One file in reports/, named reports/stem-order-YYYY-MM-DD.md:

- One order sheet per supplier, quantities in plain rows, ready to take along or read out.
- The week at a glance: which orders drove which lines.
- The question list: stems with no supplier, orders with no counts, anything that needs your call.

## Never

- Never place an order, pay a supplier, or promise a supplier anything. The sheets wait for you.
- Never guess what's in the cooler or what an order needs. No count, no line — a missing count becomes a question.
- Never treat availability as certain. The market decides what's there on the day; the sheet is a plan, not a promise.
- Never invent a supplier price. If you want costs on the sheet, they come from you or from suppliers.md.
- Never promise a customer a stem because it's on the buying list. What you tell customers is covered by the order-reply playbook, and it waits for you.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
