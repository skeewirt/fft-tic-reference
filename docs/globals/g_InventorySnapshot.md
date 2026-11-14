# g_InventorySnapshot

- **Kind:** global
- **Address:** `0x143C52740`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[261]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Inventory counts plus every item worn by a used roster entry, built by sub_140396174 (261 counts).

## Behavior

- V: read as byte_143C52740[id & 0x3FF] for ids below 261 (sub_14039684C).

## Referenced by

- Read by: [sub_14039684C](../functions/sub_14039684C.md), [sub_140396FEC](../functions/sub_140396FEC.md)
- Written by: [sub_1402C9F78](../functions/sub_1402C9F78.md), [sub_140396174](../functions/sub_140396174.md)

## Open questions

None recorded.
