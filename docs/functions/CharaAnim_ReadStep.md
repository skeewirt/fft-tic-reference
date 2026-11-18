# CharaAnim_ReadStep

- **Address:** `0x1400CC6C0`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `char CharaAnim_ReadStep(CharaAnimState *a, float *delay, int *opcode, unsigned char *value)`
- **Callers:** CharaAnim_Step
- **Callees:** sub_1403D325C, sub_1403D3C98 (row by key/key2), sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads one step of an animation from the unit's sequence table: row (animation id, step) -> opcode, value and delay.

## Behavior

- V: the sequence class is byte_140673301[4 * shape] (0..7); each class owns one nxd table (loaded by id 108, 112, 113, 114, 248, 115, 116, 117 in class order) cached in qword_143CD9FE8..; I: these are CharAnimSeq0..7.
- V: the row is found by key = animation id (a+56) and key2 = step (a+60); output: opcode = row dword +8, value = row byte +12, delay = float(row byte +13).
- V (data): CharAnimSeq0/1 key 2, step 0 -> opcode 1 (show frame), value 2: the pose the tree uses shows frame 2 (CharAnimSeq2 gives 2 for key 2 as well).

## Referenced by

- Observed behaviours: [UnitMovementAnimationTables](../behaviors/UnitMovementAnimationTables.md)
- Reads tables: [SpriteLookAttributes](../tables/SpriteLookAttributes.md)

## Notes

The classic SEQ file is zero-based (anim 2 = frame 1); the nxd tables are one-based, so animation id 2 means frame 2.

## Open questions

None recorded.
