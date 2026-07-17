# End of day

Closes out the day with you step by step, then shows you tomorrow at a glance.

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

In Claude Desktop, create a scheduled task for around the time you usually finish and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the last job is done. It works the same.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
It's the end of the day. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Walk me through the close, one question at a time: which jobs got done today, what got paid and how (cash, card, transfer, still owed), anything a client said worth keeping, and any supplies running low. Do not fill in anything I have not given you.
2. Organize what I tell you into a short close: jobs done, money in by type, money still owed with the client and job next to it, notes for next visit, supplies to restock. These are my own figures, tidied — never altered, never estimated, and never presented as checked by an accountant.
3. If something does not line up or needs a professional's eye, write it as a question for my bookkeeper at the bottom. Do not smooth it over.
4. When we finish, save the report as reports/end-of-day-[today's local date]-[local time or sequence].md.
5. Preview tomorrow in 3 lines: the first job, the route in one phrase, and any prep worth flagging. If you don't have tomorrow's list, say so and ask me for it.
6. If anything owed is getting old, suggest the payment-reminders playbook — a suggestion only, until I say go.

Use only what is in business/, reports/, or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
