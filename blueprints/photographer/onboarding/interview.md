# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

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

> I'd love to get to know your photography business — a few quick questions, one at a time. We will work at your pace. By the end of the first session, your profile and price list will be saved, and if you paste in a real inquiry I'll have a warm reply drafted and ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's your photography business called?
2. What kind of shoots fill your calendar — families, weddings, headshots, brands, something else?
3. If you had to describe the feel of your work in three words, what would they be?
4. What are your main sessions or packages? Take them one at a time: what it's called, what it costs, what's included (like how many photos they get), and roughly how long the shoot runs.
   - If they have a price list or a packages page: "If you've got it handy — a photo, a file, or a paste is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
5. Where do you usually shoot — your own studio, on location, both? And what area do you cover?
6. Who's behind the camera — just you? That's fine. If anyone second-shoots, edits, or assists, tell me their name, what they do, and when they're around.
7. How do inquiries usually reach you — email, Instagram messages, a form on your website?
8. When someone's ready to book, what makes it official today — a deposit, a signed agreement, just a yes?

After each answer, a short reflect-back. After all eight, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask the owner to paste their most recent inquiry — from email, a message, or their website form. An old one works fine for a first run.
2. Draft the reply using `skills/draft-an-inquiry-reply/` and `templates/inquiry-reply.md`: answer what was asked straight from the services you just saved, and gather the three things — the date they have in mind, where they picture it, and what they're dreaming of. If a package fact is missing (a price that never came up), stop and ask before drafting. And never say a date is free; the calendar is the owner's.
3. If there's no inquiry anywhere to paste, ask the owner to tell you about the last person who asked about a shoot, in their own words, and draft from that.
4. Save the draft to `reports/` and show it: "Here's your reply, ready to send when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before the day starts — today's shoot, inquiries waiting on a reply, drafts waiting on your yes?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — what got shot and what's owed to whom, with tomorrow at a glance so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the business? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — deposit and reschedule policies, past clients, the lab).
- That they can come back anytime and just talk to you like a person, because that's what works.
