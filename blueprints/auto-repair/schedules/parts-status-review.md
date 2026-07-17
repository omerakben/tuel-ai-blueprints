# Parts status review

When jobs sit waiting on parts, this drafts one honest status update per customer, ready for your yes — so nobody waits in silence.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task at a steady time — mid-morning works well, once you've heard from your suppliers — and paste the prompt below as the task's instructions, exactly as written.

You can also say the prompt yourself any time a part is dragging.

This review starts with you: Claude asks you to list the jobs waiting on parts. It never decides on its own which cars are waiting, and nothing here sends. The drafts wait in reports/ until you say yes to each one.

## The prompt

```text
Time for the parts status review. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Ask me to list the jobs waiting on parts — for each one: the customer, the vehicle, the part, what the technician said, and an arrival date only if a supplier actually gave me one. If nothing is waiting, say so and stop.
2. For each job I list, draft one customer status update using templates/status-update.md, in the voice from business/brand.md. Use only what I gave you. If I did not give an arrival date, the draft says we will follow up with a time — never a guessed date.
3. Keep the technician's words as their words. Do not diagnose, and do not say anything about whether a car is safe or drivable.
4. Show me every draft, one per job. I send the ones I approve from my own phone. Do not send anything.
5. Save the batch as reports/parts-status-review-[today's date].md.

Nothing goes out without my okay on each exact draft. A yes to one is not a yes to the rest.

End by listing what needs my decision, one per line.
```
