# Cancellation fill

When a slot opens, the waitlist offers are drafted and waiting within the hour — you look them over and send the ones you like.

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

In Claude Desktop, create a scheduled task that runs once an hour during the hours you work, and paste the prompt below as the task's instructions, exactly as written.

To flag an opening, drop a short note in inbox/ — a file called something like opening-today.md with the day, the time, and how long the slot is. If there's no note, the task says so quietly and stops. No drafts, no noise.

No schedule needed either: the moment a cancellation lands, open this folder and say "a slot just opened" — Claude runs the playbook right away.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check for an open slot. Read the business/ folder first — it is the source of truth for the studio.

Then:

1. Look in inbox/ for a note flagging an opening — a file named like opening-today. If there is none, say "no opening flagged" and stop.
2. If there is one, open skills/draft-a-cancellation-fill-message/ and follow that playbook: confirm the opening from the note, ask me for the waitlist if you don't have it, shortlist who fits, and draft one message per person using templates/cancellation-fill-text.md.
3. Draft only. Do not send anything, and do not set anything up to send later. I send every message myself, and each one needs my fresh yes first.
4. Save the drafts as reports/cancellation-fill-[today's local date]-[local time or sequence].md so they are ready when I look.

Use only what is in business/, inbox/, or what I tell you. If a fact is missing — the time, the length, who is on the waitlist — ask me instead of guessing.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
