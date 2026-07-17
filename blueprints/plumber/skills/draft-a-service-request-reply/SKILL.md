# Draft a service request reply

A customer writes "my sink is leaking" — this drafts the reply that gathers what you need to know and offers arrival windows you've approved, without promising anything.

## When to run this

- A message lands: a text, an email, a website form, or a voicemail you can sum up.
- You're mid-job and want the reply ready to send at the next stop.
- Someone new asks whether you even cover their area.

## What Claude reads first

- business/policies.md — your emergency script, and any rules about service calls and new customers.
- business/profile.md — your hours, your area, and whether you take after-hours calls.
- business/brand.md — how you talk, so the reply sounds like you.
- templates/service-reply.md — the shape the reply starts from.

## Steps

1. Paste the message, or describe the call in your own words.
2. Claude checks for emergency signs first: a gas smell, a burst pipe, sewage backing up, water pouring in. If it reads like an emergency, the draft uses only your approved emergency script from policies.md and urges the customer to call you right away. Nothing else gets drafted for that message. If no script is saved yet, Claude asks you what to say — it never improvises an emergency reply.
3. For everything else, Claude drafts a reply that does two jobs: it asks the questions you'd ask — what's happening, where in the building, since when — and it offers arrival windows. Claude asks you which windows to offer before drafting; it never invents your availability.
4. The reply never says what the problem is or what it will cost. Looking is your job; the reply says you'll take a look.
5. Claude shows you the draft and stops. You tweak it or okay it, then send it yourself from your own phone or account.
6. Claude saves the exchange to reports/ so nothing falls through the cracks.
7. If the customer is worth remembering — a new rental, a property manager — Claude offers one line for business/clients.md and waits for your yes.

## What you get

One file in reports/, a fresh one each run, named like reports/service-reply-YYYY-MM-DD.md. Inside:

- The message as it came in.
- The reply you approved, ready to copy and send.
- A note of the windows offered, so the week plan can see what's promised.

## Never

- Never diagnose from a message or a photo. "Sounds like the fill valve" does not go in a reply — you'll see for yourself on site.
- Never give do-it-yourself instructions for anything involving gas, sewage, electrical, water pressure, flooding, or the structure of a building. If your saved emergency script tells people where the shutoff is, those are your words — Claude adds nothing to them.
- Never promise a price, a fix, or an exact arrival time. Windows come from you; promises come from you.
- Never offer a window you haven't approved in this chat or in the current week plan.
- If a message sounds like an emergency, never draft anything except your approved emergency script.
- Never send the reply itself — it goes out from your hands.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
