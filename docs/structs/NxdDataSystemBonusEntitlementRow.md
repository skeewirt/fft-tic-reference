# NxdDataSystemBonusEntitlementRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.system_bonus_entitlement table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="entitlement"></a>`0x8` | entitlement | `string (int32 offset)` | V | Read in the code: The entitlement code: each code gets an entry (16 characters) in the application's entitlement list; sub_1401006F4 answers 'owned' for a row by matching this code. Observed in the stock rows: 4 distinct values, 28 empty. |
| <a id="dlc_path_group"></a>`0xC` | dlc_path_group | `int32` | V | Read in the code: Group number of the bonus content's files: every DLCPathList row whose group equals it gives one path of the entitlement's file list; 0 = no files. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataSystemBonusEntitlement](../tables/NxdDataSystemBonusEntitlement.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 5 columns not decoded.
