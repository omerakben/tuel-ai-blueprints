# Changelog

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
