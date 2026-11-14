# BattleRangeMarkRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 5 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One record of g_BattleRangeMarks, parallel to BattleTileRecord (512 records, layer 1 at +0x500).

## Fields

| Offset | Field | Type | Conf | Meaning | Written by | Read by |
|---|---|---|---|---|---|---|
| <a id="reach"></a>`0x0` | reach | `uint8` | V | Non-zero = inside the range being built (a spread value range + 1 - distance, or 1); BattleRange_FlagTargetTiles turns it into tile flag +5 bit 0x40. | [BattleRange_ClearWithin2](../functions/BattleRange_ClearWithin2.md), [BattleRange_MarkArcReach](../functions/BattleRange_MarkArcReach.md), [BattleRange_MarkAttack](../functions/BattleRange_MarkAttack.md), [BattleRange_MarkTileInBand](../functions/BattleRange_MarkTileInBand.md), [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md), [BattleRange_SpreadDiamond](../functions/BattleRange_SpreadDiamond.md) | [BattleRange_FlagTargetTiles](../functions/BattleRange_FlagTargetTiles.md) |
| <a id="frontier"></a>`0x1` | frontier | `uint8` | V | Set on tiles BattleRange_SpreadDiamond spreads from on its next pass. | [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md), [BattleRange_SpreadDiamond](../functions/BattleRange_SpreadDiamond.md) |  |

## Behavior

- V (live, 2026-11-05): with the target prompt up, the tiles with byte 0 non-zero were the yellow ones (records_battle_prompts).

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? bytes 2..4.
