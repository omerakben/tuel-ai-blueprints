# Morning brief

## What it does

Before the day starts, Claude reads your business/ files and current notes
in operations/, inbox/, and reports/, then writes you a short brief: what today looks like and what
needs your attention first, plus any drafts still waiting for your review. The
brief is saved to reports/ — nothing is sent anywhere.

Mode: runs on your computer — Claude Desktop and this folder need to be open
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

In Claude Desktop, ask Claude to set up a repeating task. Say something like
"run my morning brief every weekday before I open". When Claude asks what the
task should do, paste the prompt below. If the setup screen offers a folder,
choose this business folder. Work that needs local files requires Claude Desktop
and the folder to be available. If they are not, run this prompt by hand when
you are ready and review the most recent saved receipt before continuing.

## The prompt to paste

```
Read the full CLAUDE.md before doing anything. If it is unavailable, stop.
This run is A Observe or B Draft only. Use approved sources, show checked-at times for changing input, and mark missing or stale input incomplete instead of guessing.
Save output to reports/ only. Never overwrite a file; add local time or a sequence number when needed. End with a work receipt and the owner's decision list.
Do not send, post, pay, file, sign, delete, or change an outside system.
Read the business/ folder and the most recent notes in reports/. Write today's
morning brief for the owner: what today looks like and the top things that
need their attention, plus any drafts still waiting for review. Save it as
reports/morning-brief-[local date]-[local time or sequence].md. Drafts only — do not send, post, pay, or
change anything outside this folder.
```
