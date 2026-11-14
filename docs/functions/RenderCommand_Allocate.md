# RenderCommand_Allocate

- **Address:** `0x140069A38`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `_DWORD *__fastcall RenderCommand_Allocate(RenderContext *rc, int type, __int64 size)`
- **Callers:** 117 call sites: every layer pass and UI draw (GUILayer_Composite, GUILayer_BlitFinal, GUILayer_BlurShadowPass, UIRender_SubmitFrame, UIRender_DrawLetterbox, RenderContext_ResetFrame, ...)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Allocates one command of the given size from the context's current 8 KB command block, writes its type, and returns the pointer.

## Behavior

- V: size is rounded up to a multiple of 8; used = the dword at rc+52 and the block is the pointer at rc+24. When used + size <= 0x2000 the command is carved from the current block; otherwise a new block is taken from the device pool (g_RenderDevice + 5120 + the dword at +5148, advanced by 0x2000) after the pool counter at +5144 is advanced by 0x2000 and compared with the limit at +5108.
- V: when the pool limit is exceeded the counter is rolled back, the byte at g_RenderDevice + 5106 is set to 1 and the function returns null (the frame's commands are dropped).
- V: on success rc+52 = the new used size and the first dword of the command = type; the function returns the pointer (null when the block pointer was null).

## Referenced by

- Called by: [GUILayer_BlitFinal](GUILayer_BlitFinal.md), [GUILayer_Composite](GUILayer_Composite.md), [RenderCommand_ClearTarget](RenderCommand_ClearTarget.md)

## Notes

The name is ours (IDB: sub_140069A38). The command types seen at its call sites: 0 (clear target, 32 bytes), 1 (24 bytes, a second clear kind), 4 (96 bytes: a draw with the packed state), 5 (96 bytes: the fitted post draw and the letterbox), 19 (16 bytes: resource state transition).

## Open questions

? the meaning of type 1 and of the type 19 flag word (2 / 1).
