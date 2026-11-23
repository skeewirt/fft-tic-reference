# UISaveLoad_StateEnter

- **Address:** `0x1401838F0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void __fastcall UISaveLoad_StateEnter(UIAgentFFTOSaveLoad *agent, int phase)`
- **Callers:** UIAgent_SetState through the agent selector `0x140182D04` (agent state 4, vtable slot 15); no direct call site.
- **Callees:** GUICore_FocusNode, SaveLoadList_BuildAutoEntries, UIAddon_LoadByRow, UIState_EndTransition, sub_1400FB3B0, Guide_TryAutoShow, UIAgent_SetState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Agent state 4 of the save/load screen: the hand-off from the loaded save index to the live list. It closes the saving overlay, turns the five save headers into automatic entries, picks the list tab from the mode field, applies the list layout and returns the agent to its idle state.

## Behavior

- V: entry (phase 0) first reads the saving overlay at agent +0x630. When the overlay byte at +0x44 is non-zero it writes 1 to +0x46, the overlay's close request. The overlay is the 80-byte UIAddonSaving built in state 1, not a confirmation dialog.
- V: the tab index starts at 0; when mode bit 0 (agent +0x40 & 1) is clear it becomes 1, and when mode bit 2 (& 4) is also set it becomes 2. Mode 1 therefore selects tab 0, mode 2 tab 1 and mode 4 tab 2. Bit 1 is not tested in this state.
- V: bit 1 is read in the preceding state 3, which requests the five 264-byte save headers only when the bit is set. State 4 always calls SaveLoadList_BuildAutoEntries; it accepts whatever headers currently pass the FFTI test, so the automatic vector is a rebuild, not an append.
- V: entry clears the GUI focus, calls SaveLoadList_BuildAutoEntries(list_addon, agent +0x100), writes the tab to list_addon +0x1B0, loads row 252 of the addon table into the list addon with UIAddon_LoadByRow, and sets list_addon +0x4D1 to 1.
- V: SaveLoadList_BuildAutoEntries walks the five 264-byte descriptors and keeps only headers whose first dword is the FFTI magic, whose +4 dword is 122 and whose +0x0C dword is below 2. It clears the automatic-entry vector first, so a rejected header contributes no row.
- V: UIAddon_LoadByRow resolves the row through the addon table and calls UIAddon_LoadByPath with the same addon; row 252 is a layout for the list addon, not a second addon. The addon's bind/refresh virtual (vfunc_4) calls SaveLoadList_Refresh near its end; that refresh rebuilds the visible rows from the tab field state 4 wrote.
- V: phase 1 does nothing while the saving overlay byte at +0x44 is non-zero. Once it is 0, phase 1 sets agent state 0. State 0's handler is the no-op guard, so the list addon stays attached and the agent waits there for events.
- V: phase 2 (exit) clears list_addon +0x4D1, ends the current UI fade transition when g_UIStateFade +0x18 is non-zero, calls sub_1400FB3B0(0, 0, 0), and asks for guide 235 when mode bit 2 is set. It then clears mode bits 0..2 with a mask of 0xFFFFFFF8.
- V: the mode bit 0 and bit 2 tests read the low byte at +0x40; the tab write is a 32-bit store. Phase 2 preserves every mode bit above bit 2.
- I: mode 1 is the save path (sub_140182DF8 sets bit 0 and stores the save situation at +0x8C), mode 2 the Load Game path (UISaveLoad_Open writes 2) and mode 4 the New Game + path (TitleScene_Update rewrites the field to 4). The three tab compositions on the list page match those uses.
- ?: the on-screen names of tabs 0, 1 and 2; what guide 235 is; what sub_1400FB3B0's mode 0 changes.

## State touched

- Calls: [GUICore_FocusNode](GUICore_FocusNode.md), [SaveLoadList_BuildAutoEntries](SaveLoadList_BuildAutoEntries.md), [UIAddon_LoadByRow](UIAddon_LoadByRow.md), [UIState_EndTransition](UIState_EndTransition.md), [Guide_TryAutoShow](Guide_TryAutoShow.md), [UIAgent_SetState](UIAgent_SetState.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md)

## Notes

Whole body read (244 bytes). Earlier versions of this reference called +0x630 a dialog; the object is the saving overlay (UIAddonSaving, 80 bytes, UI row 256), which the struct names `saving_addon`. The list addon is created in state 3. The tab branches: tab 0 adds one entry created by sub_140186390 and then scans all 50 cache slots, tab 1 copies the automatic vector and then scans all 50, and tab 2 scans only cache slots whose byte at record +0x119 is non-zero and whose situation byte at +0x11A is 5 or 0.

## Open questions

What UI row 252's layout is called; what guide 235 is; what sub_1400FB3B0(0,0,0) changes; whether the three tab captions match the three compositions.
