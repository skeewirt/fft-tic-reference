# EventUnitStatus_RefreshNode

- **Address:** `0x14027294C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventUnitStatus_RefreshNode(int16_t slot)`
- **Callers:** EventUnitBlock_RunTask (call at 0x140235EA4); EventScript_Run (call at 0x14023C629); sub_14024138C (call at 0x140241697); EventUnitStatus_RunMembers (call at 0x1402417CD); EventUnitStatus_ApplyTask (calls at 0x1402419F6, 0x140241A65 and 0x140241B29). It is also stored as the callback at 0x140235E91, 0x14023C615, 0x14023C83B, 0x14023CAAF, 0x140241673, 0x1402417B8, 0x1402419DF, 0x140241A4F and 0x140241B16.
- **Callees:** SceneObject_FindBySlot, `sub_1401FAF54`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The unit-end callback installed by the 0x92 status paths: finds the unit node for a slot and passes it to sub_1401FAF54, which refreshes that unit's flag words and state.

## Behavior

- V: calls SceneObject_FindBySlot with the slot and passes the node (or null) to sub_1401FAF54 with a tail jump. sub_1401FAF54 does nothing when the node is null.
- V: sub_1401FAF54 sets the dword at node +348 to the dword at +356 OR-ed with the dword at +348 cleared of the bits in the dword at +364; the dword at +352 is set the same way from +360 and +368.
- V: calls sub_140268F68 on the node. Then sets bit 0 of the word at node +24 when bit 0x10 of the byte at +352 is set, and clears it otherwise.
- V: sets the byte at +880 to 1 when dword_142FF9F24 is zero and either the dword at +348 AND 0x1FFFC2C4 is not zero or the byte at +8 equals dword_140CF873C; otherwise 0. When +880 is 1 the word at +884 is set to 0.
- V: calls sub_14026947C with the node, 0 and a flag that is 1 when dword_140CDB824 is zero; then sub_14026A048, sub_140269BBC and sub_140269DC4 with the node, sub_14026A1DC with the node and 0, and sub_1402694E4 (none of these traced).
- V: then clears the qword at +356 and the qword at +364, and sets the byte at +864 to 0.

## State touched

- Calls: [SceneObject_FindBySlot](SceneObject_FindBySlot.md)

## Referenced by

- Called by: [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md), [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [sub_14024138C](sub_14024138C.md)
- Called by event opcodes: [0x92](../opcodes/README.md)

## Notes

When the callback is called through the task-slot path, the slot is passed as the argument; the direct calls pass the same slot.

## Open questions

What the flag words at node +348 and +352 and the masks 0x1FFFC2C4 and 0x40 mean; what sub_140268F68, sub_14026947C, sub_14026A048, sub_140269BBC, sub_140269DC4, sub_14026A1DC and sub_1402694E4 do.
