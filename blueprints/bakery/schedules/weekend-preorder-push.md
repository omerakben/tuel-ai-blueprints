# Weekend preorder push

Midweek, this drafts a preorder reminder post for the weekend lineup and a list of regulars who might want their usual. The drafts wait in reports/ for your yes.

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

In Claude Desktop, create a scheduled task for midweek — Wednesday afternoon works well, early enough for preorders to still shape Saturday's bake. Paste the prompt below as the task's instructions, exactly as written.

You can also say the prompt yourself any week you want the push done early, or skip a week by just ignoring the drafts.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Time for the weekend preorder push. Read the business/ folder first — it is the source of truth for the bakery.

Then:

1. Find the weekend lineup. Check reports/ for this week's production plan, or use the usual weekend bakes in business/services.md. If neither says what's baking this weekend, stop and ask me. Do not guess the lineup.
2. Draft one preorder reminder post using templates/bake-post.md, in the voice from business/brand.md: what's baking this weekend and how to place a preorder. Put [square brackets] around anything you don't know, like the cutoff day. Draft only. Do not post it anywhere.
3. Build a regulars list from business/clients.md: who usually orders for the weekend, their usual, and a one-line drafted note for each in my voice. Skip anyone who ever asked not to be contacted. Do not send anything.
4. Save the post and the list in one file, reports/weekend-preorder-push-[local date]-[local time or sequence].md, so I can review it with my coffee.

Nothing goes out without my okay on each exact item. A yes to the post is not a yes to the notes, and last week's yes does not count this week.

End by listing what needs my decision, one per line.
```
