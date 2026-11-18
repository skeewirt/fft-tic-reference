# AbilityActionRecords

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Address:** `0x140789620`
- **Rows:** 368 records of 20 bytes (ids 0..0x16F)
- **Keyed by:** ability id
- **Read by:** [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md)
- **Row layout:** [AbilityActionRow](../structs/AbilityActionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The action record of each action ability. At first use it is copied into a writable working table (AbilityActionWorking) and overridden column by column from the NXD override table; the working copy is what the game reads.

## Behavior

- V: AbilityAction_GetRecord returns working table + 20 * id and null above 0x16F; 39 call sites in 33 functions.
- V: the working copy and the override agree on the 47 bytes that differ from the stock table (seen live).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
