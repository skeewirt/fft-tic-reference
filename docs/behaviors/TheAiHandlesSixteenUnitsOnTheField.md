# TheAiHandlesSixteenUnitsOnTheField

- **Kind:** observed behaviour
- **Scope:** engine (battle AI)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Ai_UnitTurnStep](../functions/Ai_UnitTurnStep.md), [sub_1403166C0](../functions/sub_1403166C0.md), [sub_1403167E4](../functions/sub_1403167E4.md), [Battle_AITurnRun](../functions/Battle_AITurnRun.md), [Ai_SurveyTargets](../functions/Ai_SurveyTargets.md), [Action_BuildCurrentAction](../functions/Action_BuildCurrentAction.md), [Battle_SaveCapture](../functions/Battle_SaveCapture.md), [Battle_RestoreCapture](../functions/Battle_RestoreCapture.md), [g_AiCommandTable](../globals/g_AiCommandTable.md), [g_AiCurrentAction](../globals/g_AiCurrentAction.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle AI numbers the units on the field 0, 1, 2... and works only when every number is below 16: with a 17th unit on the field (any team) no AI-controlled unit acts at all, and the first player move-range build of a fresh launch then faults on the AI's never-set unit pointer. Four per-number tables of 16 entries are the reason; widened to 21 in a test, the AI played 17 units.

## Behavior

- V: sub_1403166C0 writes byte_141873038[unit] = a running number for each of the 21 records whose +0x01 is not 0xFF (0xFF otherwise); Ai_UnitTurnStep goes on only when the acting unit's number and every present unit's number are below 0x10 (0x14031F1BC, 0x14031F1D9), else it reports 'nothing to do' (a2 = 2) before sub_14031F464 sets the AI's unit pointer (qword_141872EA0); sub_1403167E4 skips a unit whose number is 0x10 or more (0x140316822).
- V: the AI's per-unit lists are sized for 16: 34 command entries of 4 bytes per number at g_AiCurrentAction + 3834 (16 x 34 x 4 = 2176 bytes, up to +6010) and g_AiCommandTable indexed by the same number x 34; the number table itself is at g_AiCurrentAction + 0x1998.
- V (static sweep of every reader of the number and of the cached current number at g_AiCurrentAction + 0xE2F, and of every operand landing in the block from +0xC00 to +0x1A00): five tables are indexed by the number. Four hold exactly 16 entries, measured by the room before the next referenced data: +0xCD4 (20 bytes each, next data +0xE14), +0xE58 (8 bytes, next +0xED8), +0xEF8 (g_AiCommandTable, 136 bytes, the two fixed entries at +0x1778 follow) and +0x1780 (8 bytes, the AI unit pointer at +0x1800 follows); 50 instructions address them, none through a data pointer. The fifth, 70 bytes per number in the buffer at 0x1417FFCE0 (pointer at +0x19D0), has 2048 bytes before the next referenced data.
- V: sub_14038AED4 and sub_14038B104 (called by Battle_AITurnRun to save and restore the units around the AI's look-ahead) write every present unit's number into the 20- and 8-byte tables and the 70-byte buffer with no check of their own, so the all-units check in Ai_UnitTurnStep is what keeps a number of 16 from writing past them.
- V: the numbering and the lists are built at battle load (BattleLoad_StepFresh) and on sub_14030476C's path, and one unit's list again when its state changes (the other callers of sub_1403167E4); Battle_SaveCapture and Battle_RestoreCapture copy the block's first 0x19D0 bytes, the four tables included.
- V (tested 2026-11-21, same battle and setup as below, 17 on the field): with the four tables moved in memory to 21 entries (the 50 references pointed at them), the three checks raised to 21 and the old ranges filled with a marker, all 17 units were numbered (slots 16..20 = 12..16) and list 16 was built; slot 20 (number 16) on Auto-battle was played by the AI (it moved and hit an enemy); in the first enemy round all 12 enemies moved and attacked; the AI unit pointer was set by the AI's own turn step; no fault was recorded and the old ranges were never written.
- V: sub_140317164 (state 5, called from sub_140204A1C when a unit's turn opens, battle state 19) reads the facing of qword_141872EA0's unit (0x140317386); that pointer is written only by sub_14031F464 inside the AI's turn step, so before any AI turn of a launch it is 0.
- V (tested 2026-11-21, random battle at Mandalia Plain, 12 enemy entries of one look + 5 party units, the scene-unit block moved to 21 records in memory): with 17 units on the field the game froze before the first player turn (one fault, 0x140317386, main thread, the AI pointer 0); with the pointer set by hand before Commence the battle ran, but over two rounds no enemy moved or acted (all at CT 42 while the party cycled); the same setup with 4 party units (16 on the field, block moved) played normally, the enemies acting.
- I: so more than 16 units on the field needs the AI's four 16-entry tables widened and its three checks raised, whatever the drawing limits; the capture copy then has to carry the moved tables too, or the lists be rebuilt after a restore.

## Open questions

None recorded.
