# TrackedDateLoopsVisitEverySlotBelowTheirBoundAndTheJumpAddsTheYearsToEachOne

- **Kind:** observed behaviour
- **Scope:** engine (calendar counters)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [sub_1402CCEE0](../functions/sub_1402CCEE0.md), [sub_14039DA58](../functions/sub_14039DA58.md), [sub_140375AD0](../functions/sub_140375AD0.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The daily tick and the jump by N days walk the slots from 1 (the tick) or 0 (the jump) up to a bound of 64 and treat every slot they visit alike: the tick counts a slot whose pair equals today, the jump adds the whole years passed to every visited counter and one more when the slot's date lies inside the span; a visited slot with no date is counted by the jump.

## Behavior

- V: the tick loop (0x1402CD0D6..0x1402CD112) reads the pair of slot rcx, compares month then day with today's month and day, and adds 1 to the counter below the cap of 99; the loop bound is a compare of rcx with 64 (an 8-bit immediate). Slot 0 is handled before the loop with event variables 95 and 96.
- V: the jump loop (0x14039DB1F..0x14039DBD2) first adds the years passed (the day count divided by 365, truncated) to the counter as an 8-bit add, then, for slots 1 and up, reads the pair; its day of the year is the days before the month plus the day minus 1 (a month below 2 sums nothing); the slot counts one more when that day is not after the target day of the year (the current day of the year plus the remaining days, modulo 365) and its distance from the current day is below the remaining days; a counter above 99 is set to 99.
- V: a slot with the pair {0, 0} gives the day of the year -1, which passes both tests: the jump counts it (checked by an emulated run of the loop).
- V: a month above 12 would read past the 12-entry days-per-month table the loops sum (0x140680FF8), and there is no leap day in that table (February has 28 days).
- V: the level list builder (0x140375B23..0x140375B7E) is a third loop with the same bound of 64 (a 32-bit compare of ebx), over positions 0..63.

## Notes

Tested by running the stock loops on a mapped copy of the image against an independent model of the arithmetic above.

## Open questions

None recorded.
