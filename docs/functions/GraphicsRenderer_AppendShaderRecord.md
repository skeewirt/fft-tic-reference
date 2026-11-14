# GraphicsRenderer_AppendShaderRecord

- **Address:** `0x1403AA8BC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 sub_1403AA8BC(__int64 r, __int64 list)`
- **Callers:** vtable slot 8 of FrequentUtilRenderer (0x140720868 + 0x40) and of SDFFontRenderer (0x1407208F8), data 0x143D401A4
- **Callees:** sub_14006635C (vector grow-insert)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Renderer vtable slot 8 (shared by SDFFontRenderer and FrequentUtilRenderer): appends a 16-byte record {r+24, 0} (the renderer's shader) to a caller-supplied vector.

## Behavior

- V: record = {qword r+24, dword 0 at +8 (+12 left uninitialised)}; list+16 is the vector end, list+24 the capacity end.
- V: if end == capacity it calls sub_14006635C(list, end, &record) (grow and insert), else stores the 16 bytes at end and advances list+16 by 16.
- I: used to enumerate every renderer's shader (hot reload or readiness polling); the callers are not decoded.

## Notes

Proposed name: GraphicsRenderer_AppendShaderRecord.

## Open questions

? the consumer of the list and the meaning of the dword 0.
