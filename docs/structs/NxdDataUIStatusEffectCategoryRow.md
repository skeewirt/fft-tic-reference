# NxdDataUIStatusEffectCategoryRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_status_effect_category table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | M | Measured over every stock row: The category's name. Observed in the stock rows: 12 distinct values, 0 empty. |
| <a id="name_2"></a>`0x8` | name_2 | `string (int32 offset)` | M | Measured over every stock row: A second copy of the name. Observed in the stock rows: 12 distinct values, 1 empty. |
| <a id="name_3"></a>`0xC` | name_3 | `string (int32 offset)` | M | Measured over every stock row: A third copy of the name. Observed in the stock rows: 12 distinct values, 1 empty. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 2 to 4, 3 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 13, 13 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIStatusEffectCategory](../tables/NxdDataUIStatusEffectCategory.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 6 columns not decoded.
