# MoveRangeScratch

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 128 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The move-range builder's scratch block at g_MoveRangeScratch, filled by Battle_MoveRangeSetup from the unit record. Only the fields the builder's rules read are listed.

## Fields

| Offset | Field | Type | Conf | Meaning | Read by | Written by |
|---|---|---|---|---|---|---|
| <a id="jump_limit"></a>`0x2` | jump_limit | `uint8` | V | 2 * jump: the largest height difference of one step, in half-steps. | [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md) |  |
| <a id="jump"></a>`0x4` | jump | `uint8` | V | Unit +0x43 capped at 7; 31 in movement mode 0 or when unit +0x9C has bit 0x02. | [Battle_MoveRange_InitTiles](../functions/Battle_MoveRange_InitTiles.md) |  |
| <a id="horizontal_jump"></a>`0x5` | horizontal_jump | `uint8` | V | Unit +0x43 capped at 7, halved (before the 31 override): the number of tiles a jump may pass over. | [Battle_MoveRange_ExpandJump](../functions/Battle_MoveRange_ExpandJump.md) |  |
| <a id="move"></a>`0x6` | move | `uint8` | V | Unit +0x42 capped at 124; the start budget is move + 1 and the spread runs at most this many passes. |  |  |
| <a id="x"></a>`0x7` | x | `uint8` | V | Unit +0x4F. |  |  |
| <a id="y"></a>`0x8` | y | `uint8` | V | Unit +0x50. |  |  |
| <a id="layer"></a>`0x9` | layer | `uint8` | V | Unit +0x51 bit 7. |  |  |
| <a id="slot"></a>`0xD` | slot | `uint8` | V | The unit slot being built. |  |  |
| <a id="mode"></a>`0xE` | mode | `uint8` | V | Movement mode: 0 Fly (flags bit 0x04), 1 Teleport (unit +0x9D bits 0x0C), 2 float (flags 0x08 or the Float status), 3 (flags 0x20), 4 (0x80), 5 (0x40), 6 (0x10), 7 plain walking; the first that applies in this order. |  | [Battle_MoveRangeSetup](../functions/Battle_MoveRangeSetup.md) |
| <a id="flags"></a>`0x10` | flags | `uint8` | V | Unit +0x9E after the adjustments: bit 0x04 cleared for Toad / Chicken, 0x08 added by the Float status, 0x40 and 0x10 cleared when unit +0x9D has bit 0x10. |  |  |
| <a id="no_water"></a>`0x11` | no_water | `uint8` | V | 1 when unit +0x9D has bit 0x10 and the flags have none of 0x8C: water tiles are not standable at all (Battle_MoveRange_InitTiles). |  |  |
| <a id="no_depth3"></a>`0x12` | no_depth3 | `uint8` | V | Starts 1, 0 when the stored flags (+0x1C) have any of 0xD0: no stopping in depth 3. |  |  |
| <a id="no_deep"></a>`0x13` | no_deep | `uint8` | V | Starts 1, 0 when the stored flags have 0x80 or 0x40: depth 4+ is neither standable nor a stop. |  |  |
| <a id="no_water_stop"></a>`0x14` | no_water_stop | `uint8` | V | Unit +0x9D bit 0x10 when the flags have neither 0x80 nor 0x08: no stopping in any water. |  |  |
| <a id="mount_job"></a>`0x15` | mount_job | `uint8` | V | 1 when the unit's job is 94..96 and it has none of the status group 10; not read by the range rules listed here. |  |  |
| <a id="can_ride"></a>`0x16` | can_ride | `uint8` | V | 1 when unit +0x06 has bit 0x80 or 0x40, it is not Toad / Chicken and unit +0x65 bit 0x20 is clear: may stop on a mountable ally. | [Battle_MoveRange_Commit](../functions/Battle_MoveRange_Commit.md) |  |
| <a id="width"></a>`0x18` | width | `uint8` | V | Map width. | [Battle_MoveRange_OutOfBounds](../functions/Battle_MoveRange_OutOfBounds.md) |  |
| <a id="height"></a>`0x19` | height | `uint8` | V | Map height. | [Battle_MoveRange_OutOfBounds](../functions/Battle_MoveRange_OutOfBounds.md) |  |
| <a id="body"></a>`0x1B` | body | `uint8` | V | Body height in half-steps: 6; 4 as Toad / Chicken; 8 with flag 0x08 (6 as Toad / Chicken); +2 for each unit riding it. | [Battle_MoveRange_CheckMount](../functions/Battle_MoveRange_CheckMount.md), [Battle_MoveRange_CheckStep](../functions/Battle_MoveRange_CheckStep.md), [Battle_MoveRange_GapBlocked](../functions/Battle_MoveRange_GapBlocked.md) |  |
| <a id="stored_flags"></a>`0x1C` | stored_flags | `uint8` | V | Unit +0x9E as read (Toad / Chicken adjusted), with 0x80 added when it has 0x08: the water terms of Battle_MoveRange_CheckSource read it. | [Battle_MoveRange_CheckSource](../functions/Battle_MoveRange_CheckSource.md) |  |
| <a id="no_jump"></a>`0x1D` | no_jump | `uint8` | V | 1 in modes 0 and 1: Battle_MoveRange_Build skips Battle_MoveRange_ExpandJump. |  |  |
| <a id="stacked"></a>`0x22` | stacked | `uint8` | V | Unit +0x51 bit 6. |  |  |
| <a id="lava_stop"></a>`0x25` | lava_stop | `uint8` | V | 1 when unit +0x9E (as read) has 0x20 or 0x08: may stop on terrain 18. |  |  |

## Behavior

- V: the working variables of the spread follow in the same block (tile and mark pointers, the target coordinates, edge heights, headrooms, the pending byte at 0x1418827FA).
- V: the terrain costs are built next to it (g_MoveTerrainCost): the set chosen by the mode, entries 0 replaced by the weather cost (or 1 with unit +0x9D bit 0x02), every cost other than 0xFF replaced by 1 with unit +0x9D bit 0x01.

## Referenced by

- Global instances: [g_MoveRangeScratch](../globals/g_MoveRangeScratch.md)
- Observed behaviours: [MoveRangeRules](../behaviors/MoveRangeRules.md)

## Notes

Detail and evidence: the function sheets linked from this page.

## Open questions

? The second mode byte (+0x0F), the byte copied from 0x140D407B3 (+0x1A) and the copy of unit +0x9D (+0x24).
