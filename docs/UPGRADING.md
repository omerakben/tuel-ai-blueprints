# Upgrading a blueprint

Blueprint 1.0 introduces TUEL Business OS v1, a stronger approval policy, and new working areas. That is a major upgrade. Do not silently replace an owner's installed folder.

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
6. Run one morning brief and one end-of-day close manually. Check sources, totals, missing inputs, and saved filenames.
7. Keep or archive the previous folder only after the owner accepts the new setup. Deletion is always an owner action.

## Version meaning

- Major: approval, safety, memory, or protected-path behavior changed.
- Minor: workflows or capabilities changed without changing the safety boundary.
- Patch: wording or content was corrected without changing behavior.

The shared sync tool updates repository-owned capability files only. It refuses to use protected owner paths as destinations.
