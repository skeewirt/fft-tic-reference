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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="palette"></a>`0x8` | palette | `uint8[] {int32 offset; uint32 count}` | M | Measured over every stock row: The colour bytes of the set. Observed in the stock rows: 15 distinct values. |
| <a id="chara_color_skin"></a>`0x10` | chara_color_skin | `int32` | M | Measured over every stock row: Every value is a key of nxd.CharaColorSkin. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="enabled"></a>`0x14` | enabled | `uint8` | V | Read in the code: When 0 the row is skipped: its 16 colours are not written into the palette. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharCLUT](../tables/NxdDataCharCLUT.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
