# NxdDataSortieConfirmRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.sortie_confirm table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="map"></a>`0x4` | map | `int32` | M | Measured over every stock row: Every value is a key of nxd.Map. Observed in the stock rows: 0 to 91, 28 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 14, 5 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: -1 in every row. |
| <a id="event_text"></a>`0x10` | event_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 1507, 3 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 3, 2 distinct values. |
| <a id="max_units_text"></a>`0x18` | max_units_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 1502, 3 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: -1 to 172, 31 distinct values. |
| <a id="threat_text"></a>`0x20` | threat_text | `int32` | M | Measured over every stock row: Every value is a line of nxd.UI. Observed in the stock rows: 0 to 1505, 4 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 48 in every row. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataSortieConfirm](../tables/NxdDataSortieConfirm.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 8 of 12 columns not decoded.
