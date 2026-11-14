# SDFFontRenderer_ReleaseResources

- **Address:** `0x1403A8E6C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 sub_1403A8E6C(_QWORD *r)  // r = SDFFontRenderer*`
- **Callers:** vtable slot (0x1407208C8), data 0x143D40144, sub_1403A9084
- **Callees:** sub_140011804, sub_14003ABD0, sub_14003AD5C, sub_140095E88, vtable +32 releases

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

SDFFontRenderer release (vtable slot 2): frees every GPU object and CPU buffer the set-up created and nulls the pointers.

## Behavior

- V: in order, each guarded by a non-null test and nulled after: r[26] (+208 glyph index buffer) released through its vtable slot +32; r[25] (+200 vertex buffer) sub_14003AD5C; r[24] (+192 input layout) sub_14003ABD0; r[29] (+232 second IB) vtable +32; r[28] (+224 second VB) sub_14003AD5C; r[27] (+216 second layout) sub_14003ABD0; r[4] (+32 technique) vtable +32; r[6] (+48 palette buffer) vtable +32; r[7] (+56 palette view) sub_14003ABD0; r[5] (+40 constant buffer) sub_14003AD5C; r[3] (+24 shader) sub_140095E88; r[1194] (+9552 CPU vertex buffer) and r[1195] (+9560 CPU palette) freed with sub_140011804(p, 0, 0).
- V: slot 2 of vtable 0x1407208B8; also reached through the vtable by sub_1403A9084 when the technique cannot be made.

## Notes

Proposed name: SDFFontRenderer_ReleaseResources. Mirror image of sub_1403A87EC.

## Open questions

? the font-object pointers at r+64.. and the +248 tables are not freed here (I: owned elsewhere).
