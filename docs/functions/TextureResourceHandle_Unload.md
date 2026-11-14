# TextureResourceHandle_Unload

- **Address:** `0x1403BB9CC`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_Unload(TextureResourceHandle *h)`
- **Callers:** vtable only: TextureResourceHandle_1407203C8 slot 19
- **Callees:** TextureLoadInfo_Alloc, TextureLoadInfo_Free, sub_14003ABD0, sub_140088674, allocator

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 19 of TextureResourceHandle: releases the GPU images of the handle (count in the upper 13 bits of h+120) and their ids, then clears the count.

## Behavior

- V: n = u16 h+120 >> 3. n == 0: TextureLoadInfo_Free-style cleanup via sub_1403BAB84(h+112). n == 1 with h+124 == 0 (a single image): releases the image (sub_14003ABD0, h+112 = 0) and either (flag 0x20000 of h+92 set) creates a fresh TextureLoadInfo that remembers the id (+276 = 1, +278 = h+136) or returns the id to the allocator (sub_140088674(qword_140C696A8, h+136), h+136 = 0xFFFF).
- V: otherwise (several images or a payload): releases each image pointer (sub_14003ABD0); with flag 0x20000 a TextureLoadInfo keeps the ids (+276 = n, +232 = the old array, h+112 = info), without it the ids are returned and the array freed through the allocator vtable +72.
- V: at the end u16 h+120 &= 7 (count cleared) and h+124 = 0.

## State touched

- Calls: [TextureLoadInfo_Alloc](TextureLoadInfo_Alloc.md), [TextureLoadInfo_Free](TextureLoadInfo_Free.md)
- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Notes

Name proposed (IDB: sub_1403BB9CC). The 0x20000 flag keeps the ids for a later reload (I).

## Open questions

? meaning of flag 0x20000.
