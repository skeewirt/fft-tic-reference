# LocationMarker

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the LocationMarkerOffsets table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="x"></a>`0x0` | x | `int16` | I | x offset of the location marker |
| <a id="mark_a"></a>`0x2` | mark_a | `uint8` | I | marker kind byte copied into the marker record |
| <a id="mark_b"></a>`0x3` | mark_b | `uint8` | I | marker flag byte copied into the marker record |
| <a id="y"></a>`0x4` | y | `int16` | I | y offset of the location marker |
| <a id="pad"></a>`0x6` | pad | `uint16` | I | always 0 |

## Referenced by

- Described by tables: [LocationMarkerOffsets](../tables/LocationMarkerOffsets.md)

## Open questions

None recorded.
