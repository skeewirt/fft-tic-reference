# NxdDataShopVoiceRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.shop_voice table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="scion_labels"></a>`0x8` | scion_labels | `int32` | M | Measured over every stock row: Every value is a key of nxd.ScionLabels. Observed in the stock rows: 351448 to 357448, 122 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `float32` | ? | Not decoded. Observed in the stock rows: 0 to 1.4013e-45, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataShopVoice](../tables/NxdDataShopVoice.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 4 columns not decoded.
