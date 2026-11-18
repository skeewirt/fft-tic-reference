# MapDrawIndexListRecord

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MapDrawIndexLists table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="map_id"></a>`0x0` | map_id | `int16` | V | battle map id the record belongs to (2 .. 127; 50 maps) |
| <a id="pad"></a>`0x2` | pad | `bytes[6]` | V | zero |
| <a id="list_a"></a>`0x8` | list_a | `pointer` | V | pointer to a u16 list (0xFFFF-terminated) of indices set as bits in the bitset at 0x142FF84A0 |
| <a id="list_b"></a>`0x10` | list_b | `pointer` | V | pointer to a u16 list (0xFFFF-terminated) of indices set as bits in the bitset at 0x142FF8290 |

## Referenced by

- Described by tables: [MapDrawIndexLists](../tables/MapDrawIndexLists.md)

## Open questions

None recorded.
