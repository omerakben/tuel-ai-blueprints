# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the gym. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the gym — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your gym's profile saved and a ready-to-post caption for a class with open spots. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the gym called?
2. What kind of place is it — weights and machines, group classes, yoga or pilates, a mix?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours are you open? If classes run on a set timetable, roughly how does the week look?
5. What do you offer — memberships, class packs, drop-ins? Take them one at a time: what it's called, what it costs, what it includes.
   - If they have a price list or timetable: "If you've got a price list or timetable handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
6. Who coaches or teaches? Just you? That's fine — plenty of great gyms are one person. If there's a crew, take them one at a time: their name, what they teach, what days they're in.
7. How do people join or book a class today — do they call, message you, walk in, or use a booking tool?
8. Which classes fill up fast, and which ones tend to have space?

After each answer, a short reflect-back. After all eight, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask: is there a class in the next few days with open spots? You need three things — the class, the day and time, and how many spots are open. If any of the three is missing, ask for it. Never guess a timetable.
2. Draft the fill post with the playbook in `skills/draft-a-class-fill-post/`, starting from `templates/class-post.md` and the feel-words from question 3. True facts only: the class as the owner described it, the spots as they counted them.
3. If every class really is full this week, say congratulations and draft something else true instead — a post about the class people love most, from what you just learned. The win is a real post, not a particular one.
4. Save what you made to `reports/` and show it: "Here's your first post, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you open — which classes run today, who's coaching, where the space is?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — sign-ups noted, takings as you read them out, loose ends written down so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the gym? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, the regulars, how renewals work).
- That they can come back anytime and just talk to you like a person, because that's what works.
