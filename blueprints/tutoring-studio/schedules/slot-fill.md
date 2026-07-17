# Slot fill

Once a week, the openings you list get drafted offers to the families who said they wanted more sessions. The drafts wait for you.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task once a week — many owners pick a quiet stretch like Sunday evening, before the week's sessions start. Paste the prompt below as the task's instructions, exactly as written. If nothing is open, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time a spot opens mid-week.

This check starts with you: Claude asks you to list the week's openings. It never decides on its own that a slot is open, and nothing here sends. The drafts wait in reports/ until you say yes to each one.

## The prompt

```text
Time for the weekly slot-fill check. Read the business/ folder first — it is the source of truth for the studio.

Then:

1. Ask me to list the openings for the coming week — for each one: the day, the time, which tutor, and the subject it suits. If nothing is open, say so and stop.
2. For each opening, look in business/clients.md for families whose notes say they asked for more sessions and whose subject fits. Skip anyone who asked for space. Show me the list of who you would write to, and wait for my okay before drafting a word.
3. For the families I approve, draft one short note each using templates/reminder-text.md, in the voice from business/brand.md — addressed to the parent or guardian, offering the time as first to reply, with an easy way to say no more notes like this. Do not send anything.
4. Show me every draft. I send the ones I approve from my own phone or email.
5. Save the batch as reports/slot-fill-[today's date].md.

Nothing goes out without my okay on each exact note. A yes to one is not a yes to the rest.

End by listing what needs my decision, one per line.
```
