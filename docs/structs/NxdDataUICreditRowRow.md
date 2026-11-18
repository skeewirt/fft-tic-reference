# NxdDataUICreditRowRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_credit_row table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="type"></a>`0x4` | type | `int32` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 39, 12 distinct values. |
| <a id="captions"></a>`0x8` | captions | `string (int32 offset)[] {int32 offset; uint32 count}` | I | Captions (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 988 distinct values. |
| <a id="icon_id"></a>`0x10` | icon_id | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUICreditRow](../tables/NxdDataUICreditRow.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 5 columns not decoded.
