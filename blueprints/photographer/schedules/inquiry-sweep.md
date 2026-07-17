# Inquiry sweep

A morning check: any inquiries you dropped in overnight get their replies drafted and waiting for your yes.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for early morning — before the morning brief works nicely — and paste the prompt below as the task's instructions, exactly as written. If nothing new came in, the task says so and stops. No drafts, no noise.

The sweep can only see what you give it. Before bed or first thing, paste new inquiries into the chat, or save them as text files in the assets/ folder. With your Gmail connected, Claude can read new inquiry emails too — reading only; every reply still waits for your yes.

You can also say the prompt yourself any time the inbox fills up.

## The prompt

```text
Time for the inquiry sweep. Read the business/ folder first — it is the source of truth for this photography business.

Then:

1. Gather anything new: inquiries I have pasted here, new text files in assets/, or new inquiry emails if my Gmail is connected. If there is nothing new, say so and stop.
2. For each inquiry, follow skills/draft-an-inquiry-reply/ — answer from business/services.md only, and gather the date, the location, and what they are dreaming of. If a package fact is missing, put that inquiry on a "needs you" list with the question spelled out. Do not guess and do not draft around it.
3. Never say a date is free or taken. Leave availability as a question for me.
4. Save all drafts in one file, reports/inquiry-sweep-[today's date].md, one section per inquiry.
5. Send nothing. Every draft waits for my yes, one by one.

Use only what is in business/, assets/, or the inquiries themselves. If a fact is not there, ask me.

End by listing what needs my decision, one per line.
```
