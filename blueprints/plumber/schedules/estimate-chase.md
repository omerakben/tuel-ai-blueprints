# Estimate chase

Once a week, this rounds up the estimates nobody answered and drafts one polite nudge each. The drafts wait in reports/ until you say so.

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

In Claude Desktop, create a scheduled task for a quiet moment once a week — Friday morning suits a lot of owners — and paste the prompt below as the task's instructions, exactly as written. If nothing is waiting on a reply, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time the quiet estimates start bugging you.

Nothing here sends. The nudges wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekly estimate chase. Read the business/ folder first — it is the source of truth for the business.

Then:

1. Go through reports/ and list every estimate that is still open: sent, no reply recorded, not yet nudged. Show me the list — customer, job, when it went out.
2. If nothing is open, say so and stop.
3. For each open estimate, draft one short, friendly follow-up using templates/follow-up-note.md, in the voice from business/brand.md. Keep the numbers exactly as the estimate had them. Skip anyone marked "don't contact" in business/clients.md, and skip anything already nudged once — put those on a "your call" list instead.
4. Save the list and the drafts as reports/estimate-chase-[today's local date]-[local time or sequence].md. Drafts only. Do not send anything.

Nothing goes out without my okay on each exact note. A yes to one is not a yes to the others, and last week's yes does not count today.

End by listing anything that needs my decision, one per line. If nothing does, say so.
```
