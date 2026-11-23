# UISaveLoadStates

- **Kind:** registry
- **Area:** [Save data](../areas/save-data.md)
- **Resolved by:** [UIAgentFFTOSaveLoad_Ctor](../functions/UIAgentFFTOSaveLoad_Ctor.md)
- **Values stored in:** [UIAgentFFTOSaveLoad.state_a](../structs/UIAgentFFTOSaveLoad.md#state_a), [UIAgentFFTOSaveLoad.state_a_handler](../structs/UIAgentFFTOSaveLoad.md#state_a_handler), [UIAgentFFTOSaveLoad.state_a_selector](../structs/UIAgentFFTOSaveLoad.md#state_a_selector)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save/load agent's eleven states (ids 0..10). The state id lives in the agent's block A at +96; state n selects vtable slot 11 + n through the selector installed at +88. State 0 is the no-op resting state, states 1..4 bring the screen up, states 5..7 load, save and erase, state 8 picks a New Game + source, state 9 closes the screen and state 10 delays a target state behind a wait on another UI agent.

## Entries

| Id | Name | Value | Conf | Meaning | Appears in flows |
|---|---|---|---|---|---|
| <a id="uisaveload_stateidle"></a>0 | `UISaveLoad_StateIdle` | `vtable slot 11; 0x1400103E0` | V | No-op guard. The list screen rests here after state 4; events 0..3 are accepted only in this state. |  |
| <a id="uisaveload_statesavingoverlay"></a>1 | `UISaveLoad_StateSavingOverlay` | `vtable slot 12; 0x140183658` | V | Enter: create and show the 80-byte UIAddonSaving overlay at +1584, load UI row 256, queue a new AUTOENHANCED autosave through sub_1400C480C, wait for the save queue and the overlay, then state 2. |  |
| <a id="uisaveload_stateloadslotfile"></a>2 | `UISaveLoad_StateLoadSlotFile` | `vtable slot 13; 0x1401836F0` | V | Set dialog block state 1 (SaveSlots_LoadFromFile through sub_14018403C), run the dialog's phase 1, and go to state 3 when the dialog reaches state 2. | [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md) |
| <a id="uisaveload_statebuildlist"></a>3 | `UISaveLoad_StateBuildList` | `vtable slot 14; 0x14018373C` | V | Allocate and attach the 1240-byte list add-on, store it at +1576. When mode bit 1 is set, request the five auto-slot summaries one per frame through sub_1400C4214(manager, n, 0) and copy each into descriptor n; then state 4. |  |
| <a id="uisaveload_statelistenter"></a>4 | `UISaveLoad_StateListEnter` | `vtable slot 15; 0x1401838F0` | V | Build the five auto entries from the descriptors at +256, select tab 0/1/2 from the mode bits, load UI row 252 and request the overlay hide. Phase 1 goes to state 0 when the hide finishes; phase 2 clears the mode bits. |  |
| <a id="uisaveload_stateload"></a>5 | `UISaveLoad_StateLoad` | `vtable slot 16; 0x1401839E4` | V | Load: phase 0 fades and either requests the slot's parts (+244 set) or calls SaveSlot_LoadToLive; phase 2 resumes the checkpoint or the scene and tears the screen down. |  |
| <a id="uisaveload_statesave"></a>6 | `UISaveLoad_StateSave` | `vtable slot 17; 0x140183C38` | V | Save: phase 0 writes the selected manual slot from live with +140 as the situation; phase 1 waits for the file write and reloads the slot file; phase 2 refreshes the list and puts the cursor on the written slot. |  |
| <a id="uisaveload_stateerase"></a>7 | `UISaveLoad_StateErase` | `vtable slot 18; 0x140183DD4` | V | Erase: phase 0 fills the slot record in the cache with 0xFF and marks the cache dirty; phase 1 waits for the write; phase 2 refreshes the list. |  |
| <a id="uisaveload_statenewgameplus"></a>8 | `UISaveLoad_StateNewGamePlus` | `vtable slot 19; 0x140183B78` | V | New Game + pick: phase 0 clears focus, loads music track 8 in mode 2, fades to 26 and detaches the list; phase 1 writes the chosen slot to g_GlobalWork+128; phase 2 cleans up. |  |
| <a id="uisaveload_stateclose"></a>9 | `UISaveLoad_StateClose` | `vtable slot 20; 0x140183ED0` | V | Close: phase 0 starts music track 7 (manual tab) or 8 (other tabs) in mode 1 and fades to 9; phase 1 waits for the fade and sets state 0; phase 2 clears the screen and cleans up. | [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md) |
| <a id="uisaveload_statedeferred"></a>10 | `UISaveLoad_StateDeferred` | `vtable slot 21; 0x140183FA0` | V | Deferred entry: while +232 is not 23, calls sub_1401D6DB0 with the UI base and the values at +232/+236; it enters +240 (5 for load or 8 for New Game +) when the helper returns 0. The pause callback sets +232 = 13 and +236 = 1; phase 2 resets +232/+236/+240. | [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md) |

## Behavior

- V: the selector installed at +88 returns vtable slot 11 + state; states 0..10 therefore use slots 11..21, which hold the guard and the ten handlers listed here.
- V: `UIAgent_SetState` runs the current handler with phase 2, stores the new state number, selects the new handler and runs it with phase 0. Phase 1 is delivered by the update virtual at vtable slot 1, which calls the handler at +80 with (agent, 1, the qword stored at g_Application+1160).
- V: phase 0 receives a 0 third argument; phase 1 receives the qword stored at `g_Application+1160`. ?: the pseudocode shows only two arguments for the phase-2 call, so its third argument is not shown.
- V: neither the old nor the new state number is passed to a handler; only the selector receives it.
- V: in state 3, mode bit 1 gates the five-header collection. In state 4, bit 0 set selects tab 0; with bit 0 clear the tab is 1, and it is 2 when bit 2 is also set. State 4's exit clears bits 0..2. The in-game save opener `sub_140182DF8` sets bit 0 and stores its situation value at +140 before it enters state 1.
- V: state 10's helper indexes the UI agent array at UI base + 296 with the value at +232 and compares the value at +236 minus 1 against a dword reached from that agent's +16 handle; what that dword means is ?.
- I: state 0 is the resting state of the open list, resting on events 0..3 testing for it and on state 4 entering it.
- ?: no code sets an agent state above 10; the selector has no bounds check.

## Notes

The state blocks are the two 32-byte controls at +72 and +104. Only block A drives this registry; block B's states are the separate UISaveLoadDialogStates registry. The handler addresses are the ordinary vtable slots, not a second table. The overlay at +1584 is an 80-byte UIAddonSaving, created by state 1 and not a dialog. The storage fields are the agent struct's `state_a`, `state_a_handler` and `state_a_selector` (offsets +96, +80 and +88).

## Open questions

? no writer for state ids above 10; ? whether the +224 flag changes any state transition (only a clear was found).
