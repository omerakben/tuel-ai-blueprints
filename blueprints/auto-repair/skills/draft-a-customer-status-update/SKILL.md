# Customer status updates

Turn your technician's notes and the ready time you've decided into a plain text the customer actually understands, ready for you to send.

## When to run this

- A customer calls asking where their car stands and you want a clean answer in writing.
- The technician just found or finished something the customer should hear about today.
- A part landed, a job moved, or a ready time changed.
- It pairs well with the parts status review: every car waiting on a part gets its update drafted in one sitting.

## What Claude reads first

- business/clients.md — the customer, their vehicle, and how they like to hear from you.
- business/brand.md — how the shop talks, so the text sounds like you.
- business/policies.md — anything you've set about promising times.
- templates/status-update.md — the shape each update starts from.

Then Claude needs two things from you: the technician's notes, exact words are perfect, and the ready time — only if you've decided one.

## Steps

1. Tell Claude which job this is: the customer, the vehicle, and what the technician said. If any of that is missing, Claude asks rather than working around it.
2. Claude sorts what you gave it into three piles and keeps them separate in the draft: what the technician observed, what the shop recommends, and what the customer has already approved. If a line could sit in two piles, Claude asks which.
3. The ready time comes from you and only you. If you haven't decided one, the draft says the shop will follow up with a time — never a guessed date or a "should be done by".
4. Claude writes the update in plain words a customer understands, keeping the technician's findings as their findings, not as a verdict on the car. It shows you the exact text and waits.
5. Ask for changes as many times as you like — shorter, warmer, more detail. Nothing moves until you say it's good.
6. You send the text from your own phone or email. Claude never sends it.
7. Claude saves a copy to reports/ so you can see what each customer was told and when.
8. If something durable came up — a customer who prefers texts, a vehicle you'll see again — Claude proposes the line for business/clients.md and writes it only on your yes.

## What you get

One file per run, named reports/status-update-YYYY-MM-DD.md: the finished text, the technician's notes it came from, and a note of what was observed, what was recommended, and what the customer has approved.

## Never

- Never diagnose, and never call the vehicle safe, unsafe, or drivable. That call belongs to the technician and you — the draft quotes it only as it was said.
- Never invent recall, warranty, emissions, inspection, or ready-time facts. Missing means ask, not guess.
- Never blur what the technician observed, what the shop recommends, and what the customer approved.
- Never put a price in the update that you didn't give for this exact job.
- Never send the update, and never set one up to go out later. Drafts live in the report; your phone does the sending.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
