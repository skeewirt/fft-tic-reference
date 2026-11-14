# TextureResourceHandle_Create

- **Address:** `0x1403BAD34`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `TextureResourceHandle *TextureResourceHandle_Create(void)`
- **Callers:** sub_1403A143C (texture manager request)
- **Callees:** CustomResourceHandle_Ctor, sub_14001A2C4, sub_140011750

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates and constructs a faith::Graphics::TextureResourceHandle (144 bytes).

## Behavior

- V: sub_140011750(144, heap, 8); null -> 0. CustomResourceHandle_Ctor, then vtable = vftable_faith::Graphics::TextureResourceHandle_1407203C8, +112 = 0, dword +128 = -1, flags +92 |= 0x104038, u16 +122 = -1, u16 +136 = -1, u16 +120 = 0, dword +124 = 0.

## State touched

- Calls: [CustomResourceHandle_Ctor](CustomResourceHandle_Ctor.md)

## Notes

Name proposed (IDB: sub_1403BAD34). +112 = the load info / image array, +120 u16 = (count << 3) | 3 flag bits, +124 = payload size, +136 u16 = single image id.

## Open questions

? meaning of flag bits 0x104038.
