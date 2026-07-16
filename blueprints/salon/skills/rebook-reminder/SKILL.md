# Rebook reminders

Build your "due back" list and draft one personal text per client, ready for you to
send from your own phone.

## When to run this

Run it when the week ahead looks light, or on a steady rhythm like Monday morning.
It pairs well with the morning brief: you see who's due while you have your coffee,
and the reminders are ready before the first client sits down.

## What Claude reads first

- business/clients.md — your regulars, their last visits, and notes like "comes in
  every five weeks" or "asked us not to text".
- business/services.md — the rebooking rhythm you gave for each service, like how
  many weeks a fade or a color usually holds.
- business/policies.md — any limits you set on reaching out, like no texts after closing.
- business/brand.md — how you talk, so every draft sounds like you.
- templates/sms-reminder.md — the shape each text starts from.

If last-visit dates live in your booking tool, paste them in or read them out. Claude
also takes it plain: "it's been about six weeks since [client name] came in."

## Steps

1. Ask for anything missing. If clients.md has no last-visit date for someone, Claude
   asks you rather than working around it.
2. Build the due-back list. For each regular, Claude compares the last visit to the
   rhythm for that service. The rhythm comes from services.md or a note in clients.md.
   If neither says, that client goes on a "need your call" list with a question — never
   a guess.
3. Keep only the clients whose notes in clients.md say they gave their number for salon
   texts. Anyone who ever asked to stop hearing from you stays off, no matter how
   overdue they look.
4. Show you the list before writing a word. Cross off anyone you like; Claude waits
   for your go-ahead.
5. Draft one text per approved client, starting from templates/sms-reminder.md. Each
   one is short, sounds like you, mentions their usual service or stylist, and ends
   with an easy out like "reply STOP and I won't text again". No two drafts read the
   same.
6. Show you the whole batch. You edit or cut any draft, then approve the keepers by
   name. You send them from your own phone — Claude never sends a text.
7. Save the report to reports/ so you can tick people off as replies come in.
8. If something new came up, like a client changing their rhythm or asking to stop,
   Claude proposes the update to clients.md and waits for your yes before writing it.

## What you get

One file in reports/, a fresh one each run, named like
reports/rebook-reminders-YYYY-MM-DD.md. Inside:

- The due-back list: client, usual service, last visit, and why they're due now.
- One draft text per approved client, ready to copy and send.
- The "need your call" list: clients Claude couldn't place without asking you.
- A skipped list with the reason for each — no number on file, or asked to stop.

## Never

- Never guess a rebooking rhythm. If services.md and clients.md are both silent, ask.
- Never draft for a client who didn't give their number for salon texts, or who ever
  said stop.
- Never send a text, and never set one up to go out later. Drafts live in the report;
  your phone does the sending.
- Never drop the easy way to say "stop texting me". Every draft carries one.
- Never bring health or skin advice into a reminder. If a client note leans that way,
  keep the text to booking and suggest they see a professional.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
