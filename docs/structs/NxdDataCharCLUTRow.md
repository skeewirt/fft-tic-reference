# NxdDataCharCLUTRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.char_clut table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="clut_data"></a>`0x8` | clut_data | `uint8[] {int32 offset; uint32 count}` | I | Clut data (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 15 distinct values. |
| <a id="chara_color_skin_id"></a>`0x10` | chara_color_skin_id | `int32` | I | Row id of CharaColorSkin (a reference by column name). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_14"></a>`0x14` | flag_14 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharCLUT](../tables/NxdDataCharCLUT.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 5 columns not decoded.
