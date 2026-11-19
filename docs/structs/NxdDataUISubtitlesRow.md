# NxdDataUISubtitlesRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 52 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_subtitles table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: text.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="subtitle"></a>`0x8` | subtitle | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 65 distinct values, 598 empty. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: -1 to 283.2, 543 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 20024, 24 distinct values. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 4, 3 distinct values. |
| <a id="scion_labels"></a>`0x18` | scion_labels | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 0 to 357479, 244 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 9, 3 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 10110, 5 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 7, 3 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1200, 22 distinct values. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUISubtitles](../tables/NxdDataUISubtitles.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 11 of 13 columns not decoded.
