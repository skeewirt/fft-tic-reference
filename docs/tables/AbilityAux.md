# AbilityAux

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140787F80`
- **Rows:** 8 bytes per id, ids 0..511
- **Keyed by:** ability id (masked to 9 bits)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The per-ability auxiliary records: classic JP cost, learn percent and two flag fields, with an extra category-specific record for each id.

## Behavior

- V: record layout is u16 classic JP cost, u8 learn percent, u8 flags3, u32 flags4.
- V: ids below 0x170 are category 0 with the per-ability action record as the extra pointer; ids from 0x170 are categories 1..8 with small byte tables.

## Open questions

None recorded.
