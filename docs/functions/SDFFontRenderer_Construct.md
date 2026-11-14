# SDFFontRenderer_Construct

- **Address:** `0x1403A8694`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 sub_1403A8694(__int64 r)  // r = SDFFontRenderer*`
- **Callers:** sub_1403A3044 (0x1403A30DA), data 0x143D4012C
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the SDFFontRenderer: sets its vtable and resets every field (run state defaults, palette / vertex pointers, texture-slot ids) to its initial value. Creates no GPU objects.

## Behavior

- V: *(r+0) = vftable SDFFontRenderer at 0x1407208B8 (slots: 0 sub_1403C4CC4, 1 sub_1403C4CF0, 2 sub_1403A8E6C, 4 SDFFontRenderer_Flush, 5 SDFFontRenderer_ResetFrame, 7 sub_1403A9084, 8 sub_1403AA8BC).
- V: +188 word = 1 (byte +188 = 1, byte +189 = 0: the batch-open flag EmitGlyph tests is cleared); +8 qword = 0; +16 word = 0xFFFF (cMaterial slot id, filled later), +18 word = 0; +184 word = 0xFFFF (tTexture0 slot id), +186 word = 0xFFFF (cSDFConstant slot id); +160..+183 = twelve words of 0xFFFF (tTexture1..12 slot ids).
- V: zeroed qwords: +24 (shader), +32 (technique), +40 (constant buffer), +48 (palette buffer), +56 (palette SRV), +192 / +200 / +208 / +216 / +224 / +232 (layouts and vertex / index buffers), +240, +7928 / +7936 / +7944 and dword +7952, +9516 (palette count; quad count dword +9520 is cleared by the same qword), +9536, +9552 (vertex CPU buffer), +9560 (palette CPU buffer), +9492 (pen x / y).
- V: run-state defaults: +9500 = 1.0f (scale x), +9504 = 1.0f (scale y), +9508 = 0x3F800000 (colour dword), +9512 = 0, +9524 = 0x3DCCCCCD = 0.1f (the italic shear factor EmitGlyph uses), +9528 word = 8, +9530 byte = 0 (italic off), +9544 = +9548 = 1.0f (the two UV-corner divisors Flush rewrites).
- V: memset(r+64, 0, 0x60) = the 12 font-object pointers *(r + 8 * slot + 64) EmitGlyph reads; memset(r+248, 0, 0x1E00) and memset(r+7956, 0, 0x600) clear two large tables (batch / run records; the layout is not read here).
- V: returns r. Called from the renderer-set constructor sub_1403A3044 (0x1403A30DA) and listed in a data table at 0x143D4012C.

## Notes

Proposed name: SDFFontRenderer_Construct. Pairs with the FrequentUtilRenderer constructor sub_1403AA900 (same base fields +8, +16, +18, +24..+56 zero / 0xFFFF).

## Open questions

? the record layout of the +248 (0x1E00) and +7956 (0x600) tables. ? meaning of the word 8 at +9528 (I: a default font slot or page count; not read where it is used).
