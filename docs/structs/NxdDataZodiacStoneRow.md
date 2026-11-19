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
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="user_situation"></a>`0x8` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 3250 to 70004, 15 distinct values. |
| <a id="zodiac_stone_owner_timeline"></a>`0xC` | zodiac_stone_owner_timeline | `int32` | V | Read in the code: The Zodiac Stone board shows a stone as held (state 'ShowStone') when the value is 0, otherwise as not acquired ('ShowUnacquired'), and for values other than 0 and 1 it also plays the state named by ZodiacStoneOwnerTimeline (table 238) row +8 of that key (the 'Show<owner>' portrait state). Observed in the stock rows: 0 to 10, 8 distinct values. |
| <a id="name"></a>`0x10` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 13 distinct values, 0 empty. |
| <a id="summary"></a>`0x14` | summary | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 13 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 27 distinct values, 0 empty. |
| <a id="icon"></a>`0x1C` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 246, 14 distinct values. |
| <a id="icon_2"></a>`0x20` | icon_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 462, 14 distinct values. |
| <a id="clear_mark"></a>`0x24` | clear_mark | `uint8` | V | Read in the code: When set on the shown stone row, the stone detail page shows the 'Clear' mark ('Enable'), else 'Disable'. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataZodiacStone](../tables/NxdDataZodiacStone.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 10 columns not decoded.
