# Slow-day promo

When tomorrow looks quiet, this drafts one promo and a short list of regulars who might like a personal note — ready for your yes in the morning.

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

In Claude Desktop, create a scheduled task for late afternoon or early evening and paste the prompt below as the task's instructions, exactly as written. If tomorrow looks like a normal day, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time the week feels thin.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check how tomorrow is shaping up. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Read the last few daily-close reports in reports/, plus anything I've said about tomorrow. If tomorrow looks like a normal day, say so and stop. If you can't tell, ask me instead of guessing.
2. If tomorrow looks quiet, draft one promo using templates/arrival-post.md, in the voice from business/brand.md, about something true — a recent arrival, a restock, a piece worth a second look. Do not invent a sale, a discount, or a "last one" line. Put [square brackets] around anything you don't know, like a price. Draft only. Do not post it anywhere.
3. Make a short regulars note list from business/clients.md: regulars who might like a personal note about something in their style, with a two-line draft note for each. Do not send anything.
4. Save both in one file, reports/slow-day-promo-[tomorrow's local date]-[local time or sequence].md, so I can review it in the morning.

Nothing goes out without my okay on each exact item. A yes to the promo is not a yes to the notes, and yesterday's yes does not count today.

End by listing what needs my decision, one per line.
```
