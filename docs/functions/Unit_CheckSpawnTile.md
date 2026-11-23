# Unit_CheckSpawnTile

- **Address:** `0x140271178`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int Unit_CheckSpawnTile(int record)`
- **Callers:** Battle_BuildRosterTeam, Battle_AddJoinedUnit, Battle_PlaceEntryUnits, Battle_RebuildUnitTable
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Answers whether battle record n may stand on its tile: 0 = yes, -1 = no.

## Behavior

- V: reads the record's tile (+0x4F, +0x50, the layer bit 7 of +0x51; the body reaches these and +0x9D / +0x9E as the absolute addresses of record 0's fields plus 512 times the record); no when it is outside the map size, when the map cell's flags or height bits refuse the unit (its +0x9D / +0x9E movement bits are tested), when the terrain kind is 18 or 28, or when a lower record whose slot byte is not 0xFF stands on the same tile and layer.

## Referenced by

- Called by: [Battle_AddJoinedUnit](Battle_AddJoinedUnit.md), [Battle_RebuildUnitTable](Battle_RebuildUnitTable.md)
- Observed behaviours: [BattleUnitTableIsSixteenEntriesPlusFiveJoiners](../behaviors/BattleUnitTableIsSixteenEntriesPlusFiveJoiners.md), [DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile](../behaviors/DeploymentCellsAreNotCheckedAgainstTheMapAndCountByTile.md)

## Notes

Named from its result; the meaning of each map flag was not read.

## Open questions

None recorded.
