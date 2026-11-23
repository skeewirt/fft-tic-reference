# EventRef_ResolveSlot

- **Address:** `0x140226A18`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventRef_ResolveSlot(uint32_t ref, char flag)`
- **Callers:** About 64 call sites in 20 routines, the widest-used resolver of the event code: EventScript_Run (32 call sites), EventSubScript_RunTask (8), EventMessage_Task (5), and about 13 others such as sub_140240144, sub_1402404CC, sub_140241BD0 and sub_140242140.
- **Callees:** ScenePreview_FindEntry, sub_140272538, ScenePreview_IndexOfSlot (ref 105 only), SceneObject_FindBySlot (ref 105 only), ScenePreview_SlotOfIndex, SceneVar_Read (argument 39)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns a script reference id into the slot number of the object it names. Most event opcodes call it to find their target; it returns 2000 when nothing matches.

## Behavior

- V: `ref` is the reference id, taken as 32 bits. Callers pass a signed 16-bit operand read from the instruction, or a constant such as 2, 23, 52, 62 or 131 to 138. `flag` is stored into a local that is overwritten before any read on every path, so the result does not depend on it; most callers pass 1.
- V: step 1 looks `ref` up with ScenePreview_FindEntry, which compares the low 8 bits. Only when that finds nothing, and `ref` is 162, 163 or 1 to 73, it asks sub_140272538 for the record index of the unit id. If the index is 0 to 20 and byte +401 of that record is 120 to 124, `ref` becomes that byte.
- V: ref 104 scans records 0 to 15 for the first whose byte +5 has bit 0 or bit 1 set, and sets `ref` to that record's byte +401. If none is found it returns 2000.
- V: record +5 is the entry's byte +24 for a battle's own unit (Unit_ApplySpawnRecord) and 11 or 8 for a party unit (UnitWork_CopySaveFields, 11 when the unit byte is below 4), so stopping at record 15 is what keeps ref 104 off the party's records 16..20 (the bound and the 'none found' test compare with 16 at 0x140226AC4 / 0x140226AC9). Stock: 4 entry keys give an entry those bits (519, 523, 524, 553). The message code has a copy, EventRef_ResolveSlotForMessage.
- V: ref 105 scans slot numbers 0 to 20 for an object (SceneObject_FindBySlot) whose preview index (ScenePreview_IndexOfSlot) names a record with byte +440 non-zero, and sets `ref` to that record's byte +401. If none matches, it looks up refs 1, 2 and 3 in turn and keeps the first with a non-negative status. If none qualifies, or the record it stopped on has bit 0x04 of byte +97 set, it returns 2000.
- V: refs 100 to 103 do not give a slot. They return the 16-bit value at index (ref - 100) of the table `qword_140783038`, and a stored 1000 becomes 2000.
- V: otherwise it calls ScenePreview_FindEntry(ref) for the record and status. A negative status other than -2 returns 2000, unless SceneVar_Read(39) equals 404.
- V: it finds the record's index k (0 to 20) by comparing pointers over the 21 records, using 21 when there is no match, and calls ScenePreview_SlotOfIndex(k). It returns 2000 when that is -1 or when bit 0 of the record's byte +98 is set. Otherwise it returns the slot number, 0 to 255.

## State touched

- Calls: [ScenePreview_FindEntry](ScenePreview_FindEntry.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [SceneObject_FindBySlot](SceneObject_FindBySlot.md), [ScenePreview_SlotOfIndex](ScenePreview_SlotOfIndex.md), [SceneVar_Read](SceneVar_Read.md)

## Referenced by

- Called by: [EventBlock_ApplyOperands](EventBlock_ApplyOperands.md), [EventMoveTargets_Rewrite](EventMoveTargets_Rewrite.md), [EventObject_MoveWorker](EventObject_MoveWorker.md), [EventPreviewUnit_StageSlot](EventPreviewUnit_StageSlot.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitMove_Task](EventUnitMove_Task.md), [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md), [EventUnitStatus_SetBit](EventUnitStatus_SetBit.md), [SceneGroup_ResolveId](SceneGroup_ResolveId.md), [ScenePlacement_WritePair](ScenePlacement_WritePair.md), [SceneUnit_ApplyFlagRow](SceneUnit_ApplyFlagRow.md), [SceneUnit_Oscillate120](SceneUnit_Oscillate120.md), [SceneUnit_ZeroPosAndReset](SceneUnit_ZeroPosAndReset.md)
- Called by event opcodes: [0x2C](../opcodes/README.md), [0x44](../opcodes/README.md), [0x46](../opcodes/README.md)

## Notes

Fixed values in the code: 2000 for no match, 1000 in the qword_140783038 table, the ref ranges 1 to 73, 100 to 105, 120 to 124 and 162 to 163. In EventScript_Run the first call reads the reference as a signed 16-bit operand at instruction offset 1.

## Open questions

What record bytes +5, +98, +401 and +440 mean; why refs 100 to 105 exist and what the scans behind 104 and 105 select; what SceneVar_Read(39) equal to 404 means. Step 7 reads byte +98 with no null test: if no record matched but ScenePreview_SlotOfIndex(21) finds an object, the read would go through a null pointer. Not confirmed whether that can happen.
