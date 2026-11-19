# NxdDataTownRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 52 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.town table (English text table; the other languages share the layout). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="description"></a>`0x4` | description | `string (int32 offset)` | M | Measured over every stock row: The plain word for what the column holds. Observed in the stock rows: 47 distinct values, 2 empty. |
| <a id="map_x"></a>`0x8` | map_x | `int32` | V | Read in the code: X position of the location on the world map, an integer converted to float (cvtdq2ps) for the map screen. Observed in the stock rows: 0 to 3035, 46 distinct values. |
| <a id="map_y"></a>`0xC` | map_y | `int32` | V | Read in the code: Y position of the location on the world map (i32 converted to float). Observed in the stock rows: 0 to 1942, 42 distinct values. |
| <a id="unknown10"></a>`0x10` | unknown10 | `string (int32 offset)` | ? | Not decoded. Observed in the stock rows: empty in every row. |
| <a id="place_name"></a>`0x14` | place_name | `int32` | M | Measured over every stock row: Every value is a key of nxd.PlaceName-en. Observed in the stock rows: 0 to 1470, 47 distinct values. |
| <a id="node_name"></a>`0x18` | node_name | `string (int32 offset)` | V | Read in the code: Name suffix of the location's node on the world map: the node is 'Base<suffix>' when +0x30 is set, else 'Point<suffix>'; an empty string leaves the location without a node. Observed in the stock rows: 46 distinct values, 3 empty. |
| <a id="picture"></a>`0x1C` | picture | `int32` | V | Read in the code: Number of the location's picture in the info panel: fills the Icon row 21 pattern 'base/textureparts/base_%02d_uitx' (as Gossip +0x28). Observed in the stock rows: 0 to 26, 26 distinct values. |
| <a id="sort_order"></a>`0x20` | sort_order | `int32` | V | Read in the code: Order of the location in its Locations list: each list is sorted by this value, then by location id. Observed in the stock rows: 0 to 510, 46 distinct values. |
| <a id="locations_list"></a>`0x24` | locations_list | `int32` | V | Read in the code: Which Locations list (tab) the location goes into: 0, 1 or 2 (values above 2 go to a separate list); 1 also suppresses the location info panel. Observed in the stock rows: 0 to 2, 3 distinct values. |
| <a id="user_situation"></a>`0x28` | user_situation | `int32` | M | Measured over every stock row: Every value is a key of nxd.UserSituation. Observed in the stock rows: 0 to 14600, 8 distinct values. |
| <a id="base_number"></a>`0x2C` | base_number | `int16` | V | Read in the code: Number of the location's base screen: the world map loads 'ui/ffto/worldmap/wm_base_%s.uib' (UIAddon row 137) with this number as two digits and plays the state 'TexChange%02d' on its node; location 21 uses '14_34' instead. Observed in the stock rows: -1 to 42, 25 distinct values. |
| <a id="unknown2e"></a>`0x2E` | unknown2e | `int16` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: -1 to 43, 44 distinct values. |
| <a id="base"></a>`0x30` | base | `uint8` | V | Read in the code: The location is a base (town-style node 'Base<name>' with its own wm_base screen and TexChange states) rather than a plain map point ('Point<name>'). Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="has_shop"></a>`0x31` | has_shop | `uint8` | V | Read in the code: When set, the world map builds the location's shop summary (which item categories its Outfitter stock contains) and the location info panel uses its shop layout with the 'Profit' part and 35 item-category On/Off marks; when 0 neither happens. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="poachers_den"></a>`0x32` | poachers_den | `uint8` | V | Read in the code: The settlement's town menu gets a fourth item (text 47200) once event variable 144 is non-zero; the world map location record also flags it. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown33"></a>`0x33` | unknown33 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataTown](../tables/NxdDataTown.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 17 columns not decoded.
