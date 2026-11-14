# UIRender_AppendCommand

- **Address:** `0x1403B83FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 __fastcall UIRender_AppendCommand(__int64 renderer, unsigned int layer, int a3, __int64 drawState)`
- **Callers:** GUIQuad_EmitGouraud, sub_1403DFCF0, sub_1403E153C, sub_1403E3828, sub_1403E40EC, sub_1403E4AE8, sub_1403E4FEC (V)
- **Callees:** UIRender_GetThreadContext, UICommand_Append

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Appends a type-32 command to the calling thread's UIContext, tagged with the current layer; also marks the layer used.

## Behavior

- V: returns 0 unless (*(u8*)(renderer + 136) & 1) (the frame is recording UI commands; GUIRenderer_ResetFrame zeroes +136).
- V: ctx = UIRender_GetThreadContext(renderer). L = *(*(qword_143CDA098 + 37936) + 208) = the current layer record (GUIRenderer_ResetFrame sets *(+208) = renderer + 303480). Sets *(u8*)(L+76) = 1 (layer used this frame; UIRender_ClearLayerFlags clears it).
- V: builds a pair v10 = {low dword = *(u32*)(L+8), high dword = a3} and calls UICommand_Append(ctx, 32, layer, &v10, drawState).
- I: type 32 matches UIRender_FlushBatch kind 32 (0x5000 draw bits), so this is the command that records a layer draw.

## State touched

- Calls: [UIRender_GetThreadContext](UIRender_GetThreadContext.md), [UICommand_Append](UICommand_Append.md)
- Reads: [Renderer.ui_manager](../structs/Renderer.md#ui_manager), [g_Renderer](../globals/g_Renderer.md)
- Writes: [GUILayer.used](../structs/GUILayer.md#used)

## Referenced by

- Called by: [GUIQuad_EmitGouraud](GUIQuad_EmitGouraud.md)

## Open questions

? meaning of a3 (a per-draw payload, perhaps vertex count or order). ? what *(L+8) is.
