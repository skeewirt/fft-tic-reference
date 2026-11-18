# MoveFind_TakeItem

- **Address:** `0x140271CA8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int *MoveFind_TakeItem(BattleUnit *unit)`
- **Callers:** sub_14020435C
- **Callees:** MoveFind_ProbeTile, Rng_Percent, SceneVar_Read, Job_IsChemistType

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Gives a unit the Move-Find item of its tile: rolls common against rare by Brave and marks the tile taken.

## Behavior

- V: the rare item (+4 of the hidden tile) is taken with a chance of (100 - Brave) percent, the common one (+2) otherwise.
- V: the chance gains 25 points (capped at 100) when a mode global is set, the unit's support bit (+158 bit 0) is set and Job_IsChemistType accepts the unit.
- V: sets the tile's taken bit (scene variable 51 selects the map's four bits).

## State touched

- Calls: [MoveFind_ProbeTile](MoveFind_ProbeTile.md), [Rng_Percent](Rng_Percent.md), [SceneVar_Read](SceneVar_Read.md), [Job_IsChemistType](Job_IsChemistType.md)

## Referenced by

- Observed behaviours: [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md)
- Reads tables: [MoveFindItems](../tables/MoveFindItems.md)

## Open questions

?: which support ability the +158 bit is.
