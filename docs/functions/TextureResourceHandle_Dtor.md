# TextureResourceHandle_Dtor

- **Address:** `0x1403BAE44`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_QWORD *TextureResourceHandle_Dtor(TextureResourceHandle *h, char flags)`
- **Callers:** vtable only (TextureResourceHandle_1407203C8 slot 0)
- **Callees:** sub_140095E5C, sub_14041FB00

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scalar deleting destructor (vtable slot 0): resets the vtable to the Custom handle, runs the base destructor and frees the 144 bytes when bit 0 of flags is set.

## Behavior

- V: *h = CustomResourceHandle vtable; sub_140095E5C() (base dtor); when (flags & 1) sub_14041FB00(h, 144) (free with size); returns h.

## Notes

Name proposed (IDB: sub_1403BAE44).

## Open questions

-
