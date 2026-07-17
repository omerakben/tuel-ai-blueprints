# AI adoption model for small businesses

This model adapts a technical AI-adoption ladder for nontechnical small-business owners using Claude Cowork. It preserves the useful progression from access, to assisted work, to repeatable routines, to supervised operations, to intent-led coordination. It replaces agent counts and broad autonomy with routine-level evidence and an unchanged human action boundary.

## Core decision

Adoption is measured per routine, not per company. A business may use supervised operations for a weekly summary while keeping hiring, payments, legal work, or sensitive customer matters at Readiness or outside Claude.

A routine advances only after the named owner reviews saved evidence. Claude never promotes itself, widens its access, changes permission mode, enables a schedule, or changes approval policy.

## Stage model

| Stage | Goal | Owner role | Claude role | Main bottleneck | Evidence gate |
|---|---|---|---|---|---|
| Readiness | Choose one useful, low-risk routine and define its boundary | Name the outcome, owner, sources, restricted data, stop point, and baseline | Interview, identify missing context, and prepare the first observation or draft | Trust, access, and an unclear use case | Manual permission, approved sources, action level, baseline, first checked output, and receipt |
| Assisted | Make one routine faster with close owner review | Supply facts, inspect sources and output, correct errors, and decide | Capture, triage, draft, verify, and show uncertainty one task at a time | Owner attention and source quality | Repeated reviewed runs show value, visible corrections, and no boundary breach |
| Repeatable | Turn proven work into clear recipes and handle several safely | Prioritize packets and review completed decision material | Run bounded routines, keep packets separate, verify results, and surface collisions | Review throughput and steering | Each routine has a named owner, packet boundary, sources, output, review, and failure path |
| Supervised operations | Run proven observation or drafting routines on an agreed rhythm | Set cadence, review outputs and exceptions, and make decisions | Save reports, stop on missing input, expose failure, and prepare owner decisions | Trust in the loop, current context, decision capacity, and cost | A full review period shows visible failures, no overwrite, manageable review, and acceptable value |
| Intent-led Business OS | Coordinate a proven portfolio around business outcomes | Set intent, limits, measures, priorities, and stop conditions | Coordinate the internal preparation and learning loop and recommend improvements | Selecting valuable work and keeping controls current | Ongoing portfolio evidence for value, quality, exceptions, cost, named ownership, and rollback |

## Invariant action boundary

The stages expand only A Observe and B Draft work.

C Internal write is not earned through adoption. The existing reviewed-memory workflow may make one reversible update to approved business memory only after fresh approval of that exact change. It is never scheduled.

D Consequential, E Licensed judgment, and F Destructive remain human work at every stage. Fresh approval never carries from one item, run, or stage to another.

Stage 4 closes only this internal loop:

1. Capture approved input.
2. Triage the outcome, source scope, freshness, owner, and action level.
3. Draft or observe.
4. Verify against named sources.
5. Prepare the owner-review packet.
6. Record the receipt and exceptions.
7. Propose an improvement or memory change.

The owner remains responsible for the Act step and every consequential decision.

## Work-packet isolation at Stage 2

A work packet contains one routine request, its approved sources, relevant facts and assumptions, expected output, review note, owner decisions, and receipt. Every packet has a clear name or identifier.

Do not share an approval, assumption, private record, source selection, or output across packets unless the owner deliberately adds it to both. If two packets conflict or need the same file, stop, surface the collision, and ask the owner which one proceeds.

## Advancement and regression

Use four possible recommendations for each routine:

- Stay at the current stage.
- Advance one stage after the owner reviews sufficient evidence.
- Return to the last proven stage and Manual permission.
- Retire a routine that is unsafe, low-value, too costly, or too difficult to review.

The owner records the decision. No routine skips a stage. A new or materially changed routine returns to Manual permission and the evidence gate appropriate to the change.

A boundary violation, hidden failure, stale source, unexplained output, packet collision, or unmanageable review queue prevents advancement and normally requires regression.

## Safe use-case filter

Prefer work that is frequent, evidence-based, rules-rich, reversible, easy to review, low sensitivity, and valuable even when Claude stops at a local draft.

Avoid beginning with rare, irreversible, emotionally sensitive, regulated, destructive, or externally binding decisions.

## Canonical artifacts

- `ADOPT-AI.md` explains the owner journey.
- `roles/adoption-guide.md` provides the evidence-review lens.
- `skills/find-next-ai-use-case/SKILL.md` selects one safe starting routine.
- `workflows/advance-ai-adoption.md` prepares stage recommendations.
- `schedules/monthly-ai-adoption-review.md` reviews the routine portfolio at B Draft only.
- `templates/ai-adoption-plan.md` records the portfolio and owner boundaries.
- `templates/ai-use-case-card.md` defines one routine and its packet.
- `templates/ai-value-review.md` records value and stage evidence.
- `templates/exception-brief.md` surfaces a failed or unusual run.
