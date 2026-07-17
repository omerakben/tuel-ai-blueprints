# Cancellation fill

When a slot opens, the waitlist offers are drafted and waiting within the hour — you look them over and send the ones you like.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task that runs once an hour during the hours you work, and paste the prompt below as the task's instructions, exactly as written.

To flag an opening, drop a short note in assets/ — a file called something like opening-today.md with the day, the time, and how long the slot is. If there's no note, the task says so quietly and stops. No drafts, no noise.

No schedule needed either: the moment a cancellation lands, open this folder and say "a slot just opened" — Claude runs the playbook right away.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Check for an open slot. Read the business/ folder first — it is the source of truth for the studio.

Then:

1. Look in assets/ for a note flagging an opening — a file named like opening-today. If there is none, say "no opening flagged" and stop.
2. If there is one, open skills/draft-a-cancellation-fill-message/ and follow that playbook: confirm the opening from the note, ask me for the waitlist if you don't have it, shortlist who fits, and draft one message per person using templates/cancellation-fill-text.md.
3. Draft only. Do not send anything, and do not set anything up to send later. I send every message myself, and each one needs my fresh yes first.
4. Save the drafts as reports/cancellation-fill-[today's date].md so they are ready when I look.

Use only what is in business/, assets/, or what I tell you. If a fact is missing — the time, the length, who is on the waitlist — ask me instead of guessing.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
