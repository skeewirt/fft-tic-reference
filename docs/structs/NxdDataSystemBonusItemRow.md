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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0x4` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 3 distinct values, 1 empty. |
| <a id="description"></a>`0x8` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 3 distinct values, 1 empty. |
| <a id="union_id"></a>`0xC` | union_id | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 3 distinct values. |
| <a id="comment"></a>`0x14` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |

## Referenced by

- Described by tables: [NxdDataSystemBonusItem](../tables/NxdDataSystemBonusItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
