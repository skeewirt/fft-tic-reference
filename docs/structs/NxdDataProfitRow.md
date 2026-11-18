# NxdDataProfitRow

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.profit table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0x4` | title | `string (int32 offset)` | I | Title text. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_08"></a>`0x8` | unk_08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_10"></a>`0x10` | unk_10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_14"></a>`0x14` | unk_14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_18"></a>`0x18` | unk_18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="profit_client_name_id"></a>`0x20` | profit_client_name_id | `int32` | I | Row id of ProfitClientName-en (a reference by column name). Observed in the stock rows: 1 to 85, 84 distinct values. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 96, 96 distinct values. |

## Referenced by

- Described by tables: [NxdDataProfit](../tables/NxdDataProfit.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

7 of 10 columns not decoded.
