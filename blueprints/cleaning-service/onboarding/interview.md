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

> I'd love to get to know your cleaning business — a few quick questions, one at a time, maybe twenty minutes. By the end you'll have your rates saved and a job estimate drafted, ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the business called?
2. Do you clean homes, offices, or both?
3. If a happy client described you in three words, what would you want those words to be?
4. What days do you work, and roughly what hours?
5. Who does the cleaning — just you? That's fine. If there's a crew, take them one at a time: their name, what they're best at, what days they work.
6. What do you charge? Take it one service at a time: what it's called, what it usually runs, roughly how long it takes.
   - If they have a rate sheet: "If you've got a rate sheet handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
7. How do you price a job you haven't seen yet — flat by size, by the hour, or a walk-through first?
8. How do new clients usually reach you — calls, texts, a website?
9. Are there jobs you turn down? Mold, sewage, that kind of thing — worth writing down now, so later I can help you say no politely and point people to the right specialist.

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask if there's a job waiting to be priced — a call or a message from this week. If there is, run the playbook in `skills/draft-a-job-estimate/`: get the rooms, the condition, and how often they want you, then draft the estimate from the rates you just saved, using `templates/estimate.md`. If the size or the scope of the job is missing, stop and ask — never fill a gap with a guess.
2. If nothing's waiting, draft a practice estimate for the kind of job the owner sees most often, so the next real call takes two minutes instead of an evening.
3. Make sure the draft says, in plain words, that the final price is the owner's call after they've seen the place.
4. Save it to `reports/` and show it: "Here's your estimate, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3 — switching on the rhythm

Offer the two daily helpers one at a time, and wait for an answer between them.

First:

> Want a two-minute morning brief before you head out — today's jobs in driving order, who's on what, anything to bring?

If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief.md`. Then:

> And a close-out at the end of the day — what got done, what got paid, what's still owed — so nothing nags at you overnight?

If yes, same walk-through with `schedules/end-of-day.md`. If either is a no, no pressure — they can just ask any morning or evening.

Also offer, once:

> Want me to save a short note so every future chat already knows the business? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — the regulars, house rules, suppliers).
- That they can come back anytime and just talk to you like a person, because that's what works.
