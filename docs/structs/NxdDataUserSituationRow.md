# NxdDataUserSituationRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 96 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.user_situation table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 16, 14 distinct values. |
| <a id="unknown0c"></a>`0xC` | unknown0c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 8, 2 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="link"></a>`0x14` | link | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 29 distinct values. |
| <a id="link_2"></a>`0x1C` | link_2 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 2 distinct values. |
| <a id="unknown24"></a>`0x24` | unknown24 | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2040, 113 distinct values. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 950, 2 distinct values. |
| <a id="unknown34"></a>`0x34` | unknown34 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="link_3"></a>`0x38` | link_3 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 3 distinct values. |
| <a id="link_4"></a>`0x40` | link_4 | `union {int32 kind; int32 id}` | M | Measured over every stock row: Typed references (table:row). Observed in the stock rows: 2 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `union {int32 kind; int32 id}` | ? | Not decoded. Observed in the stock rows: 1 distinct values. |
| <a id="unknown50"></a>`0x50` | unknown50 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 2020, 13 distinct values. |
| <a id="unknown54"></a>`0x54` | unknown54 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 1320, 2 distinct values. |
| <a id="unknown58"></a>`0x58` | unknown58 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown5c"></a>`0x5C` | unknown5c | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown5d"></a>`0x5D` | unknown5d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown5e"></a>`0x5E` | unknown5e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUserSituation](../tables/NxdDataUserSituation.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 16 of 20 columns not decoded.
