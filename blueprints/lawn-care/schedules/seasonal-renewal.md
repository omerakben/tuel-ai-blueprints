# Seasonal renewal

When you flag a season turn, this drafts renewal notes for your recurring clients — one each — and parks them in reports/ until you're ready.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

<!-- TUEL:SCHEDULE-CONTRACT:START -->
## Run contract

- Mode: local folder. Claude Desktop and this folder must be available for the run.
- Cadence: the owner chooses and confirms the repeating time.
- Time zone: use the owner's confirmed local time zone; ask if it is missing.
- Maximum action level: B Draft. A run may observe or draft only.
- Approved sources: `business/`, `operations/`, `inbox/`, `reports/`, and only the connected sources named in this schedule.
- Freshness rule: show the source date or checked-at time for time-sensitive inputs. Treat undated or stale input as missing when it could change the result.
- Output: save drafts and summaries to `reports/` only. Never change `business/` or an outside system from a schedule.
- Missing input: stop the affected step, label the result incomplete, and list exactly what the owner needs to provide.
- Duplicate rule: never overwrite an existing report. Add the local run time or a sequence number to the filename.
- Failure path: write a short failure receipt to `reports/` when possible, then surface it at the next owner check-in. Never hide, retry a consequential action, or claim success without a saved result.
- Start every run by reading the full `CLAUDE.md`. End with a work receipt and a list of items that need the owner's decision.
<!-- TUEL:SCHEDULE-CONTRACT:END -->

## How to turn it on

This one waits for your signal. You know when spring cleanups start and when leaf season hits, so nothing gets drafted until you've flagged the turn in a chat or a note. If you like, create a scheduled task in Claude Desktop for the weeks a season usually turns and paste the prompt below as the task's instructions; on weeks you haven't flagged anything, it says so and stops.

You can also skip the schedule entirely and just say the prompt when you feel the season changing.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Season check. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Check whether I have flagged a season turn — in this chat, in a recent report in reports/, or in a note in inbox/. If I have not flagged one, say so and stop. Never decide on your own that a season has turned.
2. If I flagged one: from business/clients.md, list the recurring clients this turn fits — who took this work before, whose rhythm pauses or restarts now. Show me the list.
3. Draft one renewal note per client on the list, using templates/seasonal-offer.md and the voice in business/brand.md. Real services and rates from business/services.md only. Put [square brackets] around anything you do not know.
4. Save the batch as reports/seasonal-renewal-[today's local date]-[local time or sequence].md. Drafts only. Do not send anything to anyone.

Nothing goes out without my okay on each exact note, and I do the sending.

End by listing what needs my decision, one per line.
```
