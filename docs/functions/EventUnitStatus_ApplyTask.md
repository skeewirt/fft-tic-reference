# EventUnitStatus_ApplyTask

- **Address:** `0x14024189C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventUnitStatus_ApplyTask(void)`
- **Callers:** Started as a task entry by EventScript_Run for opcode 0x92.
- **Callees:** EventRef_ResolveSlot, ScenePreview_IndexOfSlot, EventUnitStatus_RunMembers, EventUnitStatus_SetBit, EventUnitStatus_RefreshNode, sub_140272964, sub_14021F414, SceneTask_WaitFrame, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The task started by event opcode 0x92: resolves a unit id, applies a mode-dependent update to the unit's preview row and status bits, runs the unit-end callback, waits the given frames, then ends.

## Behavior

- V: tags its slot with 67 in qword_140D40B38 at the slot's index.
- V: reads the operand through the pointer at +0 of its block: bytes 0 and 1 form the unit id (unsigned 16-bit), byte 2 is the mode, and bytes 3 and 4 form a signed 16-bit frame count.
- V: resolves the id with EventRef_ResolveSlot, then takes the preview index of the slot with ScenePreview_IndexOfSlot; when the slot is 2000 or the index is -1 the index is 2000. The task ends with SceneTask_Terminate only when the second resolve of the id returns 2000.
- V: calls EventUnitStatus_RunMembers with the id and 0 before the mode branch.
- V: when the index is 0 to 20, the row is unk_141853D10 plus 512 times the index. When the index is above 20 (including 2000), the code uses the small values 48, 97 and 99 as row addresses, which are invalid (the decompile shows this; not confirmed by a run).
- V: the state is 0 when bit 5 of the row byte at +0x31 is set; otherwise it is 2 minus bit 0 of the row byte at +0x33.
- V: modes 1, 2 and 3 are switched on first. Mode 1: EventUnitStatus_SetBit with bits 5 (flag 0), 16 (flag 0) and 6 (flag 1); the per-unit byte at qword_142FF8268 plus the index plus 945 is set to 2; then the callback EventUnitStatus_RefreshNode runs with the slot.
- V: mode 2: EventUnitStatus_SetBit with bit 31 (flag 1); the per-unit byte is set to 3; EventUnitStatus_RefreshNode runs with the slot; then sub_14021F414 runs with the slot and 22.
- V: mode 3: EventUnitStatus_SetBit with bit 8 (flag 1); the per-unit byte is set to 4; EventUnitStatus_RefreshNode runs with the slot.
- V: mode 4 and above: sets the word at +0 of the row to 0, calls EventUnitStatus_SetBit with bit 5 and flag 1, sets dword_140782CAC to 65 unless it is 166, and runs EventUnitStatus_RefreshNode with the slot.
- V: modes 0 and other values (no switch case) use the state: state 2 runs sub_140272964 with the slot; state 1 does nothing; state 0 sets the per-unit byte to 1, calls EventUnitStatus_SetBit with bit 5 (flag 0) and bit 16 (flag 1), runs EventUnitStatus_RefreshNode with the slot, and sets dword_140782CAC to 65 unless it is 166.
- V: a callback run here is stored in qword_140D40940; for task slot 0 it runs at once, for other slots the qwords at +96 and +104 of block 0 are cleared first.
- V: after the branch, when the frame count is 1 or more, waits that many frames with SceneTask_WaitFrame; then ends with SceneTask_Terminate.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [EventUnitStatus_SetBit](EventUnitStatus_SetBit.md), [EventUnitStatus_RefreshNode](EventUnitStatus_RefreshNode.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Started by event opcodes: [0x92](../opcodes/README.md)

## Notes

The opcode record for 0x92 (data/opcodes.jsonl) points here through `starts_task`.

## Open questions

What sub_14021F414 and sub_140272964 do; what the per-unit byte at qword_142FF8268 plus 945 drives; what the row bits 5, 16, 6, 8 and 31 mean; the invalid row addresses for indexes above 20.
