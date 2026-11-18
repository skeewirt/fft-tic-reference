# RoadPointListPointer

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the RoadPointLists table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="points"></a>`0x0` | points | `pointer` | V | pointer to the road's list: an i16 count, then one dword (point id) per way point |

## Referenced by

- Described by tables: [RoadPointLists](../tables/RoadPointLists.md)

## Open questions

None recorded.
