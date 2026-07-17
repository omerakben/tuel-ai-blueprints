# Monthly AI adoption review

Prepare one evidence-backed review of active AI routines. This review may recommend a stage change, but only the named owner may decide it.

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

## Prompt to copy

```text
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.

Read ADOPT-AI.md, the current operations board, and the last month of reports, work receipts, reality-check notes, exception briefs, and owner decisions for active AI routines.

Review one routine at a time. Never assign one adoption stage to the whole business. For each routine, compare actual results with its baseline and expected evidence. Check source freshness, correction patterns, review effort, value, failures, and action-boundary compliance. For Stage 2, check that work packets stayed separate. For Stage 3, check schedule failures and missing inputs. For Stage 4, confirm the loop stopped at internal drafts, review packets, receipts, and improvement proposals.

Prepare one ai-value-review for each routine using templates/ai-value-review.md. Recommend stay, advance, return, or retire, but do not change any stage, schedule, permission mode, access, policy, or business memory. A new or changed routine must use Manual permission.

Save the result to reports/monthly-ai-adoption-review-[local date]-[local time or sequence].md. Never overwrite a file. End with a work receipt and a numbered list of owner decisions.
```

Action level: B - drafts only.
