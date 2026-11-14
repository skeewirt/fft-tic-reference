# g_SaveWorkCurrent

- **Kind:** global
- **Address:** `0x142C81C80`
- **Area:** [Save data](../areas/save-data.md)
- **Type:** `uint8[40164]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The live work copy of the running game, one 0x9CE4-byte slot record. The checkpoint helpers move it to and from the checkpoint block.

## Behavior

- V: one end of the checkpoint and slot-pack moves.

## Referenced by

- Read by: [sub_14021AEC0](../functions/sub_14021AEC0.md), [sub_140246014](../functions/sub_140246014.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md)
- Written by: [Save_ResumeCheckpoint](../functions/Save_ResumeCheckpoint.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md)

## Open questions

None recorded.
