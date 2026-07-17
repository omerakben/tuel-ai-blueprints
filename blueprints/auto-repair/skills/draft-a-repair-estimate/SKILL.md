# Repair estimates

From the scope you set and the rates in your files, Claude drafts a written estimate for the customer. The final number is always your call.

## When to run this

- A customer asked what a job would cost before booking it.
- A car is booked in and you want the estimate in writing before work starts.
- You gave a rough number over the phone and want a clean written version to send.

## What Claude reads first

- business/services.md — your hourly labor rate and what you usually charge for common jobs.
- business/policies.md — what you charge to look at a car, and when extra work needs an okay.
- business/clients.md — the customer and vehicle, if they're a regular.
- business/brand.md — how the shop talks.
- templates/estimate.md — the shape each estimate starts from.

Then from you: the job as you scoped it — what you'd do, the parts if you know them, and any number you've already settled on.

## Steps

1. Tell Claude the job: the vehicle, what the customer asked for, and what you'd actually do.
2. Claude pulls the rates from business/services.md. If a rate the estimate needs isn't there and you haven't said it, Claude stops and asks — never a guessed number.
3. Parts you haven't priced yet go in as [to be confirmed], plainly marked.
4. Claude drafts the estimate with the work in plain words, the numbers you gave, and this said straight: it's an estimate, not a final price — the final number is your call once the job is open, and anything beyond the estimate gets asked about first.
5. Claude shows you the exact draft and waits. You set the final figure; Claude never nudges it up or down.
6. You send it. Claude never sends.
7. Claude saves a copy to reports/, and offers to add any new rate you stated to business/services.md — written only on your yes.

## What you get

One file per estimate, named reports/estimate-YYYY-MM-DD.md: the estimate as you approved it, plus a note of which rates came from your files and which you gave fresh.

## Never

- Never invent or adjust a price, a rate, or a parts cost. Your files or your words — nothing else.
- Never call it a quote, and never let the draft read like a locked price. An estimate says the final number comes after the job is open.
- Never promise a ready date inside an estimate unless you gave one for this exact job.
- Never diagnose. The estimate covers the work you scoped, not what might be wrong beyond it, and it never calls the car safe or unsafe.
- Never send the estimate anywhere. You send it when you're happy with it.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
