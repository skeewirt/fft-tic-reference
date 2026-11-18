# NxdDataUserSituationRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 96 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.user_situation table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="check_type1"></a>`0x8` | check_type1 | `int32` | I | Check type1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 16, 14 distinct values. |
| <a id="check_type2"></a>`0xC` | check_type2 | `int32` | I | Check type2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 8, 2 distinct values. |
| <a id="check_type3"></a>`0x10` | check_type3 | `int32` | I | Check type3 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="check1_index1"></a>`0x14` | check1_index1 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 29 distinct values. |
| <a id="check2_index1"></a>`0x1C` | check2_index1 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 2 distinct values. |
| <a id="check3_index1"></a>`0x24` | check3_index1 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 1 distinct values. |
| <a id="check1_check_value1"></a>`0x2C` | check1_check_value1 | `int32` | I | Check1_check value1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 2040, 113 distinct values. |
| <a id="check2_check_value1"></a>`0x30` | check2_check_value1 | `int32` | I | Check2_check value1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 950, 2 distinct values. |
| <a id="check3_check_value1"></a>`0x34` | check3_check_value1 | `int32` | I | Check3_check value1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="check1_index2"></a>`0x38` | check1_index2 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 3 distinct values. |
| <a id="check2_index2"></a>`0x40` | check2_index2 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 2 distinct values. |
| <a id="check3_index2"></a>`0x48` | check3_index2 | `union {int32 kind; int32 id}` | I | Typed reference: a table kind and a row id in that table. Observed in the stock rows: 1 distinct values. |
| <a id="check1_check_value2"></a>`0x50` | check1_check_value2 | `int32` | I | Check1_check value2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 2020, 13 distinct values. |
| <a id="check2_check_value2"></a>`0x54` | check2_check_value2 | `int32` | I | Check2_check value2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1320, 2 distinct values. |
| <a id="check3_check_value2"></a>`0x58` | check3_check_value2 | `int32` | I | Check3_check value2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="check1_is_true_for_success"></a>`0x5C` | check1_is_true_for_success | `uint8` | I | Check1_is true for success (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="check2_is_true_for_success"></a>`0x5D` | check2_is_true_for_success | `uint8` | I | Check2_is true for success (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |
| <a id="check3_is_true_for_success"></a>`0x5E` | check3_is_true_for_success | `uint8` | I | Check3_is true for success (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUserSituation](../tables/NxdDataUserSituation.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
