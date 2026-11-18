# EventViewerEntry

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventViewerList table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="event"></a>`0x0` | event | `uint16` | V | story event number run when the entry is chosen (written to event variable 39) |

## Referenced by

- Described by tables: [EventViewerList](../tables/EventViewerList.md)

## Open questions

None recorded.
