# FastForwardStates

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable (filled at run time)
- **Address:** `0x142FCF730`
- **Rows:** 256 bytes
- **Keyed by:** battle state
- **Held in:** [g_FastForwardStateTable](../globals/g_FastForwardStateTable.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Whether fast-forward is allowed in each battle state; filled from the GameModeTypes NXD table.

## Behavior

- V: starts as all 1, then loaded from GameModeTypes (table 88) row byte +16.

## Open questions

None recorded.
