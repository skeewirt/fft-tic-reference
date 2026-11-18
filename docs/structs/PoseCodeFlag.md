# PoseCodeFlag

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventPoseCodeFlags table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="value"></a>`0x0` | value | `uint8` | I | small value substituted for the code (1 for most entries, 0 at three places) |

## Referenced by

- Described by tables: [EventPoseCodeFlags](../tables/EventPoseCodeFlags.md)

## Open questions

None recorded.
