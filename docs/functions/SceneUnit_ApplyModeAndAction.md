# SceneUnit_ApplyModeAndAction

- **Address:** `0x140241DF8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_ApplyModeAndAction(const uint8_t *operands)`
- **Callers:** EventScript_Run (opcode 0x11 case) and EventSubScript_RunTask (EventSubScript_RunTask).
- **Callees:** SceneGroup_ResolveId, SceneUnit_TestGroupMember, SceneObject_FindBySlot, sub_14021F414, sub_140235804 (frame-wait loop)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies a mode byte to the flag byte of each unit that an id names, then passes an action code to the state helper, and waits for frames when the code is 83, 84 or 85.

## Behavior

- V: reads the id as the 16-bit value at operand bytes 1 and 2 and resolves it with SceneGroup_ResolveId; when that returns 0 nothing else happens.
- V: for keys 0 to 20 in order it calls SceneUnit_TestGroupMember with the id; each key that is a member is processed. When the group mode written by SceneGroup_ResolveId is 0 (a single unit), the loop stops after the first processed member.
- V: mode byte at operand 5. Mode 0 finds the unit node with SceneObject_FindBySlot and clears bit 0 of the byte at node +143. Mode 1 sets bit 0 of the byte at node +143 and writes zero to the 16-bit word at node +24. Other values change neither.
- V: the action code is the 16-bit value at operand bytes 3 and 4.
- V: calls sub_14021F414 with the unit slot and the action code.
- V: when the action code is 83, 84 or 85 it calls sub_140235804 before the next member, which waits frames: it calls SceneTask_WaitFrame in a loop until sub_1402737D0 returns 0 (the value of dword_140CDB824), and it returns early through sub_14031A7E0 when the high dword of qword_142FF9E08 is non-zero and the high dword of qword_142FF9E00 is 3.
- V: the function does not wait for any other action code. It ends after the loop; the instruction then continues.

## State touched

- Calls: [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Notes

In the common path of sub_14021F414 (sub_140272A04) the action code is stored plus one in the 16-bit word at node +16 of the unit; the preview path can dispatch through the callback pointer instead.

## Open questions

What the flag bit at node +143 and the word at node +24 mean to the game; the rest of sub_14021F414 (the preview-table branch) and sub_1402729EC / sub_140272964 were not traced.
