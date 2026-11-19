# NxdDataCharaZodiacStoneCLUTRow

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.chara_zodiac_stone_clut table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="palette"></a>`0x8` | palette | `uint8[] {int32 offset; uint32 count}` | M | Measured over every stock row: The colour bytes of the set. Observed in the stock rows: 16 distinct values. |

## Referenced by

- Described by tables: [NxdDataCharaZodiacStoneCLUT](../tables/NxdDataCharaZodiacStoneCLUT.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 3 columns not decoded.
