# EventScript_Run

- **Address:** `0x14023A868`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventScript_Run(void)`
- **Callers:** EventScript_TaskMain
- **Callees:** SceneTask_Start, SceneTask_WaitFrame, EventScript_InstructionLength, EventScript_FindOpcode, EventScript_FindInstruction, EventScript_IsSkipStop, SceneVar_Read, SceneVar_Write, SceneVar_Alu, SceneTask_Terminate and many opcode helpers

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The event interpreter: it walks the loaded event script one instruction at a time and carries out each opcode. It is the biggest function in the event code, with about 19,000 bytes and 3,700 decompiled lines.

## Behavior

- V: reads the script through the pointer `qword_140D40A90`, with the program counter in a local; each step loads the opcode byte at the counter and the operand bytes at +1 to +4 into locals.
- V: dispatches on the opcode through 13 binary-search `switch` blocks; about 170 distinct opcode values are handled in this function.
- V: advances the counter with EventScript_InstructionLength after each instruction.
- V: the end opcode 0xDB stops the script; it is also forced when `word_141874530` is set and none of the scene tasks 2 to 15 is running.
- V: before the main loop it scans the script with EventScript_FindOpcode for 0x92 instructions and, for units whose flags allow it, starts the task `sub_14024189C` for each.
- V: starts 21 task bodies through SceneTask_Start, waits with SceneTask_WaitFrame 74 times, reads variables with SceneVar_Read (15 times) and writes them with SceneVar_Write (14 times), and calls SceneVar_Alu directly for the variable opcodes.
- V: uses EventScript_IsSkipStop (twice) to find the next instruction that matters when it skips forward.
- I: opcodes that take time (waits, walks, messages, camera moves) are handled by starting a task and waiting for it, while simple opcodes run inline.
- V: at the start of an event it tests byte +36 (skip_once) of the EventId row of the event variable; when that is 0 it reads the OverrideEntryData row for g_BattleEntrySource and tests bytes +0x93, +0x94 and +0x95 (guest_join_panel, withdrawal_panel, betrayal_panel). I: a non-zero byte there acts like the EventId byte: g_EventSkipOnce is set to 1 (the event may be skipped only once); otherwise it is cleared (see the behaviour EntryRowMarksEventSkipOnce).
- V: the objective camera tour sub_1401EA2F0 is called from this function.
- V: opcode 0x43 (scene set-up) is the default arm of the switch for opcodes 0x2D to 0x44; its behavior, by mode:
- V: opcode 0x43, the section is the default arm of the switch for opcodes 0x2D to 0x44 that has no case of its own; no case for 0x43 exists in the switches around it, so opcode 0x43 reaches this arm.
- V: opcode 0x43, the mode is the byte at +1 of the instruction. The section does nothing else with the operand bytes at +2 and +3.
- V: opcode 0x43, waits four frames with SceneTask_WaitFrame before any branch.
- V: opcode 0x43, reads scene variable 508 with SceneVar_Read. When it is zero, the mode 1 and mode 6 branches run. When it is non-zero, those two are skipped and every other branch below still runs.
- V: opcode 0x43, mode 1 (variable 508 zero): when scene variable 39 is below 78, it calls `sub_1402842CC`, reads one byte from the record at qword_143CD9DE0 (offset 171 when bit 0 of the byte at offset 16 is set, otherwise offset 91), calls `sub_140227458` with that byte and ends the section at once. When variable 39 is 78 or more, it calls `sub_140227458` with 0 and continues with the later branches.
- V: opcode 0x43, mode 6 (variable 508 zero): for each slot from 2 to 14 it writes 0 to the qword at offset 0 and 0 to the qword at offset 8 of its block in the task table `off_140783088`, writes 1 to the qword at offset 16, writes 3 to the tag qword qword_140D40B38 of that slot, and calls `sub_1402F7F4C` for the slot, which waits until the runnable qword at block offset 144 is zero.
- V: opcode 0x43, mode 6 then reads scene variable 39 (300 sets dword_142FEC514 to 1, otherwise variable 100 is written 1), writes variable 81 as 1, clears the high dword of qword_142FF9E08, calls EventSequencer_TakeTurn(14, ...)`, sets dword_140D40850 to 5 and waits until it is zero, sets the low dword of qword_142FF9E00 to 1, writes variable 100 as 0 and clears dword_142FEC514.
- V: opcode 0x43, mode 6 then repeats the same slot reset for slots 2 to 14. The repeat loop leaves the mode operand at 15, so the mode 15 branch below also runs for a mode 6 instruction.
- V: opcode 0x43, modes 2 and 7 write 365 to scene variable 84 with SceneVar_Write.
- V: opcode 0x43, mode 3 loops over 21 units: for each unit whose flag byte at unk_141853CE5 (stride 512) has bits 0x30 clear, it adds 10 to the byte at unk_141853D0B with the same stride, capped at 100. The loop bound is 21, so the branch for index 21 and above is not reached.
- V: opcode 0x43, mode 4 loops over slots 0 to 20: for each slot where SceneObject_FindBySlot returns a unit, it reads ScenePreview_IndexOfSlot; when that is not -1 and ScenePreview_FindEntry on the record byte at unk_141853E71 (stride 512) gives a status other than -2 and the byte at offset 494 has bits 0x30 set, it calls SceneUnit_ResetAndQueue4(slot, 2, -31, -31, 0). Afterwards it waits 120 frames.
- V: opcode 0x43, mode 5 sets dword_142FF8280 to 1. Mode 8 sets dword_14185670C to 0.
- V: opcode 0x43, modes 9 and 10 write scene variable 83 as 1 and as 0.
- V: opcode 0x43, mode 11 reads word_142FEC530: a value of 1 is changed to 2 first. If the value is then 0, the section ends at once; otherwise it waits until word_142FEC530 is 0.
- V: opcode 0x43, mode 12 sets word_140D40900 to 0, word_140D4091C to 19 and word_140D408FC to 0, then calls `sub_140234990(19, 0)`.
- V: opcode 0x43, mode 13 copies byte 141854B2F to byte 141854D2F and byte 141854B30 to byte 141854D30. It sets the high bit of byte 141854D31 from byte 141854B31 and keeps its low seven bits. It calls ScenePreview_ShowEntry(8, 1), waits until word_140D407D0 is zero, then waits two more frames.
- V: opcode 0x43, mode 14 loops over slots 0 to 20 with SceneObject_FindBySlot. For each unit it found, it replaces the mode with ScenePreview_IndexOfSlot of that slot, so after the loop the mode is the value from the last unit found (-1, 0 to 20), or stays 14 when no unit was found. The branch then reads the bytes at 141853D2F and 141853D30 (stride 512) and calls SceneUnit_SetFlag156 for the units that match.
- V: opcode 0x43, mode 17 copies byte 141853F2F to byte 141854B2F and byte 141853F30 to byte 141854B30. It sets byte 141854B31 from byte 141853F31, except bits 4 to 6, which keep their old values. It calls ScenePreview_ShowEntry(7, 1), waits until word_140D407D0 is zero, then waits two more frames.
- V: opcode 0x43, mode 15 uses slot 3 and the byte at 141853F31; mode 16 uses slot 4 and the byte at 141854131. Each calls ScenePreview_SlotOfIndex with its slot number. When the result is not -1 it writes the words at 142FEF860, 142FEF862 and 142FEF864, writes the seven-byte record at unk_142FEC580 plus seven times the result (byte 0 = four times the low nibble of the source byte, bytes 4 and 6 = 0), calls `sub_140272F3C(result)` and calls `sub_14021F538(result, four times the low nibble)`.
- I: opcode 0x43, in modes 15 and 16 the value written to word 142FEF860 is read through a pointer that the decompile does not assign on these paths, and the value written to word 142FEF864 is read from an address that is not set on these paths.
- V: opcode 0x43, mode 18 calls EventRef_ResolveSlot(62, flag); when the result is 2000 the section ends. Otherwise it replaces the mode with ScenePreview_IndexOfSlot of the slot, calls `sub_140241080(slot, 0)`, sets qword_140D40940 to EventUnitStatus_RefreshNode, and then: when dword_140D40948 is not zero, it writes 0 to the qwords at offsets 96 and 104 of `off_140783088` and calls qword_140D40940 with the slot; otherwise it calls EventUnitStatus_RefreshNode with the slot.
- V: opcode 0x43, mode 19 calls `sub_1402B20C0`, sets a local flag that the 0xE3 transition body reads later, and when dword_143807794 equals 2 it sets the low dword of qword_142FF9E00 to 1. When dword_143807794 is not 2, the section ends there.
- V: opcode 0x43, mode 255 calls SceneVar_Alu(190, 48, 0, ...), sets word_140D40910 to 1 and waits until it is zero, calls SceneVar_Alu(176, 48, 2, ...), sets word_140D40910 to 1, clears qword_14114A0F6, dword_14114A0FE and word_14114A102, waits until word_140D40910 is zero, and calls `sub_1402694E4` for each entry of the list that starts at qword_140D3A410.
- V: opcode 0x43, any other mode value, including 0 and 20 to 254, has no branch and only waits the four frames.
- V: opcode 0x43, after any branch the section ends at the common exit, which moves the script position past the current instruction (the same exit as the other opcodes that finish without a jump).
- V: opcode 0x43, the mode 1, mode 6, mode 11 and mode 18 branches can end the section early, which skips the branches after them.

## State touched

- Calls: [SceneTask_Start](SceneTask_Start.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [EventScript_InstructionLength](EventScript_InstructionLength.md), [EventScript_FindOpcode](EventScript_FindOpcode.md), [EventScript_FindInstruction](EventScript_FindInstruction.md), [EventScript_IsSkipStop](EventScript_IsSkipStop.md), [SceneVar_Read](SceneVar_Read.md), [SceneVar_Write](SceneVar_Write.md), [SceneVar_Alu](SceneVar_Alu.md), [SceneTask_Terminate](SceneTask_Terminate.md)
- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md)
- Writes: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Called by: [EventScript_TaskMain](EventScript_TaskMain.md)
- Called by event opcodes: [0x1F](../opcodes/README.md), [0x43](../opcodes/README.md)
- Observed behaviours: [BattleMapIdPathsAndTheirWidths](../behaviors/BattleMapIdPathsAndTheirWidths.md), [EntryRowMarksEventSkipOnce](../behaviors/EntryRowMarksEventSkipOnce.md), [EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping](../behaviors/EventIdRowOfTheCurrentEventIsReadWithoutANullTestWhenSkipping.md), [PseudoEffectWordIsASixteenBitEventOperand](../behaviors/PseudoEffectWordIsASixteenBitEventOperand.md), [ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture](../behaviors/ScenarioWordLinksRecordsByATenBitKeyAndLivesInTheBattleCapture.md)
- Reads tables: [NxdDataEventId](../tables/NxdDataEventId.md), [NxdDataOverrideEntryData](../tables/NxdDataOverrideEntryData.md)

## Notes

Opcode semantics are spread through the function; per-opcode sheets would document the individual cases. The loaded script layout and lengths are described on EventScript_InstructionLength and EventScript_LoadIntoBuffer.

## Open questions

The behavior of each opcode case.
