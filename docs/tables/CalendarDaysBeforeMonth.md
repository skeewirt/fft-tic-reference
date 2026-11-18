# CalendarDaysBeforeMonth

- **Kind:** table
- **Area:** [Math](../areas/math.md)
- **Storage:** Executable
- **Address:** `0x14067E18E`
- **Rows:** 12 rows of 2 bytes
- **Keyed by:** month 1..12
- **Row layout:** [CalendarDaysBeforeMonthRow](../structs/CalendarDaysBeforeMonthRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Days of a non-leap year before each month. Indexed by the month number 1..12 (the base address is two bytes before the first physical entry at 0x14067E190). Verdict: engine-data.

## Behavior

- V: Unit_ApplySpawnRecord computes day of year = table[month] + day, then converts it into a sign number with sub_140279328
- V: a month outside 1..12 or a day outside 1..31 gets a random day number 1..365 instead

## Notes

Our names. Tags: V layout, V reader.

## Open questions

None recorded.
