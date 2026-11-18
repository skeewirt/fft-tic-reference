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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="type"></a>`0x4` | type | `int16` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 43, 15 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int16[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 125 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 845, 109 distinct values. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 47, 44 distinct values. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 47, 43 distinct values. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 3240, 12 distinct values. |

## Referenced by

- Described by tables: [NxdDataEnhancedWorldEvent](../tables/NxdDataEnhancedWorldEvent.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

5 of 7 columns not decoded.
