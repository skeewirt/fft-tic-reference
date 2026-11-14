# TextureResourceHandle_FinishLoad

- **Address:** `0x1403BAE84`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_FinishLoad(TextureResourceHandle *h)`
- **Callers:** TextureResourceHandle_StreamStep (states 1003 end and 1005)
- **Callees:** TextureLoadInfo_Free, sub_140096190

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Last step of the TEX load (state 1005): moves the finished images from the load info into the handle and marks the handle ready.

## Behavior

- V: info = qword h+112. u16 h+120 = (h+120 & 7) | (8 * byte info+8) (image count in the upper 13 bits); dword h+124 = info+248.
- V: when info+216 (image array) == &info+208 (one inline slot): h+112 = *(info+208) (the image pointer itself) and u16 h+136 = u16 info+278 (its id), info+278 = -1. Otherwise h+112 = the array and, per image, the u16 ids of info+232 are re-matched by their dword keys against the array after the pointers and copied into the id area that follows the pointer array (the source ids are set to 0xFFFF).
- V: info+216 = 0 (the array now belongs to the handle), TextureLoadInfo_Free(&info), state dword h+84 = 5, return sub_140096190(h) (base 'mark loaded').

## State touched

- Calls: [TextureLoadInfo_Free](TextureLoadInfo_Free.md)

## Referenced by

- Called by: [TextureResourceHandle_StreamStep](TextureResourceHandle_StreamStep.md)

## Notes

Name proposed (IDB: sub_1403BAE84). The id re-matching loop was read from the decompile; its exact record layout is ?.

## Open questions

? the key dword compared at (v10 + 4 * i) (a key per image, I: the sub-image index or a hash).
