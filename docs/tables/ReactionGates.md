# ReactionGates

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x14067F730`
- **Rows:** 32 bytes
- **Keyed by:** reaction id 422..453
- **Held in:** [g_ReactionGateTable](../globals/g_ReactionGateTable.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One byte per reaction id: the reaction executor refuses an id whose byte has 1 in its low two bits.

## Open questions

None recorded.
