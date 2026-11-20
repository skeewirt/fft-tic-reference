# NxdDataRefinedVFXCameraControlRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.refined_vfx_camera_control table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="offset_x"></a>`0x8` | offset_x | `int16` | V | Read in the code: Added to the first word (x) of each of the 21 three-word points of the effect's second point table, in both copies of it, when an effect row that names this row is loaded. Observed in the stock rows: 0 in every row. |
| <a id="offset_y"></a>`0xA` | offset_y | `int16` | V | Read in the code: Added to the second word (y) of each of the 21 points, like offset_x. |
| <a id="offset_z"></a>`0xC` | offset_z | `int16` | V | Read in the code: Added to the third word (z) of each of the 21 points, like offset_x. Observed in the stock rows: 0 in every row. |
| <a id="unknown0e"></a>`0xE` | unknown0e | `uint8` | V | Read in the code: When set, two words of the effect's camera block are set to -1 and the rest of the row is not applied; what the two words are is not established. |
| <a id="zero_x"></a>`0xF` | zero_x | `uint8` | V | Read in the code: When set, the first word (x) of each of the 21 points of the effect's first point table is set to 0, in both copies, before the offsets are added to the second table. |
| <a id="zero_y"></a>`0x10` | zero_y | `uint8` | V | Read in the code: When set, the second word (y) of each of the 21 points of the first point table is set to 0, like zero_x. Observed in the stock rows: 0 in every row. |
| <a id="zero_z"></a>`0x11` | zero_z | `uint8` | V | Read in the code: When set, the third word (z) of each of the 21 points of the first point table is set to 0, like zero_x. |
| <a id="unknown12"></a>`0x12` | unknown12 | `uint8` | V | Read in the code: No code of the game reads this column. |
| <a id="unknown13"></a>`0x13` | unknown13 | `uint8` | V | Read in the code: No code of the game reads this column. |

## Referenced by

- Described by tables: [NxdDataRefinedVFXCameraControl](../tables/NxdDataRefinedVFXCameraControl.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
