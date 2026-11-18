# MoveFindRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 24 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MoveFindItems table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="tile_xy[0]"></a>`0x0` | tile_xy[0] | `uint8` | V | hidden tile 0: x << 4 \| y (repeats every 6 bytes for tiles 1..3 at +6, +12, +18) |
| <a id="flags[0]"></a>`0x1` | flags[0] | `uint8` | V | bit 7 = height layer; 0x01 trap kind 0, 0x02 kind 1, 0x04 kind 2, 0x08 kind 3; 0x10 = no trap; 0x20 = no item |
| <a id="common_item[0]"></a>`0x2` | common_item[0] | `int16` | V | item id found with probability Brave % |
| <a id="rare_item[0]"></a>`0x4` | rare_item[0] | `int16` | V | item id found with probability (100 - Brave) % (+25 points under one support condition, capped at 100) |

## Referenced by

- Described by tables: [MoveFindItems](../tables/MoveFindItems.md)

## Open questions

None recorded.
