# EventSubquestPanel_Run

- **Address:** `0x140214CEC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventSubquestPanel_Run(uint32_t panel_operand)`
- **Callers:** EventScript_Run, case 0xAC (call site 0x14023E1A4). No other code callers were found.
- **Callees:** `sub_1400EB5F4`, `sub_14013C740`, `sub_1401D1EAC`, `sub_140011750`, `sub_1401D1970`, `sub_1401D16C4`, `sub_1401D1A00`, UITable_GetRow, `sub_1401D1A3C`, `sub_1401DB4E4`, SceneTask_WaitFrame, UIName_Key, GUINode_FindState, `sub_1403D8D1C`, `sub_1400FC598`, `sub_1401D183C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows a sub-quest UI panel that holds the opcode 0xAC operand, blocks until one of the input keys 0x15, 0x1A or 0x1B is active, then hides and releases the panel.

## Behavior

- V: the argument is the 4-byte operand that EventScript_Run reads at instruction offset 1 before the call. The routine stores it in the new panel object at +80.
- V: first it calls sub_1400EB5F4 with (show flag 0, a4 -1). That routine acts only when the virtual slot +16 of the object at [[qword_143CD9DA8+16]+112] returns nonzero, and then calls sub_14013C740 with flag 0, which calls sub_1401D1EAC on the panel at that object's +64 (close). So an older panel is closed before the new one is made.
- V: allocates an 88-byte object (sub_140011750 with size 88), runs the base constructor sub_1401D1970 (base vtable, zeroes +16 to +40), then sets the vtable to the UIAddonFFTOSubquest table at 0x140710CF8 and zeroes +48, +56, +64, +72 and the dword at +80.
- V: registers the object with sub_1401D16C4 on the manager at the pointer stored at [qword_143CD9DA8+16]+424. That routine stores the manager at +16, appends the object to the manager's list at +8, and gives it an id at +32 from the counter at qword_143CD9DA8+128 (the counter is set to 1 when it is -1) and inserts it into the map at the global's +48.
- V: sets the object's +80 to the operand, then calls sub_1401D1A00 with 33. That looks up row 33 of table 24 with UITable_GetRow and, when the row exists, calls sub_1401D1A3C with the row's name-offset string (the internals of sub_1401D1A3C were not read).
- V: stores the object at +64 of the manager (the manager is the object at +424 of the [qword_143CD9DA8+16] object).
- V: sets the high dword of qword_142FF9E00 to 1 and calls sub_1401DB4E4 on the interface object at qword_143CD9FD0. Then it sets word +34 to 257, word +49 to 257 and byte +51 to 1 on that same object.
- V: state 1 (the manager's state word at +72): if the panel at +64 has a GUI node at +48, it builds the key 'Show' with UIName_Key, finds that state with GUINode_FindState, and reads the state's running byte at +105. The state moves to 2 when there is no panel, no node, no Show state, or the running byte is 0. Otherwise it stays in state 1 and waits one frame with SceneTask_WaitFrame.
- V: state 2: waits one frame at a time. When sub_1400FC598 reports the key 0x1A, 0x15 or 0x1B (each checked with the device argument 0), it checks the manager's virtual slot +16. If that is nonzero and the panel at +64 is set, it removes the panel with sub_1401D183C and clears +64. The state then becomes 3.
- V: state 3: builds the key 'Hide' and finds the state on the panel's node. While that state's running byte is nonzero it waits a frame. When the byte is zero, or the node or state is missing, it sets the state to 0, waits one frame, then clears +49 and +51 and sets +34 to 256 on the interface object at qword_143CD9FD0, and returns.
- V: the loop runs the whole time. The routine returns only after state 3 ends, so the interpreter is blocked for the full Show, input and Hide sequence.
- I: sub_1400FC598 with device 0 returns nonzero when sub_1400F0D00 finds a nonzero state byte in the key's 48-byte record (the bytes checked are at record offsets 1362 and 1378). The meaning of the key codes 0x15, 0x1A and 0x1B was not confirmed.

## State touched

- Calls: [sub_1401D1EAC](sub_1401D1EAC.md), [UITable_GetRow](UITable_GetRow.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

The panel's sub-routines are the second level: sub_1401D1A3C (addon setup), sub_1401D183C (removal, which calls the object's slot +40 when the flags at +44 and +45 are zero) and sub_1401D1F7C (a state-dispatch helper) were only partly read, so they have no sheets here.

## Open questions

What sets the manager's state word at +72 to 1 before the loop (the loop exits at once when it is 0). What sub_1401D1A3C builds from row 33 of table 24. The virtual slot +40 of the panel class and what it does. The meaning of the key codes 0x15, 0x1A and 0x1B.
