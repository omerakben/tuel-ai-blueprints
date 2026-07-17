# Parts status review

When jobs sit waiting on parts, this drafts one honest status update per customer, ready for your yes — so nobody waits in silence.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

<!-- TUEL:SCHEDULE-CONTRACT:START -->
## Run contract

- Mode: local folder. Claude Desktop and this folder must be available for the run.
- Cadence: the owner chooses and confirms the repeating time.
- Time zone: use the owner's confirmed local time zone; ask if it is missing.
- Maximum action level: B Draft. A run may observe or draft only.
- Approved sources: `business/`, `operations/`, `inbox/`, `reports/`, and only the connected sources named in this schedule.
- Freshness rule: show the source date or checked-at time for time-sensitive inputs. Treat undated or stale input as missing when it could change the result.
- Output: save drafts and summaries to `reports/` only. Never change `business/` or an outside system from a schedule.
- Missing input: stop the affected step, label the result incomplete, and list exactly what the owner needs to provide.
- Duplicate rule: never overwrite an existing report. Add the local run time or a sequence number to the filename.
- Failure path: write a short failure receipt to `reports/` when possible, then surface it at the next owner check-in. Never hide, retry a consequential action, or claim success without a saved result.
- Start every run by reading the full `CLAUDE.md`. End with a work receipt and a list of items that need the owner's decision.
<!-- TUEL:SCHEDULE-CONTRACT:END -->

## How to turn it on

In Claude Desktop, create a scheduled task at a steady time — mid-morning works well, once you've heard from your suppliers — and paste the prompt below as the task's instructions, exactly as written.

You can also say the prompt yourself any time a part is dragging.

This review starts with you: Claude asks you to list the jobs waiting on parts. It never decides on its own which cars are waiting, and nothing here sends. The drafts wait in reports/ until you say yes to each one.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the parts status review. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Ask me to list the jobs waiting on parts — for each one: the customer, the vehicle, the part, what the technician said, and an arrival date only if a supplier actually gave me one. If nothing is waiting, say so and stop.
2. For each job I list, draft one customer status update using templates/status-update.md, in the voice from business/brand.md. Use only what I gave you. If I did not give an arrival date, the draft says we will follow up with a time — never a guessed date.
3. Keep the technician's words as their words. Do not diagnose, and do not say anything about whether a car is safe or drivable.
4. Show me every draft, one per job. I send the ones I approve from my own phone. Do not send anything.
5. Save the batch as reports/parts-status-review-[today's local date]-[local time or sequence].md.

Nothing goes out without my okay on each exact draft. A yes to one is not a yes to the rest.

End by listing what needs my decision, one per line.
```
