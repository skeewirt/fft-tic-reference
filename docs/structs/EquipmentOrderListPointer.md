# EquipmentOrderListPointer

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EquipmentOrderLists table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="list"></a>`0x0` | list | `pointer` | V | pointer to the saved order list of one equipment group (u16 item ids, 0xFFFF = empty) |

## Referenced by

- Described by tables: [EquipmentOrderListPointers](../tables/EquipmentOrderListPointers.md)

## Open questions

None recorded.
