# UnitSaveSlots

- **Kind:** table
- **Area:** [Save data](../areas/save-data.md)
- **Storage:** Executable (filled at run time)
- **Address:** `0x1411A7D10`
- **Rows:** 54 records of 600 bytes
- **Keyed by:** party save slot 0..53 (the save record index)
- **Read by:** [UnitWork_BuildFromSave](../functions/UnitWork_BuildFromSave.md), [UnitWork_CopySaveFields](../functions/UnitWork_CopySaveFields.md), [SaveWork_PackFromLive](../functions/SaveWork_PackFromLive.md), [SaveWork_UnpackToLive](../functions/SaveWork_UnpackToLive.md), [JobList_RecomputeAvailability](../functions/JobList_RecomputeAvailability.md), [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md)
- **Held in:** [g_UnitSaveData](../globals/g_UnitSaveData.md)
- **Row layout:** [UnitSaveRecord](../structs/UnitSaveRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The live unit save table: the units as the save keeps them. Filled when a save is loaded or a unit is recruited, read by the party, status and job screens, and copied whole (32,400 bytes) into the save slot at +1304 and into the battle checkpoint. A record whose byte +1 is 255 is an empty slot.

## Behavior

- V: 92 functions read or write the table (cross-references in the database); the unit builder chain is UnitWork_BuildFromSaveIndex, UnitWork_BuildFromSave, UnitWork_CopySaveFields.
- V: the table is a data object that starts all zero: its content comes from the loaded save, never from the file image.
- V: no spare byte is left for a new field; 38 bytes at the end of a record (2 + 36) are not described by the save schema.

## Notes

Our names. Row layout: UnitSaveRecord, every offset of the 108 save descriptors placed.

## Open questions

- ?: how the three bytes of each base stat are packed
