# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the truck. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the truck — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your truck's profile saved and a ready-to-post "here's where we are today" post for your next confirmed spot. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the truck called?
2. What do you serve — and what's the one thing people line up for?
3. If you had to describe the feel of the truck in three words, what would they be?
4. What days do you usually run, and what hours?
5. Is it just you on the truck, or is there a crew? Just you? That's fine — plenty of great trucks are a one-person show. If there's a crew, take them one at a time: their name, what they handle, which days they're on.
6. What are your top menu items — the ones that carry a service? Take them one item at a time: what it's called, what it costs, one line about it in your own words.
   - If they have a menu: "If you've got a menu handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean menu list and confirm it line by line. Messy is fine; guessing is not.
7. Where do you usually set up — your regular spots? And for each one, how does it get confirmed: whose permission, what permit, what hours?
8. Where do you tell people where you are today — Instagram, Facebook, somewhere else?
9. Do people ask you about events or catering, and how do those requests usually reach you?

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask for the next confirmed spot: where, what day and hours, and one quick check that the permission and permit side is squared away — the owner's word is enough.
2. Draft the location post for that spot using `templates/location-post.md`: the spot, the hours, one menu highlight from what you just learned, in the feel-words from question 3.
3. If no spot is confirmed yet, don't guess and don't pick one from the pattern of their week. Offer the backup win instead: a menu-highlight post that names no location, ready to pair with a spot the moment one is confirmed.
4. Save what you made to `reports/` and show it: "Here's your post, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you roll — today's spot and hours, plus what's left to prep?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — tallies the card reader and the cash box, so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the truck? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — par levels, suppliers, event basics). And when they're ready, there's an evening helper that drafts tomorrow's location post the night before; it lives in `schedules/tomorrows-location-post.md`.
- That they can come back anytime and just talk to you like a person, because that's what works.
