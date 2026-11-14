# TextureLoadInfo_Alloc

- **Address:** `0x1403BAABC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `TextureLoadInfo *TextureLoadInfo_Alloc(void)`
- **Callers:** TextureResourceHandle_StreamStep, TextureResourceHandle_Unload (sub_1403BB9CC)
- **Callees:** sub_14001A2EC, sub_14001A2C4, sub_140011750

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates and zero-initialises the 280-byte streaming state record of a texture load (the header copy, the image pointer array and the id array).

## Behavior

- V: sub_140011750(280, heap, 8) with the heap from sub_14001A2EC(qword_140C696D0), retried once with sub_14001A2C4; null on failure.
- V: fields: +8..+39 zero (first header entry), +208 = 0, +216 = &+208 (image pointer array: self-pointing means 'one inline slot'), +224 = &+40 (header buffer: inline at +40), +232 = 0 (u16 id array), +240 = 0 (descriptor array), +248 = 0, +252 = 168 (header buffer capacity), +256 / +264 / +272 = 0 (bytes read / current image / current mip / slice counters used by TextureResourceHandle_StreamStep), +276 = 0, +278 = 0xFFFF (single image id).

## Referenced by

- Called by: [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md), [TextureResourceHandle_Unload](TextureResourceHandle_Unload.md)

## Notes

Name proposed (IDB: sub_1403BAABC); field meanings from the users.

## Open questions

? what +252 = 168 sizes (the buffer from +40 to +208 is 168 bytes).
