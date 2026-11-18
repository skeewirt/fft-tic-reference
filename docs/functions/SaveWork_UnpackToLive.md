# SaveWork_UnpackToLive

- **Address:** `0x14021B0E8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveWork_UnpackToLive(int arg)`
- **Callers:** SaveSlot_LoadToLive, sub_14021A030, sub_1402BB6B0, sub_1402D03D8 (tail jmp 0x1402D0444), sub_1403264A0, sub_140326EF8
- **Callees:** sub_1400B6CF8, sub_1400DF4A0, sub_1400FF76C, sub_1401009E8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reverse of SaveWork_PackFromLive: copies the save work copy into the live arrays: 54 unit records of 600 bytes into `g_UnitSaveData`, then the item and flag tables.

## Behavior

- V: 600-byte copy loops in both directions, so every byte of the unit record (including the 38 bytes the field schema calls unsaved) is persisted by the flat save.
- V: one of its callers (sub_1402D03D8) reaches it through a tail jmp at 0x1402D0444.

## Referenced by

- Called by: [SaveSlot_LoadToLive](SaveSlot_LoadToLive.md), [Save_ResumeCheckpoint](Save_ResumeCheckpoint.md), [sub_14021A030](sub_14021A030.md)
- Observed behaviours: [BattleForkDeterminism](../behaviors/BattleForkDeterminism.md), [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md), [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md), [TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences](../behaviors/TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences.md), [TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage](../behaviors/TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage.md)
- Reads tables: [UnitJobFlags](../tables/UnitJobFlags.md), [UnitSaveSlots](../tables/UnitSaveSlots.md)

## Notes

None.

## Open questions

None recorded.
