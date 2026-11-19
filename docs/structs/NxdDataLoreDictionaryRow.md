# NxdDataLoreDictionaryRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 84 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.lore_dictionary table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="sort_order_2"></a>`0x8` | sort_order_2 | `int32` | V | Read in the code: Sort key of the Lore Dictionary (Brave Story glossary) list in sort mode 2 (the first choice of the list's sort command): ascending, entries with 0 last. The default mode 1 uses +0x48 the same way, mode 3 sorts by the family-name-first string. Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="user_situation"></a>`0xC` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 59900, 207 distinct values. |
| <a id="lore_dictionary_category"></a>`0x10` | lore_dictionary_category | `int32` | M | Measured over every stock row: Values 1..3 are the keys of nxd.LoreDictionaryCategory and form three unbroken blocks of rows in key order; 0 only on the three empty header rows. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="lore_affiliation"></a>`0x14` | lore_affiliation | `int32` | M | Measured over every stock row: Every value is a key of nxd.LoreAffiliation-en. Observed in the stock rows: 0 to 23, 24 distinct values. |
| <a id="lore_name_alias"></a>`0x18` | lore_name_alias | `int32` | V | Read in the code: LoreNameAlias (table 240) key: the glossary detail shows that row's string +8 in the alias text part ('Text00' at glossary +4272) when non-zero. Observed in the stock rows: 0 in every row. |
| <a id="face"></a>`0x1C` | face | `int32` | V | Read in the code: Face number drawn in the glossary detail portrait (FaceWidget_SetFace(widget, value, 8)); 0 shows the 'Unknown' state instead. Observed in the stock rows: 0 to 204, 55 distinct values. |
| <a id="sprite_shape"></a>`0x20` | sprite_shape | `int32` | V | Read in the code: Sprite shape of the unit figure drawn in the glossary detail (SpriteRecord_Fill shape argument; palette from +0x50); 0 hides the figure. Observed in the stock rows: 0 to 151, 47 distinct values. |
| <a id="icon"></a>`0x24` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 299, 21 distinct values. |
| <a id="icon_2"></a>`0x28` | icon_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 290, 10 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 55125, 2 distinct values. |
| <a id="full_name"></a>`0x34` | full_name | `string (int32 offset)` | M | Measured over every stock row: The full name or title. Observed in the stock rows: 115 distinct values, 3 empty. |
| <a id="description"></a>`0x38` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 230 distinct values, 3 empty. |
| <a id="plain_name"></a>`0x3C` | plain_name | `string (int32 offset)` | M | Measured over every stock row: The name in a plain form. Observed in the stock rows: 114 distinct values, 3 empty. |
| <a id="family_name_first"></a>`0x40` | family_name_first | `string (int32 offset)` | M | Measured over every stock row: The name written family name first. Observed in the stock rows: 111 distinct values, 3 empty. |
| <a id="list_image"></a>`0x44` | list_image | `int32` | V | Read in the code: Frame number of the small picture on the glossary list row (part 'Image' of 'ListImage'); 0 hides the picture. Observed in the stock rows: 0 to 75, 75 distinct values. |
| <a id="sort_order"></a>`0x48` | sort_order | `int32` | V | Read in the code: Sort key of the glossary list in the default sort mode 1 (ascending, 0 last); +0x8 is the key of mode 2. Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="unknown4c"></a>`0x4C` | unknown4c | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 16 to 255, 3 distinct values. |
| <a id="sub_quest"></a>`0x4D` | sub_quest | `uint8` | V | Read in the code: When set on the entry's current page row, its list row plays the state 'SubQuest' instead of 'Default'. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="replaces_previous"></a>`0x4E` | replaces_previous | `uint8` | V | Read in the code: A row with this set is not a page of its own: once its user_situation is met it replaces the page before it (the latest such row wins); pages are counted and picked only among met rows with 0. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="clear_mark"></a>`0x4F` | clear_mark | `uint8` | V | Read in the code: When set on the entry's current row, the glossary shows the 'Clear' mark (node 'Clear' plays 'Enable', else 'Disable'), both in the list detail and in the character page. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="palette"></a>`0x50` | palette | `uint8` | V | Read in the code: Palette number of the glossary unit figure (SpriteRecord_Fill palette argument, with +0x20 as the shape). Observed in the stock rows: 0 to 3, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataLoreDictionary](../tables/NxdDataLoreDictionary.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 3 of 24 columns not decoded.
