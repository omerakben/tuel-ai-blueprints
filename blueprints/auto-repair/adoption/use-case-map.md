# Your AI adoption map

This map helps an auto repair shop add Claude work at a pace the owner can trust. Maturity belongs to each routine, not to the whole shop. You may stay at any stage with any routine for as long as you want.

No stage authorizes Claude to send, post, pay, order parts, approve repairs, promise a completion time, delete, or change an outside system. Use Manual mode for every new or changed routine until you review it again and approve its exact sources, output, and limits.

Only the owner may advance, pause, move back, resume, or retire a routine.

## Step 0. Readiness

Name the owner, choose one repeated job, and identify the current work order, technician note, estimate, or parts record Claude may read. Define the local draft you want and what should stop the work. Start with a customer status update or repair estimate. Stop if the vehicle facts, authorization, safety finding, or responsible owner are unclear.

## 1. Assisted

Work beside Claude on one real customer status update using `skills/draft-a-customer-status-update/`, or one estimate using `skills/draft-a-repair-estimate/`.

- Provide the current work order and technician notes.
- Check every repair, part, amount, date, and promised next step.
- Review the draft and receipt before you contact the customer yourself.

Move only this routine forward when you have seen enough accurate work to trust its pattern.

## 2. Repeatable

Run a small manual batch of status updates, repair approval requests, estimates, or invoice reminders.

- Keep one draft and one review result per vehicle.
- Let a missing authorization or disputed fact block only that item.
- Review the final drafts and owner decisions together.

## 3. Supervised operations

Turn one proven reports-only routine into a schedule. Start with the morning brief, end-of-day close, or parts status review.

Confirm the source records, run time, expected report, and pause conditions first. Every customer message, repair approval, order, and payment remains your action.

## 4. Intent-led Business OS

Ask Claude to show which bays, parts, estimates, or customer updates need your attention. Review one exception brief that names the evidence and next decision.

Claude may surface stalled work, missing parts status, aging estimates, or drafts waiting for review. It never diagnoses a vehicle, authorizes work, orders parts, or contacts anyone.

## Safe next uses

- Draft review replies from a specific review.
- Prepare invoice reminders from a current owner-confirmed list.
- Summarize the weekly bay plan and flag missing inputs.

## Stop or defer

- Pause if work-order status, parts information, authorization, or shop policy is stale or disputed.
- Defer safety judgments, repair authorization, customer promises, ordering, payment, refunds, access changes, and deletion.
- Return any routine to an earlier stage whenever you want more hands-on review.
