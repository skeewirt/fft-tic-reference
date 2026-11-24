# Party_RebuildFromBattleEntry

- **Address:** `0x1402841D0`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t Party_RebuildFromBattleEntry(int entry)`
- **Callers:** GameState_ResetParty, MenuCtl_Entry52
- **Callees:** EventThread_Yield, TextKind25_LoadPool, Battle_GetEntryBlock, memset, Unit_BuildFromRecord, UnitWork_StoreToSaveSlot, sub_1402F3A04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Replaces the whole party roster with the units of a battle entry: every roster record is emptied, then up to 16 units are built from the entry's unit rows.

## Behavior

- V: stores the entry number in the low dword of g_BattleEntrySource, waits (EventThread_Yield) until TextKind25_LoadPool succeeds and reads the entry block (Battle_GetEntryBlock); with no block it returns.
- V: writes 0xFF to byte +1 of all 54 save records (g_UnitSaveData, 600 bytes each): every roster slot becomes empty.
- V: walks 16 rows of 40 bytes; for each row whose first byte is nonzero it fills a cleared 512-byte work unit (+1 word = -224, +437 = 1, +444 = 0xFF), builds it from the row (Unit_BuildFromRecord) and stores it to the roster (UnitWork_StoreToSaveSlot(unit, 0)); g_CurrentSpawnEntry points at each row in turn.
- V: ends with sub_1402F3A04(the second qword of g_BattleEntrySource).
- V (caller's call site, 0x140284545): GameState_ResetParty calls it with entry 254 (0xFE) when its mode argument is 2; MenuCtl_Entry52 calls it with the number of the party loader (below 512).

## State touched

- Calls: [EventThread_Yield](EventThread_Yield.md), [TextKind25_LoadPool](TextKind25_LoadPool.md), [Battle_GetEntryBlock](Battle_GetEntryBlock.md), [Unit_BuildFromRecord](Unit_BuildFromRecord.md), [UnitWork_StoreToSaveSlot](UnitWork_StoreToSaveSlot.md)
- Reads: [g_BattleEntrySource](../globals/g_BattleEntrySource.md)
- Writes: [g_BattleEntrySource](../globals/g_BattleEntrySource.md), [g_UnitSaveData](../globals/g_UnitSaveData.md), [g_CurrentSpawnEntry](../globals/g_CurrentSpawnEntry.md)

## Referenced by

- Called by: [MenuCtl_Entry52](MenuCtl_Entry52.md)

## Open questions

None recorded.
