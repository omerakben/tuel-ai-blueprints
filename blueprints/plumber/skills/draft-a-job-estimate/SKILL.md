# Draft a job estimate

Turn "the water heater at the rental is done" into a written estimate — plain scope lines, your real rates, ready to send once you've okayed it.

## When to run this

- You just looked at a job and need to put a number on paper before you forget the details.
- A customer described a job on the phone and wants something in writing.
- You're pricing a bigger job and want the scope written out clearly first.

## What Claude reads first

- business/services.md — your hourly rate, service call fee, common-job prices, and how you price parts.
- business/policies.md — deposits on bigger jobs, payment terms, and how long an estimate stays good.
- business/profile.md — the business details that go at the top.
- business/brand.md — how you talk, so the estimate reads like you wrote it.
- templates/estimate.md — the shape every estimate starts from.

## Steps

1. Describe the job in your own words: what's wrong or what's wanted, where it is, what you saw if you've been out there.
2. Claude repeats the scope back in plain lines — the work, the parts likely involved, anything you said you'd leave out. If the scope is unclear, Claude stops and asks. No estimate gets drafted around a fuzzy scope.
3. Claude builds the line items from services.md. A job or rate that isn't in services.md becomes a question for you, never a guess. Parts you haven't priced yet go in as "to be priced", not as invented numbers.
4. Claude folds in what policies.md says — a deposit line if one applies, and how long the estimate stays good.
5. The draft says, plainly, that this is an estimate and the final price is your call after you've seen the job. That line stays in, every time.
6. Claude shows you the draft and stops. You change anything you like; Claude redrafts until it's right. You send it yourself, from your own email or phone.
7. Claude saves the estimate to reports/ so the follow-up playbook can find it later.
8. If the job surfaced something durable — a repeat customer's property note, a rate you want written down — Claude shows the exact line for the right business/ file and waits for your yes.

## What you get

One file in reports/, a fresh one each run, named like reports/job-estimate-YYYY-MM-DD.md. Inside:

- The scope in plain lines a customer can read without calling you to translate.
- Line items from your real rates, with [square brackets] around anything still open.
- The estimate note: the final price is your call after seeing the job.
- A "sent?" line so you can mark when it actually went out.

## Never

- Never guess a rate, a part price, or how long a job takes. If services.md is silent and you haven't said, Claude asks.
- Never promise a final price sight-unseen — every estimate says the final number comes after you've seen the job.
- Never claim the work will be up to code, permitted, safe, or covered by warranty. Those words are yours to give, or they stay out.
- Never work out what's wrong from a description or a photo. The estimate prices the work you described, and the draft says you'll confirm on site.
- Never send the estimate itself. It waits in reports/ until you send it.

Action level: B — Claude drafts; sending, posting, or paying is always the owner's call.
