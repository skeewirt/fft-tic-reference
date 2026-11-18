# EventSoundGroup

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EventSoundGroups table: four sound effect numbers played together.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sound"></a>`0x0` | sound | `uint8[4]` | V | sound effect number of each of the four voices; 0 = silent (the player is called with number + 0xE10000 - 1) |

## Referenced by

- Described by tables: [EventSoundGroups](../tables/EventSoundGroups.md)

## Open questions

None recorded.
