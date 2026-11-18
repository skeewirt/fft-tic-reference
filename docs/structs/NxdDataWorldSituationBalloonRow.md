# NxdDataWorldSituationBalloonRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 76 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.world_situation_balloon table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="ui_name"></a>`0x8` | ui_name | `string (int32 offset)` | I | Ui name text. Observed in the stock rows: 90 distinct values, 1 empty. |
| <a id="unk_0c"></a>`0xC` | unk_0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unk_10"></a>`0x10` | unk_10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_14"></a>`0x14` | unk_14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_18"></a>`0x18` | unk_18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_24"></a>`0x24` | unk_24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_28"></a>`0x28` | unk_28 | `int32` | ? | Not decoded. Observed in the stock rows: -266 to 189, 42 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_34"></a>`0x34` | unk_34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 13, 3 distinct values. |
| <a id="unk_38"></a>`0x38` | unk_38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_3c"></a>`0x3C` | unk_3c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_3e"></a>`0x3E` | unk_3e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_40"></a>`0x40` | unk_40 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_42"></a>`0x42` | unk_42 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int16` | ? | Not decoded. Observed in the stock rows: -180 to 365, 56 distinct values. |
| <a id="unk_46"></a>`0x46` | unk_46 | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 0, 2 distinct values. |
| <a id="unk_48"></a>`0x48` | unk_48 | `int16` | ? | Not decoded. Observed in the stock rows: -45 to 0, 2 distinct values. |
| <a id="unk_4a"></a>`0x4A` | unk_4a | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 0, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataWorldSituationBalloon](../tables/NxdDataWorldSituationBalloon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

20 of 23 columns not decoded.
