# MapBlock_RunCommand

- **Address:** `0x1402509E8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char MapBlock_RunCommand(unsigned char opcode, unsigned char *record)`
- **Callers:** sub_1402514E0, sub_1402516BC (the map load task, which first reads the block with Map_LoadBattleData)
- **Callees:** MapBlock_ApplyLayerCommand, sub_140248E08

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs one command record of the loaded map block (layers, camera, palettes, lights) and dispatches the layer commands to MapBlock_ApplyLayerCommand.

## Behavior

- V: it is the map setup task: its scene-task-26 branch calls the tile-table builder with the level's map record, and the nine 0xA8-byte layer records (slots 0 and 2..8; slot 1 is a runtime index) are the ones the battle snapshot captures.
- V: opcodes 0x24..0x2B call MapBlock_ApplyLayerCommand for layers 1..8; the base layer's command calls it with layer 0.
- V: with the graphics-mode flag at 0, the base layer's command also starts the classic texture load keyed by the loaded map id.
- V: a palette command compares the current map id with 26 and 127 and takes fixed values for those two.

## State touched

- Calls: [MapBlock_ApplyLayerCommand](MapBlock_ApplyLayerCommand.md), [sub_140248E08](sub_140248E08.md)
- Writes: [g_BattleTileTable](../globals/g_BattleTileTable.md), [g_SceneTaskSlots](../globals/g_SceneTaskSlots.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)

## Open questions

?: the command list and operand meanings.
