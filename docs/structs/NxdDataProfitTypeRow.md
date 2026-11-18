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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="profit_bonus_item_id1"></a>`0x8` | profit_bonus_item_id1 | `int32` | I | Row id of ProfitBonusItem-en (a reference by column name). Observed in the stock rows: 0 to 7, 6 distinct values. |
| <a id="profit_bonus_item_id2"></a>`0xC` | profit_bonus_item_id2 | `int32` | I | Row id of ProfitBonusItem-en (a reference by column name). Observed in the stock rows: 0 to 7, 6 distinct values. |
| <a id="profit_bonus_item_id3"></a>`0x10` | profit_bonus_item_id3 | `int32` | I | Row id of ProfitBonusItem-en (a reference by column name). Observed in the stock rows: 0 to 7, 6 distinct values. |

## Referenced by

- Described by tables: [NxdDataProfitType](../tables/NxdDataProfitType.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
