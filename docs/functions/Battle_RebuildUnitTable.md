# Battle_RebuildUnitTable

- **Address:** `0x1401F0AFC`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void Battle_RebuildUnitTable(DeploymentState *state)`
- **Callers:** sub_1401F0948
- **Callees:** UnitWork_BuildFromSaveIndex, Unit_CheckSpawnTile, Unit_ResolvePreviewShape, Unit_InitBattleStatusState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the battle records of the placed party units from their roster records.

## Behavior

- V: for each of the state's placed party indices (count +64, indices from +68; -1 skipped) it walks records 0..20 and, for a record whose slot byte equals its index and whose +2 equals the party index, rebuilds it with UnitWork_BuildFromSaveIndex, checks the tile (Unit_CheckSpawnTile), sets the shape and palette (+0x18F / +0x190), Unit_InitBattleStatusState and +0x1B5 = 1.

## State touched

- Calls: [Unit_CheckSpawnTile](Unit_CheckSpawnTile.md), [Unit_ResolvePreviewShape](Unit_ResolvePreviewShape.md), [Unit_InitBattleStatusState](Unit_InitBattleStatusState.md)

## Referenced by

- Observed behaviours: [BattleUnitTableIsSixteenEntriesPlusFiveJoiners](../behaviors/BattleUnitTableIsSixteenEntriesPlusFiveJoiners.md), [DeploymentStateLayout](../behaviors/DeploymentStateLayout.md)

## Open questions

None recorded.
