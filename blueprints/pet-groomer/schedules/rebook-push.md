# Rebook push

Once a week, the due-back list gets built and the reminder texts get drafted — waiting in reports/ for your yes.

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

In Claude Desktop, create a scheduled task for a quiet moment in your week — many groomers pick Monday morning — and paste the prompt below as the task's instructions, exactly as written. If nobody is due back, the task says so and stops. No drafts, no noise.

You can also say the prompt yourself any time the book looks light.

Nothing here sends. The drafts wait in reports/ until you say yes to each one, and you send them from your own phone. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekly rebook push. Read the business/ folder first — it is the source of truth for this grooming business.

Then:

1. Open skills/draft-a-rebooking-reminder/ and follow that playbook. Build the due-back list from business/clients.md: compare each pet's last visit to the rhythm from business/services.md or their own notes. If a last visit or a rhythm is missing, put that pet on a "need your call" list with a question. Never guess a date.
2. Keep only parents whose notes say texts are okay. Anyone who ever asked to stop stays off.
3. Draft one short reminder text per due parent using templates/reminder-text.md, in the voice from business/brand.md, naming the pet and their usual groom, each with an easy way out like "reply STOP and I won't text again". Put [square brackets] around anything you don't know.
4. If nobody is due back this week, say so and stop.
5. Save the list and the drafts as reports/rebook-push-[today's local date]-[local time or sequence].md so I can review them with my coffee.

Nothing goes out without my okay on each exact text, and I do the sending from my own phone. Last week's yes counts for nothing this week.

End by listing what needs my decision, one per line.
```
