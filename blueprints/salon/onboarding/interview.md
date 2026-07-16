# The first chat

This is the script for getting to know the salon. It runs the first time the owner says hello, and picks up where it left off any time after.

## How to run it

- One question at a time. Never two. Wait for the answer.
- Plain words only. Nothing technical, ever.
- Reflect back before saving: "So that's [what you heard] — did I get that right?"
- Follow the owner. If they jump ahead to what's bugging them, go there, then loop back.
- They can stop anytime. Note what's still missing (the tiers are in `onboarding/checklist.md`) and next time offer to pick up where you left off.
- Write nothing into `business/` without showing the exact lines and getting a yes.

## Opening

Say hello like a person. Then, in your own words:

> I'd love to get to know the salon — a few quick questions, one at a time, maybe twenty minutes. By the end you'll have your salon's profile saved and a ready-to-post promo for this week. And anything I ever draft, you see before it goes anywhere. Ready?

## Part 1 — the essentials

Ask these one at a time, in your own words, skipping anything the owner already said:

1. What's the salon called?
2. What kind of place is it — barbering, beauty, a bit of both?
3. If you had to describe the feel of the place in three words, what would they be?
4. What days and hours are you open?
5. How many chairs do you run?
6. What are your top services — the ones that fill your week? Take them one service at a time: what it's called, what it costs, roughly how long it takes.
   - If they have a price list: "If you've got a price list handy — a photo or a file is fine — drop it in the `assets` folder or paste it here and I'll sort it out." Structure whatever arrives into a clean service list and confirm it line by line. Messy is fine; guessing is not.
7. Who works the chairs? One person at a time: their name, what they're great at, what days they're in.
8. How do clients book today — do they call, message you, or use a booking tool?

After each answer, a short reflect-back. After all eight, show the drafted `business/profile.md`, `business/services.md`, and `business/staff.md` — the actual lines — and ask for the go-ahead to save.

## Part 2 — the first win

Right away, same session:

1. Draft a "this week at the salon" post: something true from what you just learned — a day with open chairs, a service worth showing off, a stylist worth introducing. Use `templates/promo-post.md` and the feel-words from question 3.
2. If the owner can paste tomorrow's bookings, add a one-page schedule brief: who's in which chair, where the gaps are. If they can't, skip it without fuss — the promo is the win.
3. Save what you made to `reports/` and show it: "Here's your first post, ready when you are — want changes?"

The session must not end without something real in `reports/` that the owner can use today.

## Part 3 — switching on the rhythm

Offer the two daily helpers one at a time, and wait for an answer between them.

First:

> Want a two-minute morning brief before you open — who's in, where the gaps are, anything to prep?

If yes, walk them through creating that scheduled task using the exact prompt in `schedules/morning-brief.md`. Then:

> And a close-out at the end of the day — tallies the till and tips, so nothing nags at you overnight?

If yes, same walk-through with `schedules/end-of-day.md`. If either is a no, no pressure — they can just ask any morning or evening.

Also offer, once:

> Want me to save a short note so every future chat already knows the salon? I'll show you the exact lines first.

The lines live at the end of `CLAUDE.md`, under "The short version". Show them, then save only on a yes.

## Closing

Three lines, warm:
- What got saved, and that they can change any of it by just saying so.
- What you'd love to learn next time (pull from Tier 2 of the checklist — policies, regulars, suppliers).
- That they can come back anytime and just talk to you like a person, because that's what works.
