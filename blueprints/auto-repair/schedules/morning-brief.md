# Morning brief

A short rundown of your day before the first car rolls in, saved where you can find it again.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task and pick a time before you open — half an hour before the first bay works well. Paste the prompt below as the task's instructions, exactly as written.

You don't need the schedule, though. Any morning, open this folder and say the prompt yourself. Same brief either way.

One thing the brief needs: today's board — the jobs in the shop, the cars due in, and any promises you've made. Paste it into the chat, or save the day's list from whatever you track jobs in into the assets/ folder the night before. If Claude can't find today's board, it asks you for it instead of guessing.

## The prompt

```text
Time for the morning brief. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Read yesterday's end-of-day report in reports/, if there is one.
2. Find today's board. Check assets/ for a fresh copy of it, or use what I have pasted here. If you can't find today's board, stop and ask me for it. Do not guess.
3. Write a brief of 6 to 8 lines covering: which cars are in which bays, what's due in today, any ready times I have promised, parts expected today, follow-ups still waiting on me, and one small suggestion for the day.
4. Save it as reports/morning-brief-[today's date].md.

Use only what is in business/, assets/, yesterday's report, or what I tell you. If a fact is not there, ask me. Never invent names, prices, or ready times.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
