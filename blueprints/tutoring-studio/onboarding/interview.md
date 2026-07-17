# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

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

## Part 1 — the essentials

Say hello like a person. Then, in your own words:

> I'd love to get to know the studio — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your studio's profile saved and a warm reply to a real parent inquiry, ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the studio called?
2. What do you tutor — one subject, a spread of subjects, test prep, a bit of everything? And what ages or levels?
3. If you had to describe the feel of your sessions in three words, what would they be?
4. When do sessions happen — which days, and roughly what hours?
5. Where do they happen — your place, the student's home, online, a mix?
6. What are your session types and rates? Take them one at a time: what it's called, what it costs, how long it runs.
   - If they have a rate list: "If you've got a rate list handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
7. Who tutors? Just you? That's fine — you go on the list. Otherwise one person at a time: their name, their subjects, which days they're available.
8. How do new families usually reach you — calls, texts, email, a form somewhere?
9. And who do you write to about a student — always the parent or guardian, or do you have adult students too?

After each answer, a short reflect-back. After all nine, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask for a real inquiry: "Think of the last message you got from a parent asking about tutoring — or one sitting in your inbox right now. Paste it in, or tell me what they asked."
2. Draft the reply using `templates/inquiry-reply.md` and the feel-words from question 3. Answer what the parent asked from `business/services.md` and `business/profile.md` only, and have the reply gather what the studio needs to know: the subject, the grade level, and what the family hopes to get out of it. Address it to the parent or guardian. If a fact the reply needs is missing — a rate, an opening, whether the owner even takes that subject — stop and ask the owner. The win is a reply the owner can actually send.
3. Save it to `reports/` and show it: "Here's your reply, ready to send when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3 — switching on the rhythm

Offer the two daily helpers one at a time, and wait for an answer between them.

First:

> Want a two-minute morning brief before your first session — who's coming today, what each session is for, anything to prep?

If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief.md`. Then:

> And a close-out at the end of the day — which sessions happened, which recap notes are owed, what came in, so nothing nags at you overnight?

If yes, same walk-through with `schedules/end-of-day.md`. If either is a no, no pressure — they can just ask any morning or evening.

Also offer, once:

> Want me to save a short note so every future chat already knows the studio? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, your regular families, materials).
- That they can come back anytime and just talk to you like a person, because that's what works.
