# EventEndSlate_ShowTask

- **Address:** `0x14021EB40`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventEndSlate_ShowTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0xEC
- **Callees:** `sub_1401DB4E4`, `sub_140011750`, `sub_1401D1970`, `sub_1401D16C4`, `sub_1401D1A00`, `sub_1401D183C`, `sub_1403D8D1C`, UIName_Key, GUINode_FindState, GUINode_PlayState, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0xEC: adds the end-slate UI add-on, plays its language-keyed state and its Show state, waits until the state ends or the skip test passes, then removes the add-on.

## Behavior

- V: tags its task slot with 71 (0x47) in `qword_140D40B38[256 * index]`.
- V: when the object at `qword_143CD9FD0` is set, calls `sub_1401DB4E4` on it, sets its word at +34 and its word at +49 to 257, and sets its byte at +51 to 1.
- V: reads `dword_1407D453C` (the enhanced flag) and takes the UI manager at `*(*(qword_143CD9DA8 + 16) + 312)`.
- V: creates a 72-byte object with `sub_140011750`, initializes it with `sub_1401D1970`, sets its vtable to the class `vftable_ffto::Game::UI::UIAddonFFTOEndSlate_14070D448`, sets its dword at +60 to 5 and its byte at +64 to 0, adds it to the manager with `sub_1401D16C4`, and stores it in the manager's field at +64.
- V: calls `sub_1401D1A00(object, 46 - (flag != 0))`, so the argument is 45 when the enhanced flag is set and 46 otherwise.
- V: waits one frame at a time while the manager's virtual function at vtable offset 32 returns 0.
- V: the language key comes from the dword at +8 of `g_LanguageInfo` (1 when that block is absent): 1 gives `En`, 2 gives `Fr`, 3 gives `De`, 4 gives `Cs`, 5 gives `Ct`, 6 gives `Ko`, and 0 or any other value gives `Ja`.
- V: `UIName_Key` builds a key from that name, `GUINode_FindState` looks it up in the GUI node at object+48, the state's byte at +104 is set to 1, and `GUINode_PlayState` plays it. When the second dword of the key is non-zero it calls `sub_1403D8D1C(qword_143CDA2A0, value)`.
- V: the node's byte at +416 is set to 1, and the state keyed Show is then found, set and played the same way.
- V: waits one frame at a time while the node's byte at +416 is non-zero and the skip test is not true (dword +4 of `qword_142FF9E08` zero, or dword +4 of `qword_142FF9E00` not equal to 3).
- V: removes the add-on with `sub_1401D183C(manager, object)` and sets the manager's field at +64 to 0.
- V: when the object at `qword_143CD9FD0` is set, clears its bytes at +49 and +51 and sets its word at +34 to 256, then ends through SceneTask_Terminate.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)
- Reads: [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Started by event opcodes: [0xEC](../opcodes/README.md)

## Notes

The opcode record for 0xEC (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What `sub_1401DB4E4`, `sub_1401D1A00` and `sub_1403D8D1C` do, what the manager's slot-32 function reports, what the flags written to the object at `qword_143CD9FD0` control, and what the Show state contains. The opcode record describes the start gate as a global state word, but the start path tests a byte on the handler's stack, which was not traced.
