# End of day

## What it does

At closing time, Claude pulls the day together using the close-the-day
playbook in skills/close-the-day/SKILL.md: a short note on how the day went,
plus drafts for anything needing a reply and a list of what needs you
tomorrow. Everything is saved to reports/ — nothing leaves this folder.

Mode: runs on your computer — Claude Desktop and this folder need to be open
Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, ask Claude to set up a repeating task for closing time.
Something like "close my day every evening after the last client" works fine.
When Claude asks what the task should do, paste the prompt below. If you are
already chatting with Claude at closing time, you can skip the schedule and
just say "close the day".

## The prompt to paste

```
Run the close-the-day playbook in skills/close-the-day/SKILL.md. If the owner
is not here to answer questions, write what you can from business/ and
reports/, mark the gaps clearly, and save the draft as
reports/day-close-[date].md. Drafts only — do not send, post, pay, or change
anything outside this folder.
```
