# CharaAnim_Step

- **Address:** `0x1400CC994`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `char CharaAnim_Step(CharaAnimState *a)`
- **Callers:** CharaSlot_SetParams (tail jump), sub_1400D4CB0, itself (recursion on a command that needs a second step)
- **Callees:** sub_1400CC6C0, sub_1400CD22C, itself

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Advances the slot's classic SEQ animation by one command and, for a frame command, makes sure its atlas texture is loaded (CharaRender_LoadCheck).

## Behavior

- V: reads the next (opcode, delay, frame) from the sequence data with sub_1400CC6C0; opcode 1 = show a frame (checks the 44-byte frame cache at renderer+47152), 118 = shift the x offset by a signed byte, 144 = restart the sequence, 149.. = small x offset steps (+1/+2/-1/-2) with the flag word set to 0x800000; other opcodes are not decoded.

## State touched

- Reads: [g_CharaRenderer](../globals/g_CharaRenderer.md), [g_TextureTable](../globals/g_TextureTable.md)

## Referenced by

- Called by: [CharaRenderer_Update](CharaRenderer_Update.md), [CharaSlot_SetParams](CharaSlot_SetParams.md)

## Notes

The renderer runs the classic game's SEQ/SHP bytecode (battle_type1_seq/shp) on the CPU.

## Open questions

Full opcode table not decoded (?).
