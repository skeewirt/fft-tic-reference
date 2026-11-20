# SlotIndexCarriersAreBytesAndFiveBits

- **Kind:** observed behaviour
- **Scope:** engine (battle unit slot index)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [TurnList_InsertEntry](../functions/TurnList_InsertEntry.md), [TurnList_Build](../functions/TurnList_Build.md), [Battle_TurnEngine](../functions/Battle_TurnEngine.md), [Battle_PlaceEntryUnits](../functions/Battle_PlaceEntryUnits.md), [SceneUnits_SaveRestore](../functions/SceneUnits_SaveRestore.md), [Battle_RestoreSceneVars](../functions/Battle_RestoreSceneVars.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The slot index of a battle unit is carried in bytes, in five bits of the turn-order entry and in parallel 21-wide arrays, and about 300 compares near the table bound a value by 20 or 21, so the table size is not one constant.

## Behavior

- V: 259 functions reference an address inside the unit table (the start or an interior field); 6 of them (Battle_PlaceEntryUnits, sub_140272538, sub_14030DC34, Battle_TurnEngine twice, TurnList_Build) take the end address 0x1418566E0 as a loop end, and that address is also a live dword of its own, read and written by sub_140210AF0.
- M: in those functions 317 compares with the immediate 20 or 21 are followed by a conditional jump (174 'above 20', 123 'below 21', 12 equal / not equal 21, 8 other); 285 of them lie within 25 instructions of a unit-table address, a shift by 9 or a 0x200 stride. Not each one is a slot bound: the compares of g_BattleCommandBytes and g_BattleCommandBytesB with 20 (indexed by unit +0x1B0) and of g_BattleState with 0x15 are among them.
- V: a battle turn-order entry is 4 bytes in a 40-entry list; byte 0 is the slot plus the flags 0x20, 0x40 and 0x80 (TurnList_InsertEntry adds them to the slot), so the slot has five bits (0..31) and an empty entry is 0xFF.
- V: the slot byte at +1 and the index at +0x1BC of a unit record are single bytes, 0xFF meaning none.
- V: parallel arrays indexed by the record index +0x1BC: the look pool index per unit (g_UnitLookPoolIndex, 0x140822D58) and the scene slot per unit (g_UnitSceneSlotIndex, 0x140822DAC; SceneUnit_BuildFromQueueEntry refuses an index above 0x14).
- I: the battle controller holds 21 work holders of 136 bytes (an earlier reading, not re-read here).

## Open questions

? the full list of parallel arrays and which of the 21 'below 21' bounds are loops over records and which are other 21s.
