# End of day

Wraps up the day with you step by step, then shows you tomorrow at a glance.

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

In Claude Desktop, create a scheduled task for around closing time and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the last client leaves. It works the same.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
It's closing time. Read the business/ folder first — it is the source of truth for the studio.

Then:

1. Walk me through the day's wrap-up, one step at a time: sessions finished, consults held, and money in as I read it out — deposits and payments stay exactly as I say them; organize, never adjust. Then anything left hanging: an inquiry to answer, a healed-photo ask, a piece still to schedule. Do not fill in anything I have not given you.
2. When we finish, save the report as reports/end-of-day-[today's local date]-[local time or sequence].md. Anything money-related I was unsure about goes on a short "for the bookkeeper" list at the bottom. The report is my own figures, tidied — never call it checked or verified by an accountant.
3. Preview tomorrow in 3 lines: the first appointment, plus any consult or prep worth flagging. If you don't have tomorrow's book, say so and ask me for it.

Use only what is in business/, or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
