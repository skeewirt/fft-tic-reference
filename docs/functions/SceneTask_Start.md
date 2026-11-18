# SceneTask_Start

- **Address:** `0x1402F7DE4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void *SceneTask_Start(int slot, void *entry)`
- **Callers:** About 46 callers, including the event dispatcher `sub_14023A868`.
- **Callees:** None (pure table writes)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Starts a task in the second task table: resets the slot's block, marks it runnable and records its entry function so its thread begins there.

## Behavior

- V: clears `dword_140811624`, then fills the slot's 2048-byte block in the table at `off_140783088`: the entry function goes to +136, the runnable flag at +144 is set to 1, and the fields at +24, +112 to +128, +152 and +160 to +208 are zeroed.
- V: writes the entry function to the thread record's target field (+8) in the 288-byte record table at `unk_143791D70`, and sets the flags at +272 and +280 to 1.
- V: about 46 callers across the event, world-map and battle code; nine of them pass `EventMessage_Task` as the entry.
- I: the runnable flag at +144 is the same one SceneTask_WaitFrame and EventTask_WaitFrame scan for.

## Referenced by

- Called by: [BattleAction_RunScript](BattleAction_RunScript.md), [BattleAction_StartScript](BattleAction_StartScript.md), [BattleMenu_ConfirmRow](BattleMenu_ConfirmRow.md), [BattleMenu_RunStep](BattleMenu_RunStep.md), [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md), [ClassicItemUsePage_Run](ClassicItemUsePage_Run.md), [EventScript_Run](EventScript_Run.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [Save_BootClear](Save_BootClear.md), [sub_14022F868](sub_14022F868.md), [sub_140233588](sub_140233588.md), [sub_140237CD0](sub_140237CD0.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1403015A4](sub_1403015A4.md), [sub_140323D1C](sub_140323D1C.md), [sub_140324658](sub_140324658.md)
- Called by event opcodes: [0x10](../opcodes/README.md), [0x19](../opcodes/README.md), [0x1A](../opcodes/README.md), [0x1B](../opcodes/README.md), [0x1D](../opcodes/README.md), [0x2A](../opcodes/README.md), [0x3B](../opcodes/README.md), [0x3E](../opcodes/README.md), [0x49](../opcodes/README.md), [0x58](../opcodes/README.md)

## Notes

There are two task tables with the same block layout and a shared thread table: `off_14078D5D8` (index `dword_14184B22C`) used by EventTask_WaitFrame, and `off_140783088` (index `dword_140D40948`) used here and by SceneTask_WaitFrame. EventThread_Yield sets both indices.

## Open questions

What distinguishes a task in the first table from one in the second.
