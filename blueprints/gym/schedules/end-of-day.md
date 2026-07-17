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

In Claude Desktop, create a scheduled task for around closing time and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt after the last class wraps. It works the same.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
It's closing time. Read the business/ folder first — it is the source of truth for the gym.

Then:

1. Walk me through closing out the day, one question at a time: how today's classes went and roughly how full each was, any new sign-ups or trials, any renewals or cancellations I handled myself, and the day's takings as I read them out — cash, card, and front-desk sales. Write down only what I give you. Do not fill in anything I have not said, and do not touch or change any records anywhere.
2. Note any loose ends I mention — a payment to check, a machine that needs a look, a member question to follow up — each with today's date.
3. When we finish, save the report as reports/end-of-day-[today's local date]-[local time or sequence].md. These are my own notes for my bookkeeper — never present them as checked by an accountant.
4. Preview tomorrow in 3 lines: the first class, plus any class with space or prep worth flagging. If you don't have tomorrow's list, say so and ask me for it.

Use only what is in business/ or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
