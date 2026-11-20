# UnitMovementAnimationTables

- **Kind:** observed behaviour
- **Scope:** engine (unit sprite animation)
- **Area:** [Graphics](../areas/graphics.md)
- **Affects:** [CharaAnim_ReadStep](../functions/CharaAnim_ReadStep.md), [CharaAnim_Step](../functions/CharaAnim_Step.md), [CharaRender_DrawFrame](../functions/CharaRender_DrawFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eight data tables, one per sprite class, hold the unit's movement animations only (standing, walking, floating, turning, jumping, a few single-frame poses): a row per step, keyed by animation id and step number; attack and spell animations are not in them.

## Behavior

- V: CharaAnim_ReadStep takes the class from the sprite attribute table (byte 1 of the 4-byte row of the shape), picks that class's table, and finds the row by key = animation id and key2 = step number; the row gives an opcode (dword), an operand (byte) and a delay (byte, in ticks of 1/60 s).
- V (rows): the class equals the shape's sequence kind: the humanoid layout with robes and casters uses class 1, the martial humanoid layout class 0, and the other layouts classes 2 to 7 (one class per sequence kind of the sprite attribute table).
- V (rows): opcode 1 shows the SHP frame whose number is the operand for the delay; opcode 144 restarts the animation; opcode 118 shifts the unit's x offset by a signed amount; opcodes 149, 150, 153 and 154 are small offset steps; 148, 152 and 102 appear in some classes; opcode 0 is an empty step. Only 1, 118, 144 and the 149 range are decoded in the code (CharaAnim_Step); the others are read from the rows only.
- V (rows): each class holds 21 to 25 animation ids out of the range 1 to 73. Ids 1 to 5 are one-step poses showing frames 3, 2, 1, 8 and 7 of the martial layout (the eight standing views); ids 6 to 11 are loops over five body frames in a ping-pong order with three delay sets; ids 20 and 21 hold a single frame with offset steps; ids 24 and 25 are loops like 6 and 7 with a shifted start; ids 42 and 43 step through the eight standing views in turn; ids 56 and 57 are 19-step sequences with offset opcodes that end on a held frame; ids 52, 53, 62, 63, 72 and 73 are one-step poses showing frames 23, 24, 31, 33, 72 and 73 (robed layout: 72 and 73 show 64 and 65).
- V (frame records drawn over stock sheets of the martial layout, 2026-11-20): of the standing poses, frame 1 shows the unit from the side, frame 2 three-quarter front, frame 3 front, frame 7 back and frame 8 three-quarter back; each is one whole-body cell of 32 x 40 classic pixels on the sheet's first row (frame 2 at (32, 0), frame 8 at (96, 0)), and frames 4, 5 and 6 draw the cells of frames 2, 1 and 8 mirrored.
- I: from what the steps draw, ids 6 to 11 look like a walk cycle (three speeds, front and back), ids 42 and 43 a turn on the spot through the eight views, and ids 56 and 57 a jump (a rise, a held frame, a landing); the game itself carries no names for these animations and the other ids are not given a reading here.
- V (rows): a loop of ids 6 to 11 is 8 show-frame steps followed by a restart row; in the two humanoid classes the frames are five body frames per facing in a ping-pong order; the three speeds differ only in the delays.
- V (rows): class 0 (martial humanoid layout) and class 1 (robed and caster layout) show the same frame numbers for ids 1 to 11, 20, 21, 24, 25, 56 and 57, differ on animations 72 and 73 (different frame numbers), and class 1 has no rows for ids 42 and 43 (turn on the spot).
- I: the attack, cast and hurt animations are not here; the classic animation file carries them (see BattleMotionNumbers); the menu and job-tree renderer reads only these tables.

## Notes

Table ids: the eight tables are loaded by ids 108, 112, 113, 114, 248, 115, 116 and 117 in class order. Fields of the rows: the table columns Unknown8 (opcode) and UnknownC (operand in the low byte, delay in the second byte) are now identified.

## Open questions

? the meaning of opcodes 148, 150, 152, 153, 154 and 102 beyond 'small offset or flag step'; ? whether class 2 (the chocobo layout) is used by anything but its one sprite; ? which code reads the battle unit's animation number and turns it into the classic animation pointer (see BattleMotionNumbers).
