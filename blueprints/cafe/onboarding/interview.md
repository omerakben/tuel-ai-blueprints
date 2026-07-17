# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the cafe. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the cafe — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your cafe's profile saved and today's special written up as a post, ready whenever you are. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the cafe called?
2. What kind of place is it — coffee and pastries, breakfast and lunch, a bit of both?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours are you open?
5. Who's behind the counter — just you? That's fine, plenty of great cafes run on one pair of hands. If there's a crew, take them one at a time: their name, what they're great at, what days they're usually in.
6. What are the everyday favorites — the drinks and dishes people come in for? Take them one item at a time: what it's called, what it costs.
   - If they have a menu: "If you've got a menu handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean menu list and confirm it line by line. Messy is fine; guessing is not.
7. Do you run a special — daily, weekly, whenever the kitchen feels like it? How do people usually hear about it now?
8. Where do people find the cafe online, and where do reviews land — Google, Yelp, Instagram?
9. Last one, and it sets up your first win: what's the special today, or tomorrow if today's done? The item, its price, and when it's available.

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Draft the special post from the answer to question 9, using `templates/special-post.md` and the feel-words from question 3. If the item, the price, or when it's available is missing, stop and ask — this post never guesses. No special this week? Use the everyday favorite the owner would most love a full room for, with its real price.
2. Show it: "Here's your first post, ready when you are — want changes?" Rework it until it sounds like the cafe.
3. Save it to `reports/` so it's there whenever the owner wants to post it.

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you open — who's on, today's special, anything to prep?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — tallies the till and tips, so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the cafe? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — suppliers, regulars, house policies).
- That they can come back anytime and just talk like a person, because that's what works.
