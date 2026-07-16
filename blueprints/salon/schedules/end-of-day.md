# End of day

Closes out the day with you step by step, then shows you tomorrow at a glance.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for around closing time and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the last client leaves. It works the same.

## The prompt

```text
It's closing time. Read the business/ folder first — it is the source of truth for the salon.

Then:

1. Open skills/daily-close/ and walk me through the daily close playbook, one step at a time. Ask me for each number and note as we go. Do not fill in anything I have not given you.
2. When we finish, save the report as reports/daily-close-[today's date].md.
3. Preview tomorrow in 3 lines: the first booking, plus any gap or prep worth flagging. If you don't have tomorrow's book, say so and ask me for it.

Use only what is in business/, the daily close playbook, or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
