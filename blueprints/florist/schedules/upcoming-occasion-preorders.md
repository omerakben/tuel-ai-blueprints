# Upcoming occasion preorders

About two weeks before a holiday or local event you care about, this drafts your preorder push — a post and a short note to regulars — ready for your yes.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task that runs once a week — Monday morning works well — and paste the prompt below as the task's instructions, exactly as written. If nothing is coming up, the task says so and stops: no drafts, no noise.

The dates come from the "Dates that matter" list in business/policies.md, plus anything you've mentioned out loud. Keep that list current and this schedule takes care of the rest.

Nothing here posts or sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Check what's coming up. Read the business/ folder first — it is the source of truth for the shop.

Then:

1. Read the "Dates that matter" list in business/policies.md, plus any dates I have mentioned in this chat. If the list is empty and I have said nothing, stop and ask me which holidays and local events matter to this shop. Do not guess dates.
2. If nothing on the list lands within the next three weeks, say so and stop. No drafts needed.
3. If a date is about two weeks out, draft the preorder push for it: one post using templates/bloom-post.md, in the voice from business/brand.md, inviting preorders for the occasion — and one short note I could send to regulars in business/clients.md who have ordered for this occasion before. Put [square brackets] around anything you don't know, like what will be in the cooler that week. Draft only. Do not post or send anything.
4. Save it all in one file, reports/preorder-push-[occasion].md, so I can review it when I have a minute.

Nothing goes out without my okay on each exact item. A yes to the post is not a yes to the notes, and last year's yes does not count this year.

End by listing what needs my decision, one per line.
```
