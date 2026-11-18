# NxdDataSystemBonusSpecialItemRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.system_bonus_special_item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="union_id"></a>`0x8` | union_id | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 6 distinct values. |
| <a id="quantity"></a>`0x10` | quantity | `int32` | I | Quantity (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 1 to 10, 2 distinct values. |
| <a id="caption"></a>`0x14` | caption | `string (int32 offset)` | I | Caption text. Observed in the stock rows: 6 distinct values, 0 empty. |

## Referenced by

- Described by tables: [NxdDataSystemBonusSpecialItem](../tables/NxdDataSystemBonusSpecialItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
