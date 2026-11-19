# NxdDataProfitTypeRow

- **Kind:** structure
- **Area:** [Errands](../areas/errands.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.profit_type table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="profit_bonus_item"></a>`0x8` | profit_bonus_item | `int32` | M | Measured over every stock row: Every value is a key of nxd.ProfitBonusItem-en. Observed in the stock rows: 0 to 7, 6 distinct values. |
| <a id="profit_bonus_item_2"></a>`0xC` | profit_bonus_item_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ProfitBonusItem-en. Observed in the stock rows: 0 to 7, 6 distinct values. |
| <a id="profit_bonus_item_3"></a>`0x10` | profit_bonus_item_3 | `int32` | M | Measured over every stock row: Every value is a key of nxd.ProfitBonusItem-en. Observed in the stock rows: 0 to 7, 6 distinct values. |

## Referenced by

- Described by tables: [NxdDataProfitType](../tables/NxdDataProfitType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 5 columns not decoded.
