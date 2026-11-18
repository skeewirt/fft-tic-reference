# sub_1402CCEE0

- **Address:** `0x1402CCEE0`
- **Area:** [Errands](../areas/errands.md)
- **Prototype:** `void sub_1402CCEE0(void)`
- **Callers:** sub_1402482F8
- **Callees:** EventVar_Read, EventVar_Write, sub_140340FD0, Party_EggUpkeep, sub_14015B578, sub_14041EF2C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Checks the errand state on a world tick: it reads the active errand slots and their delay bytes, ages the eggs, and posts the result message when an errand is due.

## Behavior

- V: it reads and writes the errand delay array at 0x1411A7140 (96 bytes, one per errand) and the active slot records g_ErrandActive (the body holds rbx = 0x1411A71A2, the base+2, and indexes -2/+1/+3 from it).
- V: one calendar day: event variables 46 / 47 (month, day) advance; each active slot without flag 0x04 gets now_day + 1 and, at max_day (or with flag 0x02), flag 0x04 and sub_140340FD0(its town) for a dispatch that was not called off; the low 6 bits of every g_ErrandDelay byte count down (min(d, 32) - 1).
- V: the 64 day counters at 0x1411A7220 (index 0 for the date in event variables 95 / 96, the others for the dates of byte_1407B8130) count up to 99 on their date; they are not errand finish days.
- V: Party_EggUpkeep is called as part of the same tick, so the egg counters age with the errands.
- V: the message is posted through sub_14015B578, which builds a parameterised text message; sub_1402CD168 is reached from there.
- V: EventVar_Read and EventVar_Write carry the current day and the story progress the errand rules use.
- V: the function returns without a value and does not start a task.
- I: this is the world-map errand tick, because the only caller is the world update and the state it touches is the errand delay/active block.
- ?: whether an errand whose delay has not elapsed is skipped or only logged; the branch count was not decoded.

## State touched

- Calls: [EventVar_Read](EventVar_Read.md), [EventVar_Write](EventVar_Write.md), [Party_EggUpkeep](Party_EggUpkeep.md)
- Reads: [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandActive](../globals/g_ErrandActive.md)
- Writes: [g_ErrandDelay](../globals/g_ErrandDelay.md), [g_ErrandActive](../globals/g_ErrandActive.md)

## Referenced by

- Observed behaviours: [ErrandStateIsSpreadOverFiveStores](../behaviors/ErrandStateIsSpreadOverFiveStores.md), [TodaysCalendarDateIsHeldInEventVariables46And47](../behaviors/TodaysCalendarDateIsHeldInEventVariables46And47.md), [TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage](../behaviors/TrackedDateCountersAreCountedByTwoFunctionsAndShownByTheLevelListPage.md), [TrackedDateLoopsVisitEverySlotBelowTheirBoundAndTheJumpAddsTheYearsToEachOne](../behaviors/TrackedDateLoopsVisitEverySlotBelowTheirBoundAndTheJumpAddsTheYearsToEachOne.md)
- Reads tables: [CalendarTrackedDates](../tables/CalendarTrackedDates.md)

## Notes

Whole function read (648 bytes).

## Open questions

None recorded.
