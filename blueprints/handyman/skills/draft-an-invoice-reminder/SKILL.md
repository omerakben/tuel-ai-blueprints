# Remind about unpaid invoices

Friendly reminders for finished work that hasn't been paid yet. Claude drafts them from your list; you send them, and the tone stays neighborly every time.

## When to run this

- Month-end, when you look at what's still owed.
- A job wrapped weeks ago and the invoice has gone quiet.
- Before the weekly rhythm hour, so the drafts are ready when you sit down.

## What Claude reads first

- Your list of unpaid invoices — pasted, read out, or read across from your payment tool while you confirm each line. Claude never guesses who owes what.
- business/policies.md — your payment terms, and anything you've written about reminders.
- business/clients.md — how each customer likes to be reached, and history worth knowing before you nudge.
- business/brand.md — your voice.
- templates/invoice-reminder.md — the shape each reminder starts from.

## Steps

1. Take the list from you: customer, job, amount, and when the invoice went out. Anything missing is a question back to you — an amount is never assumed and never rounded.
2. Confirm each name before drafting. A reminder to the wrong person costs more than it collects, so you check the list, not Claude.
3. Draft one reminder per confirmed invoice from templates/invoice-reminder.md: friendly, short, sure of its facts. A first reminder reads like a check-in, not a demand.
4. If someone's been reminded before, Claude says so and shows you the earlier note, so the tone can firm up a notch — your call how far.
5. Show you the batch. You edit or cut any draft, then approve the keepers by name. You send each one yourself.
6. Save the batch to reports/ so month-end knows who was reminded and when.

## What you get

One file in reports/, a fresh one each run, named like reports/invoice-reminders-YYYY-MM-DD.md. Inside:

- The unpaid list as you gave it, with the date each invoice went out.
- One draft reminder per approved invoice, ready to copy and send.
- A note of who's been reminded before, and when.

## Never

- Never state an amount you didn't give. Claude organizes your figures; it never alters them and never fills gaps.
- Never threaten, and never mention collections or legal steps. If an invoice needs more than friendly reminders, that's a conversation for you and maybe a professional, never a draft.
- Never add a late fee unless policies.md allows one and you say yes to it for this exact invoice.
- Never mark anything paid, and never touch your records. What's owed and what's settled lives with you and your bookkeeper.
- Never send a reminder. Drafts wait in reports/ until you send them.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
