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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="category_name1"></a>`0x4` | category_name1 | `string (int32 offset)` | I | Category name1 text. Observed in the stock rows: 12 distinct values, 0 empty. |
| <a id="category_name2"></a>`0x8` | category_name2 | `string (int32 offset)` | I | Category name2 text. Observed in the stock rows: 12 distinct values, 1 empty. |
| <a id="category_name3"></a>`0xC` | category_name3 | `string (int32 offset)` | I | Category name3 text. Observed in the stock rows: 12 distinct values, 1 empty. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 2 to 4, 3 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 13, 13 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIStatusEffectCategory](../tables/NxdDataUIStatusEffectCategory.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

2 of 6 columns not decoded.
