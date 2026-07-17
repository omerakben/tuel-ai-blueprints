# End of day

Closes out the day with you step by step, then shows you tomorrow at a glance.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for around closing time and paste the prompt below as the task's instructions, exactly as written.

You can skip the schedule too. Any evening, open this folder and say the prompt when the last car is locked up. It works the same.

## The prompt

```text
It's closing time. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Walk me through closing the day, one question at a time: which jobs finished today, which are still open and what they're waiting on (parts, a customer's yes, bay time), which cars are staying overnight, and the day's money as I read it out — cash, card, and anything marked to check later. Do not fill in anything I have not given you.
2. When we finish, save the report as reports/end-of-day-[today's date].md.
3. Preview tomorrow in 3 lines: the first car due, plus any promise or part worth flagging. If you don't have tomorrow's board, say so and ask me for it.

Use only what is in business/ or what I tell you tonight. If a fact is missing, ask. Never invent numbers.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
