# Quiet table fill

When tomorrow's book looks light, this drafts one promo and a list of regulars who might love a nudge — everything waits for your yes in the morning.

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

In Claude Desktop, create a scheduled task for late afternoon or early evening and paste the prompt below as the task's instructions, exactly as written. If tomorrow looks fine, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time tomorrow feels thin.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one in the morning. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check tomorrow's book for me. Read the business/ folder first — it is the source of truth for the restaurant.

Then:

1. Find tomorrow's book. Check inbox/ for a copy of it, or ask me to paste it. If you can't see tomorrow's book, stop and ask. Do not guess.
2. If tomorrow looks reasonably full, say so and stop. No promo needed.
3. If tomorrow looks light, draft one promo using templates/menu-special-post.md, in the voice from business/brand.md. Use only a dish, price, and run that I have already given you — if any of those is missing, ask me instead of drafting around it. Put [square brackets] around anything else you don't know. Draft only. Do not post it anywhere.
4. Make a short regulars list from business/clients.md: people who tend to come in on this night and might enjoy the invite, each with a one-line suggested message in our voice. Do not send anything, and leave off anyone who ever asked us not to reach out.
5. Save both in one file, reports/quiet-table-fill-[tomorrow's local date]-[local time or sequence].md, so I can review it in the morning.

Nothing goes out without my okay on each exact item. A yes to the promo is not a yes to the messages, and yesterday's yes does not count today.

End by listing what needs my decision, one per line.
```
