# NxdDataEventCharaDrawRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.event_chara_draw table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="chara_control_id"></a>`0x4` | chara_control_id | `int32` | M | Measured over every stock row: Every value is a key of nxd.CharaControlId. Observed in the stock rows: 2 to 508, 14 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown0a"></a>`0xA` | unknown0a | `int16` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown0e"></a>`0xE` | unknown0e | `int16` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int16` | ? | Not decoded. Observed in the stock rows: -8 to 2, 7 distinct values. |
| <a id="unknown12"></a>`0x12` | unknown12 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataEventCharaDraw](../tables/NxdDataEventCharaDraw.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 8 columns not decoded.
