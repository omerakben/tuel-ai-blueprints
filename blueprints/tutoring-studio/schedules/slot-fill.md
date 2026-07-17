# Slot fill

Once a week, the openings you list get drafted offers to the families who said they wanted more sessions. The drafts wait for you.

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

In Claude Desktop, create a scheduled task once a week — many owners pick a quiet stretch like Sunday evening, before the week's sessions start. Paste the prompt below as the task's instructions, exactly as written. If nothing is open, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time a spot opens mid-week.

This check starts with you: Claude asks you to list the week's openings. It never decides on its own that a slot is open, and nothing here sends. The drafts wait in reports/ until you say yes to each one.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekly slot-fill check. Read the business/ folder first — it is the source of truth for the studio.

Then:

1. Ask me to list the openings for the coming week — for each one: the day, the time, which tutor, and the subject it suits. If nothing is open, say so and stop.
2. For each opening, look in business/clients.md for families whose notes say they asked for more sessions and whose subject fits. Skip anyone who asked for space. Show me the list of who you would write to, and wait for my okay before drafting a word.
3. For the families I approve, draft one short note each using templates/reminder-text.md, in the voice from business/brand.md — addressed to the parent or guardian, offering the time as first to reply, with an easy way to say no more notes like this. Do not send anything.
4. Show me every draft. I send the ones I approve from my own phone or email.
5. Save the batch as reports/slot-fill-[today's local date]-[local time or sequence].md.

Nothing goes out without my okay on each exact note. A yes to one is not a yes to the rest.

End by listing what needs my decision, one per line.
```
