# Morning brief

## What it does

Before the day starts, Claude reads your business/ files and the latest notes
in reports/, then writes you a short brief: what today looks like and what
needs your attention first, plus any drafts still waiting for your review. The
brief is saved to reports/ — nothing is sent anywhere.

Mode: runs on your computer — Claude Desktop and this folder need to be open
Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, ask Claude to set up a repeating task. Say something like
"run my morning brief every weekday before I open". When Claude asks what the
task should do, paste the prompt below. If your computer is off or this folder
is not open at the time, the brief simply skips that day and nothing breaks.
You can also run it by hand any morning by pasting the same prompt into a chat.

## The prompt to paste

```
Read the business/ folder and the most recent notes in reports/. Write today's
morning brief for the owner: what today looks like and the top things that
need their attention, plus any drafts still waiting for review. Save it as
reports/morning-brief-[date].md. Drafts only — do not send, post, pay, or
change anything outside this folder.
```
