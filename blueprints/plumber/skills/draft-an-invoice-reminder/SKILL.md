# Draft an invoice reminder

Friendly reminders for the unpaid invoices you name — drafted in your voice, sent by you.

## When to run this

- You know who hasn't paid and it's time for a gentle word.
- Month-end is coming and you want the stragglers reminded before the books close.
- A customer promised "this week" two weeks ago.

## What Claude reads first

- What you tell it right now — which invoices, who they're for, what job, how overdue. Claude works only from what you name; it never decides on its own who owes you.
- business/policies.md — your payment terms, and anything you allow on late payments.
- business/clients.md — how each customer likes to be reached, and any notes worth knowing before nudging.
- business/brand.md — how you talk, so every reminder sounds like you.
- templates/invoice-reminder.md — the shape each reminder starts from.

## Steps

1. Name the unpaid invoices: who, for what job, roughly when it was due. Paste a list from your invoicing tool if that's easier.
2. Claude reflects the list back and asks about anything unclear — a customer with two open invoices, an amount you didn't mention. An amount appears in a draft only if you gave it.
3. You confirm who gets a reminder. Anyone you'd rather call personally comes off the list.
4. Claude drafts one reminder per invoice: friendly, short, assuming good faith — people mostly just forget. Each one names the job so the customer knows exactly what it's about.
5. Late fees or stern terms show up only if policies.md allows them and you say so for this reminder, fresh.
6. Claude shows you the whole batch. You edit or cut any draft, approve the keepers by name, and send them yourself.
7. Claude saves the run to reports/ so next time you both know who was reminded and when.

## What you get

One file in reports/, a fresh one each run, named like reports/invoice-reminders-YYYY-MM-DD.md. Inside:

- The list you named: customer, job, due date as you gave it.
- One approved reminder per invoice, ready to copy and send.
- A "sent?" line under each so you can tick off what went out.

## Never

- Never decide who owes you — Claude reminds only the invoices you named.
- Never threaten, shame, or mention collections. If it's gone past friendly, that's a conversation for you, maybe with professional advice.
- Never state an amount you didn't give, and never add interest or a late fee unless your policies allow it and you said so this time.
- Never contact a customer itself — every reminder leaves from your phone or account.
- Never mark an invoice paid or change any record — reminders are words, not bookkeeping.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
