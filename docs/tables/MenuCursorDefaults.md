# MenuCursorDefaults

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408B9EE0`
- **Rows:** 31 rows of 16 bytes
- **Keyed by:** row
- **Read by:** [BattleCommand_StoreCursorRow](../functions/BattleCommand_StoreCursorRow.md)
- **Row layout:** [MenuCursorDefault](../structs/MenuCursorDefault.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Menu numbers with a pointer to the default record of each battle command menu. Verdict: designer-data.

## Behavior

- V: the cursor row store scans the first 12 rows for the current menu number
- I: 31 rows up to the per-unit cursor memory

## Notes

Our names. Tags: V reader, I count.

## Open questions

None recorded.
