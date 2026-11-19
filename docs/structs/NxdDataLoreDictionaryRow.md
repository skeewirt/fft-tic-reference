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
| <a id="unknown08"></a>`0x8` | unknown08 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="user_situation"></a>`0xC` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 59900, 207 distinct values. |
| <a id="lore_dictionary_category"></a>`0x10` | lore_dictionary_category | `int32` | M | Measured over every stock row: Values 1..3 are the keys of nxd.LoreDictionaryCategory and form three unbroken blocks of rows in key order; 0 only on the three empty header rows. Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="lore_affiliation"></a>`0x14` | lore_affiliation | `int32` | M | Measured over every stock row: Every value is a key of nxd.LoreAffiliation-en. Observed in the stock rows: 0 to 23, 24 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 204, 55 distinct values. |
| <a id="unknown20"></a>`0x20` | unknown20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 151, 47 distinct values. |
| <a id="icon"></a>`0x24` | icon | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 299, 21 distinct values. |
| <a id="icon_2"></a>`0x28` | icon_2 | `int32` | M | Measured over every stock row: Every value is a key of nxd.Icon. Observed in the stock rows: 0 to 290, 10 distinct values. |
| <a id="unknown2c"></a>`0x2C` | unknown2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown30"></a>`0x30` | unknown30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 55125, 2 distinct values. |
| <a id="full_name"></a>`0x34` | full_name | `string (int32 offset)` | M | Measured over every stock row: The full name or title. Observed in the stock rows: 115 distinct values, 3 empty. |
| <a id="description"></a>`0x38` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 230 distinct values, 3 empty. |
| <a id="plain_name"></a>`0x3C` | plain_name | `string (int32 offset)` | M | Measured over every stock row: The name in a plain form. Observed in the stock rows: 114 distinct values, 3 empty. |
| <a id="family_name_first"></a>`0x40` | family_name_first | `string (int32 offset)` | M | Measured over every stock row: The name written family name first. Observed in the stock rows: 111 distinct values, 3 empty. |
| <a id="unknown44"></a>`0x44` | unknown44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 75, 75 distinct values. |
| <a id="unknown48"></a>`0x48` | unknown48 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="unknown4c"></a>`0x4C` | unknown4c | `uint8` | ? | Not decoded. Observed in the stock rows: 16 to 255, 3 distinct values. |
| <a id="unknown4d"></a>`0x4D` | unknown4d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown4e"></a>`0x4E` | unknown4e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown4f"></a>`0x4F` | unknown4f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown50"></a>`0x50` | unknown50 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 3, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataLoreDictionary](../tables/NxdDataLoreDictionary.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 15 of 24 columns not decoded.
