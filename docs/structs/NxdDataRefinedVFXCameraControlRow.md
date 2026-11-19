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
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | V | Read in the code: Two 16-bit offsets (+8 x, +0xA y) added to the x / y words of the 21 effect points in the two tables of qword_1411A3860 (+5518.. and +5982..). Observed in the stock rows: 327680 in every row. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | V | Read in the code: +0xC (16 bits) is the z offset added like offset_x; the bytes +0xE / +0xF are flags: +0xE sets two words (+5812, +6276) to -1 instead of applying offsets, +0xF zeroes the x words of the tables at +5392.. / +5856.. first. Observed in the stock rows: 0 in every row. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | V | Read in the code: Byte +0x10 zeroes the y words (and byte +0x11 the z words) of the tables at +5392.. / +5856.. before the offsets are added. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataRefinedVFXCameraControl](../tables/NxdDataRefinedVFXCameraControl.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
