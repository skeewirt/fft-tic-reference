# ItemShopMaskRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shop availability of one item.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="mask_hi"></a>`0x0` | mask_hi | `uint8` | V | Shops 0..7: the item is sold in shop s when (hi << 8 \| lo) & (0x8000 >> s). |
| <a id="mask_lo"></a>`0x1` | mask_lo | `uint8` | V | Shops 8..15 (shop ids below 15 are used). |

## Referenced by

- Described by tables: [ItemShopMask](../tables/ItemShopMask.md)

## Open questions

None recorded.
