# ItemWeaponRecord

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 8-byte weapon sub-record of an item whose category kind is 0 or 5 (sub_1402B8C74).

## Fields

| Offset | Field | Type | Conf | Meaning | Read by |
|---|---|---|---|---|---|
| <a id="range"></a>`0x0` | range | `uint8` | V | Attack reach of the direct and arc shapes (BattleRange_MarkWeaponReach seeds the unit's tile with range + 1 in g_BattleRangeMarks); not used by the strike (reach 1) and lunge (reach 2) shapes. Stock: guns 8, crossbows 4, bows 5, harps and books 3. | [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |
| <a id="flags"></a>`0x1` | flags | `uint8` | V | Attack shape (BattleRange_MarkWeaponReach): 0x80 strike (4 adjacent tiles), else 0x40 lunge (2 tiles in straight lines), else 0x20 direct (distance 3..range, any height), else arc (bows: distance >= 3, height bonus). Bit 0x01 empties the second hand (UnitWork_ApplyStartingEquipment); bits 0x10 / 0x20 set AI record flags (sub_140316C90). I: 0x01 two-handed only, 0x04 usable two-handed (tested with the unit's +0x9A bit 0x02). | [BattleRange_MarkWeaponReach](../functions/BattleRange_MarkWeaponReach.md) |
| <a id="formula"></a>`0x2` | formula | `uint8` | I | Formula id. |  |
| <a id="byte3"></a>`0x3` | byte3 | `uint8` | ? | 0xFF in every stock row; no reader found. |  |
| <a id="power"></a>`0x4` | power | `uint8` | V | Copied to the unit's right / left hand power. |  |
| <a id="evade"></a>`0x5` | evade | `uint8` | V | Copied to the unit's right / left hand evade. |  |
| <a id="element"></a>`0x6` | element | `uint8` | I | Element bits. |  |
| <a id="inflict"></a>`0x7` | inflict | `uint8` | I | Index of a 6-byte added-effect record (128 records). |  |

## Referenced by

- Described by tables: [ItemWeaponRecords](../tables/ItemWeaponRecords.md), [ItemWeaponRecordsHigh](../tables/ItemWeaponRecordsHigh.md)
- Observed behaviours: [AttackWeaponReach](../behaviors/AttackWeaponReach.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

None recorded.
