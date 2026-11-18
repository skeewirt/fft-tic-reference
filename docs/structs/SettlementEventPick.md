# SettlementEventPick

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 10 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the SettlementEventPicks table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="mode"></a>`0x0` | mode | `uint8` | I | stored in a scene variable (0x6B, 0x69, 0x6A, 0x6E ... seen) |
| <a id="tag"></a>`0x1` | tag | `uint8` | V | written to event variable 53 |
| <a id="choices"></a>`0x2` | choices | `bytes[8]` | V | eight candidate values; one is picked at random (index = top three bits of a 15-bit random) and written to event variable 50 |

## Referenced by

- Described by tables: [SettlementEventPicks](../tables/SettlementEventPicks.md)

## Open questions

None recorded.
