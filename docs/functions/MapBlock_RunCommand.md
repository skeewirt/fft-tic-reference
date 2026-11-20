# MapBlock_RunCommand

- **Address:** `0x1402509E8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char MapBlock_RunCommand(unsigned char opcode, unsigned char *record)`
- **Callers:** sub_1402514E0, sub_1402516BC (the map load task, which first reads the block with Map_LoadBattleData)
- **Callees:** MapBlock_ApplyLayerCommand, sub_140248E08, sub_140249F58, sub_14024A068, NxdTable_GetRowById

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one command record of the loaded map block (layers, camera, palettes, lights) and dispatches the layer commands to MapBlock_ApplyLayerCommand.

## Behavior

- V: it is the map setup task: its scene-task-26 branch calls the tile-table builder with the level's map record, and the nine 0xA8-byte layer records (slots 0 and 2..8; slot 1 is a runtime index) are the ones the battle snapshot captures.
- V: opcodes 0x24..0x2B call MapBlock_ApplyLayerCommand for layers 1..8; the base layer's command calls it with layer 0.
- V: with the graphics-mode flag at 0, the base layer's command also starts the classic texture load keyed by the loaded map id.
- V: a palette command compares the current map id with 26 and 127 and takes fixed values for those two.
- V: command 50 (0x32, reached by the running subtraction 44, 1, 1, 1, 1, 2 of the compare chain, so no immediate 0x32 appears; the chain after 44 sends 46..48 to the sub-command loop, 50 to the light block and 51 to sub_1402F7594): the light block. It reads nine 16-bit light colour values from record +0 (each clamped to 0x2000), three light vectors from record +18 (a dword and a word each), hands them to sub_140249F58, and passes the ambient colour bytes of record +36, +37 and +38 to sub_14024A068 (map id 26 takes the fixed ambient values 48 / 34 / 36 and id 127 takes 128 / 128 / 128 instead).
- V: the same block then reads the chosen variation element of the map's Map row (index from the global work record +116, taken only when below the element count) and lets its six int16 members at +0x38..+0x42 override the two background colour triples: bytes 0..2 and 4..6 of qword_14114A4E8 take the member's value, or, when the member is above 255, the byte of the command record at +39..+41 and +42..+44. The result is copied to qword_142FF9DA8, qword_142FF86A8 and qword_142FF8498 (see MapBackgroundColourPairOverride).
- V: other writers of the pair exist (sub_1402F52D8 and ClutManager_Update); sub_14024A6E8 puts it into the vertex colours.

## State touched

- Calls: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md), [sub_140248E08](sub_140248E08.md), [NxdTable_GetRowById](NxdTable_GetRowById.md)
- Writes: [g_BattleTileTable](../globals/g_BattleTileTable.md), [g_SceneTaskSlots](../globals/g_SceneTaskSlots.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Observed behaviours: [MapBackgroundColourPairOverride](../behaviors/MapBackgroundColourPairOverride.md)

## Open questions

?: the command list and operand meanings (the light block's layout is read; the other commands are not).
