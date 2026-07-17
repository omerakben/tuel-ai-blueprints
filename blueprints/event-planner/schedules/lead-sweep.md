# Lead sweep

Once a week, this looks for inquiries gone quiet and leaves drafted follow-ups waiting in reports/ — nothing sends, ever.

Mode: runs on your computer — Claude Desktop and this folder need to be open.

Drafts only — nothing goes out on a timer. <!-- action level: B -->

## How to turn it on

In Claude Desktop, create a scheduled task once a week — Monday morning pairs well with the pipeline hour. Paste the prompt below as the task's instructions, exactly as written. If nothing has gone quiet, the task says so and stops — no drafts, no noise.

You can also say the prompt yourself any time the pipeline feels stale.

Nothing here sends. The drafts wait in reports/ until you say yes to each one. If you never say yes, they just sit there.

## The prompt

```text
Time for the weekly lead sweep. Read the business/ folder first — it is the source of truth for this business.

Then:

1. Go through business/clients.md and the recent inquiry-reply files in reports/. List every inquiry still waiting on an answer — theirs or mine — and how long it has been quiet.
2. If nothing has been quiet for about a week or more, say so and stop. No drafts needed.
3. For each quiet inquiry, draft one short, friendly follow-up in the voice from business/brand.md: one warm line, one easy question, no pressure. Skip anyone who said no or asked for space, and say who you skipped and why.
4. Do not invent anything. If you don't know why a lead went quiet, keep the draft general — never guess at their reasons, their budget, or their date.
5. Save the follow-ups in one file, reports/lead-sweep-[today's date].md, so I can review them when I'm ready.

Nothing goes out without my okay on each exact item. A yes to one follow-up is not a yes to the rest.

End by listing what needs my decision, one per line.
```
