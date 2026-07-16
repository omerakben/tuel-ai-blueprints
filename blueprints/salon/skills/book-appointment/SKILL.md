# Book an appointment

Turns a booking request into two or three workable time slots and a reply ready to send, with the time-and-chair math already done.

## When to run this

A client is asking for a time. That might be a text you paste in, an Instagram message, a note from a phone call, or someone at the front desk wanting to know when you can fit them in.

A reschedule counts too. Treat the new time like a fresh request and run the same steps.

## What Claude reads first

Before suggesting anything, Claude checks:

- business/services.md — how long the service takes and what it costs.
- business/staff.md — who does that service and which days they work.
- business/policies.md — deposits, cancellation rules, and your hard limits.
- business/brand.md — your tone of voice, so the reply sounds like you.
- Your appointment book. Claude cannot see it on its own, so it will ask you to paste today's or this week's book, or just tell it the open gaps. No book, no time suggestions.

## Steps

1. Tell Claude about the request — paste the text or message, or describe the call or walk-in in your own words.
2. Claude repeats back what it heard: the service they want and when they'd like to come in, plus whether they asked for anyone in particular. If a piece is missing, Claude asks you instead of guessing.
3. Claude looks up the service in services.md for its length and price. If it is not listed there, Claude asks you — it never makes a number up.
4. Claude checks staff.md for who does that service and which days they are in.
5. If Claude has not seen your book in this chat, it asks you to paste today's or this week's schedule, or to tell it the open gaps. It works only from what you give it.
6. Claude proposes two or three slots where the service fits and the right person is free.
7. Claude checks policies.md and folds anything that applies into the plan — if a deposit is due, the reply will say so.
8. Claude drafts the reply with the proposed times, written in your tone. It shows you the draft and stops there. You send it from your own phone or account, or tell Claude what to change and it redrafts.
9. The client picks a time and you write it in your book. Tell Claude once it is in — until then, Claude keeps calling the time "proposed", never "booked".
10. If the client mentioned something worth remembering, Claude offers one line for business/clients.md, for example "[first name] — prefers [day and time], usually sees [stylist]". It shows you the exact line and writes it only after you say yes.

## What you get

- The reply message, ready for you to copy and send yourself.
- A short note saved as reports/booking-[date]-[client-first-name].md holding the request, the slots offered, the draft you approved, and what ended up confirmed. Handy when the client replies two days later and you need the thread back.
- Your business files stay untouched unless you said yes to that one clients.md line.

## Never

- Never tells a client a time is booked or held until you say it is written in your book.
- Never sends the reply itself — every message goes out from your hands.
- Never invents prices, hours, open slots, or anything else about your salon. If it is not in your files or in what you just told it, Claude asks.
- Never takes card details, and never promises a refund or an exception to your own policies.
- Never advises on skin or scalp problems or anything health-related — it suggests the client check with a professional.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
