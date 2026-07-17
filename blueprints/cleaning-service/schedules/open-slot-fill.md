# Open-slot fill

When a cancellation opens a slot, this drafts the "a spot just opened up" texts for the clients waiting for one — ready for your yes.

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

In Claude Desktop, create a scheduled task for a time you'd want to catch cancellations — many owners pick early evening, after clients have had the day to write in. Paste the prompt below as the task's instructions, exactly as written. If nothing opened up, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself the moment a cancellation lands. That's the faster way, and it works the same.

Nothing here texts anyone. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check whether a slot opened up. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Look for a cancellation: something I have pasted here, a note in inbox/, or a gap I have pointed out against this week's route plan in reports/. If you can't see that a slot opened, say so and stop. Do not guess.
2. If a slot did open, read the "Waiting for a slot" list in business/clients.md — clients who asked for more visits, a different day, or a heads-up when something opens. If nobody is waiting, say so and stop.
3. Draft one short text per waiting client, in the voice from business/brand.md: the day and rough window that opened, an easy yes like "reply and it's yours", and an easy no. Put [square brackets] around anything you don't know. Do not include any door code, alarm code, or entry instruction.
4. If more than one client gets a draft, note at the top of the report that I choose who gets the slot — these texts are offers, not bookings.
5. Save the drafts in one file, reports/open-slot-fill-[today's local date]-[local time or sequence].md, so I can review and send from my phone.

Nothing goes out without my okay on each exact text. A yes to one text is not a yes to the others.

End by listing what needs my decision, one per line.
```
