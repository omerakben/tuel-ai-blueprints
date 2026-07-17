# Morning brief

A short rundown of your day before you head out, saved where you can find it again.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task and pick a time before you leave — half an hour before the first job works well. Paste the prompt below as the task's instructions, exactly as written.

You don't need the schedule, though. Any morning, open this folder and say the prompt yourself. Same brief either way.

One thing the brief needs: today's job list. Paste it into the chat, keep this week's route plan in reports/, or save the day's list into the assets/ folder the night before. If Claude can't find today's jobs, it asks you for them instead of guessing.

## The prompt

```text
Time for the morning brief. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Read yesterday's end-of-day report in reports/, if there is one.
2. Find today's jobs. Check reports/ for this week's route plan, check assets/ for a fresh list, or use what I have pasted here. If you can't find today's jobs, stop and ask me for them. Do not guess.
3. Write a brief of 6 to 8 lines covering: today's jobs in driving order, who's on each job if there's a crew, anything to bring (a client preference noted in business/clients.md, supplies flagged low), follow-ups still waiting on me, and one small suggestion for the day.
4. Save it as reports/morning-brief-[today's date].md.

Use only what is in business/, assets/, reports/, or what I tell you. If a fact is not there, ask me. Never invent names or rates. Never put a door code, alarm code, key location, or entry instruction in the brief — if one turns up anywhere, leave it out and write "owner handles getting in".

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
