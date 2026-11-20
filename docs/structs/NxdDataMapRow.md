# NxdDataMapRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.map table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |
| <a id="unknown04"></a>`0x4` | unknown04 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="place_name"></a>`0x8` | place_name | `int32` | V | Read in the code: Key of a PlaceName row (table 85): the full name of the map, shown as the title in the sortie confirm window and the map-name text nodes. Observed in the stock rows: 0 to 21100, 112 distinct values. |
| <a id="place_name_2"></a>`0xC` | place_name_2 | `int32` | V | Read in the code: Key of a PlaceName row: the shorter place (settlement / area) name; when nonzero it is the text the save list shows for the map, otherwise +0x8 is used. Observed in the stock rows: 0 to 15500, 9 distinct values. |
| <a id="place_name_3"></a>`0x10` | place_name_3 | `int32` | V | Read in the code: Key of a PlaceName row: the part name (floor / section) of the area; when nonzero the save list pushes it as a second text argument with a flag 1. Observed in the stock rows: 0 to 36100, 27 distinct values. |
| <a id="variations"></a>`0x14` | variations | `struct[] {int32 offset; uint32 count}` | V | Read in the code: Offset (from the row start) of an array of 72-byte variation elements, element count in the dword at +0x18; one element is chosen per battle from scene variables, element 0 is the fallback. Observed in the stock rows: 85 distinct values. |
| <a id="title_ja_state"></a>`0x1C` | title_ja_state | `int32` | V | Read in the code: Byte flag handed to the map-title builder: nonzero lets the title label play its 'Ja' state for some languages; 0 keeps the 'En' state in every language. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataMap](../tables/NxdDataMap.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

None recorded.
