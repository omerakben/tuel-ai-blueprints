# Upgrading a blueprint

Blueprint 1.0 introduces TUEL Business OS v1, a stronger approval policy, and new working areas. That is a major upgrade. Do not silently replace an owner's installed folder.

Blueprint 1.1 adds routine-level AI adoption guidance. It does not change policy version 1.0.0, data-layout version 1.0.0, protected owner paths, or the draft-only unattended ceiling. It adds `ADOPT-AI.md`, an adoption guide, a business-specific use-case map, adoption records, an advancement workflow, and a monthly review recipe.

## Protected owner paths

An upgrade must not overwrite:

- `business/`
- `assets/`
- `reports/`
- `operations/`
- `inbox/`

These paths may contain approved business truth, owner files, active work, inputs, and past outputs. Copy shared capability files into a new folder or review an exact proposed diff. Keep the old folder until the owner verifies the new one.

## Safe upgrade sequence

1. Download the new blueprint into a separate folder.
2. Read its `UPGRADE.md` and compare the version fields in `blueprint.yaml`.
3. Review changes to `CLAUDE.md`, especially approval, privacy, memory, and action-level rules.
4. Copy owner data into the protected paths only after the owner confirms the destination and scope.
5. Reconnect tools with the minimum permissions needed. A prior permission is not approval for a new write.
6. Put each existing repeated job into its own adoption plan. Start changed routines in Manual mode and let the owner decide whether evidence supports Assisted, Repeatable, Supervised operations, or Intent-led Business OS.
7. Run one morning brief and one end-of-day close manually. Check sources, totals, missing inputs, and saved filenames.
8. Keep or archive the previous folder only after the owner accepts the new setup. Deletion is always an owner action.

## Version meaning

- Major: approval, safety, memory, or protected-path behavior changed.
- Minor: workflows or capabilities changed without changing the safety boundary.
- Patch: wording or content was corrected without changing behavior.

The shared sync tool updates repository-owned capability files only. It refuses to use protected owner paths as destinations.
