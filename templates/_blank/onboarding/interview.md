# Your first chat: getting to know {{NAME}}

<!-- TUEL:SETUP-CONTROLS:START -->
## Keep setup resumable

Before the first question, read the full `CLAUDE.md` and `ADOPT-AI.md`. Ask for the named decision owner, local time zone, usual working days, sources the owner allows, and how long changing exports should be kept. Show the proposed notes before saving them to `operations/setup-status.md`.

Ask which repeated job costs the owner time, how it works today, how often it happens, what a useful result looks like, and what mistake or missing input should stop the work. Draft one use-case card and adoption plan in `reports/`. Keep the routine in Manual mode at Assisted. Do not offer a repeating task until reviewed runs show useful results and the owner chooses to advance that exact routine.

Treat proposed `business/` text as a memory proposal. Use `workflows/review-business-memory.md` for every write to approved business memory, and write only after the named owner freshly approves the exact proposed change.

After each confirmed answer, update the setup status with what is complete, what is still missing, and the next single question. Never put passwords, payment details, government IDs, health records, or private legal material into the setup record.
<!-- TUEL:SETUP-CONTROLS:END -->

This is the script Claude follows the first time you say hello. You do not need to read it — just open this folder in Claude Desktop and start talking. Claude, the rest of this file is for you.

## How to run this interview

- One question at a time. Never bundle two questions into one message.
- Plain words only. If the owner would need to look something up, rewrite the question.
- Confirm before saving. Read back what you heard in your own words, get a yes, then write it to the right business/ file.
- Never overwrite the owner's words silently. If something changes, show the change first.
- The owner can stop anytime. Keep a short list of what is still missing so the next chat picks up exactly where this one stopped.

## Part 1 — the basics

Work through these in order, one at a time. This is enough for a first win.

1. "What's the name of your business?" → business/profile.md
2. "In one or two sentences, what do you do?" → business/profile.md
3. "What are your opening hours?" → business/profile.md
4. "What are your top services, and what do you charge for each?" → business/services.md
   - Invite the owner to paste a price list instead, even a messy one. Tidy it up, show your version, and confirm before saving.
5. TODO: add one or two Part 1 questions specific to a {{BUSINESS_TYPE}} — the facts Claude cannot work a single day without.

## Part 2 — deeper, when the owner has time

These can wait for a second or third chat. Same rules: one at a time, confirm before saving.

- Who works here, and which days each person is in → business/staff.md
- What each person is great at → business/staff.md
- Your regulars and what they like → business/clients.md
- Your cancellation rules and deposit rules, plus any hard limits → business/policies.md
- Who supplies what, and how often you reorder → business/suppliers.md
- How you like to sound, and your colors and logo → business/brand.md
- TODO: add the deeper questions that fit a {{BUSINESS_TYPE}}, working from onboarding/checklist.md.

## End on a win

Before the first chat ends, make something real. Offer a choice and let the owner pick, for example:

- a one-page plan for the week ahead
- a draft note to bring quiet clients back in
- TODO: add a first-win option that fits a {{BUSINESS_TYPE}}.

Make it, show the draft, take corrections, and save the approved version to reports/. Then say plainly: this is the kind of thing Claude can do every day from now on.

## Prove one routine before repeating it

After the first draft, create an adoption plan using `templates/ai-adoption-plan.md`. Run the chosen routine manually and review the evidence. Offer a repeating task only after reviewed runs meet the owner's success and stop signals and the owner chooses to advance that exact routine. A routine may stay Assisted for as long as the owner wants.

## If the owner stops early

No problem at all. Save what was confirmed, note what is still open, and end warmly. Next time, pick up exactly where you left off — no repeated questions.
