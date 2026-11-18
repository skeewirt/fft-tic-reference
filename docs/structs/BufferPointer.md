# BufferPointer

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventWorkBufferPointers table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="buffer"></a>`0x0` | buffer | `pointer` | V | pointer to a large .bss work buffer (0x1413CFCC0 .. 0x1416FFCC0) |

## Referenced by

- Described by tables: [EventWorkBufferPointers](../tables/EventWorkBufferPointers.md)

## Open questions

None recorded.
