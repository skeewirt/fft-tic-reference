# CommandKindMessageOffsets

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140681208`
- **Rows:** 24 rows of 1 bytes
- **Keyed by:** battle command kind
- **Read by:** [BattleCommand_BuildMenu](../functions/BattleCommand_BuildMenu.md)
- **Row layout:** [CommandKindMessageOffset](../structs/CommandKindMessageOffset.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Offset of the screen / message code of each battle command kind (code = 0x1000 + offset). Verdict: designer-data.

## Behavior

- V: BattleCommand_BuildMenu reads byte [kind] and adds 0x1000 unless the unit is in a special state
- I: 24 bytes up to the function pointer table that follows

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
