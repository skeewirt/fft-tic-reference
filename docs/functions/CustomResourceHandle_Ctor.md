# CustomResourceHandle_Ctor

- **Address:** `0x1403BA5B4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 CustomResourceHandle_Ctor(ResourceHandle *h)`
- **Callers:** TextureResourceHandle_Create, sub_1403B9F94, sub_1403BC1F4, sub_1403BF2D8 (the other handle constructors)
- **Callees:** sub_140095DA0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructor of the base 'custom' resource handle: runs the base ResourceHandle constructor, sets the CustomResourceHandle vtable and clears its extra fields.

## Behavior

- V: sub_140095DA0(h) (base ctor); *(h) = vftable_faith::Graphics::CustomResourceHandle_140720578; flags dword +92 |= 0x2000; qword +96 = 0; dword +104 = 0; byte +108 = 0; returns h.

## Referenced by

- Called by: [TextureResourceHandle_Create](TextureResourceHandle_Create.md)

## Notes

Name proposed (IDB: sub_1403BA5B4). Subclass constructors (Texture, ...) call it and then overwrite the vtable.

## Open questions

? the meaning of flag 0x2000 and of +96 / +104 (see sub_1403BA7A0: both cleared on release; +96 / +104 are written by the TEX loader as the payload tail pointer and size).
