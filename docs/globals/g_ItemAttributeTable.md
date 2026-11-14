# g_ItemAttributeTable

- **Kind:** global
- **Address:** `0x14080FEA0`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[85][26]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The equipment attribute records: 85 rows of 26 bytes, selected by the item record attribute index. Rows hold the stat bonuses, move and jump bonuses, status bytes and elements.

## Behavior

- V: the item attribute line builder reads the five leading bonus bytes and emits one text line per non-zero value.

## Referenced by

- Described by tables: [ItemAttributes](../tables/ItemAttributes.md)
- Read by: [Item_BuildAttributeLines](../functions/Item_BuildAttributeLines.md)

## Open questions

None recorded.
