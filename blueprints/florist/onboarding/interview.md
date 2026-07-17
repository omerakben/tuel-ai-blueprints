# The first chat

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script for getting to know the flower shop. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the shop — a few quick questions, one at a time. We will work at your pace. By the end of the first session you'll have your shop's profile saved, plus a reply to a real order inquiry, drafted and ready to send. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the shop called?
2. What do you sell most — wrapped bouquets, arrangements, plants, weddings and events, a mix?
3. If you had to describe the feel of the shop in three words, what would they be?
4. What days and hours are you open?
5. Is it just you, or does anyone help out? Just you? That's fine — plenty of great shops are one pair of hands. If there's a crew, take them one at a time: name, what they're great at, what days they're in.
6. What are your go-to offerings — the things people order most? Take them one at a time: what it's called, the usual price range, anything worth knowing.
   - If they have a price list: "If you've got a price list handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean list and confirm it line by line. Messy is fine; guessing is not.
7. How do orders reach you — walk-ins, calls, messages, a website?
8. Do you deliver? If so, roughly how far, and on which days?

After each answer, a short reflect-back. After all eight, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Ask for a real order inquiry: "Got an order inquiry sitting in your messages or inbox — even one from last week? Paste it in, or just tell me what they asked." If nothing is handy, ask for the last inquiry they remember, in their own words.
2. Draft the reply using `skills/draft-a-custom-order-reply/` and the shape in `templates/order-form.md`: warm, in the shop's voice, gathering whatever is missing among occasion, date, budget, and the feel. The draft confirms nothing — no delivery date, no specific stems, no final price. Those stay the owner's to give.
3. Save the reply to `reports/` and show it: "Here's your reply, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3: prove one routine before repeating it

Show the owner the two daily helpers as future options. Do not turn either one on during setup. First run the chosen routine manually and review the saved evidence against the adoption plan.

First:

> Want a two-minute morning brief before you open — what's due out today, deliveries and pickups, what to make first?

If interested, run the exact prompt in `schedules/morning-brief.md` manually. Only after reviewed runs meet the owner's success and stop signals may the owner choose to set up that exact repeating task. Then:

> And a close-out at the end of the day — tallies the till and notes what sold out, so nothing nags at you overnight?

If interested, treat `schedules/end-of-day.md` the same way: manual reviewed runs first, then an owner decision about that exact repeating task. If either is a no, leave it and move on.

Also offer, once:

> Want me to save a short note so every future chat already knows the shop? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, the regulars, suppliers, and the holidays and local dates the shop gears up for).
- That they can come back anytime and just talk to you like a person, because that's what works.
