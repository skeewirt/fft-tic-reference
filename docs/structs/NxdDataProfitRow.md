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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="title"></a>`0x4` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown08"></a>`0x8` | unknown08 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown10"></a>`0x10` | unknown10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="profit_client_name"></a>`0x20` | profit_client_name | `int32` | M | Measured over every stock row: Every value is a key of nxd.ProfitClientName-en. Observed in the stock rows: 1 to 85, 84 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 1 to 96, 96 distinct values. |

## Referenced by

- Described by tables: [NxdDataProfit](../tables/NxdDataProfit.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 8 of 10 columns not decoded.
