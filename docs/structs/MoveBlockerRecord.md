# MoveBlockerRecord

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 7 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One entry of g_MoveBlockers: another unit on the map as the move-range builder sees it. Built by Battle_MoveRangeSetup for every unit that is present, not Crystal, KO, Jumping or Chest, and not the acting unit (at most 16).

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="x"></a>`0x0` | x | `uint8` | V | Unit +0x4F. |  |
| <a id="y"></a>`0x1` | y | `uint8` | V | Unit +0x50. |  |
| <a id="layer"></a>`0x2` | layer | `uint8` | V | Bit 0 = unit +0x51 bit 7 (map layer); bit 7 = unit +0x51 bit 6, cleared for Toad / Chicken. |  |
| <a id="id"></a>`0x3` | id | `uint8` | V | Low 5 bits the unit slot; 0x40 = other side ((unit +0x05 XOR the acting unit's +0x1EE) & 0x30 non-zero); 0x20 = not a mount the acting unit may take (set unless the job is 94..96 with none of the status group 10 and a zero mount byte, or the unit is the acting unit's own mount); 0xFF = unused entry. | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |
| <a id="body"></a>`0x4` | body | `uint8` | V | 6 half-steps, 4 as Toad / Chicken, +2 when ridden by a unit other than the acting one. |  |
| <a id="base"></a>`0x5` | base | `uint8` | V | Half-step height of its feet: tile height * 2 + slope, plus the water terms (floating: 2 * depth + 2, or 2 on dry land; unit +0x9E bit 0x80: 2 * depth; bit 0x40: 2 * depth - 2). |  |
| <a id="top"></a>`0x6` | top | `uint8` | V | base + body. |  |

## Behavior

- V: a unit whose mount byte (+0x1B4) has bit 7 and names the acting unit is not entered; the acting unit's body grows by 2 instead.
- V: status group 10 (the masks 0x60, 0x85, 0x0E, 0x00, 0x20 over unit +0x61..+0x65, built by Status_BuildFlagMasks): Crystal, KO, Stone, Vampire, Chest, Berserk, Chicken, Toad, Charmed.

## Referenced by

- Global instances: [g_MoveBlockers](../globals/g_MoveBlockers.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? What unit +0x51 bit 6 and the mount byte's bit 6 stand for (I: riding / ridden pairs).
