# UIRender_QueueImageDraw

- **Address:** `0x1403B84EC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall UIRender_QueueImageDraw(__int64 renderer, unsigned int layer, int a3, __int64 drawState)`
- **Callers:** GUICore_DrawOutsideBars, UIDraw_QuadTransformed, UIImage_DrawTiled, sub_1403DF9E0, sub_1403DFE34, sub_1403E2278 (V)
- **Callees:** UIRender_GetThreadContext, UICommand_Append

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a type-34 (image) command that carries a copy of the draw state, flagging the layer used and recording whether the draw state asks for a flag at bit 12.

## Behavior

- V: same preamble as UIRender_AppendCommand: returns 0 unless *(u8*)(renderer+136) & 1; ctx = UIRender_GetThreadContext; L = *(*(qword_143CDA098 + 37936) + 208); L+76 = 1.
- V: additionally *(u8*)(L+78) = (*(u32*)(drawState + 24) & 0x1000) != 0 (drawState dword +24 bit 12 copied into the layer's byte +78; ClearLayerFlags clears words +78..79).
- V: pair v10 = {*(u32*)(L+8), a3}; UICommand_Append(ctx, 34, layer, &v10, drawState).

## State touched

- Calls: [UIRender_GetThreadContext](UIRender_GetThreadContext.md), [UICommand_Append](UICommand_Append.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUICore_DrawOutsideBars](GUICore_DrawOutsideBars.md), [UIDraw_QuadTransformed](UIDraw_QuadTransformed.md), [UIImage_DrawTiled](UIImage_DrawTiled.md)

## Notes

Differs from UIRender_AppendCommand only in the type code (34 vs 32) and the bit-12 flag capture.

## Open questions

? what drawState bit 12 (0x1000 of +24) is (possibly 'needs previous contents' / blend). ? what *(L+78) is used for later.
