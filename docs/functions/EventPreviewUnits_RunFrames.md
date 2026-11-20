# EventPreviewUnits_RunFrames

- **Address:** `0x140214A70`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventPreviewUnits_RunFrames(void)`
- **Callers:** EventScript_Run, case 0xC1 (call site 0x14023E3CE).
- **Callees:** `sub_140214404`, `sub_140216C78`, `sub_140214610`, `sub_140214828`, `sub_1402B20C0`, `sub_1400F4BCC`, `sub_1401DB4E4`, `sub_14013FAB0`, `sub_14013F71C`, `sub_1400EDC68`, SceneTask_WaitFrame, UITable_GetRowByKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs the per-frame preview-unit update for opcode 0xC1: it applies flagged preview-unit slots and, when any were flagged, waits while the UI reports busy.

## Behavior

- V: reads no operand. EventScript_Run calls it with four register values (0, 1, a value and 193), and the body does not read them directly. Two of them are passed on to sub_1402B20C0, which takes no arguments in the decompiled form.
- V: does nothing when the low dword of qword_142FF9E4C is nonzero.
- V: when dword_140782A94 is 8 and the high dword of qword_142FF9E08 is nonzero, it waits one frame at a time while the high dword of qword_142FF9E00 is nonzero and not 3, then waits 30 frames.
- V: sets the high dword of qword_142FF9E00 to 2. When the interface object at qword_143CD9FD0 is non-null it sets word +49 to 257 and byte +51 to 1.
- V: when byte_142FCF85F is set and byte_142FD1588 has bit 0x40, it calls sub_140214404 on the staging buffer unk_142FD1390 and clears byte_142FCF85F.
- V: loops over the 21 records of g_BattleUnitTable (512 bytes each). When byte +1 is not 0xFF and byte +504 has bit 0x40, it calls sub_140216C78 with the slot index, then sub_140214404 with the record.
- V: loops over 21 records at unk_141853CE1 (512 bytes each). When byte +0 is not 0xFF and byte +503 has bit 0x20, it calls sub_140216C78 with the index. For the first two such records it stores the index in a dword list at (the pointer at +144 of the object at [qword_143CD9DA8+16]) + 188 + 4 times the count.
- V: if any record was flagged in that second pass, it calls sub_1402B20C0, looks up the key 167 in table 69 with UITable_GetRowByKey and dispatches on that row's type code (the four targets were not read), sets word +34 of the interface object to 257, calls sub_1401DB4E4, calls sub_14013FAB0 with the object at +144 and the flagged count, sets the low dword of qword_142FF9E00 to 1, and waits one frame at a time while sub_14013F71C on that object returns nonzero.
- V: loops over the 21 slots of g_BattleUnitTable again. When byte +1 is not 0xFF and byte +504 is negative (bit 0x80), it calls sub_140214610 (no arguments).
- V: calls sub_140214828 with the last argument values. It returns no value that the routine uses.
- V: clears word +49 and byte +51 of the interface object and sets its word +34 to 256 (on the interface object at qword_143CD9FD0). If the object at +144 holds a non-null pointer at +136, it calls sub_1400EDC68 twice on g_CharaRenderMgr, with the sub-objects at +2440 and +2472 of that pointer.
- I: the bodies of sub_140216C78, sub_140214404, sub_140214610, sub_140214828, sub_14013FAB0 and sub_14013F71C were not read in full. The statements about what they change are from the calls and their use, not from their internals.

## State touched

- Calls: [sub_140214404](sub_140214404.md), [sub_140214610](sub_140214610.md), [sub_1400F4BCC](sub_1400F4BCC.md), [sub_14013F71C](sub_14013F71C.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)
- Reads: [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)

## Referenced by

- Observed behaviours: [UnitEventFlagWord](../behaviors/UnitEventFlagWord.md)

## Notes

The high dword of qword_142FF9E00 is set to 2 here and is not cleared in this routine. The callee sub_14013F71C or the wait loop may clear it elsewhere, which was not checked.

## Open questions

Which routine clears the high dword of qword_142FF9E00 after this one returns. What sub_140216C78 and sub_140214404 do to a slot. What the four targets of table 69 row 167 do.
