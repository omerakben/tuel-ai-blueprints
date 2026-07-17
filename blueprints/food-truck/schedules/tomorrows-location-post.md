# Tomorrow's location post

An evening check: if tomorrow's spot is confirmed, Claude drafts the location post tonight so it's waiting for your yes in the morning. If it isn't confirmed, Claude asks — it never guesses where you'll be.

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

In Claude Desktop, create a scheduled task for the evening — after the close works well — and paste the prompt below as the task's instructions, exactly as written. If tomorrow's spot isn't confirmed, the task leaves you a question instead of a draft. No guessing, no noise.

You can also say the prompt yourself any evening.

Nothing here posts anything. The draft waits in reports/ until you say yes to it in the morning. If you never say yes, it just sits there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Evening check on tomorrow's location post. Read the business/ folder first — it is the source of truth for the truck.

Then:

1. Find tomorrow's plan. Check the latest weekly route sheet in reports/, today's daily close, and anything I have told you in this chat. Tomorrow's spot counts as confirmed only if I have said so — permission, permit, and hours squared away. A spot I often use on this day of the week does not count.
2. If tomorrow's spot is confirmed, draft the location post using templates/location-post.md, in the voice from business/brand.md, with one menu highlight from business/services.md. Put [square brackets] around anything you don't know. Draft only. Do not post it anywhere.
3. If tomorrow's spot is not confirmed, do not draft a post. Instead, write me a two-line note asking which spot to confirm for tomorrow, and list any spots I mentioned this week that are still waiting on a yes.
4. Save what you made as reports/location-post-[tomorrow's local date]-[local time or sequence].md, marked "draft — waiting for your yes".

Nothing goes out without my okay on the exact post in the morning. Yesterday's yes does not count today.

End by listing what needs my decision, one per line.
```
