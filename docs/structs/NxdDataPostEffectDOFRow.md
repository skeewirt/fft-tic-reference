# NxdDataPostEffectDOFRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.post_effect_dof table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="unk_08"></a>`0x8` | unk_08 | `float32` | ? | Not decoded. Observed in the stock rows: -100 to 0.157, 21 distinct values. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `float32` | ? | Not decoded. Observed in the stock rows: -0.03 to 0.175, 26 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 18 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 23 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 100, 11 distinct values. |

## Referenced by

- Described by tables: [NxdDataPostEffectDOF](../tables/NxdDataPostEffectDOF.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 7 columns not decoded.
