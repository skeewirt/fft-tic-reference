# NxdDataPoachItemRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 56 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.poach_item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="name"></a>`0x8` | name | `string (int32 offset)` | V | Read in the code: The poach item's display name (title case): the name used by the poacher list rows and by the noun tags when no count is given. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="singular"></a>`0xC` | singular | `string (int32 offset)` | V | Read in the code: Lower-case singular form of the noun, used for a count of 1 by the noun tags; PoachTable_GetRowById also returns it. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="plural"></a>`0x10` | plural | `string (int32 offset)` | V | Read in the code: Plural form of the noun, used for a count of 2 or more by the noun tags. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="sort_name"></a>`0x14` | sort_name | `string (int32 offset)` | V | Read in the code: String compared by the poach list's two alphabetical sorters (ties fall back to the id). Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="description"></a>`0x18` | description | `string (int32 offset)` | V | Read in the code: Description text of the poach item, shown in the poacher's tip window. Observed in the stock rows: 96 distinct values, 0 empty. |
| <a id="noun_class"></a>`0x1C` | noun_class | `uint8` | V | Read in the code: Grammar byte 0 of the noun record (+24; English: 0 'a ', 1 'an '); same record bytes as Item +0x18 and Ability +0x16. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="noun_number_form"></a>`0x1D` | noun_number_form | `uint8` | V | Read in the code: Grammar byte 1 (noun record +25, see Item +0x19): read only by the French noun tag builder. Observed in the stock rows: 1 in every row. |
| <a id="noun_class_2"></a>`0x1E` | noun_class_2 | `uint8` | V | Read in the code: Grammar byte 2 (noun record +26, see Item +0x1A): gender-like class of the noun for the German and French tags. Observed in the stock rows: 0 in every row. |
| <a id="noun_prefix_flag"></a>`0x1F` | noun_prefix_flag | `uint8` | V | Read in the code: Grammar byte 3 (noun record +27, see Item +0x1B): bare noun without article when non-zero (English tag). Observed in the stock rows: 0 in every row. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="price"></a>`0x24` | price | `int32` | V | Read in the code: Price of the item in the poacher shop list (shown greyed when gil is below it). Observed in the stock rows: 5 to 30000, 38 distinct values. |
| <a id="sell_price"></a>`0x28` | sell_price | `int32` | V | Read in the code: Sell price per item in the poacher sell list; when a poach finds 99 already held, half of it is paid in gil instead. Observed in the stock rows: 3 to 15000, 38 distinct values. |
| <a id="item"></a>`0x2C` | item | `int32` | V | Read in the code: Key of the Item table (V): the poacher list entry for this carcass takes its item id from here, draws that item's cell and counts the item's equipped and held numbers. I: this is the item the poacher gives for the carcass. Observed in the stock rows: 4 to 253, 82 distinct values. |
| <a id="icon"></a>`0x30` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 1 to 48, 48 distinct values. |
| <a id="rare"></a>`0x34` | rare | `uint8` | V | Read in the code: Non-zero marks a rare poach: the monster icon plays 'Rare' (else 'Normal') and the job-tree style icon uses icon 504 instead of 503. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="sort_order"></a>`0x35` | sort_order | `uint8` | V | Read in the code: Sort key (byte) of the poach list: rows with the larger value come first; rows with equal values keep the order of their ids. Observed in the stock rows: 1 to 98, 96 distinct values. |
| <a id="notice_mark"></a>`0x36` | notice_mark | `uint8` | V | Read in the code: Non-zero puts the poach row's label in the 'notice' form (text 2099 with a notice icon instead of 2098) and picks the other possession-index values of ItemList_GetPossessionIndex. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [PoachItem](../tables/PoachItem.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
