# SceneUnit_MeasureRange

- **Address:** `0x1403130C4`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneUnit_MeasureRange(int16_t sourceIndex, int16_t *point, int32_t targetIndex)`
- **Callers:** EventScript_Run, at 0x14023D995 (opcode 0x87, which sets qword_140D40940 to this routine just before the dispatch). One data reference at 0x143D3D870 (a function-pointer table entry, not traced).
- **Callees:** `sub_1402736D0` (speed value), `sub_140272BD0` (unit point), `BattleMap_GetTileRecord` (grid cell lookup), `sub_1402746E8` (scaled square root). Level 2, not traced past its use here: `sub_140260ABC`, `sub_140262AF4`, `sub_140262B20`, `sub_140262808`.

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The callback that opcode 0x87 installs in the global qword_140D40940: it measures a scaled distance from a source unit to a target unit, or to a fixed three-word point when no target unit has a preview index, and returns that value.

## Behavior

- V: from opcode 0x87 it is called through SceneCallback_Dispatch mode 3, which passes the second unit's preview index as the first argument, the address of word_142FEF848 as the second and the first unit's preview index (or -1) as the third. The dispatcher's extra arguments reach the callback in registers; the decompiler shows only the first.
- V: the source is the unit whose preview index is `sourceIndex`. A unit is found by preview index with `sub_140260ABC`, which returns the scene node whose sub-record byte +444 equals the index.
- V: source height adjustment: v6 = (2 times the speed of the source) divided by 3 (integer division). The speed comes from `sub_1402736D0`, which returns byte_140673303 at offset 4 times byte +10 of the unit node, or 0 when the node's byte +352 has bits 0x09 set or its byte +348 has bit 0x04 set. The source's height word at word_14186D77A is set to that word minus v6.
- V: the source point is written by `sub_140272BD0` into the three words at word_14186D778 (x, height, z): x is 28 times sub-record byte +79 plus 14, z is 28 times byte +80 plus 14, and the height comes from `sub_140262B20`.
- V: when targetIndex is -1: the target x is 28 times point[0] plus 14, the target z is 28 times point[2] plus 14, and the target height is -12 times the unsigned byte at offset 2 of the grid cell that `BattleMap_GetTileRecord` returns for (point[0], point[2], point[1]). The target words are at word_14186D780 (x), word_14186D782 (height) and word_14186D784 (z).
- V: when targetIndex is not -1: the target point is the unit's point from `sub_140272BD0` (same layout, into word_14186D780 to word_14186D784). Its height is lowered by v5, which is (3 times the target unit's speed) divided by 4 (integer division).
- V: D is the sum of the squares of the x, height and z differences between the target and the adjusted source; the height difference uses the adjusted source height. The result is the integer square root of D divided by 8, computed by `sub_1402746E8` as a floating-point square root scaled by 4096 and then shifted back down; a value of 0 or less gives 0.
- V: the result is stored in dword_14186D770 and returned as an unsigned 32-bit value, zero-extended.
- V: the opcode 0x87 body does not read the returned value.
- I: the value is a range measure between the two units. Its use by any other caller is not read.

## State touched

- Calls: [BattleMap_GetTileRecord](BattleMap_GetTileRecord.md)

## Referenced by

- Called by event opcodes: [0x87](../opcodes/README.md)

## Notes

The 0x87 record names its operands as unit slots; the values passed to this routine are preview indexes from ScenePreview_IndexOfSlot, and the target is the first operand's unit (or the point when that unit has no preview index). The result is stored in the global dword_14186D770.

## Open questions

What fills the three words at word_142FEF848 (used as the point when the first unit has no preview index). What byte_140673303, unit byte +10, and the grid cell byte at offset 2 mean. The meaning of the height offsets 2/3 and 3/4 and of the sub-record height from sub_140262B20.
