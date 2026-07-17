# Changelog

## 1.1.0 - 2026-07-17

### Added

- A readiness gate and four-stage adoption path for each routine: Assisted, Repeatable, Supervised operations, and Intent-led Business OS.
- Owner-facing adoption guides, business-specific use-case maps, adoption plans, use-case cards, value reviews, exception briefs, and an adoption-guide role.
- A playbook for finding the next useful AI job, an evidence-based advancement workflow, and a monthly adoption review recipe.
- Isolated work-packet fields so one blocked item cannot disappear into a batch or contaminate ready work.
- Manifest and linter enforcement for the routine evidence profile and adoption-map completeness.

### Changed

- New and materially changed routines now start in Manual mode and advance only through saved evidence plus an owner decision.
- Onboarding now pilots one repeated job before offering any repeating task.
- The public storefront now explains the four-step path and makes clear that owners may stay at any stage.
- Standard version is 1.1.0. Safety policy, protected data layout, and the draft-only unattended ceiling remain at 1.0.0.

### Upgrade note

This is an additive capability upgrade. Review the new adoption files and onboarding behavior, then merge capability files without overwriting `business/`, `assets/`, `reports/`, `operations/`, or `inbox/`.

## 1.0.0 - 2026-07-17

### Added

- TUEL Business OS v1 with operator and reality-checker role cards.
- A common task loop for intake, classification, drafting, verification, owner decisions, receipts, and reviewed learning.
- Structured templates for decisions, work receipts, memory proposals, incidents, operations, and weekly review.
- A local weekly operations review recipe and incident-handling workflow.
- Versioned policy, data-layout, platform-check, connection-capability, and protected-path metadata.

### Changed

- Strengthened the draft-first safety floor and added explicit handling for untrusted instructions inside email, web pages, documents, and connected tools.
- Separated current work in `operations/`, transient input in `inbox/`, durable truth in `business/`, stable references in `assets/`, and outputs in `reports/`.
- Corrected data-processing, account, scheduling, and connection claims against current official Claude documentation.
- Made generated work collision-safe and required a separate reality check before owner decisions.

### Upgrade note

This is a major upgrade because safety, approval, and workspace layout changed. Follow `docs/UPGRADING.md`. Never overwrite an installed owner's protected paths.
