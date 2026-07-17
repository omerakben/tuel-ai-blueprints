# Quiet-morning promo

When tomorrow morning looks slow, this drafts one promo — never posts it — and leaves it in reports/ for you to find with your first coffee.

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

In Claude Desktop, create a scheduled task for the late afternoon or evening and paste the prompt below as the task's instructions, exactly as written. If tomorrow morning looks fine, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time tomorrow feels thin.

Nothing here posts or sends. The draft waits in reports/ until you say yes to it. If you never say yes, it just sits there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check tomorrow morning for me. Read the business/ folder first — it is the source of truth for the cafe.

Then:

1. Work out whether tomorrow morning looks quiet. Use what I have told you about slow days, any notes in business/profile.md, and the last few day-close reports in reports/. If you can't tell, ask me instead of guessing.
2. If tomorrow morning looks fine, say so and stop. No promo needed.
3. If it looks quiet, draft one promo using templates/special-post.md, in the voice from business/brand.md. Real items and real prices only, from business/services.md or what I have told you. Put [square brackets] around anything you don't know, like tomorrow's special. Draft only. Do not post it anywhere.
4. Save it as reports/quiet-morning-promo-[tomorrow's local date]-[local time or sequence].md so I can look at it in the morning.

Nothing goes out without my okay on that exact draft, and yesterday's yes does not count today.

End by listing what needs my decision, one per line. If nothing does, say so.
```
