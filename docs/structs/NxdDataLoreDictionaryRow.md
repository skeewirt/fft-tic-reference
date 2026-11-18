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
| <a id="dlc_flags"></a>`0x0` | dlc_flags | `int32` | I | Downloadable-content gate bit set (0 in the stock rows). Observed in the stock rows: 0 in every row. |
| <a id="comment"></a>`0x4` | comment | `string (int32 offset)` | I | Designer comment slot. Observed in the stock rows: empty in every row. |
| <a id="sort_order1"></a>`0x8` | sort_order1 | `int32` | I | Sort order1 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="user_situation_id"></a>`0xC` | user_situation_id | `int32` | I | Row id of UserSituation (a reference by column name). Observed in the stock rows: 0 to 59900, 207 distinct values. |
| <a id="type"></a>`0x10` | type | `int32` | I | Type (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 3, 4 distinct values. |
| <a id="lore_affiliation_id"></a>`0x14` | lore_affiliation_id | `int32` | I | Row id of LoreAffiliation-en (a reference by column name). Observed in the stock rows: 0 to 23, 24 distinct values. |
| <a id="lore_name_alias_id"></a>`0x18` | lore_name_alias_id | `int32` | I | Row id of LoreNameAlias-en (a reference by column name). Observed in the stock rows: 0 in every row. |
| <a id="unk_1c"></a>`0x1C` | unk_1c | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 204, 55 distinct values. |
| <a id="unk_20"></a>`0x20` | unk_20 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 151, 47 distinct values. |
| <a id="icon_id1"></a>`0x24` | icon_id1 | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 299, 21 distinct values. |
| <a id="icon_id2"></a>`0x28` | icon_id2 | `int32` | I | Row id of Icon (a reference by column name). Observed in the stock rows: 0 to 290, 10 distinct values. |
| <a id="unk_2c"></a>`0x2C` | unk_2c | `int32` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unk_30"></a>`0x30` | unk_30 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 55125, 2 distinct values. |
| <a id="full_name_title"></a>`0x34` | full_name_title | `string (int32 offset)` | I | Full name_title text. Observed in the stock rows: 115 distinct values, 3 empty. |
| <a id="description"></a>`0x38` | description | `string (int32 offset)` | I | Description text. Observed in the stock rows: 230 distinct values, 3 empty. |
| <a id="normalized_name"></a>`0x3C` | normalized_name | `string (int32 offset)` | I | Normalized name text. Observed in the stock rows: 114 distinct values, 3 empty. |
| <a id="last_name_first_name"></a>`0x40` | last_name_first_name | `string (int32 offset)` | I | Last name_first name text. Observed in the stock rows: 111 distinct values, 3 empty. |
| <a id="unk_44"></a>`0x44` | unk_44 | `int32` | ? | Not decoded. Observed in the stock rows: 0 to 75, 75 distinct values. |
| <a id="sort_order2"></a>`0x48` | sort_order2 | `int32` | I | Sort order2 (name taken from the column; role inferred, not traced to a reader). Observed in the stock rows: 0 to 227, 108 distinct values. |
| <a id="unk_4c"></a>`0x4C` | unk_4c | `uint8` | ? | Not decoded. Observed in the stock rows: 16 to 255, 3 distinct values. |
| <a id="flag_4d"></a>`0x4D` | flag_4d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_4e"></a>`0x4E` | flag_4e | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="flag_4f"></a>`0x4F` | flag_4f | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unk_50"></a>`0x50` | unk_50 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 3, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataLoreDictionary](../tables/NxdDataLoreDictionary.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

10 of 24 columns not decoded.
