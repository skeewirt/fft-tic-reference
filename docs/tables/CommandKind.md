# CommandKind

- **Kind:** table
- **Area:** [Job data](../areas/job-data.md)
- **Storage:** Executable
- **Address:** `0x14067E010`
- **Rows:** 256 rows of 1 byte
- **Keyed by:** skillset id (0..255)
- **Read by:** [Action_SetWeaponItem](../functions/Action_SetWeaponItem.md), [BattleAction_GetRangeInfo](../functions/BattleAction_GetRangeInfo.md), [BattlePreview_BuildAction](../functions/BattlePreview_BuildAction.md), [sub_140206F90](../functions/sub_140206F90.md), [sub_140217630](../functions/sub_140217630.md), [sub_1402828E4](../functions/sub_1402828E4.md), [sub_14030B1A0](../functions/sub_14030B1A0.md), [sub_14030B4F0](../functions/sub_14030B4F0.md)
- **Held in:** [g_CommandKind](../globals/g_CommandKind.md)
- **Row layout:** [CommandKindRow](../structs/CommandKindRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The command kind of each skillset id: the battle range and action builders switch on it to decide how the skillset acts.

## Behavior

- V: indexes past the stock skillsets are zero.
- V: 11 functions read this table (cross-references in the database); the first ten are linked.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: kinds 4, 5 and 8 are not seen in the stock rows
