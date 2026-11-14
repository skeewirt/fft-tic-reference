# GUIVector32_Free

- **Address:** `0x1403FD598`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUIVector32_Free(GUIVector32 *v)`
- **Callers:** GUICore_UpdateFrame, sub_1400FE2D0, sub_1401F7D1C, sub_1403FC2E8 and a vtable entry
- **Callees:** allocator vtable +24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases the vector's storage through its allocator (vtable +24) and resets begin / end / cap.

## Behavior

- V: when v+8 != 0: allocator->free(v+8, (v+24 - v+8) & ~0x1F) (size rounded down to a multiple of 32); v+8 = v+16 = v+24 = 0.

## Referenced by

- Called by: [GUIInput_IsPointerOverLayer](GUIInput_IsPointerOverLayer.md)

## Notes

The name is ours (IDB: sub_1403FD598). 812 hits per 4 s.

## Open questions

None recorded.
