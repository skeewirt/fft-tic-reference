# CalendarTrackedDates

- **Kind:** table
- **Area:** [Event system](../areas/event-system.md)
- **Storage:** Executable
- **Address:** `0x1407B8130`
- **Rows:** 64 rows of 2 bytes
- **Keyed by:** date slot 0..63
- **Read by:** [sub_1402CCEE0](../functions/sub_1402CCEE0.md), [sub_14039DA58](../functions/sub_14039DA58.md)
- **Row layout:** [CalendarDateRow](../structs/CalendarDateRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Month and day of 63 tracked dates; slot 0 is the player's date from event variables 95 and 96. Every time the calendar reaches a date its counter (max 99) grows. Verdict: designer-data.

## Behavior

- V: sub_1402CCEE0 compares the new month and day with each slot and adds 1 to that slot's counter when below 99
- I: the player-chosen slot matches the birthday asked on the new game page

## Notes

Our names. Tags: V layout, I that the dates are birthdays.

## Open questions

- ?: which date belongs to which slot
