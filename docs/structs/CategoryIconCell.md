# CategoryIconCell

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the ItemCategoryIconCells table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="tex_u"></a>`0x0` | tex_u | `uint8` | V | texture u of the category icon, written into the shop row's cell word |
| <a id="tex_v"></a>`0x1` | tex_v | `uint8` | V | texture v of the category icon |

## Referenced by

- Described by tables: [ItemCategoryIconCells](../tables/ItemCategoryIconCells.md)

## Open questions

None recorded.
