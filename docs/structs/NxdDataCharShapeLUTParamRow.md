# NxdDataCharShapeLUTParamRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.char_shape_lut_param table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `float32` | ? | Not decoded. Observed in the stock rows: 0.225 to 0.9, 7 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `float32` | ? | Not decoded. Observed in the stock rows: 0.175 to 2.5, 11 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_12"></a>`0x12` | unk_12 | `int16` | ? | Not decoded. Observed in the stock rows: -40 to 16, 10 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharShapeLUTParam](../tables/NxdDataCharShapeLUTParam.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

4 of 6 columns not decoded.
