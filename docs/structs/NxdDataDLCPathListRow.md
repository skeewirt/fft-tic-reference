# NxdDataDLCPathListRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.dlc_path_list table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="path"></a>`0x4` | path | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 1 distinct values, 0 empty. |
| <a id="group"></a>`0x8` | group | `int32` | V | Read in the code: Group number: a SystemBonusEntitlement row takes the paths of every row whose group equals its dlc_path_group. Observed in the stock rows: 1 in every row. |

## Referenced by

- Described by tables: [NxdDataDLCPathList](../tables/NxdDataDLCPathList.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 3 columns not decoded.
