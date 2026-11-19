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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="check"></a>`0x8` | check | `int32` | V | Read in the code: Kind of the first check (0 = no more checks): 1 flag set, 2 flag clear, 3 counter == value, 4 <=, 5 <, 6 >=, 7 >; 8..11 counter id against value and counter id2 against value b; 12..15 scene variable id == 12..15; 16 scene variable in 12..15. Observed in the stock rows: 0 to 16, 14 distinct values. |
| <a id="check_2"></a>`0xC` | check_2 | `int32` | V | Read in the code: Kind of the second check (same codes as check; 0 = no more checks). Observed in the stock rows: 0 to 8, 2 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="link"></a>`0x14` | link | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 29 distinct values. |
| <a id="link_2"></a>`0x1C` | link_2 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 2 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="check_value"></a>`0x2C` | check_value | `int32` | V | Read in the code: Value the first check compares its counter with (kinds 3..11). Observed in the stock rows: 0 to 2040, 113 distinct values. |
| <a id="check_value_2"></a>`0x30` | check_value_2 | `int32` | V | Read in the code: Value the second check compares its counter with. Observed in the stock rows: 0 to 950, 2 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="link_3"></a>`0x38` | link_3 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 3 distinct values. |
| <a id="link_4"></a>`0x40` | link_4 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 2 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="check_value_b"></a>`0x50` | check_value_b | `int32` | V | Read in the code: Second value of the first check: the bound for the second counter (id2) in kinds 8..11. Observed in the stock rows: 0 to 2020, 13 distinct values. |
| <a id="check_value_b_2"></a>`0x54` | check_value_b_2 | `int32` | V | Read in the code: Second value of the second check (bound for its second counter). Observed in the stock rows: 0 to 1320, 2 distinct values. |
| <a id="unknown58"></a>`0x58` | unknown58 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="blocking_result"></a>`0x5C` | blocking_result | `uint8` | V | Read in the code: Result of the first check that blocks the situation: an entry makes the situation false when each of its checks returns its blocking_result (or a kind-0 check is reached); the situation holds when every entry has a check that differs. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown5d"></a>`0x5D` | unknown5d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown5e"></a>`0x5E` | unknown5e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUserSituation](../tables/NxdDataUserSituation.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 9 of 20 columns not decoded.
