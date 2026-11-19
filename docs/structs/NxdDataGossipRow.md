# NxdDataGossipRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.gossip table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2, 2 distinct values. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 90, 3 distinct values. |
| <a id="title"></a>`0xC` | title | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="text"></a>`0x10` | text | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 23 distinct values, 0 empty. |
| <a id="unknown14"></a>`0x14` | unknown14 | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32[] {int32 offset; uint32 count}` | ? | Not decoded. Observed in the stock rows: 3 distinct values. |
| <a id="user_situation"></a>`0x24` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 3510, 4 distinct values. |
| <a id="unknown28"></a>`0x28` | unknown28 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 26, 3 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataGossip](../tables/NxdDataGossip.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 7 of 10 columns not decoded.
