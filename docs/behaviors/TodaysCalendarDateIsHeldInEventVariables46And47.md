# TodaysCalendarDateIsHeldInEventVariables46And47

- **Kind:** observed behaviour
- **Scope:** engine (calendar)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_1402CCEE0](../functions/sub_1402CCEE0.md), [EventVar_Read](../functions/EventVar_Read.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The calendar's current month and day are event variables 46 (month 1..12) and 47 (day). The daily tick compares each tracked date with these two; event variables 95 and 96 hold a different date, the one slot 0 counts (the player's birthday).

## Behavior

- V: the tick reads variable 0x2E (46) and variable 0x2F (47) through EventVar_Read and compares them with each slot's month and day (0x1402CD08D..0x1402CD0F2).
- V: seen live, variables 46 / 47 advance with world-map travel (April 3 to April 5 on one trip, April 9 to April 11 on another), and a tracked counter rose by one on the trip that passed its date, also when the date was passed mid-trip.
- V: seen live, variables 95 / 96 read January 1 on a New Game with the birthday January 1.

## Notes

Seen 2026-11-16 on the Steam PC build.

## Open questions

None recorded.
