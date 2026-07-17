# Estimate chase

Once a week, a sweep of the estimates that went out and got no answer — with a friendly nudge drafted for each one, waiting in reports/ for your yes.

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

In Claude Desktop, create a scheduled task for a quiet moment once a week — many owners pick Monday morning, so the nudges are ready with the coffee. Paste the prompt below as the task's instructions, exactly as written.

No schedule needed, though. Any time you wonder "did they ever get back to me?", open this folder and say the prompt.

Nothing here sends. The nudges wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekly estimate sweep. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Gather the estimates in reports/ that went out and show no reply. Check past follow-up reports so nobody gets a second nudge without me knowing about the first. If you cannot tell whether an estimate was answered, list it and ask me — do not assume.
2. Skip anyone who said no, asked for space, or has a "don't chase" note in business/clients.md.
3. For each estimate still quiet, draft one short friendly nudge using templates/follow-up-note.md, in the voice from business/brand.md. Facts come from the saved estimate only. Draft only — do not send anything.
4. Save the sweep as reports/estimate-chase-[today's local date]-[local time or sequence].md: the quiet list, each draft, and who was skipped and why.

Nothing goes out without my okay on each exact draft. Last week's yes does not count this week.

End by listing what needs my decision, one per line. If nothing does, say so.
```
