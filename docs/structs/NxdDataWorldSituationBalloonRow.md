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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="element"></a>`0x8` | element | `string (int32 offset)` | M | Measured over every stock row: The name of the interface element. Observed in the stock rows: 90 distinct values, 1 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 5 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: -266 to 189, 42 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 13, 3 distinct values. |
| <a id="unknown38"></a>`0x38` | unknown38 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown3c"></a>`0x3C` | unknown3c | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown3e"></a>`0x3E` | unknown3e | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown40"></a>`0x40` | unknown40 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown42"></a>`0x42` | unknown42 | `int16` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int16` | ? | Not decoded. Observed in the stock rows: -180 to 365, 56 distinct values. |
| <a id="unknown46"></a>`0x46` | unknown46 | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 0, 2 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `int16` | ? | Not decoded. Observed in the stock rows: -45 to 0, 2 distinct values. |
| <a id="unknown4a"></a>`0x4A` | unknown4a | `int16` | ? | Not decoded. Observed in the stock rows: -1 to 0, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataWorldSituationBalloon](../tables/NxdDataWorldSituationBalloon.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 22 of 23 columns not decoded.
