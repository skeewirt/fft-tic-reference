# StatusProperties

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140788FE0`
- **Rows:** 40 rows of 16 bytes
- **Keyed by:** status id (bit 0..39 of the 5-byte status sets)
- **Read by:** [Ability_GetAuxRecord](../functions/Ability_GetAuxRecord.md), [sub_140274DB0](../functions/sub_140274DB0.md), [sub_140279110](../functions/sub_140279110.md), [sub_140278CF0](../functions/sub_140278CF0.md)
- **Row layout:** [StatusPropertyRow](../structs/StatusPropertyRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per status: priority, countdown, group flags, the statuses it cancels and the statuses that block it.

## Behavior

- V: statuses 24..39 have countdown slots; two readers use folded displacements inside the aux table and the kind 6 table.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

None recorded.
