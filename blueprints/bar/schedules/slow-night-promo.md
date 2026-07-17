# Slow-night promo

When tonight or tomorrow looks quiet, this drafts one promo and a short text list for your regulars, ready for your yes.

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

In Claude Desktop, create a scheduled task for the early afternoon and paste the prompt below as the task's instructions, exactly as written. If the night looks steady, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time a night feels thin.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check how tonight and tomorrow look for me. Read the business/ folder first — it is the source of truth for the bar.

Then:

1. Work out whether tonight or tomorrow night looks quiet: check the rhythm of the week in business/profile.md, this week's events plan in reports/ if there is one, and recent close reports. If you can't tell, ask me instead of guessing.
2. If both nights look steady, say so and stop. No promo needed.
3. If a night looks quiet, draft one promo for it using templates/event-post.md, in the voice from business/brand.md. It needs a real reason to come in — something true from business/ or from me. Put [square brackets] around anything you don't know, like a start time. Draft only. Do not post it anywhere. Nothing aimed at minors, nothing that pushes heavy or fast drinking, and no special stated as final — I decide what runs.
4. Draft a short text for my regulars and list who would get it — only people in business/clients.md marked okay to text about bar news. Write out the message once. Do not send anything.
5. Save both drafts in one file, reports/slow-night-promo-[local date]-[local time or sequence].md, so I can review them.

Nothing goes out without my okay on each exact item. A yes to the promo is not a yes to the texts, and yesterday's yes does not count today.

End by listing what needs my decision, one per line.
```
