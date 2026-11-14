# EventTask_Start

- **Address:** `0x1402BA5AC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *EventTask_Start(int slot, void *entry)`
- **Callers:** About 70 callers, including EventCmd_StartMessage and several of the task procedures.
- **Callees:** None (pure table writes)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a task in the first task table: resets the slot's block, marks it runnable and records its entry function. The twin of SceneTask_Start.

## Behavior

- V: sets `dword_140811624` to 1 (SceneTask_Start sets it to 0), then fills the slot's 2048-byte block in `off_14078D5D8`: the entry function at +136, the runnable flag at +144 set to 1, and the fields at +24, +112 to +128, +152 and +160 to +208 zeroed.
- V: writes the entry function to the thread record's target field (+8) in the 288-byte record table at `unk_143791D70`, and sets the flags at +272, +280 and +284 to 1 (the second-table starter leaves +284 alone).
- V: about 70 callers across the event, world-map and battle code.

## Referenced by

- Called by: [BattleCommand_BuildMenu](BattleCommand_BuildMenu.md), [BattleMsg_SetCellText](BattleMsg_SetCellText.md), [EventCmd_ShowMessage](EventCmd_ShowMessage.md), [EventCmd_StartMessage](EventCmd_StartMessage.md), [EventScene_QueueHelpText](EventScene_QueueHelpText.md), [Shop_Open](Shop_Open.md), [sub_14021A030](sub_14021A030.md), [sub_1402D62EC](sub_1402D62EC.md), [sub_14033F8C0](sub_14033F8C0.md), [sub_1403456D4](sub_1403456D4.md), [sub_140364408](sub_140364408.md)

## Notes

See SceneTask_Start for the second table; the two differ in the table written, the global flag value and the extra thread flag.

## Open questions

What `dword_140811624` and the flag at +284 control.
