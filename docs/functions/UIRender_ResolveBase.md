# UIRender_ResolveBase

- **Address:** `0x1403B8BF4`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void UIRender_ResolveBase(__int64 ui, __int64 a2)`
- **Callers:** UIRender_SubmitFrame
- **Callees:** UILayer_GetTarget, sub_1403B7E2C, sub_1403A8468, sub_140087AB4, sub_1403AC420, sub_14003ABD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the base (bottom) layer surface to the frame target once per frame, with the base-layer sort key.

## Behavior

- V: needs a thread state, the blur object g_Renderer+37928 and layer pointer ui+216; base target = UILayer_GetTarget(layer 0), or the current target when that is 0. Skipped when byte ui+141 is negative (already done). When the stored size qword ui+8664 differs from (W, H) = g_Renderer + 6568 / 6572 it calls sub_1403B7E2C to resize first.
- V: sort key state+8: when DWORD2(xmmword_142E80230) == 0 it is (targetByte << 43) | 0x1AB00080000 (targetByte 1 -> 0), otherwise ((lastLayer+12 & 0x1FF) | ((lastLayer+16 & 0x3F | targetByte << 18) << 15) | 0x6AC01C00) << 10.
- V: builds a rect (0, 0, W, H), creates a view with sub_140087AB4 (from ui+8648 or null) and calls sub_1403AC420(blurObj, view, destination) where destination is the render target of the base target's byte, or the frame target (*(qword_140C696A8+88) +128) when the flag is 0; then ui+141 = -1 and releases the view.

## State touched

- Calls: [UILayer_GetTarget](UILayer_GetTarget.md)
- Reads: [Renderer.output_width](../structs/Renderer.md#output_width), [Renderer.output_height](../structs/Renderer.md#output_height), [g_RenderDevice](../globals/g_RenderDevice.md), [g_Renderer](../globals/g_Renderer.md)
- Writes: [RenderContext.sort_key](../structs/RenderContext.md#sort_key)

## Referenced by

- Called by: [UIRender_SubmitFrame](UIRender_SubmitFrame.md)

## Notes

The name is ours (IDB: sub_1403B8BF4; role I: a copy of the base target, not verified live). The copy rectangle is the whole render size without scaling.

## Open questions

What sub_1403AC420 / sub_140087AB4 do exactly (copy region vs resolve).
