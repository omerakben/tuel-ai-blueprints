# Lead sweep

Once a week, this looks for inquiries gone quiet and leaves drafted follow-ups waiting in reports/ — nothing sends, ever.

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

In Claude Desktop, create a scheduled task once a week — Monday morning pairs well with the pipeline hour. Paste the prompt below as the task's instructions, exactly as written. If nothing has gone quiet, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time the pipeline feels stale.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekly lead sweep. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Go through business/clients.md and the recent inquiry-reply files in reports/. List every inquiry still waiting on an answer — theirs or mine — and how long it has been quiet.
2. If nothing has been quiet for about a week or more, say so and stop. No drafts needed.
3. For each quiet inquiry, draft one short, friendly follow-up in the voice from business/brand.md: one warm line, one easy question, no pressure. Skip anyone who said no or asked for space, and say who you skipped and why.
4. Do not invent anything. If you don't know why a lead went quiet, keep the draft general — never guess at their reasons, their budget, or their date.
5. Save the follow-ups in one file, reports/lead-sweep-[today's local date]-[local time or sequence].md, so I can review them when I'm ready.

Nothing goes out without my okay on each exact item. A yes to one follow-up is not a yes to the rest.

End by listing what needs my decision, one per line.
```
