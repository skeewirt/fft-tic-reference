# EventSideYaw

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventSideYawTargets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="yaw"></a>`0x0` | yaw | `int16` | V | camera / unit yaw angle in 4096-per-turn units; the four values are the four facing yaws 0xE00, 0xA00, 0x600, 0x200 |

## Referenced by

- Described by tables: [EventSideYawTargets](../tables/EventSideYawTargets.md)

## Open questions

None recorded.
