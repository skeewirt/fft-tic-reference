# CalendarDaysPerMonth

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** Executable
- **Address:** `0x14069300F`
- **Rows:** 13 rows of 1 byte
- **Keyed by:** month number
- **Row layout:** [CalendarDaysPerMonthRow](../structs/CalendarDaysPerMonthRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Days per month for the new-game birthday picker (February 28); right behind it a table of the 12 zodiac sign start dates (month, day) and a dword table of 7 values (75 to 465, step 65). Verdict: engine-data.

## Behavior

- V: first value after the stray byte is 31, then 28, 31, 30 ...; 12 months; the candidate is the 1-based base
- V: OpeningTask_5 (0x14037E83C): birthday picker clamps the day to the days of the chosen month
- V: sub_14037FFF1 and sub_1402F0B68: the same table through another displacement

## Notes

Our names. Tags: V.

## Open questions

- ?: the 7-value dword table behind the zodiac dates
