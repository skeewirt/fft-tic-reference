# ErrandBlob

- **Kind:** table
- **Area:** [Errands](../areas/errands.md)
- **Storage:** Executable
- **Address:** `0x1407B7650`
- **Rows:** 1 block of 2768 bytes
- **Keyed by:** errand index 0..95 through a 15-entry header of sub-table offsets
- **Read by:** [Errand_ComputeRewards](../functions/Errand_ComputeRewards.md), [Errand_LoadRecord](../functions/Errand_LoadRecord.md), [Errand_ReactionPose](../functions/Errand_ReactionPose.md), [Errand_RollBonusLoot](../functions/Errand_RollBonusLoot.md), [Errand_ScoreParty](../functions/Errand_ScoreParty.md)
- **Row layout:** [ErrandBlobLayout](../structs/ErrandBlobLayout.md), [ErrandRecordRow](../structs/ErrandRecordRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The errand data block: 96 errand records and every table the errand scoring and rewards read. Errand_LoadRecord copies a record into the working row; the NXD Profit table supplies names.

## Behavior

- V: job columns are fixed at 22 (jobs 74..93 plus two spare).
- V: 49 / 31 / 16 stock errands use treasure pool 0 / 1 / 2.

## Notes

Our names. Tags per member and behaviour line; read statically in the decompilation of the Enhanced executable.

## Open questions

- ?: meaning of the header offsets
- ?: columns 3, 13, 14, 15, 18, 20 of the record have no reader
- ?: the 24-byte tail has no reader
