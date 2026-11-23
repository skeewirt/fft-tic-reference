# UISaveLoad_StateSourcePick

- **Address:** `0x140183B78`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void __fastcall UISaveLoad_StateSourcePick(UIAgentFFTOSaveLoad *agent, int phase)`
- **Callers:** UIAgent_SetState through the agent selector `0x140182D04` (agent state 8, vtable slot 19); no direct call site.
- **Callees:** GUICore_FocusNode, sub_1401D7DDC, UIState_BeginTransition, UIAgent_DetachAddon, UIAgent_SetState, sub_140182E7C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Agent state 8 of the save/load screen: the pick that hands a chosen save slot back to the caller. It fades the list out, waits for the fade, writes the selected slot to `g_GlobalWork+128` and returns the agent to its idle state; its exit runs the agent's active test and detaches the remaining addons.

## Behavior

- V: entry (phase 0) clears the GUI focus, calls the music helper sub_1401D7DDC(qword_143CD9DD8, 8, 2) for track 8, requests UI fade 26, detaches the list addon at +0x628 and clears that pointer.
- I: sub_1401D7DDC (not shown in this body) looks up the queued music entry whose id is 8. Its mode-2 path unlinks that entry and calls sub_1402B1ED0 and sub_1402B1E74(2) without loading a track; mode 1 (used by state 9) calls sub_1402B1E74(1) as well and loads the entry's tracks through EventSlot_LoadTrack. State 8 does not load a track.
- V: the fade request sets g_UIStateFade+0x10 to 0 when another transition is active, stores 26 at +0x18 and starts the transition through UIState_BeginTransition.
- V: phase 1 waits until the fade timer at g_UIStateFade+0x10 is 0 or less, then stores the selected slot (+0xE4) at g_GlobalWork+0x80 (128) and sets agent state 0.
- V: phase 2 calls sub_140182E7C. I: that helper (not shown in this body) runs the agent's IsActive test and, when the agent still has an addon attached, calls sub_1400FB3B0(-1,0,0), detaches the list addon (+0x628) and the saving overlay (+0x630), and clears both pointers.
- V: UISaveLoad_OnEvent event 3 is the direct entry: while the agent is in state 0 it stores the chosen slot at +0xE4 and sets state 8. The pause-prompt command 4 also reaches state 8, through +0xF0 = 8 and state 10.
- V: TitleScene_Update opens the screen, rewrites the save/load mode field to 4 and seeds g_GlobalWork+128 with -1 before it starts polling. After the screen closes it shows the title menu again when +128 is still -1; any other value opens the play mode screen. State 8 is the only screen state that writes +128.
- I: in that mode-4 path state 8 is the New Game + source-save picker: the written value is the chosen source save and the title's -1 means the picker was backed out (rests on the -1 seed, the mode-4 tab filtering and the title's two branches). The state itself does not read the mode field.
- ?: what the picker shows on screen; which UI agent the state-10 wait at slot 13 tests; whether the music helper's mode 2 also stops a track that is already playing.

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md), [UIAgent_DetachAddon](UIAgent_DetachAddon.md), [UIAgent_SetState](UIAgent_SetState.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md)
- Writes: [g_GlobalWork](../globals/g_GlobalWork.md), [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md)

## Notes

Whole body read (190 bytes). The state writes `g_GlobalWork+128` only after the fade finishes; the field is the dword at +0x80 of the GlobalWork singleton. The title code seeds it with -1 and tests it after the screen closes; this state is the writer. The registry `UISaveLoadStates` lists the state as `UISaveLoad_StateNewGamePlus`; this page keeps the assigned name `UISaveLoad_StateSourcePick`.

## Open questions

What the picker draws; which UI agent occupies slot 13 that state 10 waits on; whether the music helper's mode 2 stops the current track or only drops the queued entry.
