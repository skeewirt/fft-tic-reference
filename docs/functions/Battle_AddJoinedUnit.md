# Battle_AddJoinedUnit

- **Address:** `0x140270FBC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Battle_AddJoinedUnit(uint8_t *spawn)`
- **Callers:** Battle_JoinUnitAndLoad
- **Callees:** UnitWork_BuildFromSaveIndex, Unit_CheckSpawnTile, Unit_ResolvePreviewShape, LookQueue_Add, Unit_InitBattleStatusState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds a battle unit record for a party unit that enters the battle (a deployment placement or a mid-battle join) in the first free record of 16..20.

## Behavior

- V: looks for the first record from 16 to 20 whose slot byte (+1) is 0xFF (record +0x1BC is set to the index on the way); when none is free and g_BattleState is 83 it looks in 0..15; otherwise it returns -1 without adding a unit.
- V: for the record found: +1 = the record index, +0x1B5 = 1, UnitWork_BuildFromSaveIndex(record, spawn[0]); then the tile from spawn[1] / spawn[2] and the layer and facing bits of spawn[3] into +0x4F..+0x51.
- V: when Unit_CheckSpawnTile accepts the tile: the shape and palette (Unit_ResolvePreviewShape) into +0x18F / +0x190, the event-unit byte +401 (the marker when it is 1..3, else 120), the look queue count cleared and the look queued (LookQueue_Add), Unit_InitBattleStatusState.
- V: always returns -1 (the caller does not use the value).
- V (seen live): five deployment placements took records 16, 17, 18, 19 and 20 in order.

## State touched

- Calls: [Unit_CheckSpawnTile](Unit_CheckSpawnTile.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [LookQueue_Add](LookQueue_Add.md), [Unit_InitBattleStatusState](Unit_InitBattleStatusState.md)

## Referenced by

- Called by: [Battle_JoinUnitAndLoad](Battle_JoinUnitAndLoad.md)
- Observed behaviours: [BattleUnitTableIsSixteenEntriesPlusFiveJoiners](../behaviors/BattleUnitTableIsSixteenEntriesPlusFiveJoiners.md)

## Open questions

None recorded.
