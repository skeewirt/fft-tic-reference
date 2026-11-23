# UISaveLoad_Open

- **Address:** `0x140183580`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall UISaveLoad_Open(void *saveLoadAgent)`
- **Callers:** TitleScene_Update (0x1401DEA56, 0x1401DEA95), sub_1401DDD2C (0x1401DDDAA), sub_140182A74 (0x140182AAB)
- **Callees:** sub_1401D9174, UIState_BeginTransition, UIAgent_SetState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens the save/load screen: it selects the load mode, starts the screen's music transition, fades the UI to state 9, and sets the save/load agent's own state machine to state 1. It does not push a scene task.

## Behavior

- V: called from `TitleScene_Update` twice (0x1401DEA56 for New Game +, 0x1401DEA95 for Load Game), from the blocking helper `sub_1401DDD2C` (0x1401DDDAA), and from `sub_140182A74` (0x140182AAB).
- V: clears the low three bits of the save/load agent's mode field at +64 and sets bit 1, so the mode value is 2.
- V: calls `sub_1401D9174(qword_143CD9DD8+1328, 8, ...)`. I: it starts BGM transition 8 and binds the music id of the sound entry it names to music slot 1 (callee body not in this function).
- V: when the UI fade object's requested state (`g_UIStateFade+24`) is not 9, it stores 9 and starts the transition with `UIState_BeginTransition`.
- V: returns `UIAgent_SetState(agent+72, 1)`: the embedded agent state machine runs the old state's exit handler, stores state 1, and runs the new state's entry handler. This is the save/load agent's state, not the scene task stack.
- V: no scene task id is pushed. The title scene stays in its state 2 or 3 and polls the save/load agent reached at `[qword_143CD9DA8+16]+304`: its vtable +16 test and its state dword at +96 of that agent object (+24 of the embedded agent at +72).
- V: the New Game + caller overrides the mode field to 4 immediately after the call, clearing its low two bits and setting bit 2; the Load Game caller leaves the 2 set here.
- V: the screen reaches the title path through `g_GlobalWork+128` for New Game + and through `g_GlobalWork+102` for Load Game. The New Game + caller sets +128 to -1 before the screen opens; the load state writes +102 = 1 when it confirms a load (I: the writer is not in this function).
- I: +128 carries the chosen New Game + source save and -1 means the screen was backed out; the update tests -1 to decide whether to rebuild the menu or open the play mode screen (rests on the initial -1 write and on the two state-2 branches).
- I: mode 2 is the plain load list and mode 4 is the New Game + source-save picker (rests on the two callers and on the different flags each caller tests after the screen closes).
- ?: what the other mode bits at +64 select, and whether the screen ever returns without either flag being written.

## State touched

- Calls: [sub_1401D9174](sub_1401D9174.md), [UIAgent_SetState](UIAgent_SetState.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)
- Called by: [TitleScene_Update](TitleScene_Update.md)

## Notes

Whole function read (102 bytes). `UIAgent_SetState` writes the state dword at +24 of the embedded agent (agent+72, so +96 of the save/load agent), which is the value the title path polls. The mode field at +64 is the same dword the two callers later rewrite; this function's own write is always 2. The BGM transition call is the only music work and is not part of the screen's state machine. The list rows are the subject of `SaveLoadList_BuildEntries` and `SaveLoadList_FillItem`; this page covers only the open path.

## Open questions

? what save/load agent modes besides 2 and 4 select; ? what the BGM transition 8 is called in the sound table.
