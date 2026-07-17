# End of day

Closes out the day with you step by step, then shows you tomorrow at a glance.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for around the time you usually get back and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the truck is parked. It works the same.

## The prompt

```text
It's the end of the day. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Walk me through closing out the day, one question at a time: which stops got done, which got skipped and why, anything a client said worth keeping, anything that broke or is running low, and the day's money as I give it to you — what came in and what is still owed. Write down only what I say. Do not fill in anything I have not given you, and do not total anything I have not confirmed.
2. When we finish, save the report as reports/end-of-day-[today's date].md.
3. Preview tomorrow in 3 lines from the route plan in reports/: the first stop, plus anything to load or prep. If there is no plan for tomorrow, say so and ask me if I want to make one.
4. If any visits are still unpaid, offer to draft the reminders using skills/draft-an-invoice-reminder/ and wait for my yes.

Use only what is in business/, reports/, or what I tell you tonight. If a fact is missing, ask. Never invent numbers, and never mark anything paid on your own.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
