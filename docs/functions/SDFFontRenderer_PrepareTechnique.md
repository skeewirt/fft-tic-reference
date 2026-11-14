# SDFFontRenderer_PrepareTechnique

- **Address:** `0x1403A9084`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `char sub_1403A9084(_QWORD *r)  // r = SDFFontRenderer*`
- **Callers:** vtable slot 7 (0x1407208F0), data 0x143D40150
- **Callees:** sub_14039EB08 (create Technique from a shader)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

SDFFontRenderer shader-ready check (vtable slot 7): when the SDFFont shader has finished loading, creates the technique and sets the 'renderer usable' flag.

## Behavior

- V: byte r+189 = (atomic read of dword *(r[3] + 80) == 1), r[3] being the shader loaded by sub_1403A87EC. This is the r+189 flag SDFFontRenderer_EmitGlyph tests before emitting.
- V: when set it also requires dword shader+84 == 1, shader+80 == 1 and dword shader+104 == 0, then r[4] (+32 technique) = sub_14039EB08(shader, 0); non-null -> return 1.
- V: otherwise (flag clear, a condition failed, or technique creation returned null) it calls vtable slot 2 (+16) on r, i.e. sub_1403A8E6C, and returns 0.
- I: shader+80 / +84 are load-state values (1 = done) and +104 an error count; the names are not read. No retry loop is in this function.

## Notes

Proposed name: SDFFontRenderer_PrepareTechnique. A failed state releases everything (slot 2), including the shader.

## Open questions

? who calls slot 7 and how often; ? the semantics of shader+80 / +84 / +104.
