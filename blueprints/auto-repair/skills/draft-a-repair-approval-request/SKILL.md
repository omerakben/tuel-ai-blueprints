# Repair approval requests

The technician found extra work mid-job. Claude drafts the message that explains it plainly and asks the customer for a clear yes or no. You send it.

## When to run this

- A job is open and the technician found something the customer hasn't approved yet.
- The estimate you gave no longer covers what the job actually needs.
- A customer said "just tell me what it'll cost first" and you want that ask in writing.

## What Claude reads first

- business/clients.md — the customer and the vehicle.
- business/policies.md — the line above which extra work always needs a customer's okay, if you've set one.
- business/services.md — your rates, so the numbers you give land in the right shape.
- business/brand.md — how the shop talks.
- templates/approval-request.md — the shape each request starts from.

Then from you: the technician's findings in their words, what the shop recommends, and the cost — your number, or a blank to fill in before sending.

## Steps

1. Tell Claude what the technician found and what you recommend doing about it. Exact words are perfect; Claude keeps the finding and the recommendation separate in the draft.
2. Give the cost if you've settled on one. If you haven't, the draft carries [the estimate] as a blank for you to fill in before sending — Claude never fills it with a guess.
3. Say what happens if the customer says no, if you've decided that — for example, the car goes back together as it came in. If you haven't decided, the draft leaves it out.
4. Claude drafts the request: what was found, what the shop recommends, what it would run, and one clear question — "Want us to go ahead? A yes or no by reply is all we need."
5. Claude shows you the exact message and waits. Edit until it reads like you.
6. You send it. Claude never sends, and never marks the work approved — that happens when the customer answers you.
7. Claude saves a copy to reports/ so there's a record of what was asked and when.
8. When the customer answers, tell Claude — the yes or no goes in the record, and the next status update reflects it.

## What you get

One file per request, named reports/approval-request-YYYY-MM-DD.md: the message you approved, the technician's findings behind it, and space to note the customer's answer.

## Never

- Never diagnose, and never call the vehicle safe, unsafe, or drivable — the request quotes the technician's words as theirs and leaves the judgment with them.
- Never invent or round a price. The number is yours; missing means a blank, not a guess.
- Never use fear to get a yes. No "you really don't want to drive it like this" unless those are the technician's exact words, quoted as theirs.
- Never write as if the work has started. The ask comes before the wrench.
- Never bundle two decisions into one ask. Two extra jobs means two clear questions.
- Never send the request, and never treat silence as approval.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
