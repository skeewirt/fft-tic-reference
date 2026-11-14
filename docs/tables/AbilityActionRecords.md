# AbilityActionRecords

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable
- **Rows:** 368 records of 20 bytes (ids 0..0x16F)
- **Keyed by:** ability id
- **Read by:** [AbilityAction_GetRecord](../functions/AbilityAction_GetRecord.md), [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The action record of each action ability, copied into a writable table on first use. Ids from 368 up (the passive abilities) have no action record.

## Behavior

- V: AbilityAction_GetRecord returns the working table + 20 * id and null above 0x16F.

## Open questions

None recorded.
