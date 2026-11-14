# Battle_MoveRange_OutOfBounds

- **Address:** `0x14027BA88`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool Battle_MoveRange_OutOfBounds(void)`
- **Callers:** Battle_MoveRange_Expand, Battle_MoveRange_ExpandJump, sub_14027D794, sub_14027D97C
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

True when the target coordinates in the scratch (two signed words) are outside the map.

## Behavior

- V: true when x or y is negative, x is not below the width (scratch byte 0x141882618) or y not below the height (scratch byte 0x141882619).

## State touched

- Reads: [MoveRangeScratch.width](../structs/MoveRangeScratch.md#width), [MoveRangeScratch.height](../structs/MoveRangeScratch.md#height)

## Referenced by

- Called by: [Battle_MoveRange_Expand](Battle_MoveRange_Expand.md), [Battle_MoveRange_ExpandJump](Battle_MoveRange_ExpandJump.md)

## Open questions

None recorded.
