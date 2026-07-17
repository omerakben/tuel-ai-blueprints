# Inquiry sweep

A morning check: any inquiries you dropped in overnight get their replies drafted and waiting for your yes.

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

In Claude Desktop, create a scheduled task for early morning — before the morning brief works nicely — and paste the prompt below as the task's instructions, exactly as written. If nothing new came in, the task says so and stops. No drafts, no noise.

The sweep can only see what you give it. Before bed or first thing, paste new inquiries into the chat, or save them as text files in the inbox/ folder. With your Gmail connected, Claude can read new inquiry emails too — reading only; every reply still waits for your yes.

You can also say the prompt yourself any time the inbox fills up.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the inquiry sweep. Read the business/ folder first — it is the source of truth for this photography business.

Then:

1. Gather anything new: inquiries I have pasted here, new text files in inbox/, or new inquiry emails if my Gmail is connected. If there is nothing new, say so and stop.
2. For each inquiry, follow skills/draft-an-inquiry-reply/ — answer from business/services.md only, and gather the date, the location, and what they are dreaming of. If a package fact is missing, put that inquiry on a "needs you" list with the question spelled out. Do not guess and do not draft around it.
3. Never say a date is free or taken. Leave availability as a question for me.
4. Save all drafts in one file, reports/inquiry-sweep-[today's local date]-[local time or sequence].md, one section per inquiry.
5. Send nothing. Every draft waits for my yes, one by one.

Use only what is in business/, inbox/, or the inquiries themselves. If a fact is not there, ask me.

End by listing what needs my decision, one per line.
```
