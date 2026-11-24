# LegacyWorldMenu_StartTestBattle

- **Address:** `0x1402B3FD4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t LegacyWorldMenu_StartTestBattle(void)`
- **Callers:** LegacyMenu_NumberEntryTask (through the range record); the task entry of node 8 of the old world menu node table (LegacyWorldMenuNodes)
- **Callees:** EventVar_Write, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a test battle on the map number entered in node 16: sets the test-battle variable 510 and the map number, then ends the task.

## Behavior

- V: adds 3 to the classic menu state dword 0x141D32E14.
- V: writes event variables 510 = 1, then 39, 48, 34, 35 and 36 = 0 (EventVar_Write).
- V: copies the dword at 0x140789374 (node 16's number word, 1..200) to dword 0x140D4C944, then EventTask_Terminate.
- V (data): it is the task of node 8 and the function of the number entry's range record (0x1407893A0 +8), which LegacyMenu_NumberEntryTask calls through record +64.
- I: dword 0x140D4C944 is the map number the battle loads; the effects of variable 510 on the battle are in TestBattleModeVariable510.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventTask_Terminate](EventTask_Terminate.md)

## Referenced by

- Observed behaviours: [TestBattleModeVariable510](../behaviors/TestBattleModeVariable510.md)

## Open questions

None recorded.
