# UnitWork_StoreToSaveSlot

- **Address:** `0x140274EB8`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int UnitWork_StoreToSaveSlot(UnitWork *c, int keep)`
- **Callers:** 6 (recruit and battle-end paths)
- **Callees:** sub_1402751D0, sub_14002630C, Party_CountMasteredJobs, Job_IdToIndex(161), Job_GetJpForLevel

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes a work record back into a save record: the unit's slot (a new slot for a recruit), job, flags, equipment and the per-job arrays. Returns the save slot or -1.

## Behavior

- V: chooses the save slot (`sub_1402751D0`); a guest slot 50..53 can be freed first.
- V: copies job (+3 -> A +2), marker, flags, the unlock mask (3 bytes), learned bits (66), levels (12), JP (46) and total JP (46) with a memcpy-style helper.
- V: then sets total JP of job index 21 to Job_GetJpForLevel(21, mastered jobs + 1) and its level nibble (the Onion-Knight-like rule) and clears C +286.

## State touched

- Calls: [Party_CountMasteredJobs](Party_CountMasteredJobs.md), [Job_IdToIndex](Job_IdToIndex.md), [Job_GetJpForLevel](Job_GetJpForLevel.md)

## Referenced by

- Called by: [sub_1402C60E4](sub_1402C60E4.md)

## Notes

V: c +2 (the save index) is only read, never written, so after the call it still says where the unit came from.

## Open questions

None recorded.
