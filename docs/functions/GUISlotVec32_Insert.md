# GUISlotVec32_Insert

- **Address:** `0x1403EE918`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned int GUISlotVec32_Insert(__int64 unused, GUISlotVec *vec, const __m128i rec[2])`
- **Callers:** GUIFontSlots_AcquireTexturePart
- **Callees:** allocator vtable +16 / +24, std::vector<void *>::_Xlen

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The 32-byte-record twin of GUISlotVec16_Insert (used for the kind-2 texture-part vector).

## Behavior

- V: same algorithm: first record with first qword 0 is overwritten (32 bytes copied), else append with 1.5x growth through the vec allocator (+16 allocate, +24 free), returning the index.

## Referenced by

- Called by: [GUIFontSlots_AcquireTexturePart](GUIFontSlots_AcquireTexturePart.md)

## Notes

The name is ours (IDB: sub_1403EE918).

## Open questions

-
