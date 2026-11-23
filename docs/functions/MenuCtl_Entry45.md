# MenuCtl_Entry45

- **Address:** `0x140319860`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MenuCtl_Entry45(int *record)`
- **Callers:** the screen dispatcher ClassicMenu_RunScreenStack (table index 45)
- **Callees:** EventVar_Write, EventVar_Read, SceneVar_Write, HelpMessage_Open

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Step of a list of 8 flagged entries opened from index 43 (table index 45): confirm marks the entry as seen and starts the event numbered for it.

## Behavior

- V: sub_1403196DC builds the list: 8 rows, flag 8 on rows whose bit in the array at 0x141D330B0 is set.
- V: it follows the same states as index 44 (cancel, confirm and help text id 4236).
- V: the start path sets the bit of the chosen row, writes event variable 508 = 1, writes event variable 39 with the scene number from the table at 0x1406830B8 indexed by the row, copies event variable 35, sets mask 0x200000 of the state dword (and toggles 0x1) and sets scene variables 508 and 100 as index 44 does.
- V: the cancel path writes 0 to scene variables 41, 42 and 40.
- I: the list looks like an event replay list.

## State touched

- Calls: [EventVar_Write](EventVar_Write.md), [EventVar_Read](EventVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [HelpMessage_Open](HelpMessage_Open.md)

## Open questions

None recorded.
