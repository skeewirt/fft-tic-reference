# UIAgentFFTOSaveLoad

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 1592 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The save/load screen's UI agent (1592 bytes, vtable 0x14070DE48, slot 38 of the UI agent manager). It carries the screen mode, two 32-byte state machines, five 264-byte save headers, an embedded save-data handler with a completion queue, and pointers to the list addon and the saving overlay.

## Fields

| Offset | Field | Type | Conf | Meaning | Indexed by registries |
|---|---|---|---|---|---|
| <a id="vtable"></a>`0x0` | vtable | `void *` | V | Agent vtable 0x14070DE48. The base constructor sub_1401D14F4 runs first; the manager reaches this agent at [[UI agent manager+16]+304] (vector begin + 38 * 8), slot 38. |  |
| <a id="mode"></a>`0x40` | mode | `uint32` | V | Screen mode, low three bits. 0 at construction; UISaveLoad_Open sets 2, TitleScene_Update rewrites it to 4, and sub_140182DF8 sets 1. State 3 tests bit 1 before collecting the five headers; state 4 maps bit 0 and bit 2 to the list tab; state 4's exit clears bits 0..2. |  |
| <a id="state_a_owner"></a>`0x48` | state_a_owner | `UIAgentFFTOSaveLoad *` | V | Owner pointer of agent state block A; the constructor stores the agent itself. |  |
| <a id="state_a_handler"></a>`0x50` | state_a_handler | `void (*)(void *, int, void *)` | V | Current agent-state handler. Starts as the no-op guard 0x1400103E0 and is replaced with the selector's result by UIAgent_SetState. | [UISaveLoadStates](../registries/UISaveLoadStates.md) |
| <a id="state_a_selector"></a>`0x58` | state_a_selector | `void *(*)(int)` | V | Selector 0x140182D04: returns off_14070DEA0[state], the vtable entry at slot 11 + state. | [UISaveLoadStates](../registries/UISaveLoadStates.md) |
| <a id="state_a"></a>`0x60` | state_a | `uint32` | V | Agent state 0..10: 0 idle, 1 saving overlay, 2 load the save index, 3 build the list addon, 4 enter the list, 5 load, 6 save, 7 erase, 8 source pick, 9 close, 10 deferred switch. | [UISaveLoadStates](../registries/UISaveLoadStates.md) |
| <a id="dialog_owner"></a>`0x68` | dialog_owner | `UIAgentFFTOSaveLoad *` | V | Owner pointer of the second state block; the constructor stores the agent itself. |  |
| <a id="dialog_handler"></a>`0x70` | dialog_handler | `void (*)(void *, int, void *)` | V | Current handler of the second block; starts as the no-op guard. | [UISaveLoadDialogStates](../registries/UISaveLoadDialogStates.md) |
| <a id="dialog_selector"></a>`0x78` | dialog_selector | `void *(*)(int)` | V | Selector 0x140182D14: returns off_14070DE88[state], the vtable entry at slot 8 + state. |  |
| <a id="dialog_state"></a>`0x80` | dialog_state | `uint32` | V | State of the second block. 0 is the guard, 1 runs sub_14018403C (load the save index), 2 is the guard used as done. The table also has a guard at 3, but no writer sets a state above 2. | [UISaveLoadDialogStates](../registries/UISaveLoadDialogStates.md) |
| <a id="descriptor_count"></a>`0x88` | descriptor_count | `uint32` | V | Index 0..5 of the next 264-byte header to fill. State 3 resets it and increments it once per collected header. |  |
| <a id="save_situation"></a>`0x8C` | save_situation | `uint32` | V | Situation value passed to SaveSlot_WriteFromLive by state 6. 0 at construction; sub_140182DF8 stores the save path's value here. The writer copies its low byte to the work copy's +0x11A. |  |
| <a id="allocator"></a>`0x90` | allocator | `void *` | V | The UI module's allocator (qword_143CDAA80+0x20), or 0 when the module is absent. |  |
| <a id="list_head"></a>`0x98` | list_head | `void *` | V | 24-byte sentinel of the save-message queue. The update drains 24-byte records through it under the critical section at +0xB8; a record's +0x10 dword is the message code that selects the prompt it builds. |  |
| <a id="list_count"></a>`0xA0` | list_count | `uint64` | V | Number of records in the queue; the constructor zeroes it and the drain decrements it. |  |
| <a id="save_handler_vtable"></a>`0xA8` | save_handler_vtable | `void *` | V | Embedded UISaveDataHandler, vtable 0x14070DF80. The constructor stores agent+0xA8 at g_SaveRequestManager+0x58. |  |
| <a id="save_handler_state"></a>`0xB0` | save_handler_state | `uint32` | ? | Zeroed by the constructor; its use was not established in this pass. |  |
| <a id="critical_section"></a>`0xB8` | critical_section | `CRITICAL_SECTION` | V | Critical section initialised by the constructor; it guards the queue sentinel and count while the update drains results. |  |
| <a id="interlock"></a>`0xE0` | interlock | `uint32` | V | 32-bit flag, 0 at construction. The pause-prompt callback clears it with an interlocked exchange for commands 6 and 7. No setter was found in the screen's code, so its meaning is unknown (?). |  |
| <a id="slot_index"></a>`0xE4` | slot_index | `int32` | V | Selected slot, -1 at construction. Events 1..7 and the list action store the chosen index here; states 5, 6, 7 and 8 consume it. |  |
| <a id="guide_id"></a>`0xE8` | guide_id | `uint32` | V | Starts at 23. The pause-prompt callback stores 13 here, with +0xEC = 1, before state 10. It is the UI agent slot that sub_1401D6DB0 tests, not a guide id: the field name is a misnomer. |  |
| <a id="pending_code"></a>`0xEC` | pending_code | `uint32` | V | Starts at 0. Set to 1 with +0xE8 = 13 before state 10; the helper compares the value minus 1 with the slot object's state, so 1 expects state 0. State 10's exit resets it. The field name is ours. |  |
| <a id="next_state"></a>`0xF0` | next_state | `uint32` | V | Target state for state 10: 5 (load) or 8 (source pick). The pause-prompt callback sets it; state 10 switches to it once the wait clears, and its exit resets it. |  |
| <a id="checkpoint_flag"></a>`0xF4` | checkpoint_flag | `uint8` | V | Load flag, 0 at construction. Event 1 sets it from its flag, event 4 sets it and event 5 clears it. State 5 uses it to choose sub_1400C4214/Save_ResumeCheckpoint instead of SaveSlot_LoadToLive. |  |
| <a id="descriptors"></a>`0x100` | descriptors | `SaveLoadDescriptor[5]` | V | Five 264-byte save headers, stride 0x108. A header starts with the FFTI magic, has dword 122 at +4 and a kind below 2 at +0x0C, a timestamp at +0x38, a progress dword at +0x40 and six 32-byte preview records from +0x44. State 3 fills them and state 4 builds the automatic rows from them. |  |
| <a id="list_addon"></a>`0x628` | list_addon | `UIAddonFFTOSaveLoad *` | V | The 1240-byte list addon. State 3 allocates and attaches it; states 5, 8 and 9 detach it. |  |
| <a id="saving_addon"></a>`0x630` | saving_addon | `UIAddonSaving *` | V | The 80-byte saving overlay (IDB class UIAddonSaving), created and attached in state 1 with UI row 256. +0x44 is the shown flag, +0x45 the open request and +0x46 the close request. It is not a confirmation dialog; states 5, 8 and 9 tear it down. |  |

## Behavior

- V: the constructor sub_140182B38 runs the base agent constructor, stores vtable 0x14070DE48, and writes the mode, both state blocks, the descriptor count/situation pair, the allocator, the 24-byte queue sentinel, the embedded save-data handler, the critical section and the preview records of the five descriptor slots.
- V: the two state blocks are 32 bytes each at +0x48 and +0x68. Each has owner, handler, selector and state; the selector returns an ordinary vtable slot, 11 + state for block A and 8 + state for block B.
- V: UIAgent_SetState runs the old handler with phase 2, stores the new state and runs the new handler with phase 0; phase 1 arrives from the agent update virtual at vtable slot 1, which calls the block-A handler with (owner, 1, the qword stored at g_Application+1160).
- V: agent states 0..10 are all used; state 0 is the no-op guard the list rests in. Dialog states 0..2 are used (guard, load the save index, guard); the table's state-3 entry is also the guard and has no writer.
- V: mode bit 1 gates the five-header collection in state 3; bit 0 and bit 2 select the list tab in state 4 (bit 0 first, then bit 2); state 4's exit masks the low three bits off.
- V: the queue at +0x98/+0xA0 is drained by the update helper under the +0xB8 lock. Each record carries a message code at +0x10; a system message opens prompt 6 and a game message prompt 7 through the pause addon.
- V: state 6 passes the low byte of +0x8C to SaveSlot_WriteFromLive, which copies it into the work copy's +0x11A situation byte; state 5 later treats a cache slot whose +0x11A byte is 1 as the resume case.
- V: the embedded save-data handler is registered in the save request manager, so the manager's completion path reaches this agent without a separate global.
- V: the saving overlay and the list addon are both agent addons. The overlay is created first (state 1); the list addon is created later (state 3) and is the event source the agent forwards.
- I: the object is one screen agent rather than a scene task: its states are screen phases, the two addons are its only child objects, and the title/save helpers poll its state instead of a task id (rests on the state bodies and on the title pages).
- ?: what the +0xE0 interlock gates; which UI agent occupies slot 13 that +0xE8 names; what the 480-byte gap +0x448..+0x628 holds.

## Notes

Read: sub_140182B38, UIAgentFFTOSaveLoad_Update, UISaveLoad_OnEvent, the state handlers 1..10, the pause callback sub_1401834B8, the update pump sub_140182F68, the saving-overlay constructor sub_1401CA6C4 and the selector tables at 0x14070DEA0/0x14070DE88. +0x630 is the UIAddonSaving overlay, not a confirmation dialog; +0x8C is the save situation byte, not a target slot (SaveSlot_WriteFromLive writes its third argument there and copies it to +0x11A); the constructor's descriptor initialiser starts at descriptor+0x44 and covers six 32-byte records, not a separate serializer. The field names are our own descriptive names; the two state registries name them as storage; save_situation (+0x8C) and list_count (+0xA0) are named from their use.

## Open questions

What sets +0xE0 and what reads it; which UI agent occupies slot 13, the slot state 10 waits on; what the gap +0x448..+0x628 contains; whether +0xB0 is a handler state or a flag.
