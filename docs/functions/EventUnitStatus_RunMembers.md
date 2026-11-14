# EventUnitStatus_RunMembers

- **Address:** `0x1402416C8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventUnitStatus_RunMembers(int64_t ref, int flag)`
- **Callers:** EventUnitStatus_ApplyTask (call at 0x140241949); EventScript_Run (calls at 0x14023A9EA and 0x14023EC94, opcodes not identified here).
- **Callees:** SceneGroup_ResolveId, SceneUnit_TestGroupMember, ScenePreview_IndexOfSlot, ScenePreview_FindEntry, `sub_14024138C`, `sub_140241128`, EventUnitStatus_RefreshNode, `sub_140273270`, SceneTask_WaitFrame

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

For each unit the reference selects, refreshes its per-unit block from its preview row and runs the unit-end callback for it, then waits 0, 40 or 80 frames; when flag is zero it finishes with the group-end callback sub_140273270.

## Behavior

- V: sets qword_142FF8268 to qword_14184A9B0 plus 2040, the per-unit block base. Returns at once when word_140D408E8 is not zero.
- V: calls SceneGroup_ResolveId on ref. When that returns 0 (no unit) the routine does nothing more.
- V: clears the word at +1008 of the per-unit block.
- V: loops over keys 0 to 20 with SceneUnit_TestGroupMember. For each member the slot is the resolved id; ScenePreview_IndexOfSlot gives its preview index, and when that index is not -1 the byte at +401 of the row for that index is passed to ScenePreview_FindEntry. For an index above 20 the code reads address 401 (not confirmed).
- V: when the status from ScenePreview_FindEntry is 0 or more: if flag is not zero, calls sub_14024138C with the index and the slot. If flag is zero and sub_140241128 with the index returns non-zero, sets the callback to EventUnitStatus_RefreshNode (EventUnitStatus_RefreshNode) and calls it with the slot (directly for task slot 0, or after clearing the qwords at +96 and +104 of block 0 otherwise).
- V: stops the key loop after the first member when the group mode is 0 (one unit).
- V: when the word at +1008 is not zero, waits 40 frames with SceneTask_WaitFrame. When bit 0 of the low byte of +1008 is set, waits 40 more frames.
- V: when flag is zero, sets the callback to sub_140273270 and calls it with 0 (same slot rule). That routine walks the unit list from qword_140D3A410 and calls SceneUnit_SetFlag156 with the key byte of each node whose byte at +0x160 has bit 0x40.
- V: returns the value its last call left; nothing is set on purpose.

## State touched

- Calls: [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [SceneUnit_TestGroupMember](SceneUnit_TestGroupMember.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [ScenePreview_FindEntry](ScenePreview_FindEntry.md), [sub_14024138C](sub_14024138C.md), [EventUnitStatus_RefreshNode](EventUnitStatus_RefreshNode.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Referenced by

- Called by: [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md)

## Notes

For the 0x92 task the reference is a single unit, so the group loop runs once with mode 0 and the callback runs once.

## Open questions

What bits 0 and 1 of the word at +1008 mean and which flag bytes of the per-unit block set them (sub_140241128 sets them; its bytes are not named); what sub_14024138C does; why bit 0 adds a second 40-frame wait; what the 0x9x callers pass as flag.
