# NxdDataPostEffectGlareRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.post_effect_glare table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 14 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 15 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 4 distinct values. |

## Referenced by

- Described by tables: [NxdDataPostEffectGlare](../tables/NxdDataPostEffectGlare.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 6 of 6 columns not decoded.
