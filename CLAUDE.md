# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

The TUEL AI blueprint library: downloadable working folders ("blueprints") that turn Claude Desktop into an operator for one kind of small business. Everything is markdown, YAML, JSON, and two Python tools. `standard/SPEC.md` is the authority for every rule below; `standard/blueprint.schema.json` is the manifest contract.

A blueprint is an ordinary working folder — never a Claude plugin, never a Skill ZIP. A `skills/` directory inside a blueprint registers nothing; `blueprint.yaml` and `START-HERE.md` are repository conventions Claude Desktop does not auto-read. Keep the three deliverable types (working folder, Skill ZIP, plugin ZIP) strictly separate and keep the disclaimers that say so.

## Commands

- `python3 tools/lint.py` — lint all blueprints plus `templates/_blank` (add `--strict` to fail on warnings, `--json` for machine output).
- `python3 tools/lint.py --self-test` — the linter's own fixture tests. Run after any change to `tools/lint.py` or the schema.
- `python3 tools/create_blueprint.py <slug> --name "..." --business-type "..."` — scaffold a new blueprint from `templates/_blank`.

CI (`.github/workflows/lint.yml`) runs both lint commands on every push to main and every PR.

## Rules for all blueprint content

- **Draft-first is absolute.** No file may authorize sending, posting, paying, filing, signing, deleting, or deciding without a named human's fresh approval of that exact item. The full never-autonomous list is in `standard/SPEC.md` §6 and must appear in every blueprint's `CLAUDE.md` Hard rules.
- **No real or invented data.** `business/` files ship as empty, friendly stubs. The linter warns on dollar amounts, phone numbers, and email addresses in stubs — treat those warnings as failures.
- **Owner-facing text is jargon-free.** "Connector", "MCP", "schema", "API", "endpoint" are banned in `START-HERE.md`, `onboarding/`, `templates/`, `business/`, and `connectors.md`. Write "connect your Gmail". The voice bar is `docs/brand.md`; read it before writing any owner-facing prose.
- **Connections are recommendations.** Each carries a status in `blueprint.yaml` (`confirmed-official-example`, `candidate-remote-mcp`, `local-or-export-fallback`) and never claims installation, authorization, or compliance.
- **No health workflows.** Nothing clinical, no patient records; health-adjacent verticals stay admin-only and say so.
- **Versioning.** Bump a blueprint's `version` minor for material workflow changes, major for approval/safety/memory changes. Never silently change an installed owner's approval rules in an upgrade; updates never overwrite `business/`, `assets/`, or `reports/`.

## Conventions

- Blueprint layout, minimums (3 skills, 2 schedules), and the CLAUDE.md Hard-rules requirement are in `standard/SPEC.md` §3–§5. The linter enforces them — run it before considering any content change done.
- Skills end with an action-level line; schedules declare their mode and are copy-paste recipes (there is no schedule-file import).
- Git: feature branches (`feature/`, `fix/`), conventional commits, never work directly on main.
