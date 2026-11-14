# TextureResourceHandle_RegisterImages

- **Address:** `0x1403BBB78`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 TextureResourceHandle_RegisterImages(TextureResourceHandle *h)`
- **Callers:** vtable only: TextureResourceHandle_1407203C8 slot 21
- **Callees:** sub_140088604 (allocate id), sub_1400886A8 (set image)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slot 21 of TextureResourceHandle: when the handle's status dword (+80) is 1 (loaded), registers each of its images in the global image table under an id (allocating a fresh id when the stored one is 0xFFFF).

## Behavior

- V: does nothing unless the atomic dword h+80 == 1. Always returns 0.
- V: single image (count 1 and h+124 == 0): id = u16 h+136, allocated with sub_140088604(qword_140C696A8) when 0xFFFF and stored back; sub_1400886A8(qword_140C696A8, id, image h+112).
- V: several images: same per image with the id array after the pointer array (h+112 + (h+120 & 0xFFF8)) and the image pointer (h+112)[i].

## State touched

- Reads: [g_RenderDevice](../globals/g_RenderDevice.md)

## Notes

Name proposed (IDB: sub_1403BBB78). Counterpart of the id release in TextureResourceHandle_Unload.

## Open questions

? what the table at qword_140C696A8 is read by (the draw path resolves texture ids through it, I).
