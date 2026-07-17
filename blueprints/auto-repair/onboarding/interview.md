# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the shop. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the shop — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your shop's profile saved and a customer status update drafted and ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the shop called?
2. What kind of work fills your week — general repair, brakes and tires, a bit of everything?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours are you open?
5. How many bays do you run?
6. What do you charge? Start with the hourly labor rate, then the jobs you do most, one at a time: what the job's called, what you usually charge or the range, roughly how long it takes.
   - If they have a rate sheet: "If you've got a rate sheet handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
7. Who works the bays? Just you? That's fine — you go on the list. Otherwise one person at a time: their name, what they're best at, what days they're in.
8. How does work come in — calls, texts, walk-ins, a booking tool?
9. And once a car is here, how do you keep the customer posted — do you call, or text?

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask for a real car: "Think of a car in the shop right now — or the last one that left. Tell me what the technician found, exact words are perfect, and the ready time you've promised the customer, if you've promised one."
2. Draft the status update using `templates/status-update.md` and the feel-words from question 3. Keep the technician's findings, the shop's recommendation, and what the customer approved clearly separate. If the owner hasn't set a ready time, the draft says the shop will follow up with one — never a guessed time. If a fact the text needs is missing — the customer's name, what was approved — stop and ask. The win is a text the owner can actually send.
3. Save it to `reports/` and show it: "Here's your update, ready to send when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you open — what's in the bays, what's due in, which promises come due today?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — what got finished, what's still waiting on parts or a yes, so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the shop? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, regulars, parts suppliers).
- That they can come back anytime and just talk to you like a person, because that's what works.
