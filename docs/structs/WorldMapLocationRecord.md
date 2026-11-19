# WorldMapLocationRecord

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 64 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 64-byte record per world-map location that the location-list builder accepts (location ids 0..46): what is on offer there and its state at the current story progress. The location info panel is filled from it.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="errands_offered"></a>`0x0` | errands_offered | `int32` | V | Number of errands offered there (Errand_IsOffered over ids 0..95). |
| <a id="value_a"></a>`0x4` | value_a | `int32` | V | The location's entry of the first per-location array the builder fills (v88); the panel shows it as a counter. |
| <a id="value_b"></a>`0x8` | value_b | `int32` | V | The location's entry of the second per-location array (v89); the panel shows it as a counter. |
| <a id="no_open_errand"></a>`0xC` | no_open_errand | `uint8` | V | 1 when no errand record is open for the location; selects panel text 1583 or 1584 for a location without a shop. |
| <a id="category_mask"></a>`0x10` | category_mask | `uint8[35]` | V | One flag per item category (Item record byte +5) that the location's shops sell (Shop_BuildItemList kinds 1, 2, 3, 4 and 7); filled only when Town has_shop is set. The panel plays 'On' / 'Off' on 35 nodes from it. |
| <a id="progress_state"></a>`0x33` | progress_state | `uint8` | V | 3 when the location is the current WorldMapProgressInfo row's town, 2 when it is town_2, else 0. |
| <a id="location_id"></a>`0x34` | location_id | `int32` | V | The location id (Town key). |
| <a id="sort_order"></a>`0x38` | sort_order | `int32` | V | Town sort_order (+0x20); the three Locations lists are insertion-sorted by it, then by id. |
| <a id="byte_60"></a>`0x3C` | byte_60 | `uint8` | ? | Set by the builder; meaning not decoded. |
| <a id="not_marked"></a>`0x3D` | not_marked | `uint8` | V | 1 when the location is not marked. |
| <a id="poachers_den"></a>`0x3E` | poachers_den | `uint8` | V | Town poachers_den (+0x32) when event variable 144 is above 0. |

## Behavior

- V: the builder (sub_14036E5DC) pushes each record into the list for Town locations_list (+0x24): list 53 + value (values 0..2) or the separate list at +1696 for values above 2.
- I: the first array entries (+4, +8) come from per-location values filled earlier in the same function; their meaning (the panel's counters) was not followed to the source.

## Notes

Sheets: sub_14036E5DC (the builder), WorldMapLocationPanel_Fill (the reader).

## Open questions

? the value of byte +60; ? what the two per-location arrays hold.
