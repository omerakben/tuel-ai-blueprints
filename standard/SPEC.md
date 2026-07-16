# TUEL Blueprint Standard

Version 0.1.0 · Platform claims verified against Anthropic documentation on 2026-07-16. Re-verify before packaging or selling anything.

This document defines what a TUEL blueprint is, the files it must contain, the safety rules it must enforce, and the checks `tools/lint.py` runs. Every blueprint in `blueprints/` conforms to this standard. Blueprints may make these rules stricter for their business type; they may never weaken them.

## 1. What a blueprint is

A blueprint is a downloadable business folder for one kind of business. The owner downloads it, opens it in Claude Desktop, and Claude runs their operational work from the files inside — always drafting first, never acting externally without the owner's fresh approval.

A blueprint is an **ordinary working folder**. Three deliverable types exist in the Claude ecosystem and they never blur:

| Type | What it is | What registers |
|---|---|---|
| Working-folder ZIP | Business context, instructions, playbooks, templates, memory stubs | Nothing. Claude reads the files as context. |
| Skill ZIP | One narrow workflow with `SKILL.md` at its root, packaged and validated separately | A Skill, after separate packaging |
| Plugin ZIP | Registered skills, commands, sub-agents, hooks per Anthropic's plugin structure | Plugin components, after separate security and distribution review |

A TUEL blueprint is the first type. A `skills/` directory inside a blueprint registers nothing with Claude Desktop — it is a library of playbooks Claude reads as ordinary files. A blueprint may graduate into Skill or plugin packaging later; that is a separate product with its own validation, labels, and version numbers. Never imply one package type automatically registers as another.

**Naming disclaimer.** `START-HERE.md`, `blueprint.yaml`, `CLAUDE.md`, and the directory names in this standard are TUEL conventions. Anthropic does not document an auto-discovered entrypoint for an ordinary folder, and a Markdown file is not automatically saved Project instructions. Owner-facing text must reflect this: the owner opens `START-HERE.md` and says hello; the blueprint never claims Claude Desktop auto-loads anything.

## 2. Vocabulary

Use these exact terms everywhere.

| Term | Meaning |
|---|---|
| Blueprint | A downloadable business folder for one kind of business (e.g. `salon`). |
| Onboarding Agent | The in-folder interview flow that learns the owner's business. |
| Operating Agent | The in-folder instructions (`CLAUDE.md`) that run the business day to day. |
| Business memory | Plain-markdown files the owner owns: profile, services, staff, clients, policies. |
| Assets | Files the owner uploads: logo, photos, price list, brand docs. |
| Skill | A focused, reusable playbook Claude runs (e.g. `fill-the-chair`). A folder convention, not a registered Skill. |
| Schedule | A copy-pasteable prompt the owner sets to run on a timer (morning brief, end-of-day close). There is no schedule-file import; the files are recipes. |
| Capability vs. workspace | Shipped, versioned capability (skills, workflows, schedules, templates) stays separate from owner-owned data (business memory, assets, reports). Updates never overwrite the owner's data. |

## 3. Layout

```
<blueprint-slug>/
├── START-HERE.md            # The one file the owner opens first. Warm, about 6 lines.
├── blueprint.yaml           # Manifest. Validated against standard/blueprint.schema.json.
├── CLAUDE.md                # Operating Agent instructions. Must contain a Hard rules section.
├── onboarding/
│   ├── interview.md         # The interview script the Onboarding Agent runs on first open.
│   └── checklist.md         # Facts and assets to collect, in priority tiers.
├── business/                # BUSINESS MEMORY. Owner-owned. Ships as empty, friendly stubs.
│   └── profile.md services.md staff.md clients.md suppliers.md policies.md brand.md
├── assets/                  # Owner uploads. Ships with a README only.
├── skills/<slug>/SKILL.md   # At least 3 real playbooks the business needs.
├── workflows/<slug>.md      # Multi-step procedures referenced by skills and schedules.
├── schedules/<slug>.md      # At least 2 timed prompts (morning brief + end-of-day minimum).
├── templates/<slug>.md      # Owner-facing output formats (posts, texts, replies, reports).
├── reports/                 # Generated outputs. Starts empty.
└── connectors.md            # Which connections help, each with a plain-English why. All optional.
```

`blueprint.yaml` is a repository convention. Claude Desktop does not read it. It exists so `tools/lint.py`, the catalog, and packaging can verify the folder. Required and optional fields are defined in `standard/blueprint.schema.json`.

## 4. The Onboarding Agent

`onboarding/interview.md` is the heart of the product. Requirements:

- One question at a time. Never two things at once. No jargon — the words "connector", "MCP", "schema", "API" are banned from every owner-facing file; write "connect your Gmail".
- Progressive. Tier 1 facts first (name, what you do, hours, top services and prices), enough for a first win; deepen in later sessions. The owner can stop anytime and resume; the agent tracks what is still missing in `business/`.
- Absorbs assets. Invite, never require, uploads. A messy pasted price list gets structured into `business/services.md` and confirmed.
- Confirms, never assumes. Reflect back what was heard before saving. Never overwrite the owner's words silently.
- Ends on a win. The first session ends with a tangible deliverable saved to `reports/`.
- Sets up autonomy. Finishes by helping the owner turn on the morning brief and end-of-day schedules, in plain language.

`onboarding/checklist.md` lists facts and assets in three tiers: Tier 1 = needed for the first win, Tier 2 = makes it good, Tier 3 = nice to have.

## 5. The Operating Agent

Each blueprint's `CLAUDE.md` defines how Claude runs the business between check-ins. It must contain:

- **Role.** A competent operator and chief of staff for this specific business.
- **A "Hard rules" section** (the linter checks for the heading) containing at minimum:
  - Never send anything external — post, text, email, review reply — without showing a draft first.
  - Never invent facts, prices, or numbers. If it is not in `business/`, `assets/`, or something the owner just said, ask.
  - Never overwrite the owner's data silently — append or confirm.
  - Money, refunds, and client-facing commitments always require explicit owner approval.
  - The never-autonomous list in §6, in full.
- **Operating loop.** Read `business/` (the source of truth) → do the work → write deliverables to `reports/`, durable facts to `business/` only through the approval gate in §7.
- **Coverage.** The four operational pillars, scoped to the business type: marketing, money, customers/operations, admin.
- **Voice.** Plain, warm, owner-facing. Lead with what needs the owner's decision.

In Claude Desktop Projects, the owner (guided by onboarding) pastes the operating instructions into Project instructions; the file itself is not auto-applied. The blueprint text must ask approval before changing saved instructions.

## 6. Safety rules

These are absolute. A blueprint may add stricter rules for its domain; it may not relax these.

**Draft-first.** No blueprint text may authorize sending, posting, paying, filing, signing, deleting, or deciding without a named human's fresh approval. Fresh approval means the exact action, destination, content, and consequences were shown and the accountable owner approved during the relevant task. A past approval for a similar action is not reused. Silence is not approval.

**Never autonomous** — no schedule, skill, or workflow may perform these unattended:

- Payments, bank transfers, refunds, payroll release, financing commitments, or tax filing.
- Hiring, ranking, rejection, promotion, compensation, discipline, benefit, leave, or termination decisions.
- Legal advice, contract execution, court filing, privilege waiver, or final regulatory interpretation.
- Diagnosis, treatment, crisis assessment, medication guidance, clinical documentation, or safety-to-work decisions.
- Safety shutdowns, emergency commands, or regulatory incident classifications.
- Credit, insurance, eligibility, or public-company materiality decisions.
- Public posting, mass communication, or binding customer promises.
- Credential changes, access grants, production mutations, or penetration testing.
- Destruction of records, evidence, legal-hold material, or approved memory.
- Silent changes to role authority, approval rules, data classification, retention, or escalation policy.

**Action levels.** Every skill, workflow, and schedule declares its maximum action level:

| Level | Scope | Boundary |
|---|---|---|
| A Observe | Read approved sources, classify, summarize, calculate, flag | Source links, confidence, timestamps |
| B Draft | Create local drafts, checklists, recommendations | Draft or review queue only; no external action |
| C Internal write | Update a non-sensitive tracker or reviewed record | Prior authorization, reversible, named owner |
| D Consequential | Send, publish, pay, refund, file, sign, commit | Fresh approval for that exact action |
| E Licensed judgment | Legal, tax, clinical, credit, safety decisions | Qualified human decides; Claude prepares evidence only |
| F Destructive | Delete, credentials, permissions, irreversible edits | Explicit scope, backup, rollback, human execution |

**Data rules.** `business/` is the owner's sensitive data: local, owner-owned, never shipped back upstream. Client lists, pricing, and staff data are confidential — least privilege, no general chat memory. Credentials, bank data, government IDs, payroll detail, health records, and privileged legal material are restricted — they never belong in a blueprint folder. No blueprint ships with real or invented customer or financial data; business memory ships as empty, friendly stubs.

**No health workflows.** Claude Cowork is not available in HIPAA-ready Enterprise configurations. Blueprints must not be marketed or configured for PHI or clinical workflows. Beauty and wellness content stays nonclinical: no diagnosis, treatment, or medication guidance.

**Disclaimers.** Every blueprint is an operational aid, not professional advice or a compliance certification. It does not make a business tax, legal, employment, or safety compliant.

## 7. Business memory and the promotion gate

Daily work produces observations, not business truth. The Operating Agent writes day-to-day outputs to `reports/`. A fact becomes durable business memory in `business/` only after the owner reviews it. A proposed learning carries: the statement, its evidence, confidence, a named owner, an effective date, and a review date. The owner approves, edits, or rejects; only approved learning is written. Claude never silently changes approval authority, retention rules, safety boundaries, or professional-review requirements.

## 8. Schedules

Two automation modes exist, and every schedule file declares which it uses:

1. **Remote, read-only.** Recurring summaries and briefs from account files or approved read-only connections.
2. **Local, with Desktop open.** Routines that read or write the blueprint folder; they run only while Claude Desktop and the folder are available.

There is no schedule-file import. Each `schedules/<slug>.md` is a recipe: what the schedule does, its mode, its action level, and the exact prompt the owner copies when creating the scheduled task. Never schedule unattended sends, posts, payments, refunds, filings, decisions, record deletion, or security changes.

## 9. Connectors

`connectors.md` recommends connections in plain language — what to connect and why an owner would want it, jargon-free. Rules:

- Every recommendation is labeled internally (in `blueprint.yaml`): `confirmed-official-example`, `candidate-remote-mcp`, or `local-or-export-fallback`.
- A recommendation never claims installation, authorization, security review, or compliance approval. Availability must be checked at setup.
- Default to read-only. Write-capable connections require per-task approval.
- Adoption order: prove value with no connections first, from a sample or export; add one read-only connection for the highest-value workflow; add write access only when reversible value justifies it.
- Every blueprint must deliver its first win with zero connections. Where a connection is missing, the fallback says exactly which report to export.

## 10. Versioning and upgrades

- `version` in `blueprint.yaml` is semantic. Bump minor for material workflow or skill changes, major for changes to approval rules, safety boundaries, or memory layout.
- Never silently change an installed owner's approval or retention policy in an upgrade. Policy changes ship as a proposed diff the owner reviews.
- Updates replace capability files (skills, workflows, schedules, templates, CLAUDE.md); they never overwrite `business/`, `assets/`, or `reports/`.

## 11. What the linter enforces

`tools/lint.py` (stdlib + PyYAML) checks every blueprint:

- `START-HERE.md`, `blueprint.yaml`, `CLAUDE.md`, `onboarding/interview.md`, `onboarding/checklist.md` exist and are non-empty.
- `blueprint.yaml` validates against `standard/blueprint.schema.json`; `slug` matches the directory name.
- `CLAUDE.md` has a Hard rules section and names `business/` as the source of truth.
- At least 3 skills and 2 schedules exist; every manifest entry has a matching file and every file a manifest entry.
- `assets/README.md` and `reports/` exist.
- Warnings: possible data in `business/` stubs; platform jargon in owner-facing files.

Run `python tools/lint.py` locally; CI runs it on every push to main and every pull request.
