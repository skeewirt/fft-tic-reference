# PartyUnit_FillFromWork

- **Address:** `0x140284A08`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `int PartyUnit_FillFromWork(uint8_t *work, int16_t *party, const uint8_t *save)`
- **Callers:** sub_140284F6C, PartyUnit_WriteBackToSave (sub_140285744), sub_140286FEC, PartyUnit_BuildFromRecord, PartyUnit_ReloadEquipment
- **Callees:** Unit_BuildJobUnlockMask, Job_IsHiddenFromTree, sub_140275980, Item_IsValidId, sub_1401E8B7C, sub_140284998, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the 640-byte party record B from a work record C and the save record A. B is the record the status and job screens read, including the job unlock mask they test.

## Behavior

- V: zeroes all 640 bytes of B first.
- V: scalar fields: B+0 = min(A+29, 99), B+8 = min(A+28, 99), B+10 = C+2, B+34 = C+2, B+36 (word) = A+2 (job id), B+112 = A+4 (flags), B+114 = A+0 (marker), B+115 = dword C+82, B+119 = C+86; several stat words come from C+50..C+78 with caps of 999 or 100; B+62 is a flag set when byte C+18 falls in a fixed range.
- V: unlock mask: if Job_IsHiddenFromTree(C+3) is true, or that B+62 flag is set, B+120..122 are copied from the stored mask C+159..161; otherwise the mask is recomputed with Unit_BuildJobUnlockMask(levels C+228, flags C+6 & 0xC0, learned bits C+162, story stage C+500) and stored at B+120 (high), +121, +122 (low).
- V: block copies from A: A+50 -> B+123 (66 bytes, learned bits, ending in a word at B+187 from A+114); A+116 -> B+189 (12 bytes, job levels); A+128 -> B+202 (46 bytes, current JP); A+174 -> B+248 (46 bytes, second JP array).
- I: a 264-byte tail of A starting at A+294 is copied to B+376 by a three-iteration block loop (read from the decompiled pointer arithmetic).
- V: after the copies the first 20 words of the JP arrays at B+202 and B+248 are clamped to 9999.
- V: a 64-byte block derived from A+220 (via sub_1401E8B7C, keyed by dword A+560) is stored at B+294; B+358 = C+398, B+359 = A+286, B+364 = dword C+152.
- V: finally B+64 (word) = sub_140284998 result computed from the words at B+84.

## State touched

- Calls: [Unit_BuildJobUnlockMask](Unit_BuildJobUnlockMask.md), [Job_IsHiddenFromTree](Job_IsHiddenFromTree.md), [Item_IsValidId](Item_IsValidId.md)
- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [PartyUnit_ReloadEquipment](PartyUnit_ReloadEquipment.md), [PartyUnit_WriteBackToSave](PartyUnit_WriteBackToSave.md), [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md)
- Observed behaviours: [CombatSetJobBytesAreOnlyCopied](../behaviors/CombatSetJobBytesAreOnlyCopied.md), [JobArraysInThePartyRecordHoldStockIndicesOnly](../behaviors/JobArraysInThePartyRecordHoldStockIndicesOnly.md), [JobChangeReachesTheSaveRecordOnlyThroughWriteBack](../behaviors/JobChangeReachesTheSaveRecordOnlyThroughWriteBack.md), [PartyJobWordIsSixteenBits](../behaviors/PartyJobWordIsSixteenBits.md), [PartyWriteBackCopiesSecondarySetAndReactionLowByteInOneLoop](../behaviors/PartyWriteBackCopiesSecondarySetAndReactionLowByteInOneLoop.md), [WarriorsGuildCandidatesAreMadeEachVisit](../behaviors/WarriorsGuildCandidatesAreMadeEachVisit.md)

## Notes

V: copies the work record's equipment words to record B +0x54..+0x5C (0x140284C19-0x140284C51) and zeroes each word whose full 16-bit value fails sub_1402B8EBC (0x140284C59-0x140284C62).

## Open questions

Final B+64 value (sub_140284998) and the purpose of the 264-byte tail copy.
