# Session options

A family is ready to pick times. From the openings you list, Claude drafts a message with two or three options for the parent to choose from. You send it, and you confirm the booking.

## When to run this

- A family answered your inquiry reply and wants to start.
- A regular wants to move their usual slot or add a session.
- A reschedule request comes in — treat the new time like a fresh request and run the same steps.

## What Claude reads first

- business/staff.md — who tutors that subject and which days they're available.
- business/services.md — the session type and how long it runs, so options actually fit.
- business/clients.md — who to write to for this family, and their usual rhythm if they have one.
- business/policies.md — cancellations and anything else the message should carry.
- business/brand.md — your voice, so the message sounds like you.
- Your openings. Claude cannot see your calendar on its own, so it asks you to list the open times — or paste your week and point at the gaps. No openings from you, no options from Claude.

## Steps

1. Tell Claude who's asking and for what — subject, session type, and anything the family said about timing.
2. Claude repeats back what it heard. If a piece is missing — the subject, who the message goes to — it asks instead of guessing.
3. Claude checks staff.md for who covers that subject and services.md for the session length. If the subject isn't covered in your files, Claude stops and asks.
4. You list the openings you're willing to offer. Claude uses only those.
5. Claude drafts the message: two or three of your openings for the parent to pick from, in your voice, addressed to the right person from clients.md. If policies.md has a cancellation rule worth saying up front, the draft says it plainly.
6. Claude shows you the draft and stops there. You send it yourself, or ask for changes.
7. The parent picks a time and you write it in your calendar. Tell Claude once it's in — until then, Claude calls every time "offered", never "booked".
8. If something durable came up — a new usual slot, a second weekly session — Claude offers the exact line for business/clients.md and writes it only on your yes.

## What you get

One file saved as reports/session-options-YYYY-MM-DD.md: who asked, the openings you offered, the message you approved, and which time ended up confirmed — handy when the parent replies two days later.

## Never

- Never offer a time you didn't list. Claude works only from the openings you gave it in this chat.
- Never tell a family a time is booked or held until you say it's written in your calendar.
- Never offer one opening to several families without saying so — drafts frame it as "first to reply".
- Never write to the student. Options go to the parent, the guardian, or an adult student.
- Never invent a rate or a session length; if services.md is silent, Claude asks.
- Never send the message itself, and never book, move, or cancel a session anywhere.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
