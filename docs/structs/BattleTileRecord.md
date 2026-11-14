# BattleTileRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One tile of the battle map in g_BattleTileTable: 256 records per layer, two layers (layer 1 at +0x800), index x + y * width. Only the bytes the reach and target code reads are listed.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="surface"></a>`0x0` | surface | `uint8` | V | Low 6 bits 0x3F: BattleRange_FlagTargetTiles never flags the tile (I: no surface, e.g. an unused layer-1 record). | [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md) |  |
| <a id="height"></a>`0x2` | height | `uint8` | V | Counted twice in the half-step heights of the reach rules (I: the height in whole steps; the HUD 'Height' agrees). | [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md), [BattleRange_MarkArcReach](../functions/BattleRange_MarkArcReach.md), [BattleRange_MarkTileInBand](../functions/BattleRange_MarkTileInBand.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |
| <a id="slope_depth"></a>`0x3` | slope_depth | `uint8` | V | Bits 0..4 add to the half-step height; bits 5..7 times 2 add to a target's height and only conditionally to the attacker's (Unit_GetReachHeight). I: bits 0..4 slope / half step, bits 5..7 water depth. | [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md), [BattleRange_MarkArcReach](../functions/BattleRange_MarkArcReach.md), [BattleRange_MarkTileInBand](../functions/BattleRange_MarkTileInBand.md), [Unit_GetReachHeight](../functions/Unit_GetReachHeight.md) |  |
| <a id="corners"></a>`0x4` | corners | `uint8` | V | Four 2-bit fields, one per edge (shift 0 = the +x edge, 2 = -x, 4 = -y, 6 = +y): the edge's height is 2 * height + slope * field in half-steps (the move-range builder). (corners & 5) equal to 1 or 4 marks a one-axis slope for Battle_MoveRange_InitTiles. | [Battle_MoveRange_CeilingAbove](../functions/Battle_MoveRange_CeilingAbove.md), [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md), [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md) |  |
| <a id="flags5"></a>`0x5` | flags5 | `uint8` | V | Bit 0x40 set by BattleRange_FlagTargetTiles on the targetable tiles (I: the yellow mark). Bit 0x20 = a lit Move tile, written by Battle_MoveRange_Commit (live, 2026-11-05 and the 2026-11-09 captures). Low 5 bits: the tile's thickness in height steps; its underside is 2 * (height - thickness) half-steps (Battle_MoveRange_CeilingAbove). | [Battle_MoveRange_CeilingAbove](../functions/Battle_MoveRange_CeilingAbove.md) | [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md), [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md) |
| <a id="flags6"></a>`0x6` | flags6 | `uint8` | V | Bit 0x01: BattleRange_FlagTargetTiles skips the tile; bit 0x02: BattleRange_MarkWeaponReach clears its weapon mark. Meaning ?. | [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md), [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |  |

## Behavior

- V: the reach code reads it through g_BattleTileTable + 8 * (x + y * width + 256 * layer), width and height from g_BattleMapSize.

## Referenced by

- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? bytes +1 and +7 (not read by the reach or move-range code).
