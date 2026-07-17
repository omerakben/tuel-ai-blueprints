# End of day

Winds down the day with you — what moved on each event, what came in, what's due tomorrow — so nothing nags at you overnight.

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

In Claude Desktop, create a scheduled task for around the time you usually stop and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the day is done. It works the same.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
It's the end of the day. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Ask me what moved today, one thing at a time: inquiries that came in, replies that went out, decisions made on booked events, and any money notes worth writing down — a deposit received, a balance still open. Do not fill in anything I have not given you.
2. Write the day into a short note: what moved, what came in, what is due tomorrow, and anything I said I would do.
3. Save it as reports/end-of-day-[today's local date]-[local time or sequence].md.
4. If anything durable came up — a new lead, a confirmed date, a vendor detail — show me the exact lines you would add to the right business/ file and wait for my yes before writing them.

Use only what is in business/, reports/, or what I tell you tonight. If a fact is missing, ask. Never invent numbers or dates.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
