# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the studio. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the studio — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your studio's profile saved and a real inquiry answered: a reply drafted in your voice, ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the studio called?
2. What kind of work comes out of here — custom pieces, flash, cover-ups, a mix?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours do you work — and is it appointment only, or do walk-ins happen?
5. Who tattoos here? Just you? That's fine — plenty of great studios are one chair. If there's a crew, take them one at a time: their name, what they're known for, which days they're in.
6. How do people usually reach you when they want work — Instagram messages, email, a form on your site, walking in?
7. Once someone's serious, how does booking go — a consult first, a deposit to hold the date? Tell it the way you'd tell a friend.
8. What's your age and ID rule, in your own words? Whatever it is, it gets followed to the letter — Claude never drafts anything that works around it.
9. Do you keep a waitlist? Where does it live — a notebook, a notes app, a spreadsheet, the back of the appointment book? It stays yours; Claude only works from what you share.

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md`, plus the age and ID line for `business/policies.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask the owner to paste a real inquiry — an Instagram message or an email from someone who wants work. Run `skills/draft-an-inquiry-reply/`: a reply in the studio's voice that gathers the idea, rough size, placement, and reference pictures. No prices and no dates — those stay the artist's call. If a fact the reply needs is missing (the age rule, how consults work here), stop and ask rather than writing around it.
2. If no inquiry is handy, draft the studio's go-to reply instead: the message the owner can adapt the moment the next inquiry lands, built from everything Part 1 just covered.
3. Save what you made to `reports/` and show it: "Here's your reply, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you open — who's in today, which consults still need a brief, anything to get ready?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a wrap-up at the end of the day — sessions done, money in as you read it out, tomorrow at a glance — so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

One more is worth naming, without a walk-through unless they want it: when a cancellation opens a slot, `schedules/cancellation-fill.md` keeps drafted waitlist offers ready within the hour.

Also offer, once:

> Want me to save a short note so every future chat already knows the studio? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — the deposit and cancellation rules, the aftercare sheet, the waitlist itself).
- That they can come back anytime and just talk to you like a person, because that's what works.
