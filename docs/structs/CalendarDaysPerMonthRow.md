# CalendarDaysPerMonthRow

- **Kind:** structure
- **Area:** [Data access](../areas/data.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the CalendarDaysPerMonth table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="days"></a>`0x0` | days | `uint8` | V | days in the month (31, 28, 31, 30 ...); entry 0 is a stray byte |

## Referenced by

- Described by tables: [CalendarDaysPerMonth](../tables/CalendarDaysPerMonth.md)

## Open questions

None recorded.
