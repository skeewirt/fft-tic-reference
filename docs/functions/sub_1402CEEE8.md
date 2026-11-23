# sub_1402CEEE8

- **Address:** `0x1402CEEE8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void sub_1402CEEE8(void)`
- **Callers:** sub_1402B8690
- **Callees:** UnitWork_BuildForSlot, SaveWork_PackFromParty, `sub_1402CD788`, memset, memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The checkpoint writer: it builds a fresh work copy of the party, stores it in the checkpoint copy, and then overwrites the checkpoint copy's unit area and many other fields with the live state, so the checkpoint holds the live records and not what the pack produced.

## Behavior

- V: takes no argument. Points the save work pointer (Src) at g_SaveWorkCurrent (0x142C81C80), fills the 0x9CE4 bytes (40,164, one slot record) with the byte -1 (all bits set), calls UnitWork_BuildForSlot(0) and SaveWork_PackFromParty(0).
- V: copies the 0x9CE4-byte work copy to g_SaveCheckpointCopy (0x142E80450) with one memmove.
- V: calls `sub_1402CD788` with section pointers inside the checkpoint block (0x142E898B0 and further addresses up to 0x142E8A12C) to store the world / campaign half; I: that is what the name of its restore twin sub_1402CD9D8 (called by sub_1402CF768) suggests.
- V: then copies many live fields into the checkpoint block by fixed offsets: scalar and 16-byte copies from the live area around 0x1411A7030..0x1411A7270 and 0x1411A7560 (two rounds of 128 bytes plus 24) to 0x142E80608..0x142E8095D.
- V: copies 0x7E90 bytes (54 unit records of 600) from g_UnitSaveData (0x1411A7D10) to 0x142E80968 with a memmove. 0x142E80968 - 0x142E80450 = 0x518, which is the unit area offset inside a slot record (arithmetic of the two addresses; the pack code writes the units at work copy + 1304, the same number, in SaveWork_PackFromLive), so this write lands exactly on the unit area of the checkpoint's slot record.
- V: copies the inventory counts (261 bytes from g_InventoryCounts) to 0x142E887F8 and the Poachers' Den stock (261 bytes from g_PoachersDenStock) to 0x142E888FD, 128 bytes from 0x1411A7680 to 0x142E88A02, 1,024 bytes (eight rounds of 128) from the event variable store behind off_1407830D8 to 0x142E88A84, a run of scalar and block copies from a run of globals in the 0x1407B2xxx range to 0x142E88E84..0x142E890CC, and the item-new flags (g_ItemNewFlags, 0x1411A7810) to 0x142E894BE.
- V: consequence for any hook on the pack step: whatever a hook on SaveWork_PackFromLive or SaveWork_PackFromParty changed in the unit area of the work copy (job bytes, spare bytes) is in the checkpoint copy only until the live-record memmove of this function overwrites it; the checkpoint copy then holds the live records. See the behaviour CheckpointCopyHoldsTheLiveUnitRecords.
- V: the one caller sub_1402B8690 calls it when event variable 508 reads 0 and the byte at +100 of g_GlobalWork is 0, and then sets the low dword of a state word (in the caller, not in this function) to 3; sub_1402B8690 has thirteen callers in the event and scene code (ClassicMenu_RunScreenStack and others). I: so the checkpoint is captured from scene-change and event paths, not on a save-menu action; the trigger of each caller was not read.
- ?: what the group copies from that 0x1407B2xxx range are (names of those globals were not studied).

## State touched

- Calls: [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [SaveWork_PackFromParty](SaveWork_PackFromParty.md)
- Reads: [g_UnitSaveData](../globals/g_UnitSaveData.md), [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_SaveWorkCurrent](../globals/g_SaveWorkCurrent.md)
- Writes: [g_SaveWorkCurrent](../globals/g_SaveWorkCurrent.md), [g_SaveCheckpointCopy](../globals/g_SaveCheckpointCopy.md)

## Referenced by

- Observed behaviours: [CheckpointCopyHoldsTheLiveUnitRecords](../behaviors/CheckpointCopyHoldsTheLiveUnitRecords.md), [TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences](../behaviors/TrackedDateCountersAreCopiedBySixteenByteMovesInFiveSequences.md), [TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage](../behaviors/TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage.md)

## Notes

Whole function read (decompiled in IDA, 2026-11-09), rewritten from scratch: the earlier sheet described item order lists of 282, 60, 76, 68, 42 and 1010 bytes and a callee `sub_140284F6C`, which this body does not contain. The restore twin is sub_1402CF768, which copies the checkpoint's unit area back to g_UnitSaveData.

## Open questions

? which caller of sub_1402B8690 fires the capture in a battle; ? the scalar groups from that 0x1407B2xxx range.
