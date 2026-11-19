# NxdDataEnhancedWorldEventRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.enhanced_world_event table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int16` | ? | Not decoded. Observed in the stock rows: 0 to 43, 15 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 125 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 845, 109 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 47, 44 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 47, 43 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3240, 12 distinct values. |

## Referenced by

- Described by tables: [NxdDataEnhancedWorldEvent](../tables/NxdDataEnhancedWorldEvent.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 7 columns not decoded.
