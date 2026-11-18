# SpriteLookAttributeRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One look attribute row.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="frame_kind"></a>`0x0` | frame_kind | `uint8` | V | Frame file kind (0 to 4, 6 or 7 in the stock rows); 5 and up loads that row of the frame file table in load pass 0. |
| <a id="sequence_kind"></a>`0x1` | sequence_kind | `uint8` | V | Animation sequence file kind (0 to 7); 5 and up loads that row of the sequence file table in load pass 1. |
| <a id="pose_remap"></a>`0x2` | pose_remap | `uint8` | V | Pose remap flag (0 or 1): the slot request draws pose 6 as 12 and 7 as 13. |
| <a id="scale_byte"></a>`0x3` | scale_byte | `uint8` | I | Four values in the stock rows (0 and three others); halved and scaled by the renderer factor at +0x240D0 in two frame setup functions. What it measures is not named. |

## Referenced by

- Described by tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Open questions

None recorded.
