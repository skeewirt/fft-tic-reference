# NxdDataUDSActivityRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 28 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.uds_activity table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 95, 68 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 68 distinct values. |

## Referenced by

- Described by tables: [NxdDataUDSActivity](../tables/NxdDataUDSActivity.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 5 of 5 columns not decoded.
