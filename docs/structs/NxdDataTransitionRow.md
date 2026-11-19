# NxdDataTransitionRow

- **Kind:** structure
- **Area:** [Display](../areas/display.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.transition table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 1 in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 5 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1.5, 4 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1, 3 distinct values. |

## Referenced by

- Described by tables: [NxdDataTransition](../tables/NxdDataTransition.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 5 of 5 columns not decoded.
