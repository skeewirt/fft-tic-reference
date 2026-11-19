# NxdDataSystemBonusItemRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.system_bonus_item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0x4` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 3 distinct values, 1 empty. |
| <a id="description"></a>`0x8` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 3 distinct values, 1 empty. |
| <a id="link"></a>`0xC` | link | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 3 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataSystemBonusItem](../tables/NxdDataSystemBonusItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 5 columns not decoded.
