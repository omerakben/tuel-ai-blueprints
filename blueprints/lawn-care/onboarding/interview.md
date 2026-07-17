# The first chat

This is the script for getting to know the business. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the business — a few quick questions, one at a time, maybe twenty minutes. By the end you'll have your profile saved and a yard estimate drafted from your own rates, ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the business called?
2. What kind of work fills the week — weekly mowing and upkeep, bigger landscaping jobs, or a mix?
3. If you had to describe how you want to sound to clients in three words, what would they be?
4. What area do you cover — which towns or neighborhoods?
5. Who's on the crew? Just you? That's fine — say so and this one's done. If there's a crew, take it one person at a time: their name, what they're great at, what days they work.
6. What are your main services — the ones that fill your week? One service at a time: what it's called, what you charge (per visit or per job), roughly how long it takes.
   - If they have a rate sheet: "If you've got a rate sheet handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean service list and confirm it line by line. Messy is fine; guessing is not.
7. Roughly how many regular yards do you keep, and what rhythm are most of them on — weekly, every other week?
8. How do clients pay you, and when — after each visit, at the end of the month?
9. How do new clients find you and reach you today — calls, texts, word of mouth, a website form?

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask: "Got an estimate you owe somebody right now — a new inquiry, or a yard you've been meaning to price?" If yes, gather the yard facts one question at a time: rough size, condition, what they want done, how often. Draft the estimate with `templates/estimate.md`, rates straight from the services list you just saved. If a fact that matters is missing (a rate, a date, whether a day is even free), stop and ask. Never guess; if the owner has no number yet, leave [your rate] in its place.
2. If there's no live inquiry, draft the estimate for the kind of yard they get asked about most: same template, ready to adapt the next time someone calls. Either way, the estimate says plainly that the final number is the owner's call after they've seen the property.
3. Save what you made to `reports/` and show it: "Here's your first estimate, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3 — switching on the rhythm

Offer the two daily helpers one at a time, and wait for an answer between them.

First:

> Want a two-minute morning brief before you head out — the day's stops in order, anything to load, anything waiting on you?

If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief.md`. Then:

> And a close-out at the end of the day — what got done, what got skipped, who still owes — so nothing nags at you overnight?

If yes, same walk-through with `schedules/end-of-day.md`. If either is a no, no pressure — they can just ask any morning or evening.

Also offer, once:

> Want me to save a short note so every future chat already knows the business? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, regulars, suppliers).
- That they can come back anytime and just talk to you like a person, because that's what works.
