# NxdDataSystemBonusItemContentsRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.system_bonus_item_contents table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="link"></a>`0x4` | link | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 12 distinct values. |

## Referenced by

- Described by tables: [NxdDataSystemBonusItemContents](../tables/NxdDataSystemBonusItemContents.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 2 columns not decoded.
