# Month-end tidy-up

Claude gathers the month's end-of-day notes into one plain summary you can hand to your bookkeeper. This is a tidy-up, not bookkeeping and not tax advice.

## When

In the first few days of a new month, once the last end-of-day note of the old month is saved in reports/. It takes about fifteen minutes. Say "let's close out the month" and Claude starts.

## Steps

1. Gather the month. Claude collects every end-of-day report for the month from reports/ and shows you two lists: the days it found and the days that are missing. Missing days stay missing — Claude never fills a gap with a guess.
2. Add it up. Claude totals the month in one plain table: jobs finished, what was invoiced, what was paid, and what's still owed. Every figure comes straight from an end-of-day note or from you. If you want to check one, Claude points to the day it came from.
3. List the loose ends. Anything a day flagged but never settled goes on one list: a job finished but not billed, a payment marked "check later", an invoice with no reply, a day with no note at all. Each item keeps its date.
4. Review the draft. Claude shows you the whole summary before saving anything. You say it looks right, or point at what is off and Claude corrects it from the daily notes. Nothing is saved until you say yes.
5. Save it. With your yes, Claude saves the summary as reports/month-summary-[month].md.
6. Write the bookkeeper questions. Claude ends with a short list of questions for your bookkeeper — the loose ends from step 3, written in plain words, one per line, ready to hand over as is. The list sits at the bottom of the saved summary.

## What you get

- One plain summary of the month, saved as reports/month-summary-[month].md: jobs finished, invoiced, paid, and still owed, plus the days covered, the days missing, and the loose-end list.
- A short list of questions for your bookkeeper at the bottom of the same file.

## Never

- This is a tidy-up, not bookkeeping. Claude does not do your books, does not give tax advice, and never presents this summary as checked by an accountant. Those calls belong to your bookkeeper.
- Claude never invents a number and never smooths one over. A missing day shows up as missing, never as an estimate.
- Claude never sends the summary anywhere. It stays in your folder until you choose to share it.
- Claude never pays anything and never files anything. Money only moves when you move it.
- Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
