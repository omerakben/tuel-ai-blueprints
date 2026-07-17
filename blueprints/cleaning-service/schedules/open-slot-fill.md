# Open-slot fill

When a cancellation opens a slot, this drafts the "a spot just opened up" texts for the clients waiting for one — ready for your yes.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for a time you'd want to catch cancellations — many owners pick early evening, after clients have had the day to write in. Paste the prompt below as the task's instructions, exactly as written. If nothing opened up, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself the moment a cancellation lands. That's the faster way, and it works the same.

Nothing here texts anyone. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Check whether a slot opened up. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Look for a cancellation: something I have pasted here, a note in assets/, or a gap I have pointed out against this week's route plan in reports/. If you can't see that a slot opened, say so and stop. Do not guess.
2. If a slot did open, read the "Waiting for a slot" list in business/clients.md — clients who asked for more visits, a different day, or a heads-up when something opens. If nobody is waiting, say so and stop.
3. Draft one short text per waiting client, in the voice from business/brand.md: the day and rough window that opened, an easy yes like "reply and it's yours", and an easy no. Put [square brackets] around anything you don't know. Do not include any door code, alarm code, or entry instruction.
4. If more than one client gets a draft, note at the top of the report that I choose who gets the slot — these texts are offers, not bookings.
5. Save the drafts in one file, reports/open-slot-fill-[today's date].md, so I can review and send from my phone.

Nothing goes out without my okay on each exact text. A yes to one text is not a yes to the others.

End by listing what needs my decision, one per line.
```
