# Close the day

This playbook wraps up your day in a few minutes and tees up tomorrow.

## When to run this

At closing time, or whenever the last client has left and you have a moment.
It is also what the end-of-day routine in schedules/end-of-day.md runs, so you
never have to remember it yourself.

## What Claude reads first

- business/profile.md — your hours and the basics
- business/staff.md — who was in today
- business/services.md — for tidying up the names of what was done

And from you: how today actually went. Paste today's appointment list, or just
talk it through in a few sentences. Share numbers only if you want them in the
note — leaving them out is always fine.

## Steps

1. Claude asks how the day went and listens. Short answers are fine.
2. Claude tidies it into a day note: what got done, plus anything unusual or
   left unfinished.
3. Claude lists what needs you tomorrow — replies to look at, anything running
   low, any loose end from today.
4. If something needs a written reply, Claude drafts it now and shows you. The
   draft waits inside the note until you choose to send it yourself.
5. If today surfaced a fact worth keeping — a new regular, say, or a corrected
   price — Claude proposes adding it to business/ and waits for your yes before
   writing anything there.
6. Claude shows you the finished note as a draft. When you approve it, Claude
   saves it to reports/.

## What you get

A short day note saved as reports/day-close-[date].md: the day in brief, then
what needs you tomorrow and any drafts waiting for your decision. Over a week,
these notes become the raw material for your weekly review.

## Never

- Never send the drafted replies. They stay in the note until you send them.
- Never write to business/ without your yes on that exact change.
- Never guess at numbers or fill in blanks. Whatever you did not share stays
  blank, marked plainly as not shared.
- Never copy client details into the note beyond what you shared for it.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
