# FrequentUtilRenderer_Construct

- **Address:** `0x1403AA900`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 sub_1403AA900(__int64 r)  // r = FrequentUtilRenderer*`
- **Callers:** sub_1403A3044 (0x1403A307A), data 0x143D401B0
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the FrequentUtilRenderer (copy, blur, mip-generation and model-buffer utility passes): sets its vtable and resets all fields.

## Behavior

- V: *(r) = vftable FrequentUtilRenderer 0x140720868 (slots 0 sub_1403C4C70, 1 sub_1403C4CBC, 2 sub_1403ABAD0, 7 sub_1403ABB58, 8 sub_1403AA8BC); +8 = 0, +16 word = 0xFFFF, +18 = 0; zero qwords +24..+56, memset(+64, 0, 0x80) (16 texture handles), +192..+240, +248 dword = 0 (a count), +312..+328, +344..+384; memset(+392, 0, 0x100) (16 views + 16 buffers).
- V: slot ids = 0xFFFF words at +252..+270 (tTexture0..9 ids) and +288..+306 (constant buffer ids); byte +308 = 0.
- V: only caller is the renderer-set constructor sub_1403A3044 (0x1403A307A), which also constructs the SDFFontRenderer.

## Notes

Proposed name: FrequentUtilRenderer_Construct.

## Open questions

? fields +272..+286 and +328..+344 are not touched here (the initialiser sets +272..+286).
