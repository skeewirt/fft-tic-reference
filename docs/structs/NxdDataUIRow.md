# NxdDataUIRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_text table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unk_00"></a>`0x0` | unk_00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="text"></a>`0x4` | text | `string (int32 offset)` | I | Text text. Observed in the stock rows: 1466 distinct values, 1956 empty. |

## Referenced by

- Described by tables: [NxdDataUI](../tables/NxdDataUI.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 2 columns not decoded.
