# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the grooming business. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know your grooming business — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your business profile saved, plus a due-back list and a friendly reminder text drafted for each pet parent who's about ready to book again. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the business called?
2. How do you groom — a shop, a mobile van, house calls, or a mix?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours do you groom?
5. Who does the grooming — just you? That's fine, plenty of great groomers work solo. If there's a crew, take them one at a time: name, what they're great at, what days they're in.
6. What are your main grooms — the ones that fill your week? Take them one at a time: what it's called, what it usually costs, roughly how long it takes, and about how many weeks before that pet is due back.
   - If they have a price list: "If you've got a price list handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
   - Prices go in as usual prices, not promises: note plainly that the final price is the owner's call once they see the coat.
7. How do pet parents book today — do they call, text you, message on social, or use a booking tool?
8. Who are your regulars? A few is plenty for today. For each one: the pet's name, the parent's first name, their usual groom, roughly when they last came in, and whether the parent is okay getting texts from you. Only what the owner actually knows — a blank is better than a guess.

After each answer, a short reflect-back. After all eight, show the drafted `business/profile.md`, `business/services.md`, `business/staff.md`, and `business/clients.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Build the due-back list from the regulars you just saved: compare each pet's last visit to the rhythm for their usual groom. If a last visit, a rhythm, or the okay to text is missing, stop and ask — never guess. A pet with no clear answer goes on a "need your call" list instead.
2. Keep only the parents the owner said are okay with texts. Anyone else stays off the list, no matter how due their pup looks.
3. Draft one short reminder text per parent using `templates/reminder-text.md` — personal, in the owner's voice, each with an easy way to say "no more texts". Show the whole batch and let the owner edit or cut any of them.
4. Save the list and the approved drafts to `reports/` and show it: "Here's your due-back list with a text ready for each one — you send them from your phone whenever you like."

The session must not end without something real in `reports/` that the owner can use today. If there are no regulars yet, the first win is the business profile plus a drafted reply to the most recent booking request the owner can paste in.

## Part 3 — switching on the rhythm

Offer the two daily helpers one at a time, and wait for an answer between them.

First:

> Want a two-minute morning brief before you start — who's coming in, coat notes, anything to prep?

If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief.md`. Then:

> And a close-out at the end of the day — adds up the day from what you tell me, so nothing nags at you overnight?

If yes, same walk-through with `schedules/end-of-day.md`. If either is a no, no pressure — they can just ask any morning or evening.

Also offer, once:

> Want me to save a short note so every future chat already knows the business? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, more regulars, suppliers).
- That they can come back anytime and just talk to you like a person, because that's what works.
