# MoveFind_ProbeTile

- **Address:** `0x140271D80`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `MoveFindResult *MoveFind_ProbeTile(int x, int y, int layer)`
- **Callers:** sub_140271AC0, MoveFind_TakeItem, MoveFind_ApplyTrap
- **Callees:** Battle_IsTileOccupied, SceneVar_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reports what a battle tile hides: another unit, a Move-Find item not yet taken and a trap kind.

## Behavior

- V: bit 4 of the result: a unit stands on the tile (its slot kept beside the result).
- V: matches the tile against the four hidden tiles of the live Move-Find row (x high nibble, y low nibble, layer bit 7 of the flags).
- V: bit 1: the hidden tile has an item (flag 0x20 clear) whose taken bit is still clear; the taken bits are indexed by scene variable 51 (two maps per byte, four bits per map); the common and rare item ids are copied into the result.
- V: bit 2: the hidden tile has a trap (flag 0x10 clear); flags 0x01 / 0x02 / 0x04 / 0x08 give trap kind 0 / 1 / 2 / 3.
- V: it is the only reader of the loaded Move-Find row (g_MoveFindWorkingRow) and tests exactly the bits 0x80, 0x20, 0x10 and 0x0F of each tile's flag byte; bit 0x40 is read by nothing.

## State touched

- Calls: [Battle_IsTileOccupied](Battle_IsTileOccupied.md), [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [MoveFind_ApplyTrap](MoveFind_ApplyTrap.md), [MoveFind_TakeItem](MoveFind_TakeItem.md)
- Observed behaviours: [MoveFindTakenBitsAreFourPerMapInA128ByteArray](../behaviors/MoveFindTakenBitsAreFourPerMapInA128ByteArray.md)
- Reads tables: [MoveFindItems](../tables/MoveFindItems.md)

## Open questions

None recorded.
