# Tomorrow's location post

An evening check: if tomorrow's spot is confirmed, Claude drafts the location post tonight so it's waiting for your yes in the morning. If it isn't confirmed, Claude asks — it never guesses where you'll be.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task for the evening — after the close works well — and paste the prompt below as the task's instructions, exactly as written. If tomorrow's spot isn't confirmed, the task leaves you a question instead of a draft. No guessing, no noise.

You can also say the prompt yourself any evening.

Nothing here posts anything. The draft waits in reports/ until you say yes to it in the morning. If you never say yes, it just sits there.

## The prompt

```text
Evening check on tomorrow's location post. Read the business/ folder first — it is the source of truth for the truck.

Then:

1. Find tomorrow's plan. Check the latest weekly route sheet in reports/, today's daily close, and anything I have told you in this chat. Tomorrow's spot counts as confirmed only if I have said so — permission, permit, and hours squared away. A spot I often use on this day of the week does not count.
2. If tomorrow's spot is confirmed, draft the location post using templates/location-post.md, in the voice from business/brand.md, with one menu highlight from business/services.md. Put [square brackets] around anything you don't know. Draft only. Do not post it anywhere.
3. If tomorrow's spot is not confirmed, do not draft a post. Instead, write me a two-line note asking which spot to confirm for tomorrow, and list any spots I mentioned this week that are still waiting on a yes.
4. Save what you made as reports/location-post-[tomorrow's date].md, marked "draft — waiting for your yes".

Nothing goes out without my okay on the exact post in the morning. Yesterday's yes does not count today.

End by listing what needs my decision, one per line.
```
