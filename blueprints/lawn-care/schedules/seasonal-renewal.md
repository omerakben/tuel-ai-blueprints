# Seasonal renewal

When you flag a season turn, this drafts renewal notes for your recurring clients — one each — and parks them in reports/ until you're ready.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

This one waits for your signal. You know when spring cleanups start and when leaf season hits, so nothing gets drafted until you've flagged the turn in a chat or a note. If you like, create a scheduled task in Claude Desktop for the weeks a season usually turns and paste the prompt below as the task's instructions; on weeks you haven't flagged anything, it says so and stops.

You can also skip the schedule entirely and just say the prompt when you feel the season changing.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Season check. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Check whether I have flagged a season turn — in this chat, in a recent report in reports/, or in a note in assets/. If I have not flagged one, say so and stop. Never decide on your own that a season has turned.
2. If I flagged one: from business/clients.md, list the recurring clients this turn fits — who took this work before, whose rhythm pauses or restarts now. Show me the list.
3. Draft one renewal note per client on the list, using templates/seasonal-offer.md and the voice in business/brand.md. Real services and rates from business/services.md only. Put [square brackets] around anything you do not know.
4. Save the batch as reports/seasonal-renewal-[today's date].md. Drafts only. Do not send anything to anyone.

Nothing goes out without my okay on each exact note, and I do the sending.

End by listing what needs my decision, one per line.
```
