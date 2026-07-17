# End of day

Closes out the day with you step by step, then shows you tomorrow at a glance.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for around the end of service and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt once the window is shut. It works the same.

## The prompt

```text
Service is over. Read the business/ folder first — it is the source of truth for the truck.

Then:

1. Open skills/close-the-day/ and walk me through the close playbook, one step at a time. Ask me for each number and note as we go. Do not fill in anything I have not given you.
2. When we finish, save the report as reports/daily-close-[today's date].md.
3. Preview tomorrow in 3 lines: tomorrow's spot and hours if they are confirmed, plus any prep or restock worth starting tonight. If tomorrow's plan is not confirmed anywhere you can see, say so and ask me — do not guess a location.

Use only what is in business/, the close playbook, or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
