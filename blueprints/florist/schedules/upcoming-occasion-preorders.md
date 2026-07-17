# Upcoming occasion preorders

About two weeks before a holiday or local event you care about, this drafts your preorder push — a post and a short note to regulars — ready for your yes.

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

In Claude Desktop, create a scheduled task that runs once a week — Monday morning works well — and paste the prompt below as the task's instructions, exactly as written. If nothing is coming up, the task says so and stops: no drafts, no noise.

The dates come from the "Dates that matter" list in business/policies.md, plus anything you've mentioned out loud. Keep that list current and this schedule takes care of the rest.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Check what's coming up. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Read the "Dates that matter" list in business/policies.md, plus any dates I have mentioned in this chat. If the list is empty and I have said nothing, stop and ask me which holidays and local events matter to this shop. Do not guess dates.
2. If nothing on the list lands within the next three weeks, say so and stop. No drafts needed.
3. If a date is about two weeks out, draft the preorder push for it: one post using templates/bloom-post.md, in the voice from business/brand.md, inviting preorders for the occasion — and one short note I could send to regulars in business/clients.md who have ordered for this occasion before. Put [square brackets] around anything you don't know, like what will be in the cooler that week. Draft only. Do not post or send anything.
4. Save it all in one file, reports/preorder-push-[occasion].md, so I can review it when I have a minute.

Nothing goes out without my okay on each exact item. A yes to the post is not a yes to the notes, and last year's yes does not count this year.

End by listing what needs my decision, one per line.
```
