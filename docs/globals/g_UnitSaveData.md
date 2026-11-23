# g_UnitSaveData

- **Kind:** global
- **Address:** `0x1411A7D10`
- **Area:** [Unit data](../areas/unit-data.md)
- **Type:** `data`
- **Points to / is a:** [UnitSaveRecord](../structs/UnitSaveRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

54 x 600 bytes; builder sub_140275C70 -> sub_140275B84 -> sub_140276758

## Referenced by

- Described by tables: [UnitSaveSlots](../tables/UnitSaveSlots.md)
- Observed behaviours: [BattleLoadWritesThePartyBackToTheSaveRecords](../behaviors/BattleLoadWritesThePartyBackToTheSaveRecords.md)
- Read by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [PartyUnit_BuildJobRecord](../functions/PartyUnit_BuildJobRecord.md), [PartyUnit_FillFromWork](../functions/PartyUnit_FillFromWork.md), [PartyUnit_ReloadEquipment](../functions/PartyUnit_ReloadEquipment.md), [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [UnitWork_BuildForSlot](../functions/UnitWork_BuildForSlot.md), [UnitWork_BuildFromGuestOrPartyRecord](../functions/UnitWork_BuildFromGuestOrPartyRecord.md), [Unit_ApplySpawnRecord](../functions/Unit_ApplySpawnRecord.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md), [sub_14032AB3C](../functions/sub_14032AB3C.md), [sub_14039651C](../functions/sub_14039651C.md)
- Written by: [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [EventScript_Run](../functions/EventScript_Run.md), [GameState_ResetParty](../functions/GameState_ResetParty.md), [Game_MainLoop](../functions/Game_MainLoop.md), [PartyUnit_WriteBackToSave](../functions/PartyUnit_WriteBackToSave.md), [sub_1402BBBCC](../functions/sub_1402BBBCC.md), [sub_1402C60E4](../functions/sub_1402C60E4.md), [sub_1403358FC](../functions/sub_1403358FC.md)

## Notes

V: the five equipment words of the 600-byte save record live at +0x0E, +0x10, +0x12 and at +0x14/+0x16 or +0x18/+0x1A (the hand pair is placed by equip category). PartyUnit_WriteBackToSave stores the party word raw; PartyUnit_FillFromWork copies the save word back and zeroes it when the full 16-bit word fails its 1..0x104 id test.

## Open questions

None recorded.
