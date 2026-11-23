# UISaveLoadDialogStates

- **Kind:** registry
- **Area:** [Save data](../areas/save-data.md)
- **Resolved by:** [UIAgentFFTOSaveLoad_Ctor](../functions/UIAgentFFTOSaveLoad_Ctor.md)
- **Values stored in:** [UIAgentFFTOSaveLoad.dialog_state](../structs/UIAgentFFTOSaveLoad.md#dialog_state), [UIAgentFFTOSaveLoad.dialog_handler](../structs/UIAgentFFTOSaveLoad.md#dialog_handler)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save/load agent's dialog block states (ids 0..2). The state id lives at agent +128; state n selects vtable slot 8 + n through the selector installed at +120. The block only loads the manual-save file: state 1 runs SaveSlots_LoadFromFile and the other two states are the no-op guard.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="uisaveload_dialogidle"></a>0 | `UISaveLoad_DialogIdle` | `vtable slot 8; 0x1400103E0` | V | No-op guard; the block starts here. |
| <a id="uisaveload_dialogloadslots"></a>1 | `UISaveLoad_DialogLoadSlots` | `vtable slot 9; 0x14018403C` | V | Phase 0 calls SaveSlots_LoadFromFile(g_SaveManager) and sets the save-I/O word at qword_140D405B8+260 to 3; phase 1 waits until sub_1400C3790() returns 0 and then sets state 2. |
| <a id="uisaveload_dialogdone"></a>2 | `UISaveLoad_DialogDone` | `vtable slot 10; 0x1400103E0` | V | No-op guard; state 1 sets it when the file load is idle. |

## Behavior

- V: the selector installed at +120 returns vtable slot 8 + state; states 0..2 use slots 8..10 (guard, sub_14018403C, guard).
- V: the block has its own owner, handler and state fields; the agent update virtual does not advance it. I: only the agent state-2 handler advances it, by calling the handler at +112 each frame (that handler is not shown in the pseudocode read).
- I: the selector has no bounds check, so a state 3 would read vtable slot 11, which is the same no-op guard used by agent state 0 (rests on the table layout read in the constructor; the table itself is not shown in the pseudocode).
- ?: no caller sets a dialog state above 2.

## Notes

State 1 is the file-load step that runs after the agent's saving overlay has covered the entry auto-save; state 2 tells agent state 2 to build the list. The dialog block is not the saving overlay at +1584. The storage fields are the agent struct's `dialog_state` and `dialog_handler` (offsets +128 and +112).

## Open questions

? whether a dialog state 3 was intended (the table reaches the guard, but no writer sets it); ? what the save-I/O word value 3 means beyond starting the copy into the slot cache.
