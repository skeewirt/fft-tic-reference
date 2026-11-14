# UIRender_ClearLayerFlags

- **Address:** `0x1403B8574`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void __fastcall UIRender_ClearLayerFlags(__int64 renderer, int a2)`
- **Callers:** none found (0 code xrefs; ? may be called via a vtable slot of the Renderer class)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

When a2 == 0, resets the per-frame bookkeeping of all 512 layer records and the active layer counter.

## Behavior

- V: only acts when a2 == 0; otherwise a no-op.
- V: iterates 512 qword pointers starting at renderer+216; for each non-null layer: *(u32*)(L+36) = -1, *(u8*)(L+76) = 0, *(u16*)(L+78) = 0 (the flags set by UIRender_AppendCommand / QueueImageDraw).
- V: *(u32*)(renderer + 172) = 0 (active layer count).

## Notes

Likely a virtual method of the UIRender Renderer (vftable at 1407207D8); the xref scan found no direct callers.

## Open questions

? the real caller (check Renderer vtable slots). ? what L+36 = -1 marks (unassigned render target / command index).
