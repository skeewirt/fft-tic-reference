# TheAiHandlesSixteenUnitsOnTheField

- **Kind:** observed behaviour
- **Scope:** engine (battle AI)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Ai_UnitTurnStep](../functions/Ai_UnitTurnStep.md), [sub_1403166C0](../functions/sub_1403166C0.md), [sub_1403167E4](../functions/sub_1403167E4.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The battle AI numbers the units on the field 0, 1, 2... and works only when every number is below 16: with a 17th unit on the field (any team) no AI-controlled unit acts at all, and the first player move-range build of a fresh launch then faults on the AI's never-set unit pointer.

## Behavior

- V: sub_1403166C0 writes byte_141873038[unit] = a running number for each of the 21 records whose +0x01 is not 0xFF (0xFF otherwise); Ai_UnitTurnStep goes on only when the acting unit's number and every present unit's number are below 0x10 (0x14031F1BC, 0x14031F1D9), else it reports 'nothing to do' (a2 = 2) before sub_14031F464 sets the AI's unit pointer (qword_141872EA0); sub_1403167E4 skips a unit whose number is 0x10 or more (0x140316822).
- V: the AI's per-unit lists are sized for 16: 34 command entries of 4 bytes per number at g_AiCurrentAction + 3834 (16 x 34 x 4 = 2176 bytes, up to +6010) and g_AiCommandTable indexed by the same number x 34; the number table itself is at g_AiCurrentAction + 0x1998.
- V: sub_140317164 (state 5, called from sub_140204A1C when a unit's turn opens, battle state 19) reads the facing of qword_141872EA0's unit (0x140317386); that pointer is written only by sub_14031F464 inside the AI's turn step, so before any AI turn of a launch it is 0.
- V (tested 2026-11-21, random battle at Mandalia Plain, 12 enemy entries of one look + 5 party units, the scene-unit block moved to 21 records in memory): with 17 units on the field the game froze before the first player turn (one fault, 0x140317386, main thread, the AI pointer 0); with the pointer set by hand before Commence the battle ran, but over two rounds no enemy moved or acted (all at CT 42 while the party cycled); the same setup with 4 party units (16 on the field, block moved) played normally, the enemies acting.
- I: so more than 16 units on the field needs the AI's numbering, its 16-number checks and its per-number lists widened, whatever the drawing limits.

## Open questions

None recorded.
