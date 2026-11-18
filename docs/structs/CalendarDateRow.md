# CalendarDateRow

- **Kind:** structure
- **Area:** [Event system](../areas/event-system.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of CalendarTrackedDates.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="month"></a>`0x0` | month | `uint8` | V | month 1..12 |
| <a id="day"></a>`0x1` | day | `uint8` | V | day of month |

## Referenced by

- Described by tables: [CalendarTrackedDates](../tables/CalendarTrackedDates.md)

## Open questions

None recorded.
