# GUIVector32_Init

- **Address:** `0x1403FD550`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIVector32 *GUIVector32_Init(GUIVector32 *v)`
- **Callers:** GUICore_UpdateFrame, sub_1400FE2D0, sub_1401F7D1C, sub_1403FC2E8
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Constructs an empty vector of 32-byte elements: allocator pointer (from qword_143CDAA80 + 32) at +0, begin / end / cap = 0, extra fields zeroed.

## Behavior

- V: v+0 = allocator (0 when qword_143CDAA80 = 0), v+8 = v+16 = v+24 = 0, v+32..+47 = 0, v+48 = 0, u16 v+52 = 0, byte v+54 = 0. Returns v.

## Referenced by

- Called by: [GUIInput_IsPointerOverLayer](GUIInput_IsPointerOverLayer.md)

## Notes

The name is ours (IDB: sub_1403FD550). 812 hits per 4 s. Paired with GUIVector32_Free; both run once per frame from GUICore_UpdateFrame for a scratch list.

## Open questions

? Which element type the 32-byte records are.
