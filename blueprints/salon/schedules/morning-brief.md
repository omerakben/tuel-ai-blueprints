# Morning brief

A short rundown of your day before you open, saved where you can find it again.

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

In Claude Desktop, create a scheduled task and pick a time before you open — half an hour before the first chair works well. Paste the prompt below as the task's instructions, exactly as written.

You don't need the schedule, though. Any morning, open this folder and say the prompt yourself. Same brief either way.

One thing the brief needs: today's book. Paste it into the chat, or save the day's list from your booking tool into the inbox/ folder the night before. If Claude can't find today's book, it asks you for it instead of guessing.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the morning brief. Read the business/ folder first — it is the source of truth for the salon.

Then:

1. Read yesterday's end-of-day report in reports/, if there is one.
2. Find today's book. Check inbox/ for a fresh copy of it, or use what I have pasted here. If you can't find today's book, stop and ask me for it. Do not guess.
3. Write a brief of 6 to 8 lines covering: who is in which chair today, where the gaps are, anything to prep (color to mix, a client preference noted in business/clients.md), follow-ups still waiting on me, and one small suggestion for the day.
4. Save it as reports/morning-brief-[today's local date]-[local time or sequence].md.

Use only what is in business/, inbox/, yesterday's report, or what I tell you. If a fact is not there, ask me. Never invent names or prices.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
