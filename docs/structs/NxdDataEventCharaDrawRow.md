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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="chara_control_id"></a>`0x4` | chara_control_id | `int32` | I | Chara control id (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 2 to 508, 14 distinct values. |
| <a id="unk_08"></a>`0x8` | unk_08 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_0a"></a>`0xA` | unk_0a | `int16` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_0e"></a>`0xE` | unk_0e | `int16` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int16` | ? | Not decoded. Observed in the stock rows: -8 to 2, 7 distinct values. |
| <a id="unk_12"></a>`0x12` | unk_12 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataEventCharaDraw](../tables/NxdDataEventCharaDraw.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

6 of 8 columns not decoded.
