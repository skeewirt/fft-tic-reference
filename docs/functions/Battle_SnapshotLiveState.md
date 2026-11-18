# Battle_SnapshotLiveState

- **Address:** `0x140279BF4`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void Battle_SnapshotLiveState(void *work, int direction)`
- **Callers:** Battle_SaveCapture, Battle_RestoreSceneVars
- **Callees:** memmove

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Captures or restores the live save state the battle image carries: the item stores and the unit save records, copied between the live globals and a save work block in the direction the second argument selects.

## Behavior

- V: the first argument is the base of the save work block and the second is the direction: 1 copies work to live, 0 copies live to work.
- V: the largest move is a block of 0x7E90 bytes (54 records of 0x258, so the 0x258 comes from 0x7E90/54 and is not an immediate) between the work base and the live unit save table at 0x1411A7D10; it is done with memmove.
- V: the item stores follow at later work offsets: the inventory counts at 0x1411A7C00, the den stock at 0x1411A7700 and the badge flags at 0x1411A7810, each copied with its own loop.
- V: the unit save records outside the block are copied in a separate loop of 16-byte units with a tail, so the whole 600-byte record shape survives the round trip.
- V: the direction is tested in front of each sub-block, so a single call either captures the whole set or restores it.
- V: the routine is shared by the battle capture and the battle restore paths, which is why it takes a direction instead of having two bodies.
- V: direction 1 is the restore: Battle_RestoreSceneVars calls it with the snapshot buffer (a global of the caller, not addressed in this body) and 1, so a resumed battle's live unit records (g_UnitSaveData) and item stores come from the snapshot; Save_ResumeCheckpoint does not run SaveWork_UnpackToLive for a battle resume (behaviour ResumedBattleRestoresUnitRecordsWithoutUnpack).
- I: this is the live-state half of the battle image; the five memory blocks A..E are copied by the caller around it.
- ?: whether the work block is cleared before a capture; this body only moves bytes.

## State touched

- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [Battle_RestoreSceneVars](Battle_RestoreSceneVars.md), [Battle_SaveCapture](Battle_SaveCapture.md)
- Observed behaviours: [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md), [ResumedBattleRestoresUnitRecordsWithoutUnpack](../behaviors/ResumedBattleRestoresUnitRecordsWithoutUnpack.md)

## Notes

Whole function read (1182 bytes). The 0x7E90 block move and the record loop are visible in the body; the item-store offsets are the live globals the same body addresses.

## Open questions

None recorded.
