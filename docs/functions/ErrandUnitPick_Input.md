# ErrandUnitPick_Input

- **Address:** `0x14036CC50`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char *ErrandUnitPick_Input(void)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 36)
- **Callees:** Errand_LoadRecord, Errand_Start, JobScreen_RefreshAfterChange, sub_14019DF88, sub_14019DCD4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Input step of the unit picker of the errand board (table index 36): reads the unit grid's result code and starts the errand when it is confirmed.

## Behavior

- V: reads the result code of the unit grid object (sub_14019DF88): 4 pops the screen and refreshes; 25 only refreshes (sub_1400ECEE4, sub_1402C1244); 6 changes the highlighted unit and refreshes the job and unit panels; 7 and 8 print text ids 47123 and 47124; 9 is the confirm.
- V: on 9 it copies the grid's unit-id list into the errand row (Errand_LoadRecord), stores the fee in 0x140D49460 and the day count in 0x140D49424, counts the picked units by looking each up in the party table, then calls Errand_Start, refreshes the gil display and prints text id 47125.
- V: a leading check of byte 0x142FF3CAE clears the pad word and returns.

## State touched

- Calls: [Errand_LoadRecord](Errand_LoadRecord.md), [Errand_Start](Errand_Start.md), [JobScreen_RefreshAfterChange](JobScreen_RefreshAfterChange.md)

## Notes

Result codes 7 and 8 were not traced further than their message ids.

## Open questions

None recorded.
