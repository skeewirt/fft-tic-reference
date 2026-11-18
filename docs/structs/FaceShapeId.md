# FaceShapeId

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the FaceSlotShapeIds table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="shape"></a>`0x0` | shape | `uint32` | V | sprite shape number of the face with this slot number (below 0x52) |

## Referenced by

- Described by tables: [FaceSlotShapeIds](../tables/FaceSlotShapeIds.md)

## Open questions

None recorded.
