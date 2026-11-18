# MusicSlotRecordsRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 12 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MusicSlotRecords table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="enabled"></a>`0x0` | enabled | `uint32` | V | 1 when the id has a record |
| <a id="value_a"></a>`0x4` | value_a | `uint32` | I | first number (position?) |
| <a id="value_b"></a>`0x8` | value_b | `uint32` | I | second number (position?) |

## Referenced by

- Described by tables: [MusicSlotRecords](../tables/MusicSlotRecords.md)

## Open questions

None recorded.
