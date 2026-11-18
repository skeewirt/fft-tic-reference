# TownMenuKind

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the TownMenuKindBySettlement table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="pad"></a>`0x0` | pad | `uint16` | I | always 0 |
| <a id="ordinal"></a>`0x2` | ordinal | `uint8` | I | running number (1..15 for the first rows), 0 or a larger id for the others |
| <a id="kind"></a>`0x3` | kind | `uint8` | V | 1 = the settlement offers the three-row town menu, 2 or 0 = no town menu items from this table |

## Referenced by

- Described by tables: [TownMenuKindBySettlement](../tables/TownMenuKindBySettlement.md)

## Open questions

None recorded.
