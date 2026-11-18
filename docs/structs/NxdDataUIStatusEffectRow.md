# NxdDataUIStatusEffectRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 36 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_status_effect table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="type"></a>`0x8` | type | `int32` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 13, 5 distinct values. |
| <a id="name"></a>`0xC` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 42 distinct values, 4 empty. |
| <a id="caption"></a>`0x10` | caption | `string (int32 offset)` | I | Caption text. Observed in the stock rows: 36 distinct values, 10 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 66, 31 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 23, 3 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 1004, 43 distinct values. |
| <a id="unk_22"></a>`0x22` | unk_22 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIStatusEffect](../tables/NxdDataUIStatusEffect.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 10 columns not decoded.
