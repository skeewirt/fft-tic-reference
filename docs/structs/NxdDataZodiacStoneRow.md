# NxdDataZodiacStoneRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.zodiac_stone table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="user_situation_id"></a>`0x8` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 3250 to 70004, 15 distinct values. |
| <a id="zodiac_stone_owner_timeline"></a>`0xC` | zodiac_stone_owner_timeline | `int32` | I | Zodiac stone owner timeline (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 10, 8 distinct values. |
| <a id="name"></a>`0x10` | name | `string (int32 offset)` | I | Name text. Observed in the stock rows: 13 distinct values, 0 empty. |
| <a id="summary"></a>`0x14` | summary | `string (int32 offset)` | I | Summary text. Observed in the stock rows: 13 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 27 distinct values, 0 empty. |
| <a id="icon_id1"></a>`0x1C` | icon_id1 | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 246, 14 distinct values. |
| <a id="icon_id2"></a>`0x20` | icon_id2 | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 462, 14 distinct values. |
| <a id="flag_24"></a>`0x24` | flag_24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataZodiacStone](../tables/NxdDataZodiacStone.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

1 of 10 columns not decoded.
