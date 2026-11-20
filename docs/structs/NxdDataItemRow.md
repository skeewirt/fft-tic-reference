# NxdDataItemRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.item table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="name"></a>`0x4` | name | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="singular"></a>`0x8` | singular | `string (int32 offset)` | M | Measured over every stock row: The name in its singular form. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="plural"></a>`0xC` | plural | `string (int32 offset)` | M | Measured over every stock row: The name in its plural form. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="description"></a>`0x10` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 259 distinct values, 3 empty. |
| <a id="name_2"></a>`0x14` | name_2 | `string (int32 offset)` | M | Measured over every stock row: A second copy of the name. Observed in the stock rows: 258 distinct values, 2 empty. |
| <a id="noun_class"></a>`0x18` | noun_class | `uint8` | V | Read in the code: Grammar byte 0 of the noun record (tag record +24): the English noun tag (ennoun) selects the article entry 3 * value of UIAttributive with it (0 gives 'a ', 1 gives 'an '); the French tag uses it in the form index. Same record bytes as Ability +0x16. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="noun_number_form"></a>`0x19` | noun_number_form | `uint8` | V | Read in the code: Grammar byte 1 of the noun record (+25): read only by the French noun tag builder, where 0 / 1 / 2 pick the article form (index +3; singular or plural by count; always plural); the English tag ignores it. Observed in the stock rows: 1 in every row. |
| <a id="noun_class_2"></a>`0x1A` | noun_class_2 | `uint8` | V | Read in the code: Grammar byte 2 of the noun record (+26): gender-like class for the German and French noun tags (German: base index of the article forms, 3 = plural; French: 2 * value in the form index); also returned as a character by sub_1402B89F8 and pushed as a numeric argument of item-obtained / confirm messages. Observed in the stock rows: 0 in every row. |
| <a id="noun_prefix_flag"></a>`0x1B` | noun_prefix_flag | `uint8` | V | Read in the code: Grammar byte 3 of the noun record (+27): when non-zero the English noun tag writes the bare noun with no article (the named swords, 'nothing equipped'); the German tag drops the article too; the French tag reads it as a prefix switch. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="ui_status_effect"></a>`0x1C` | ui_status_effect | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIStatusEffect-en. Observed in the stock rows: 0 to 1002, 3 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="ui_item_category"></a>`0x24` | ui_item_category | `int32` | M | Measured over every stock row: Every value is a key of nxd.UIItemCategory-en. Observed in the stock rows: 0 to 34, 35 distinct values. |
| <a id="sort_order"></a>`0x28` | sort_order | `int32` | V | Read in the code: Order key: lists sorted by it put the smaller value first (the Throw item list; item sort field 12). Observed in the stock rows: 0 to 6106, 260 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `uint8` | V | Read in the code: Not 0: the item counts for the story condition 'item owned' (only items with this byte answer it) and its row is flagged in the sell list. 0 on every row of the game. Observed in the stock rows: 0 in every row. |
| <a id="random_icon"></a>`0x2D` | random_icon | `uint8` | V | Read in the code: Non-zero on either weapon of an attack shows the 'random' icon (IconRandom) next to the damage number in the battle action panel. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [Item](../tables/Item.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
