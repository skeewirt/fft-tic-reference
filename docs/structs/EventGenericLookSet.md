# EventGenericLookSet

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 32 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventGenericLookSets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="look[8]"></a>`0x0` | look[8] | `bytes[32]` | V | sprite sheet id for generic event actor slots 0..7 (u32 each) |

## Referenced by

- Described by tables: [EventGenericLookSets](../tables/EventGenericLookSets.md)

## Open questions

None recorded.
