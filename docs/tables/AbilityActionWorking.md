# AbilityActionWorking

- **Kind:** table
- **Area:** [Ability data](../areas/ability-data.md)
- **Storage:** Executable (filled at run time)
- **Address:** `0x14078B2E0`
- **Rows:** 368 records of 20 bytes
- **Keyed by:** ability id
- **Read by:** [AbilityAction_BuildWorkingCopy](../functions/AbilityAction_BuildWorkingCopy.md), [AbilityAction_GetRecord](../functions/AbilityAction_GetRecord.md)
- **Row layout:** [AbilityActionRow](../structs/AbilityActionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Working copy of AbilityActionRecords built at first use and read by every action builder.

## Behavior

- V: written at run time (three code sites).

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
