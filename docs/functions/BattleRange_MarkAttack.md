# BattleRange_MarkAttack

- **Address:** `0x14027FD2C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int BattleRange_MarkAttack(const uint8 request[20])`
- **Callers:** BattleRange_MarkRing
- **Callees:** sub_14002630C, BattleRange_MarkWeaponReach, BattleRange_FlagTargetTiles

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the target tiles of the Attack command (and of command kind 10): clears the range-mark array, marks the weapon's reach of the acting unit, removes the unit's own tile and flags the targetable tiles in the tile table.

## Behavior

- V: copies the 20-byte request (memcpy sub_14002630C); its byte 0 is the unit slot, the unit record is g_BattleUnitTable + 512 * slot.
- V: zeroes bytes 0 and 1 of all 512 range-mark records (g_BattleRangeMarks, both layers).
- V: calls BattleRange_MarkWeaponReach with the unit record.
- V: then zeroes byte 0 of the unit's own tile in both layers (index x + y * width and the same + 256, x = unit +0x4F, y = unit +0x50): the own tile is never a target of Attack.
- V: returns BattleRange_FlagTargetTiles (the number of targetable tiles).
- V: BattleRange_MarkRing calls it for command kinds 8 and 10 (g_CommandKind of the request's command byte).
- I: kind 8 is the Attack command (Action_BuildCurrentAction reads the per-unit weapon record for kind 8) and kind 10 Charge (its power table g_AbilityKind4); not checked against a command id table.

## State touched

- Calls: [BattleRange_MarkWeaponReach](BattleRange_MarkWeaponReach.md), [BattleRange_FlagTargetTiles](BattleRange_FlagTargetTiles.md)
- Reads: [g_BattleUnitTable](../globals/g_BattleUnitTable.md), [g_BattleMapSize](../globals/g_BattleMapSize.md)
- Writes: [g_BattleRangeMarks](../globals/g_BattleRangeMarks.md), [BattleRangeMarkRecord.reach](../structs/BattleRangeMarkRecord.md#reach)

## Referenced by

- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Open questions

None recorded.
