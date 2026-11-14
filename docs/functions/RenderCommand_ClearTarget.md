# RenderCommand_ClearTarget

- **Address:** `0x140054C24`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int64 __fastcall RenderCommand_ClearTarget(RenderThread *rt, ClearCommand *cmd)`
- **Callers:** the render-thread command dispatcher (table at 0x1406FD168, not a direct call)
- **Callees:** sub_14005BA74 (flush barriers), sub_140060A1C (bind target), sub_140050BC0 (close barriers), ID3D12GraphicsCommandList::ClearRenderTargetView

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Render-thread executor of the command type 0 that GUILayer_Composite and RenderContext_ResetFrame queue: clears one render target to the colour stored in the command.

## Behavior

- V: command layout as built by GUILayer_Composite: dword +0 = type 0 (written by RenderCommand_Allocate), qword +8 = the target view object (the +40 member of the render target object), 16 bytes at +16 = the clear colour (four floats). GUILayer_Composite writes the 16 bytes as zero, so a layer target and its scratch targets are cleared to (0, 0, 0, 0).
- V: the function flushes pending resource barriers (sub_14005BA74: the command list's vtable slot +208, ResourceBarrier), binds the target (sub_140060A1C with the thread's binding state at rt+896; sub_140050BC0 closes the pending barrier list) and calls the command list's vtable slot +384 with (list, the render-target descriptor handle of the view at view + 56 + 8 x (dword_140C69D24 & 1), the colour pointer cmd + 16, 0, 0).
- I: vtable slot +384 is ID3D12GraphicsCommandList::ClearRenderTargetView (index 48 of the interface, five arguments including the two rectangle arguments 0 / 0), so the whole target is cleared. Basis: the argument list and the slot arithmetic; the interface order was taken from the D3D12 header, not from the game.
- I: the descriptor handle is selected by the low bit of a frame counter, so each target has two descriptors used on alternate frames. Basis: the address arithmetic (+ 8 x (counter & 1)).
- I: the command type number 0 maps to this function through the handler table at 0x1406FD168 (data, code pointers): the entry for type 0 sits at index 4 and the entries at index 8 and 23 are the handlers (sub_140055484, sub_1400564F8) that match the draw type 4 and the barrier type 19 by position. Basis: the order of the table; the dispatcher that indexes it was not read.

## State touched

- Calls: [RenderCommand_Allocate](RenderCommand_Allocate.md)

## Referenced by

- Observed behaviours: [LayerContentDrawnIntoCleared8BitTarget](../behaviors/LayerContentDrawnIntoCleared8BitTarget.md)

## Notes

The name is ours (IDB: sub_140054C24). GUILayer_Composite queues this command, once per atlas page, for slots 26, 27, 28 and 29 of the layer's target-type slot table (RT 26 layer content, RT 27, RT 28, RT 29), for slot 3 (RT 3, the effect alpha) when the layer has a drop shadow and for slot 30 when the layer is masked; RenderContext_ResetFrame queues one with the colour (1, 1, 1, 1) (all ones) for the main window target.

## Open questions

? the handler table's exact first index (the table has four standard entries before the commands; the type-to-index offset 4 was read from the three known commands 0, 4 and 19, not from the dispatcher). ? what the type 1 handler (sub_140054C90, used with a 24-byte command by GUILayer_Composite for g_Renderer + 20632) clears.
